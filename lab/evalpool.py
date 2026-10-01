"""Evaluate an agent against a pool of rivals, both seat orders.

The ladder only scores win/loss, and it pairs you against a spread of opponents,
so the number that matters is the overall win rate across the pool -- not the
bank against any single bot.
"""

import argparse
import glob
import os
import statistics
import sys
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness  # noqa: E402

# Distinct behaviours only -- several published agents are byte-identical forks.
POOL = [
    "rivals/yhay81_the-35-0-tape-a-causal-shop-router/main.py",
    "rivals/boatlee_v29-r1-adaptive-market-hysteresis/main.py",
    "rivals/yhay81_fieldbook-commit-for-three-days/main.py",
    "rivals/kaitofukami_238-238-known-streams-v58-minimax-closed-loop/main.py",
    "rivals/lynnsakurai_farming-score-v5-timing-optimized/main.py",
    "rivals/prvsiyan_kaggriculture-frontier-the-soil-remembers-rain/main.py",
    "rivals/boatlee_v16-rc5-high-score-8c-4s-premium-market-lead/main.py",
    "rivals/romanrozen_strong-barnyard-economist/main.py",
    "rivals/pilkwang_kaggriculture-structured-economic-policy/main.py",
]


def available(paths=None):
    return [p for p in (paths or POOL) if os.path.exists(p)]


def _job(args):
    me, opp, seed, swap = args
    a, b = (opp, me) if swap else (me, opp)
    r = harness.run_episode(a, b, seed=seed, catch_errors=True)
    x, y = r["reward"]
    sx, sy = r["status"]
    if swap:
        x, y = y, x
        sx, sy = sy, sx
    if sx == "ERROR":
        x = -1.0
    return dict(opp=opp, seed=seed, me=x, them=y, err=r["errors"][1 if swap else 0])


def run(me, seeds, pool=None, workers=9, quiet=False):
    pool = available(pool)
    jobs = []
    for opp in pool:
        for s in seeds:
            jobs.append((me, opp, s, False))
            jobs.append((me, opp, s, True))
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(_job, jobs))
    by = defaultdict(list)
    for r in res:
        by[r["opp"]].append(r)
    total_w = total_n = 0
    rows = []
    for opp, rs in by.items():
        w = sum(1 for r in rs if r["me"] > r["them"])
        t = sum(1 for r in rs if r["me"] == r["them"])
        n = len(rs)
        total_w += w + 0.5 * t
        total_n += n
        rows.append((os.path.basename(os.path.dirname(opp))[:38],
                     (w + 0.5 * t) / n, statistics.mean(r["me"] for r in rs),
                     statistics.mean(r["them"] for r in rs), w, n,
                     statistics.mean(r["me"] - r["them"] for r in rs)))
    rows.sort(key=lambda r: r[1])
    if not quiet:
        print(f"{'opponent':<40}{'wr':>7}{'ourBank':>10}{'theirBank':>11}{'margin':>10}{'W/N':>8}")
        for name, wr, mb, tb, w, n, mg in rows:
            print(f"{name:<40}{wr:>7.3f}{mb:>10.0f}{tb:>11.0f}{mg:>10.0f}{f'{w}/{n}':>8}")
        errs = [r["err"] for r in res if r["err"]]
        if errs:
            print("ERRORS:", errs[0][:200])
        print(f"{'OVERALL':<40}{total_w/total_n:>7.3f}"
              f"{statistics.mean(r['me'] for r in res):>10.0f}"
              f"{statistics.mean(r['them'] for r in res):>11.0f}"
              f"{statistics.mean(r['me'] - r['them'] for r in res):>10.0f}"
              f"{f'{int(total_w)}/{total_n}':>8}")
    return total_w / total_n, statistics.mean(r["me"] for r in res)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("-n", type=int, default=4)
    ap.add_argument("--seed0", type=int, default=1)
    ap.add_argument("-w", type=int, default=9)
    a = ap.parse_args()
    run(a.agent, list(range(a.seed0, a.seed0 + a.n)), workers=a.w)
