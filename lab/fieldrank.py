"""Does our offline benchmark predict the LADDER? Rank the 5 submitted builds against a
diverse pool of real published rivals and compare the ordering to their live scores."""
import glob, os, sys, statistics, itertools, json
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

POOL = [
 "rivals/prvsiyan_kaggriculture-frontier-the-moon-counts-melons/main.py",
 "rivals/evelyn3976_kaggriculture-frontier-v156-coherent-liquidity-v6/main.py",
 "rivals/stevenleehans_kaggriculture-x578-i-m-the-strongest/main.py",
 "rivals/indarkarhana_shape-the-shop-work-the-pasture-top-10/main.py",
 "rivals/yhay81_public-match-history-router-rating-2929-aug-30/main.py",
 "rivals/kaitofukami_238-238-known-streams-v58-minimax-closed-loop/main.py",
 "rivals/yhay81_fieldbook-commit-for-three-days/main.py",
 "rivals/prvsiyan_kaggle-frontier-lab-strategy-improvement/main.py",
 "rivals/romanrozen_strong-barnyard-economist/main.py",
 "rivals/evelyn3976_kaggriculture-v6-limited-dynamic-v8/main.py",
 "rivals/desyatio_93-wr-vs-kaito-s-v21-1-local-tuning-experiment/main.py",
 "rivals/boatlee_v29-r1-adaptive-market-hysteresis/main.py",
 "rivals/hboyang_kitex-v0/main.py",
 "rivals2/salem2900.py",
]

BUILDS = [("sub_hover", "sub_hover.py", 2609.9), ("sub_tuned", "sub_tuned.py", 2573.0),
          ("sub_final", "sub_final.py", 2437.4), ("sub_impact", "sub_impact.py", 2396.6),
          ("sub_slot", "sub_slot.py", 2304.0)]


def _job(a):
    me, opp, seed, swap = a
    x, y = (opp, me) if swap else (me, opp)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    p, q = r["reward"][::-1] if swap else r["reward"]
    return (me, opp, p, q)


if __name__ == "__main__":
    seeds = list(range(101, 101 + int(sys.argv[1] if len(sys.argv) > 1 else 10)))
    jobs = [(b[1], o, s, sw) for b in BUILDS for o in POOL for s in seeds for sw in (0, 1)]
    print(f"{len(jobs)} games", flush=True)
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=8))
    print(f"\n{'build':<12}{'ladder':>9}{'margin':>11}{'winrate':>9}{'ourBank':>10}")
    out = []
    for name, path, lad in BUILDS:
        rs = [r for r in res if r[0] == path]
        m = [r[2] - r[3] for r in rs]
        wr = sum(1 for x in m if x > 0) / len(m)
        out.append((name, lad, statistics.mean(m), wr, statistics.mean(r[2] for r in rs)))
        print(f"{name:<12}{lad:>9.1f}{statistics.mean(m):>11,.0f}{wr:>9.3f}"
              f"{statistics.mean(r[2] for r in rs):>10,.0f}")
    def spearman(a, b):
        ra = {v: i for i, v in enumerate(sorted(a))}
        rb = {v: i for i, v in enumerate(sorted(b))}
        x = [ra[v] for v in a]; y = [rb[v] for v in b]
        n = len(x); mx = sum(x)/n; my = sum(y)/n
        num = sum((p-mx)*(q-my) for p, q in zip(x, y))
        den = (sum((p-mx)**2 for p in x)*sum((q-my)**2 for q in y))**0.5
        return num/den if den else 0.0
    lad = [o[1] for o in out]
    print(f"\nSpearman(ladder, margin)  = {spearman(lad,[o[2] for o in out]):+.3f}")
    print(f"Spearman(ladder, winrate) = {spearman(lad,[o[3] for o in out]):+.3f}")
    print(f"Spearman(ladder, ourBank) = {spearman(lad,[o[4] for o in out]):+.3f}")
    json.dump([list(r) for r in res], open("data/fieldrank.json", "w"))
