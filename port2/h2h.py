"""Head-to-head: a port2 candidate vs port/main.py, both seat orders.

Always checks r["errors"] == [None, None]; a broken agent banks exactly 3000.
"""
import argparse
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import harness  # noqa: E402
import tune  # noqa: E402

REF = os.path.join(ROOT, "port/main.py")


def _job(args):
    path, params, opp, seed, swap = args
    mod = tune.load_module(path, params, tag="h2h")
    a, b = (opp, mod.agent) if swap else (mod.agent, opp)
    r = harness.run_episode(a, b, seed=seed, catch_errors=True)
    x, y = r["reward"]
    e = list(r["errors"])
    if swap:
        x, y = y, x
        e = [e[1], e[0]]
    return dict(seed=seed, swap=swap, me=x, them=y, err=e)


def run(path, params, seeds, workers=8, opp=REF, quiet=False):
    jobs = [(path, params, opp, s, sw) for s in seeds for sw in (False, True)]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(_job, jobs))
    errs = [r for r in res if r["err"] != [None, None]]
    banked3000 = [r for r in res if r["me"] == 3000.0]
    w = sum(1 for r in res if r["me"] > r["them"])
    t = sum(1 for r in res if r["me"] == r["them"])
    n = len(res)
    margin = statistics.mean(r["me"] - r["them"] for r in res)
    out = dict(wr=(w + 0.5 * t) / n, w=w, t=t, n=n, margin=margin,
               bank=statistics.mean(r["me"] for r in res),
               theirs=statistics.mean(r["them"] for r in res),
               errs=len(errs), b3000=len(banked3000))
    if not quiet:
        print(f"  wr={out['wr']:.3f} ({w}W {t}T /{n})  bank={out['bank']:.0f} "
              f"vs {out['theirs']:.0f}  margin={margin:+.0f}  "
              f"errors={len(errs)} bank3000={len(banked3000)}")
        if errs:
            print("   ERR:", errs[0]["err"])
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("-n", type=int, default=8)
    ap.add_argument("--seed0", type=int, default=1)
    ap.add_argument("-w", type=int, default=8)
    ap.add_argument("--set", default=None)
    ap.add_argument("--opp", default=REF)
    a = ap.parse_args()
    seeds = list(range(a.seed0, a.seed0 + a.n))
    params = json.loads(a.set) if a.set else None
    print(f"{a.agent} vs {os.path.relpath(a.opp, ROOT) if a.opp.endswith('.py') else a.opp} "
          f"seeds {seeds[0]}..{seeds[-1]}  set={params}")
    run(os.path.join(ROOT, a.agent) if not os.path.isabs(a.agent) else a.agent,
        params, seeds, a.w, a.opp)
