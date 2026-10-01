"""Benchmark candidates against the CURRENT meta, not the stale rival set.

The old pool (rivals/ as of Sept 3) is far too weak -- every member loses to us by 15-27k, so it
cannot discriminate between candidates and it flattered h_over, which dies against any aggressive
opponent. This pool is the strongest published agents as of Sept 6.
"""
import os, sys, statistics
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

POOL = [
 ("router", "rivals/thomastschinkel_kaggriculture-public-state-router-74-5-win-rate/main.py"),
 ("wheat-remembers", "rivals/prvsiyan_where-the-wheat-remembers-tomorrow-kaggriculture/main.py"),
 ("lynn-math", "rivals/lynnsakurai_farming-score-a-mathematical-approach/main.py"),
 ("apex-v7", "rivals/avioon_kaggriculture-apex-v7-god-emperor/main.py"),
 ("tetsutani-new", "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py"),
 ("v65", "rivals/leoprovorov_kaggriculture-v65/main.py"),
 ("moon-melons", "rivals/prvsiyan_kaggriculture-frontier-the-moon-counts-melons/main.py"),
 ("coherent-liq", "rivals/evelyn3976_kaggriculture-frontier-v156-coherent-liquidity-v6/main.py"),
 ("x578", "rivals/stevenleehans_kaggriculture-x578-i-m-the-strongest/main.py"),
 ("yhay-2929", "rivals/yhay81_public-match-history-router-rating-2929-aug-30/main.py"),
]


def _job(a):
    me, opp, seed, swap = a
    x, y = (opp, me) if swap else (me, opp)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    p, q = r["reward"][::-1] if swap else r["reward"]
    return (me, opp, p, q)


def run(cands, seeds, workers=7, detail=True):
    jobs = [(c, p, s, sw) for c in cands for _, p in POOL for s in seeds for sw in (0, 1)
            if os.path.basename(os.path.dirname(p)) not in c]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    print(f"{'candidate':<26}{'margin':>10}{'winrate':>9}{'ourBank':>10}{'games':>7}")
    out = []
    for c in cands:
        rs = [r for r in res if r[0] == c]
        m = [r[2] - r[3] for r in rs]
        out.append((c, statistics.mean(m), sum(1 for x in m if x > 0) / len(m),
                    statistics.mean(r[2] for r in rs), len(m)))
    for c, mg, wr, ob, n in sorted(out, key=lambda r: -r[1]):
        print(f"{os.path.basename(c):<26}{mg:>+10,.0f}{wr:>9.3f}{ob:>10,.0f}{n:>7}")
    if detail:
        print()
        for c in cands:
            print(f"  -- {os.path.basename(c)}")
            for nm, p in POOL:
                rs = [r for r in res if r[0] == c and r[1] == p]
                if not rs: continue
                m = [r[2] - r[3] for r in rs]
                print(f"     {nm:<20}{statistics.mean(m):>+10,.0f}"
                      f"{sum(1 for x in m if x>0)/len(m):>8.2f}")
    return out


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    run(sys.argv[2:] or ["sub_router.py", "sub_final.py", "sub_hover.py"],
        list(range(3000, 3000 + n)))
