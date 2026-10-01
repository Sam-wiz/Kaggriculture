"""Oracle gap for V48's step-144 route choice.

Patches m._IMPL.chassis.router so the FULL wrapped agent (all layers intact)
is measured, with only the day-6 route pick forced to a pinned route_id.

Usage: route_oracle.py START_SEED N_SEEDS [OPP_PATH]
"""
import importlib.util
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

V48 = "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py"
OPP = "rivals/ahmedberatozer_kaggriculture-v45-first-turn-wheat-round-trip/_entry.py"


def load_module():
    spec = importlib.util.spec_from_file_location("v48oracle", V48)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def full_agent(m):
    return [v for v in vars(m).values() if callable(v)][-1]


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
    seed, sw = arg
    m = load_module()
    opp = kload(OPP)
    agent = full_agent(m)
    chassis = m._IMPL.chassis
    orig_router = chassis.router

    def run(pa):
        x, y = (opp, pa) if sw else (pa, opp)
        r = harness.run_episode(x, y, seed=seed, catch_errors=True)
        p, q = r["reward"][::-1] if sw else r["reward"]
        return p - q

    ship_margin = run(agent)
    margins = {}
    for rid in sorted(m._ROUTES.keys()):
        chassis.router = make_pinned_router(rid)
        margins[rid] = run(agent)
    chassis.router = orig_router
    best = max(margins, key=margins.get)
    return seed, sw, ship_margin, margins[best], best, margins


def kload(path):
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    nseeds = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    args = [(s, sw) for s in range(start, start + nseeds) for sw in (0, 1)]
    res = list(ProcessPoolExecutor(7).map(job, args))
    gap = 0.0
    better = 0
    n = 0
    for seed, sw, ship, bestm, bestrid, margins in res:
        n += 1
        gap += bestm - ship
        if bestm > ship:
            better += 1
    print("over %d (seed,seat) games: mean oracle-gap %+8.0f; oracle beats map in %d/%d"
          % (n, gap / n, better, n))
