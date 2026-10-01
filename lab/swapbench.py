"""Does the demand-matched herd pay? Measured where it bites and where it costs.

The router buys all nine cows on days 0-8, when at most one YARN_STORE is visible, so any swap has
to act on a weak signal. Shops are drawn iid uniform over eight types, so given k yarn stores seen
in the first m unlocks the final count is k + Binomial(8-m, 1/8): seeing 2 by day 8 implies a ~49%
chance of finishing at 3+, seeing 1 implies ~9%. That may still be worth it, because the payoff is
not binary -- wool demand is 2 units per yarn store per firing against milk's fixed ~3 -- but it has
to be measured on both populations:

  HIGH  seeds that finish with 3+ YARN_STOREs  (7% of games, where we lose 16-20k)
  RAND  an unselected sample                    (where a wrong swap costs us)
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
    "rivals/yhay81_public-match-history-router-rating-2929-aug-30/main.py",
]


def _job(a):
    cand, opp, seed, swap = a
    x, y = (opp, cand) if swap else (cand, opp)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    p, q = r["reward"][::-1] if swap else r["reward"]
    return (cand, seed, p - q)


def run(cands, seeds, label):
    jobs = [(c, o, s, sw) for c in cands for o in POOL for s in seeds for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    base = None
    print(f"\n{label}: {len(seeds)} seeds x {len(POOL)} opponents x 2 seats = "
          f"{len(seeds)*len(POOL)*2} games each")
    print(f"{'candidate':<22}{'margin':>10}{'winrate':>9}{'vs base':>10}")
    out = []
    for c in cands:
        m = [r[2] for r in res if r[0] == c]
        mg = statistics.mean(m)
        if base is None:
            base = mg
        out.append((c, mg, sum(1 for x in m if x > 0) / len(m)))
    for c, mg, wr in out:
        print(f"{os.path.basename(c):<22}{mg:>+10,.0f}{wr:>9.3f}{mg-base:>+10,.0f}")
    return out


if __name__ == "__main__":
    idx = json.load(open("data/seedindex_700000_1200.json"))
    hi = [r["seed"] for r in idx if r["yarn"] >= 3][:26]
    rand = [r["seed"] for r in idx][:60]
    cands = sys.argv[1:]
    run(cands, hi, "HIGH-YARN (final 3+)")
    run(cands, rand, "RANDOM sample")
