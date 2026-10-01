"""Sweep the shed-vent parameters, then confirm the pick on seeds it never saw.

The vent is the only intervention that measured positive on both populations (+247 on a random
sample, +175 on high-yarn draws), so it is worth tuning -- but a grid search reports its own maximum
whether or not there is a signal, which is how the tape patches fooled me. Fit on FIT seeds, choose,
then read HOLD once.
"""
import json
import os
import statistics
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

POOL = [
    "rivals/leoprovorov_kaggriculture-v65/main.py",
    "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py",
    "rivals/avioon_kaggriculture-apex-v7-god-emperor/main.py",
]
GRID = [(hi, px, q) for hi in (70, 80, 90) for px in (10, 40) for q in (6, 12)]


def build(hi, px, q):
    path = "bench_frozen/V_%d_%d_%d.py" % (hi, px, q)
    if not os.path.exists(path):
        subprocess.run([sys.executable, "mkvent.py", path, str(hi), str(px), str(q)],
                       capture_output=True)
    return path


def _job(a):
    cand, opp, seed, swap = a
    x, y = (opp, cand) if swap else (cand, opp)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    p, q = r["reward"][::-1] if swap else r["reward"]
    return (cand, p - q)


def run(cands, seeds, label):
    jobs = [(c, o, s, sw) for c in cands for o in POOL for s in seeds for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    out = []
    for c in cands:
        m = [r[1] for r in res if r[0] == c]
        out.append((c, statistics.mean(m), sum(1 for x in m if x > 0) / len(m), len(m)))
    print(f"\n{label}  ({len(seeds)} seeds x {len(POOL)} opps x 2 seats)")
    print(f"{'variant':<22}{'margin':>10}{'winrate':>9}{'vs base':>10}{'n':>6}")
    base = next(m for c, m, _, _ in out if "A_router" in c)
    for c, m, wr, n in sorted(out, key=lambda r: -r[1]):
        print(f"{os.path.basename(c):<22}{m:>+10,.0f}{wr:>9.3f}{m-base:>+10,.0f}{n:>6}")
    return out


if __name__ == "__main__":
    idx = json.load(open("data/seedindex_700000_1200.json"))
    seeds = [r["seed"] for r in idx]
    fit, hold = seeds[100:150], seeds[400:460]
    cands = ["bench_frozen/A_router.py"] + [build(*g) for g in GRID]
    out = run(cands, fit, "FIT")
    best = max((r for r in out if "A_router" not in r[0]), key=lambda r: r[1])[0]
    print(f"\npicked on FIT: {os.path.basename(best)}")
    run(["bench_frozen/A_router.py", best], hold, "HOLDOUT (unseen seeds)")
