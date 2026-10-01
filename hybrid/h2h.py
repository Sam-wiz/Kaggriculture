"""Head-to-head: A vs B over n seeds, both seat orders, parallel."""
import argparse, os, statistics, sys
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness

def _job(t):
    a, b, seed, swap = t
    x, y = (b, a) if swap else (a, b)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    ra, rb = r["reward"]
    sa, sb = r["status"]
    if swap:
        ra, rb = rb, ra
        sa, sb = sb, sa
    err = r["errors"][1 if swap else 0]
    if sa == "ERROR":
        ra = -1.0
    return dict(seed=seed, swap=swap, a=ra, b=rb, sa=sa, sb=sb, err=err)

def run(a, b, seeds, workers=8, quiet=False):
    jobs = [(a, b, s, sw) for s in seeds for sw in (False, True)]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(_job, jobs))
    w = sum(1 for r in res if r["a"] > r["b"])
    t = sum(1 for r in res if r["a"] == r["b"])
    n = len(res)
    mg = statistics.mean(r["a"] - r["b"] for r in res)
    bad = [r for r in res if r["sa"] != "DONE" or r["sb"] != "DONE"]
    if not quiet:
        print(f"A={os.path.basename(a) if isinstance(a,str) else a}")
        print(f"  wr={(w+0.5*t)/n:.3f}  W/T/N={w}/{t}/{n}  margin={mg:>9.0f}  "
              f"bankA={statistics.mean(r['a'] for r in res):.0f}  bankB={statistics.mean(r['b'] for r in res):.0f}")
        if bad:
            print("  NOT DONE:", [(r['seed'], r['swap'], r['sa'], r['sb'], (r['err'] or '')[:120]) for r in bad[:3]])
    return (w + 0.5 * t) / n, mg, len(bad)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("a"); p.add_argument("b")
    p.add_argument("-n", type=int, default=8)
    p.add_argument("--seed0", type=int, default=1)
    p.add_argument("-w", type=int, default=8)
    ar = p.parse_args()
    run(ar.a, ar.b, list(range(ar.seed0, ar.seed0 + ar.n)), ar.w)
