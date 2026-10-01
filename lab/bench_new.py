"""Screen new kernels head-to-head vs the live base, paired seeds x both seats.

Loads every agent the way Kaggle does (exec, last callable) so shims and
weirdly-named entry points are handled faithfully.
"""
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

BASE = "subF_v45.py"
CANDS = {
    "v48": "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py",
    "v47": "rivals/ahmedberatozer_kaggriculture-v47-reactive-market-coordination/v47_main.py",
    "v46": "rivals/ahmedberatozer_kaggriculture-v46-first-turn-microstructure-and-s/_entry.py",
    "pipe7": "rivals/nathanjacob_kaggriculture-pipe-7-wheat-microstructure/_entry.py",
    "aurax7": "rivals/aurax7_kaggriculture-shop-router-reactive-v7/_entry.py",
    "alperen": "rivals/alperen5252525_kaggriculture-ready-stock-earlier-sales/_entry.py",
}


def kload(path):
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


def _job(a):
    cand_path, base_path, s, sw = a
    cand = kload(cand_path)
    base = kload(base_path)
    x, y = (base, cand) if sw else (cand, base)
    r = harness.run_episode(x, y, seed=s, catch_errors=True)
    p, q = r["reward"][::-1] if sw else r["reward"]
    return (s, sw, p, q, r["errors"])


def main():
    seeds = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else list(range(2000, 2040))
    only = sys.argv[2].split(",") if len(sys.argv) > 2 else list(CANDS)
    jobs = [(CANDS[c], BASE, s, sw) for c in only for s in seeds for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=2))
    out = {}
    for (s, sw, p, q, errs) in res:
        # figure which cand by matching job order is fragile; recompute via index instead
        pass
    # simpler: res order == jobs order
    agg = {c: {"w": 0, "l": 0, "t": 0, "m": [], "err": 0} for c in only}
    for job, (s, sw, p, q, errs) in zip(jobs, res):
        cname = [k for k, v in CANDS.items() if v == job[0]][0]
        a = agg[cname]
        if errs[0] or errs[1]:
            a["err"] += 1
        a["m"].append(p - q)
        a["w" if p > q else "l" if p < q else "t"] += 1
    for c in only:
        a = agg[c]
        n = len(a["m"])
        mm = sum(a["m"]) / n
        print(f"{c:8s}  W{a['w']}-L{a['l']}-T{a['t']}  wr={a['w']/n:.3f}  margin={mm:+,.0f}  errs={a['err']}")
    json.dump({c: agg[c]["m"] for c in only}, open("bench_new_margins.json", "w"))


if __name__ == "__main__":
    main()
