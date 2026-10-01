"""Compare the market-model overlay against what is live, fit then holdout.

Candidates:
  A_router      the public-state router, bare
  V_80_10_12    + price-impact slot ordering + shed vent      (this is sub_vent.py, live now)
  M_model       + price-impact slot ordering + market model   (the h_over overlay, ported)
  MV_model_vent + slot ordering + market model + shed vent

The model and the vent attack the same constraint from different ends -- the model meters sales
against a shed target using a town-drain forecast, the vent just dumps whatever is about to overflow
-- so the combination could be redundant or could conflict. That is why all four run.
"""
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

POOL = [
    "rivals/leoprovorov_kaggriculture-v65/main.py",
    "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py",
    "rivals/avioon_kaggriculture-apex-v7-god-emperor/main.py",
    "rivals/y3uanm_kaggriculture-market-impact-router-v4/main.py",
]
CANDS = [
    "bench_frozen/A_router.py",
    "bench_frozen/V_80_10_12.py",
    "bench_frozen/M_model.py",
    "bench_frozen/MV_model_vent.py",
]


def _job(a):
    c, o, s, sw = a
    x, y = (o, c) if sw else (c, o)
    r = harness.run_episode(x, y, seed=s, catch_errors=True)
    p, q = r["reward"][::-1] if sw else r["reward"]
    return (c, p - q)


def run(seeds, label):
    jobs = [(c, o, s, sw) for c in CANDS for o in POOL for s in seeds for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    print(f"\n{label}  ({len(seeds)} seeds x {len(POOL)} opponents x 2 seats = "
          f"{len(seeds)*len(POOL)*2} games each)", flush=True)
    print(f"{'candidate':<24}{'margin':>10}{'winrate':>9}{'vs router':>11}")
    base = None
    out = []
    for c in CANDS:
        m = [r[1] for r in res if r[0] == c]
        mg = statistics.mean(m)
        if base is None:
            base = mg
        out.append((c, mg, sum(1 for x in m if x > 0) / len(m)))
    for c, mg, wr in sorted(out, key=lambda r: -r[1]):
        print(f"{os.path.basename(c):<24}{mg:>+10,.0f}{wr:>9.3f}{mg-base:>+11,.0f}", flush=True)
    return out


if __name__ == "__main__":
    idx = json.load(open("data/seedindex_700000_1200.json"))
    seeds = [r["seed"] for r in idx]
    run(seeds[100:150], "FIT")
    run(seeds[400:460], "HOLDOUT (unseen seeds)")
