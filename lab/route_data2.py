"""Wide route-margin collection: reduced candidate routes, one rotating opp
per seed, for pair->route remap coverage.

Usage: route_data2.py OUT.jsonl START_SEED N_SEEDS
"""
import importlib.util
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

V48 = "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py"

OPPS = {
    "v45": "rivals/ahmedberatozer_kaggriculture-v45-first-turn-wheat-round-trip/_entry.py",
    "aurax7": "rivals/aurax7_kaggriculture-shop-router-reactive-v7/_entry.py",
    "pipe7": "rivals/nathanjacob_kaggriculture-pipe-7-wheat-microstructure/_entry.py",
}
OPPNAMES = ["v45", "aurax7", "pipe7"]

# herd-group reps + observed winners + common map picks
CANDIDATES = [0, 4, 8, 10, 11, 12, 101, 103, 105, 106, 107, 108,
              110, 111, 114, 115, 118, 120, 123, 126]


def load_module():
    spec = importlib.util.spec_from_file_location("v48oracle", V48)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def full_agent(m):
    return [v for v in vars(m).values() if callable(v)][-1]


def kload(path):
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


def make_pinned_router(route_id):
    def router(observation, step, state):
        if step >= 144 and not state.get("day6"):
            state["route"] = route_id
            state["day6"] = True
        if step >= 648 and not state.get("day27"):
            state["route"] = 2
            state["day27"] = True
        return state.get("route", 0)
    return router


def job(arg):
    seed, oppname, sw = arg
    m = load_module()
    opp = kload(OPPS[oppname])
    agent = full_agent(m)
    chassis = m._IMPL.chassis
    shops2 = [None]
    shops_final = [None]

    def spy(step, state, env):
        if step == 144:
            shops2[0] = tuple(state[0].observation["town"]["unlocked_shops"][:2])
        if step >= 718:
            shops_final[0] = list(state[0].observation["town"]["unlocked_shops"])

    x, y = (opp, agent) if sw else (agent, opp)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True, on_step=spy)
    p, q = r["reward"][::-1] if sw else r["reward"]
    ship_margin = p - q

    margins = {}
    for rid in CANDIDATES:
        chassis.router = make_pinned_router(rid)
        r = harness.run_episode(x, y, seed=seed, catch_errors=True)
        p, q = r["reward"][::-1] if sw else r["reward"]
        margins[rid] = p - q
    best = max(margins, key=margins.get)
    return {
        "seed": seed, "opp": oppname, "seat": sw,
        "shops2": list(shops2[0] or []),
        "shops_final": shops_final[0],
        "ship_margin": ship_margin,
        "margins": margins, "best": best, "best_margin": margins[best],
    }


if __name__ == "__main__":
    out = sys.argv[1]
    start = int(sys.argv[2])
    nseeds = int(sys.argv[3])
    args = [(s, OPPNAMES[s % 3], sw) for s in range(start, start + nseeds)
            for sw in (0, 1)]
    with open(out, "w") as f:
        for rec in ProcessPoolExecutor(7).map(job, args):
            f.write(json.dumps(rec) + "\n")
            f.flush()
    print("wrote", len(args), "records ->", out)
