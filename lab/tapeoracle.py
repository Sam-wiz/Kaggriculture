"""How much is left on the table by the published router's routing rule?

`model.json` is two single-node decision trees over four tapes -- one split at step 144, one at
step 648 -- and that agent still wins 92% against the current meta. So the question worth answering
before building anything is: how much better would PERFECT routing over the same four tapes be?

Pinning each tape for the whole episode gives the per-seed best (the oracle); comparing it to the
shipped rule bounds everything a better router could ever earn without new tapes. If the gap is
large, retraining the router is the lever. If it is small, the lever is more tapes, not better
routing -- and that is a different and much bigger project.
"""
import json
import os
import shutil
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

SRC = "rivals/yhay81_shop-router-0908/pkg"
POOL = [
    "rivals/leoprovorov_kaggriculture-v65/main.py",
    "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py",
    "rivals/avioon_kaggriculture-apex-v7-god-emperor/main.py",
    "rivals/y3uanm_kaggriculture-market-impact-router-v4/main.py",
]


def build_pinned(idx):
    """A copy of the package whose model always returns tape `idx`."""
    out = "bench_frozen/pin%d" % idx
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    for f in ("main.py", "observation.py", "actions.json"):
        shutil.copy(os.path.join(SRC, f), os.path.join(out, f))
    model = json.load(open(os.path.join(SRC, "model.json")))
    model["default"] = idx
    model["stages"] = []          # no decisions: the default tape runs the whole game
    json.dump(model, open(os.path.join(out, "model.json"), "w"))
    return os.path.join(out, "main.py")


def _job(a):
    cand, opp, seed, swap = a
    x, y = (opp, cand) if swap else (cand, opp)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    p, q = r["reward"][::-1] if swap else r["reward"]
    return (cand, (opp, seed, swap), 1 if p > q else (0.5 if p == q else 0), p - q)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    routed = os.path.join(SRC, "main.py")
    pins = [build_pinned(i) for i in range(4)]
    cands = [routed] + pins
    idx = json.load(open("data/seedindex_900000_1400.json"))
    seeds = [r["seed"] for r in idx][300:300 + n]
    jobs = [(c, o, s, sw) for c in cands for o in POOL for s in seeds for sw in (0, 1)]
    print(f"{len(jobs)} games", flush=True)
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=6))
    cell = {}
    for c, k, w, m in res:
        cell.setdefault(k, {})[c] = (w, m)

    print(f"\n{'agent':<28}{'winrate':>9}{'margin':>10}")
    for c in cands:
        rs = [r for r in res if r[0] == c]
        lab = "ROUTED (shipped rule)" if c == routed else "pinned tape %s" % c.split("pin")[1][0]
        print(f"{lab:<28}{statistics.mean(r[2] for r in rs):>9.4f}"
              f"{statistics.mean(r[3] for r in rs):>+10,.0f}")

    full = [v for v in cell.values() if len(v) == len(cands)]
    best_w = statistics.mean(max(v[p][0] for p in pins) for v in full)
    best_m = statistics.mean(max(v[p][1] for p in pins) for v in full)
    rt_w = statistics.mean(v[routed][0] for v in full)
    rt_m = statistics.mean(v[routed][1] for v in full)
    print(f"\n{'ORACLE (best tape per cell)':<28}{best_w:>9.4f}{best_m:>+10,.0f}")
    print(f"{'routed':<28}{rt_w:>9.4f}{rt_m:>+10,.0f}")
    print(f"{'HEADROOM from routing alone':<28}{best_w-rt_w:>+9.4f}{best_m-rt_m:>+10,.0f}")
    print(f"\ncells: {len(full)}")
