"""Field benchmark: candidate builds vs rival pool, both seats, N seeds."""
import sys, statistics
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, '.')
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
]


def _job(a):
    me, opp, seed, swap = a
    x, y = (opp, me) if swap else (me, opp)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    p, q = r["reward"][::-1] if swap else r["reward"]
    return (me, opp, p - q, p)


if __name__ == "__main__":
    builds = sys.argv[1].split(',')
    seeds = list(range(int(sys.argv[2]), int(sys.argv[2]) + int(sys.argv[3] if len(sys.argv) > 3 else 8)))
    jobs = [(b, o, s, sw) for b in builds for o in POOL for s in seeds for sw in (0, 1)]
    print(f"{len(jobs)} games", flush=True)
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=8))
    for b in builds:
        rs = [r for r in res if r[0] == b]
        m = [r[2] for r in rs]
        wr = sum(1 for x in m if x > 0) / len(m)
        ties = sum(1 for x in m if x == 0)
        print(f"{b:24s} winrate={wr:.3f} ties={ties} avg_margin={statistics.mean(m):+7.0f} avg_bank={statistics.mean(r[3] for r in rs):7.0f}", flush=True)
        # per-rival
        for o in POOL:
            rr = [r for r in rs if r[1] == o]
            mm = [r[2] for r in rr]
            w = sum(1 for x in mm if x > 0); l = sum(1 for x in mm if x < 0)
            oname = o.split('/')[-2][:30]
            print(f"    {oname:32s} {w}W-{l}L margin={statistics.mean(mm):+6.0f}", flush=True)
