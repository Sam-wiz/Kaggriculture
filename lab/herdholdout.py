"""Validate the chain-conversion herd on seeds from a different index entirely.

The +2,187 on high-yarn seeds was measured on the same set the conversion count was chosen on, so
it is a fit-set maximum. This re-runs on seeds 900000+ (a separate index built after the parameter
was picked) for both populations: the high-yarn draws the change targets, and an unselected sample
where it must not cost anything.
"""
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

POOL = [
    "rivals/leoprovorov_kaggriculture-v65/main.py",
    "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py",
    "rivals/avioon_kaggriculture-apex-v7-god-emperor/main.py",
    "rivals/y3uanm_kaggriculture-market-impact-router-v4/main.py",
]
CANDS = [
    "bench_frozen/A_router.py",
    "bench_frozen/V_80_10_12.py",
    "bench_frozen/HV_c2y1.py",
    "bench_frozen/HV_c3y1.py",
]


def _job(a):
    c, o, s, sw = a
    x, y = (o, c) if sw else (c, o)
    r = harness.run_episode(x, y, seed=s, catch_errors=True)
    p, q = r["reward"][::-1] if sw else r["reward"]
    return (c, (o, s, sw), p - q)


def run(seeds, label):
    jobs = [(c, o, s, sw) for c in CANDS for o in POOL for s in seeds for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    cells = {}
    for c, key, m in res:
        cells.setdefault(key, {})[c] = m
    base = CANDS[0]
    print(f"\n{label}  ({len(seeds)} seeds x {len(POOL)} opponents x 2 seats = "
          f"{len(seeds)*len(POOL)*2} games each)", flush=True)
    print(f"{'candidate':<22}{'margin':>10}{'winrate':>9}{'vs router':>11}{'paired sd':>11}")
    for c in CANDS:
        m = [r[2] for r in res if r[0] == c]
        d = [v[c] - v[base] for v in cells.values() if base in v and c in v]
        sd = statistics.pstdev(d) if len(d) > 1 else 0.0
        print(f"{os.path.basename(c):<22}{statistics.mean(m):>+10,.0f}"
              f"{sum(1 for x in m if x>0)/len(m):>9.3f}{statistics.mean(d):>+11,.0f}"
              f"{sd:>11,.0f}", flush=True)


if __name__ == "__main__":
    idx = json.load(open("data/seedindex_900000_1400.json"))
    hi = [r["seed"] for r in idx if r["yarn"] >= 3][:40]
    rand = [r["seed"] for r in idx][:50]
    run(hi, "HOLDOUT HIGH-YARN (3+), seeds 900000+")
    run(rand, "HOLDOUT RANDOM, seeds 900000+")
