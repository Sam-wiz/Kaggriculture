"""Compare candidates by PAIRED WIN RATE, which is what the ladder and the final fit actually score.

Margin and win rate disagree here: the herd conversion raises mean margin fourfold while lowering
win rate, i.e. it wins bigger and loses more often. Neither the TrueSkill ladder nor the
Bradley-Terry refit sees margin at all, and our own three converged submissions rank by offline win
rate (0.925 / 0.915 / 0.835 -> 2612 / 2547 / 2325) but NOT by offline margin, which puts the top two
backwards. So win rate is the target and margin is the diagnostic.

Reports, per candidate against the same baseline cell-for-cell: wins, losses, the paired
win-rate difference and its standard error (McNemar-style on discordant cells), plus a
population-weighted figure using the measured 6.5% frequency of 3+ yarn draws.
"""
import json
import math
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
BASE = "bench_frozen/V_80_10_12.py"
CANDS = [BASE, "bench_frozen/HV_c2y1.py", "bench_frozen/HV_c3y1.py",
         "bench_frozen/HV_c2y2.py", "bench_frozen/HV_c3y2.py"]
P_HIGH = 0.065          # measured frequency of 3+ YARN_STORE draws


def _job(a):
    c, o, s, sw = a
    x, y = (o, c) if sw else (c, o)
    r = harness.run_episode(x, y, seed=s, catch_errors=True)
    p, q = r["reward"][::-1] if sw else r["reward"]
    return (c, (o, s, sw), 1 if p > q else (0.5 if p == q else 0), p - q)


def run(seeds, label):
    jobs = [(c, o, s, sw) for c in CANDS for o in POOL for s in seeds for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    cell = {}
    for c, key, w, m in res:
        cell.setdefault(key, {})[c] = (w, m)
    print(f"\n{label}  ({len(seeds)} seeds x {len(POOL)} opps x 2 seats = "
          f"{len(seeds)*len(POOL)*2} games each)", flush=True)
    print(f"{'candidate':<20}{'winrate':>9}{'margin':>10}{'dWR':>9}{'SE':>7}{'z':>7}"
          f"{'better':>8}{'worse':>7}")
    out = {}
    for c in CANDS:
        pairs = [(v[BASE][0], v[c][0]) for v in cell.values() if BASE in v and c in v]
        wr = statistics.mean(b for _, b in pairs)
        mg = statistics.mean(v[c][1] for v in cell.values() if c in v)
        up = sum(1 for a, b in pairs if b > a)
        dn = sum(1 for a, b in pairs if b < a)
        d = statistics.mean(b - a for a, b in pairs)
        se = (statistics.pstdev([b - a for a, b in pairs]) / len(pairs) ** 0.5) if len(pairs) > 1 else 0
        z = d / se if se else 0.0
        out[c] = (wr, mg)
        print(f"{os.path.basename(c):<20}{wr:>9.3f}{mg:>+10,.0f}{d:>+9.3f}{se:>7.3f}"
              f"{z:>+7.2f}{up:>8}{dn:>7}", flush=True)
    return out


if __name__ == "__main__":
    idx = json.load(open("data/seedindex_900000_1400.json"))
    hi = [r["seed"] for r in idx if r["yarn"] >= 3][40:85]
    rand = [r["seed"] for r in idx][200:260]
    h = run(hi, "HIGH-YARN (3+), unused seeds")
    r = run(rand, "RANDOM, unused seeds")
    print(f"\nPOPULATION-WEIGHTED (3+ yarn is {P_HIGH:.1%} of games)")
    print(f"{'candidate':<20}{'weighted WR':>13}{'weighted margin':>17}")
    for c in CANDS:
        wr = (1 - P_HIGH) * r[c][0] + P_HIGH * h[c][0]
        mg = (1 - P_HIGH) * r[c][1] + P_HIGH * h[c][1]
        print(f"{os.path.basename(c):<20}{wr:>13.4f}{mg:>+17,.0f}")
