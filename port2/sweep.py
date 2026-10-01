"""Sweep a port2 candidate's P dict against the FULL rival pool.

tune.py scores bank against one reference opponent; the ladder scores win rate
across a spread, and this tape's margin is dominated by a single mirror match,
so every sweep here runs the whole evalpool set.

  --grid  '{"interval": [36, 72, 144]}'      full cartesian product
  --ablate '{"protect": 0, "sales_first": 0}' one change at a time vs baseline
"""
import argparse
import itertools
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import evalpool  # noqa: E402
import harness  # noqa: E402
import tune  # noqa: E402


def _job(args):
    path, params, opp, seed, swap = args
    mod = tune.load_module(path, params, tag="sweep")
    a, b = (opp, mod.agent) if swap else (mod.agent, opp)
    r = harness.run_episode(a, b, seed=seed, catch_errors=True)
    x, y = r["reward"]
    e = list(r["errors"])
    if swap:
        x, y = y, x
        e = [e[1], e[0]]
    return dict(opp=opp, seed=seed, me=x, them=y, err=e)


def score(path, params, seeds, workers, pool=None):
    pool = evalpool.available(pool)
    jobs = [(path, params, opp, s, sw) for opp in pool for s in seeds for sw in (False, True)]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(_job, jobs))
    w = sum(1 for r in res if r["me"] > r["them"])
    t = sum(1 for r in res if r["me"] == r["them"])
    n = len(res)
    errs = [r for r in res if r["err"] != [None, None]]
    return dict(wr=(w + 0.5 * t) / n, w=w, t=t, n=n,
                bank=statistics.mean(r["me"] for r in res),
                margin=statistics.mean(r["me"] - r["them"] for r in res),
                errs=len(errs), err0=(errs[0]["err"] if errs else None),
                b3000=sum(1 for r in res if r["me"] == 3000.0), res=res)


def show(label, r, base=None):
    line = (f"{label:<52} wr={r['wr']:.3f} ({r['w']}W {r['t']}T/{r['n']})"
            f"  bank={r['bank']:>8.0f}  margin={r['margin']:>+8.0f}")
    if base is not None:
        line += f"   dWR={r['wr'] - base['wr']:+.3f} dM={r['margin'] - base['margin']:+.0f}"
    if r["errs"]:
        line += f"   !! ERRORS={r['errs']} {str(r['err0'])[:60]}"
    if r["b3000"]:
        line += f"   !! bank3000 x{r['b3000']}"
    print(line, flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("-n", type=int, default=4)
    ap.add_argument("--seed0", type=int, default=1)
    ap.add_argument("-w", type=int, default=8)
    ap.add_argument("--set", default=None)
    ap.add_argument("--grid", default=None)
    ap.add_argument("--ablate", default=None)
    a = ap.parse_args()

    path = a.agent if os.path.isabs(a.agent) else os.path.join(ROOT, a.agent)
    seeds = list(range(a.seed0, a.seed0 + a.n))
    base_params = json.loads(a.set) if a.set else {}
    print(f"{a.agent}  seeds {seeds[0]}..{seeds[-1]}  base={base_params}")
    base = score(path, dict(base_params), seeds, a.w)
    show("baseline", base)

    if a.ablate:
        for k, v in json.loads(a.ablate).items():
            p = dict(base_params)
            p[k] = v
            show(f"{k}={v}", score(path, p, seeds, a.w), base)
    if a.grid:
        grid = json.loads(a.grid)
        keys = list(grid)
        rows = []
        for combo in itertools.product(*[grid[k] for k in keys]):
            p = dict(base_params)
            p.update(dict(zip(keys, combo)))
            lbl = ", ".join(f"{k}={v}" for k, v in zip(keys, combo))
            r = score(path, p, seeds, a.w)
            show(lbl, r, base)
            rows.append((r["wr"], r["margin"], lbl))
        rows.sort(reverse=True)
        print("\nTOP:")
        for wr, m, lbl in rows[:8]:
            print(f"   wr={wr:.3f} margin={m:+.0f}   {lbl}")


if __name__ == "__main__":
    main()
