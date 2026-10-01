"""Round-robin arena for Kaggriculture agents."""
import argparse, os, statistics, sys, time
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness


def _job(args):
    a, b, seed, swapped = args
    t = time.time()
    r = harness.run_episode(a, b, seed=seed)
    x, y = r["reward"]
    sa, sb = r["status"]
    if sa == "ERROR": x = -1.0
    if sb == "ERROR": y = -1.0
    if swapped: x, y = y, x; sa, sb = sb, sa
    return dict(seed=seed, a=x, b=y, sa=sa, sb=sb, t=time.time() - t,
                ea=r["errors"][1 if swapped else 0], eb=r["errors"][0 if swapped else 1])


def duel(a, b, seeds, workers=8, quiet=False):
    jobs = []
    for s in seeds:
        jobs.append((a, b, s, False))
        jobs.append((b, a, s, True))
    if workers > 1:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            res = list(ex.map(_job, jobs))
    else:
        res = [_job(j) for j in jobs]
    wa = sum(1 for r in res if r["a"] > r["b"])
    wb = sum(1 for r in res if r["b"] > r["a"])
    ties = len(res) - wa - wb
    ma = statistics.mean(r["a"] for r in res)
    mb = statistics.mean(r["b"] for r in res)
    errs = [r for r in res if r["sa"] != "DONE" or r["sb"] != "DONE"]
    if not quiet:
        print(f"{str(a):>34} vs {str(b):<34} W{wa}-L{wb}-T{ties}  "
              f"money {ma:9.0f} / {mb:9.0f}  wr={wa/max(1,len(res)):.3f}  "
              f"{statistics.mean(r['t'] for r in res):.1f}s/ep")
        for e in errs[:3]:
            print("   !!", e["sa"], e["sb"], (e["ea"] or e["eb"])[:200] if (e["ea"] or e["eb"]) else "")
    return wa, wb, ties, ma, mb, res


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("a"); ap.add_argument("b")
    ap.add_argument("-n", type=int, default=8)
    ap.add_argument("-w", type=int, default=8)
    ap.add_argument("--seed0", type=int, default=1000)
    args = ap.parse_args()
    seeds = list(range(args.seed0, args.seed0 + args.n))
    duel(args.a, args.b, seeds, workers=args.w)
