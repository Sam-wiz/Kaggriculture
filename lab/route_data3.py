"""Day-9 re-route probe: prefix = shipped map pick (days 6-8), switch to
candidate tail route at step 216 using shops 1-3. Records tail margins keyed
by first-3-shops to test whether a later decision beats the day-6 map.

Usage: route_data3.py OUT.jsonl START_SEED N_SEEDS OPP1,OPP2,...
"""
import collections
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

CANDIDATES = [0, 4, 8, 10, 11, 12, 101, 103, 105, 106, 107, 108,
              110, 111, 114, 115, 118, 120, 123, 126]


def load_module():
    spec = importlib.util.spec_from_file_location("v48d9", V48)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def full_agent(m):
    return [v for v in vars(m).values() if callable(v)][-1]


def kload(path):
    env = {}
    exec(compile(open(path).read(), path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


def make_d9_router(ship_pick, tail):
    """map pick at 144, tail at 216, route 2 at 648."""
    def router(observation, step, state):
        if step >= 144 and not state.get("d6"):
            state["route"] = ship_pick
            state["d6"] = True
        if step >= 216 and not state.get("d9"):
            state["route"] = tail
            state["d9"] = True
        if step >= 648 and not state.get("d27"):
            state["route"] = 2
            state["d27"] = True
        return state.get("route", 0)
    return router


def job(arg):
    seed, oppname, sw = arg
    m = load_module()
    opp = kload(OPPS[oppname])
    agent = full_agent(m)
    chassis = m._IMPL.chassis
    orig_router = chassis.router
    shops = [None]

    def spy(step, state, env):
        if step == 216:
            shops[0] = list(state[0].observation["town"]["unlocked_shops"][:3])
        if step >= 718:
            shops[0] = shops[0] or list(state[0].observation["town"]["unlocked_shops"][:3])

    x, y = (opp, agent) if sw else (agent, opp)
    # shipped run (records shops3 + baseline margin)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True, on_step=spy)
    p, q = r["reward"][::-1] if sw else r["reward"]
    ship_margin = p - q
    shops3 = shops[0] or []
    ship_pick = m._R110_OLD_SHOPS.get(tuple(shops3[:2]), 0) \
        if tuple(shops3[:2]).count("YARN_STORE") > 0 \
        else m._R108_SHOP_ROUTES.get(tuple(shops3[:2]), 100)

    margins = {}
    for tail in CANDIDATES:
        chassis.router = make_d9_router(ship_pick, tail)
        r = harness.run_episode(x, y, seed=seed, catch_errors=True)
        p, q = r["reward"][::-1] if sw else r["reward"]
        margins[tail] = p - q
    chassis.router = orig_router
    best = max(margins, key=margins.get)
    return {
        "seed": seed, "opp": oppname, "seat": sw,
        "shops3": shops3, "ship_pick": ship_pick,
        "ship_margin": ship_margin,
        "margins": margins, "best": best, "best_margin": margins[best],
    }


if __name__ == "__main__":
    out = sys.argv[1]
    start = int(sys.argv[2])
    nseeds = int(sys.argv[3])
    oppnames = sys.argv[4].split(",") if len(sys.argv) > 4 else OPPNAMES
    args = [(s, o, sw) for s in range(start, start + nseeds)
            for o in oppnames for sw in (0, 1)]
    with open(out, "w") as f:
        for rec in ProcessPoolExecutor(7).map(job, args):
            f.write(json.dumps(rec) + "\n")
            f.flush()
    print("wrote", len(args), "records ->", out)
