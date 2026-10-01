"""Parameter sweep / ablation driver.

Loads an agent module by path, overrides its P dict per trial, and scores the
trial across seeds in parallel. Two scoring modes:
  bank  -- mean final money vs a fixed reference opponent (fast, low variance)
  duel  -- win rate vs an opponent, both seat orders (what the ladder measures)
"""

import argparse
import importlib.util
import itertools
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness  # noqa: E402

_CACHE = {}


def load_module(path, params=None, tag="cand"):
    """Modules are cached per worker process, so P must be reset to its pristine
    defaults on every call -- otherwise overrides from one trial leak into the
    next and the whole comparison is meaningless."""
    key = (path, tag)
    entry = _CACHE.get(key)
    if entry is None:
        name = "tunemod_%s_%d" % (tag, abs(hash(path)) % 100000)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
        entry = (mod, dict(mod.P))
        _CACHE[key] = entry
    mod, defaults = entry
    mod.P.clear()
    mod.P.update(defaults)
    if params:
        mod.P.update(params)
    return mod


def _one(job):
    path, params, opp, seed, swap = job
    mod = load_module(path, params)
    a, b = (opp, mod.agent) if swap else (mod.agent, opp)
    r = harness.run_episode(a, b, seed=seed, catch_errors=True)
    x, y = r["reward"]
    sx, sy = r["status"]
    if swap:
        x, y = y, x
        sx, sy = sy, sx
    if sx == "ERROR":
        return dict(seed=seed, me=-1.0, opp=y, err=r["errors"][1 if swap else 0])
    return dict(seed=seed, me=x, opp=y, err=None)


def score(path, params, opp, seeds, workers, swap_seats=True):
    jobs = []
    for s in seeds:
        jobs.append((path, params, opp, s, False))
        if swap_seats:
            jobs.append((path, params, opp, s, True))
    if workers > 1:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            res = list(ex.map(_one, jobs))
    else:
        res = [_one(j) for j in jobs]
    banks = [r["me"] for r in res]
    wins = sum(1 for r in res if r["me"] > r["opp"])
    ties = sum(1 for r in res if r["me"] == r["opp"])
    errs = [r["err"] for r in res if r["err"]]
    margins = [r["me"] - r["opp"] for r in res]
    return dict(bank=statistics.mean(banks), median=statistics.median(banks),
                lo=min(banks), hi=max(banks), margin=statistics.mean(margins),
                wr=(wins + 0.5 * ties) / len(res), n=len(res), errs=errs[:2])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("--opp", default="starter")
    ap.add_argument("-n", type=int, default=8, help="number of seeds")
    ap.add_argument("--seed0", type=int, default=1)
    ap.add_argument("-w", type=int, default=9)
    ap.add_argument("--noswap", action="store_true")
    ap.add_argument("--grid", default=None,
                    help='JSON dict of param -> list of values, swept as a full grid')
    ap.add_argument("--ablate", default=None,
                    help='JSON dict of param -> value, tested one at a time vs baseline')
    ap.add_argument("--set", default=None, help="JSON dict of fixed param overrides")
    args = ap.parse_args()

    seeds = list(range(args.seed0, args.seed0 + args.n))
    base = json.loads(args.set) if args.set else {}
    swap = not args.noswap

    def run(params, label):
        r = score(args.agent, params, args.opp, seeds, args.w, swap)
        print(f"{label:<46} bank={r['bank']:>8.0f} margin={r['margin']:>9.0f}  "
              f"wr={r['wr']:.3f}  [{r['lo']:.0f}..{r['hi']:.0f}]"
              + (f"  ERR {r['errs'][0][:60]}" if r["errs"] else ""))
        return r

    b = run(dict(base), "baseline")
    if args.ablate:
        for k, v in json.loads(args.ablate).items():
            p = dict(base)
            p[k] = v
            r = run(p, f"{k}={v}")
            print(f"{'':<46}   dBank {r['bank'] - b['bank']:+.0f}  dMargin {r['margin'] - b['margin']:+.0f}")
    if args.grid:
        grid = json.loads(args.grid)
        keys = list(grid)
        best, bestv = None, -1e18
        for combo in itertools.product(*[grid[k] for k in keys]):
            p = dict(base)
            p.update(dict(zip(keys, combo)))
            r = run(p, ", ".join(f"{k}={v}" for k, v in zip(keys, combo)))
            if r["margin"] > bestv:
                best, bestv = dict(zip(keys, combo)), r["margin"]
        print("\nBEST:", best, f"margin={bestv:.0f}")


if __name__ == "__main__":
    main()
