"""Measure the PAIRED spread, which is what a well-designed offline benchmark actually faces.

The unpaired per-game margin spread is ~6,000, and a power calculation on that says a +277 effect
needs thousands of games -- yet a 480-game holdout separated it cleanly. The reconciliation is that
a benchmark which fixes the seed, the opponent and the seat, and differences two candidates within
that cell, cancels almost all of the variance: both agents meet the same shop draw, the same
opponent and the same market.

This measures both spreads on the same games so the difference is not hand-waved.
"""
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

A = "bench_frozen/A_router.py"
B = "bench_frozen/V_80_10_12.py"
POOL = [
    "rivals/leoprovorov_kaggriculture-v65/main.py",
    "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py",
    "rivals/avioon_kaggriculture-apex-v7-god-emperor/main.py",
]


def _job(a):
    cand, opp, seed, swap = a
    x, y = (opp, cand) if swap else (cand, opp)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    p, q = r["reward"][::-1] if swap else r["reward"]
    return (cand, opp, seed, swap, p - q)


if __name__ == "__main__":
    idx = json.load(open("data/seedindex_700000_1200.json"))
    seeds = [r["seed"] for r in idx][600:660]
    jobs = [(c, o, s, sw) for c in (A, B) for o in POOL for s in seeds for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    by = {}
    for c, o, s, sw, m in res:
        by[(o, s, sw)] = by.get((o, s, sw), {})
        by[(o, s, sw)][c] = m
    cells = [v for v in by.values() if len(v) == 2]
    unpaired = [m for _, _, _, _, m in res]
    diffs = [v[B] - v[A] for v in cells]
    print(f"cells: {len(cells)}   games: {len(res)}\n")
    print(f"UNPAIRED margin      mean {statistics.mean(unpaired):>+9,.0f}   "
          f"sd {statistics.pstdev(unpaired):>9,.0f}")
    print(f"PAIRED   difference  mean {statistics.mean(diffs):>+9,.0f}   "
          f"sd {statistics.pstdev(diffs):>9,.0f}")
    sd = statistics.pstdev(diffs)
    se = sd / len(diffs) ** 0.5
    print(f"\nwith {len(diffs)} paired cells: SE = {se:,.0f}, "
          f"effect/SE = {statistics.mean(diffs)/se:.2f}")
    import math
    for eff in (68, 117, 277, 374):
        n = math.ceil(2 * ((1.959964 + 0.8416212) * sd / eff) ** 2) // 2
        print(f"   effect {eff:>4}: needs ~{n:,} paired cells for 80% power")
    print(f"\nvariance removed by pairing: "
          f"{100*(1 - (sd/statistics.pstdev(unpaired))**2):.1f}%")
