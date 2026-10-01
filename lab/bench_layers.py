"""Benchmark V48 with each disabled layer toggled ON, vs stock V48.
Paired seeds x both seats. Usage: bench_layers.py START_SEED N_SEEDS
"""
import copy
import importlib.util
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

V48 = "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py"


def kload(path):
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


def variant(layer):
    spec = importlib.util.spec_from_file_location("v48_" + layer, V48)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    settings = dict(m._SETTINGS)
    settings[layer] = True
    return m.make_agent(m._ROUTES, router=m._router, **settings)


def job(arg):
    layer, seed, sw = arg
    base = kload(V48)
    mod = variant(layer)
    x, y = (base, mod) if sw else (mod, base)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    p, q = r["reward"][::-1] if sw else r["reward"]
    return layer, p, q, r.get("errors")


if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    nseeds = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    layers = ["front_run", "budget_guard", "room_guard",
              "clamp_sells", "dead_stock", "terminal_liquidation"]
    args = [(l, s, sw) for l in layers
            for s in range(start, start + nseeds) for sw in (0, 1)]
    res = list(ProcessPoolExecutor(7).map(job, args))
    for l in layers:
        rows = [r for r in res if r[0] == l]
        w = sum(1 for _, p, q, _ in rows if p > q)
        margin = sum(p - q for _, p, q, _ in rows) / len(rows)
        errs = sum(1 for _, _, _, e in rows if e and e != [None, None])
        print("%-22s mod %2dW-%2dL  mean margin %+7.0f  err_games %d"
              % (l, w, len(rows) - w, margin, errs))
