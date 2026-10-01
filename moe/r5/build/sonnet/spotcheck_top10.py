"""
r5 sonnet — independent spot check of opus's r4 top-family decode claims (moe/r4/opus.md Q2),
using a fresh random sample and a from-scratch parse (not opus's decode.py/teams.py), as a red-team
cross-check before betting architecture A/C's build effort on those numbers.

Checks, on a fresh random sample of moe/r4/opus.md's data source (mine/top10/*.json.gz, 1,773 games):
  1. Opening signature: step-1 market order list contains both
     ["BUY_ANIMAL","COW",1] and ["BUY_PRODUCT","WHEAT",5] (opus: "6 of top 8"/"the family").
  2. Land timing: step index of the 3rd successful-looking BUY_LAND call among family-opening seats
     (opus: "all 4 quadrants by step ~253", land steps "149/219/253").

Note: mine/top10 is NOT restricted to literal rank<=10 -- it is Kaggle's official daily dump of
top-RATED episodes (median player ~2970 per HANDOFF 09-26a), so "family-opening fraction" here is a
looser population than opus's "6 of top 8" line and is expected to be lower, not an exact match.

Run: .venv/bin/python moe/r5/build/sonnet/spotcheck_top10.py
"""
import gzip
import json
import glob
import random
import statistics
import collections


def has_op(order_list, op, *args):
    for o in order_list:
        if o and o[0] == op and (not args or tuple(o[1:1 + len(args)]) == args):
            return True
    return False


def main(n_sample=120, seed=11):
    files = sorted(glob.glob("mine/top10/*.json.gz"))
    random.seed(seed)
    sample = random.sample(files, min(n_sample, len(files)))

    open_sig = 0
    open_total = 0
    land_count_hist = collections.Counter()
    thirds = []

    for f in sample:
        with gzip.open(f, "rt") as fh:
            d = json.load(fh)
        acts = d["actions"]
        if len(acts) < 2:
            continue
        step1 = acts[1]
        for seat in (0, 1):
            open_total += 1
            mkt = step1[seat]["market"]
            sig = has_op(mkt, "BUY_ANIMAL", "COW", 1) and has_op(mkt, "BUY_PRODUCT", "WHEAT", 5)
            if not sig:
                continue
            open_sig += 1
            land_steps = [t for t, frame in enumerate(acts)
                          if any(o and o[0] == "BUY_LAND" for o in frame[seat]["market"])]
            land_count_hist[len(land_steps)] += 1
            if len(land_steps) >= 3:
                thirds.append(land_steps[2])

    print(f"files on disk: {len(files)}; sampled: {len(sample)}")
    print(f"seats checked: {open_total}; family-opening seats (COW1 + WHEAT5 at step 1): "
          f"{open_sig} ({open_sig/open_total:.2%})")
    print(f"BUY_LAND call-count histogram among family-opening seats: {dict(sorted(land_count_hist.items()))}")
    if thirds:
        print(f"median step of the 3rd BUY_LAND call (proxy for '4th quadrant') among seats with "
              f">=3 calls: {statistics.median(thirds)} (n={len(thirds)}); "
              f"opus's r4 claim: ~253")


if __name__ == "__main__":
    main()
