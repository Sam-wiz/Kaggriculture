"""What is occupying the shed when it binds, and what does the engine discard?

A reviewer's claim: WHEAT and FERTILIZER are the only two items the engine lets you BUY back
(`BUY_PRODUCT` is honoured for exactly those), and both need thousands of surplus units to move
their price -- so the market is a near-free warehouse for them. Anything deep-market sitting in a
capped 100-item shed is therefore occupying a slot whose opportunity cost is a wool unit that gets
discarded instead.

Two things to check on data already in hand:
  1. the shed's composition through days 18-25, when it runs at 76-100 of cap
  2. which item the end-of-day routine actually drops when it runs out of room
"""
import collections
import glob
import gzip
import json
import os
import statistics

ROOT = os.path.dirname(os.path.abspath(__file__))
DEEP = ("WHEAT", "FERTILIZER", "EGG")      # >4,000 surplus units to halve
THIN = ("STRAWBERRY", "MILK", "WOOL", "MELON", "CARROT", "TOMATO")


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "mine/loss/*.json.gz")))
    comp = collections.Counter()
    n_rows = 0
    at_cap = 0
    cap_comp = collections.Counter()
    per_game_deep = []
    for p in files:
        d = json.load(gzip.open(p, "rt"))
        me = d["our_seat"]
        deep_share = []
        for r in d["trace"]:
            day = r["t"] // 24
            # The replay stores each step's PRE-action observation and
            # `_drop_inventories_to_shed` runs at end of day, so hour 23 is the daily trough
            # (everything sold off, nothing dropped in yet) and hour 0 is the peak.
            if not (18 <= day <= 25) or r["t"] % 24 != 0:
                continue
            shed = r["shed"][me] or {}
            tot = sum(shed.values())
            if tot <= 0:
                continue
            n_rows += 1
            for k, v in shed.items():
                comp[k] += v
            deep_share.append(sum(shed.get(k, 0) for k in DEEP) / tot)
            if tot >= 95:
                at_cap += 1
                for k, v in shed.items():
                    cap_comp[k] += v
        if deep_share:
            per_game_deep.append(statistics.mean(deep_share))

    tot = sum(comp.values())
    print(f"{len(files)} games, {n_rows} end-of-day snapshots in days 18-25 "
          f"({at_cap} of them at >=95/100)\n")
    print("SHED COMPOSITION, days 18-25")
    print(f"{'item':<14}{'share':>8}{'mean units':>12}{'class':>8}")
    for k, v in comp.most_common():
        cls = "deep" if k in DEEP else ("thin" if k in THIN else "")
        print(f"{k:<14}{v/tot:>8.1%}{v/max(1,n_rows):>12.1f}{cls:>8}")
    deep = sum(comp.get(k, 0) for k in DEEP)
    print(f"\ndeep-market items (buyable back, price barely moves): {deep/tot:.1%} of the shed")
    print(f"per-game mean deep share: {statistics.mean(per_game_deep):.1%} "
          f"(median {statistics.median(per_game_deep):.1%})")

    if at_cap:
        ct = sum(cap_comp.values())
        print(f"\nWHEN THE SHED IS AT >=95/100 ({at_cap} snapshots):")
        for k, v in cap_comp.most_common(6):
            cls = "deep" if k in DEEP else "thin"
            print(f"   {k:<14}{v/ct:>7.1%}  {cls}")
        capdeep = sum(cap_comp.get(k, 0) for k in DEEP)
        print(f"   -> {capdeep/ct:.1%} of a FULL shed is items we could have parked in the market")
        print(f"   -> that is {capdeep/max(1,at_cap):.0f} slots per snapshot")


if __name__ == "__main__":
    main()
