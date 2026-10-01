"""Head-to-head side/farm.py vs port2/h_over.py, both seat orders, in parallel.

Always asserts errors == [None, None]: the interpreter stamps DONE over an
ERROR status on the final step, and a crashed agent banks exactly startingMoney,
so neither the status nor a plausible-looking bank proves anything.
"""
import argparse
import importlib.util
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
import harness  # noqa: E402

CAND = os.path.join(REPO, "side", "farm.py")
REF = os.path.join(REPO, "port2", "h_over.py")
_CACHE = {}


def load(path, tag, params=None):
    key = (path, tag)
    ent = _CACHE.get(key)
    if ent is None:
        name = "m_%s_%d" % (tag, abs(hash(path)) % 99991)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
        ent = (mod, dict(mod.P))
        _CACHE[key] = ent
    mod, base = ent
    mod.P.clear()
    mod.P.update(base)
    if params:
        mod.P.update(params)
    return mod


def _job(job):
    params, seed, swap, cand, ref = job
    c = load(cand, "cand", params).agent
    r = load(ref, "ref").agent
    a, b = (r, c) if swap else (c, r)
    res = harness.run_episode(a, b, seed=seed, catch_errors=True)
    if res["errors"] != [None, None]:
        return dict(seed=seed, swap=swap, me=-1.0, them=0.0, err=str(res["errors"]))
    x, y = res["reward"]
    if swap:
        x, y = y, x
    return dict(seed=seed, swap=swap, me=x, them=y, err=None)


def run(params, seeds, workers, cand=CAND, ref=REF, quiet=False):
    jobs = [(params, s, sw, cand, ref) for s in seeds for sw in (False, True)]
    if workers > 1:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            res = list(ex.map(_job, jobs))
    else:
        res = [_job(j) for j in jobs]
    errs = [r["err"] for r in res if r["err"]]
    assert not errs, "AGENT ERRORS: %s" % errs[:2]
    marg = [r["me"] - r["them"] for r in res]
    w = sum(1 for r in res if r["me"] > r["them"])
    t = sum(1 for r in res if r["me"] == r["them"])
    out = dict(n=len(res), wins=w, ties=t, wr=(w + 0.5 * t) / len(res),
               margin=statistics.mean(marg), med=statistics.median(marg),
               bank=statistics.mean(r["me"] for r in res),
               ref=statistics.mean(r["them"] for r in res),
               lo=min(marg), hi=max(marg))
    if not quiet:
        print(f"  n={out['n']:>3} W-L-T {w}-{len(res)-w-t}-{t}  wr={out['wr']:.3f}  "
              f"margin={out['margin']:>+9.0f} (med {out['med']:>+8.0f}, "
              f"[{out['lo']:>+8.0f}..{out['hi']:>+8.0f}])  bank={out['bank']:>8.0f} "
              f"ref={out['ref']:>8.0f}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", type=int, default=8)
    ap.add_argument("--seed0", type=int, default=1)
    ap.add_argument("-w", type=int, default=9)
    ap.add_argument("--set", default=None)
    ap.add_argument("--grid", default=None)
    ap.add_argument("--ablate", default=None)
    ap.add_argument("--cand", default=CAND)
    a = ap.parse_args()
    seeds = list(range(a.seed0, a.seed0 + a.n))
    base = json.loads(a.set) if a.set else {}
    print("seeds", seeds[0], "..", seeds[-1])
    print("baseline", base)
    b = run(dict(base), seeds, a.w, cand=a.cand)
    if a.ablate:
        for k, v in json.loads(a.ablate).items():
            p = dict(base)
            p[k] = v
            print(f"{k}={v}")
            r = run(p, seeds, a.w, cand=a.cand)
            print(f"    dMargin {r['margin'] - b['margin']:+.0f}")
    if a.grid:
        import itertools
        g = json.loads(a.grid)
        keys = list(g)
        best, bv = None, -1e18
        for combo in itertools.product(*[g[k] for k in keys]):
            p = dict(base)
            p.update(dict(zip(keys, combo)))
            print(", ".join(f"{k}={v}" for k, v in zip(keys, combo)))
            r = run(p, seeds, a.w, cand=a.cand)
            if r["margin"] > bv:
                best, bv = dict(zip(keys, combo)), r["margin"]
        print("\nBEST:", best, "margin=%.0f" % bv)


if __name__ == "__main__":
    main()
