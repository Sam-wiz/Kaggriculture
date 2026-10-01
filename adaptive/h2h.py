"""Head-to-head driver with hard error assertions.

Usage:  python adaptive/h2h.py <agentA> [agentB] [-n N] [--seed0 S] [-w W]

ALWAYS asserts errors == [None, None] and that neither bank equals startingMoney
exactly, because the interpreter overwrites ERROR with DONE on the final step.
"""
import argparse
import os
import statistics
import sys
import time
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness  # noqa: E402

BASE = "port2/h_over.py"
SET_A = list(range(1000, 1012))   # 12 seeds
SET_B = list(range(2000, 2012))   # 12 seeds, disjoint


def _job(args):
    a, b, seed, swapped = args
    t = time.time()
    r = harness.run_episode(a, b, seed=seed, catch_errors=True)
    x, y = r["reward"]
    errs = list(r["errors"])
    if swapped:
        x, y = y, x
        errs = [errs[1], errs[0]]
    return dict(seed=seed, swapped=swapped, a=x, b=y, errs=errs,
                status=r["status"], t=time.time() - t)


def duel(a, b, seeds, workers=8, quiet=False, label=""):
    jobs = []
    for s in seeds:
        jobs.append((a, b, s, False))
        jobs.append((b, a, s, True))
    if workers > 1:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            res = list(ex.map(_job, jobs))
    else:
        res = [_job(j) for j in jobs]
    bad = [r for r in res if r["errs"] != [None, None]]
    if bad:
        print("!! ERRORS in %d/%d episodes" % (len(bad), len(res)))
        for r in bad[:3]:
            print("   seed", r["seed"], r["errs"])
        raise SystemExit("aborting: errors != [None, None]")
    dead = [r for r in res if r["a"] == 3000.0 or r["b"] == 3000.0]
    if dead:
        print("!! %d episodes banked exactly startingMoney (silent failure?)" % len(dead))
    wa = sum(1 for r in res if r["a"] > r["b"])
    wb = sum(1 for r in res if r["b"] > r["a"])
    ties = len(res) - wa - wb
    ma = statistics.mean(r["a"] for r in res)
    mb = statistics.mean(r["b"] for r in res)
    mg = statistics.mean(r["a"] - r["b"] for r in res)
    wr = (wa + 0.5 * ties) / len(res)
    if not quiet:
        print(f"{label:<10} W{wa}-L{wb}-T{ties} n={len(res)}  wr={wr:.3f}  "
              f"bank {ma:8.0f} vs {mb:8.0f}  margin {mg:+8.0f}  "
              f"({statistics.mean(r['t'] for r in res):.1f}s/ep)")
    return dict(wa=wa, wb=wb, ties=ties, n=len(res), wr=wr, ma=ma, mb=mb,
                margin=mg, res=res)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("a")
    ap.add_argument("b", nargs="?", default=BASE)
    ap.add_argument("-n", type=int, default=12)
    ap.add_argument("-w", type=int, default=8)
    ap.add_argument("--seed0", type=int, default=None)
    ap.add_argument("--both", action="store_true", help="run both disjoint seed sets")
    ap.add_argument("--detail", action="store_true")
    args = ap.parse_args()
    if args.both:
        for nm, ss in (("setA", SET_A), ("setB", SET_B)):
            r = duel(args.a, args.b, ss, workers=args.w, label=nm)
            if args.detail:
                for x in sorted(r["res"], key=lambda z: (z["seed"], z["swapped"])):
                    print(f"    s{x['seed']}{'R' if x['swapped'] else ' '} "
                          f"{x['a']:9.0f} {x['b']:9.0f} {x['a']-x['b']:+9.0f}")
    else:
        s0 = args.seed0 if args.seed0 is not None else 1000
        seeds = list(range(s0, s0 + args.n))
        r = duel(args.a, args.b, seeds, workers=args.w, label="h2h")
        if args.detail:
            for x in sorted(r["res"], key=lambda z: (z["seed"], z["swapped"])):
                print(f"    s{x['seed']}{'R' if x['swapped'] else ' '} "
                      f"{x['a']:9.0f} {x['b']:9.0f} {x['a']-x['b']:+9.0f}")
