"""What the opponents who out-sold us on wool actually bought, and when.

Animals, land, seeds and feed are all bought through the MARKET order stream (BUY_ANIMAL / BUY_LAND
/ BUY_SEED / BUY_PRODUCT), not through unit actions -- an earlier version of this script looked in
the unit stream, found nothing, and reported "nobody buys animals", which was a decoder bug.

Note BUY_PRODUCT is honoured by the engine only for WHEAT and FERTILIZER; any other item is
rejected outright, so those orders are wasted slots rather than a strategy.
"""
import collections
import glob
import gzip
import json
import os
import statistics

ROOT = os.path.dirname(os.path.abspath(__file__))
VALID_BUY_PRODUCT = ("WHEAT", "FERTILIZER")


def decode(path):
    d = json.load(gzip.open(path, "rt"))
    me, tr, acts = d["our_seat"], d["trace"], d["actions"]
    if not tr:
        return None
    qty = [collections.Counter(), collections.Counter()]
    days = [collections.defaultdict(list), collections.defaultdict(list)]
    sells = [collections.Counter(), collections.Counter()]
    waste = [0, 0]
    for t, pair in enumerate(acts):
        for s in (0, 1):
            for o in ((pair[s] or {}).get("market") or []):
                if not o:
                    continue
                op = o[0]
                item = o[1] if len(o) > 1 else ""
                n = int(o[2]) if len(o) > 2 else 1
                if op == "SELL":
                    sells[s][item] += n
                elif op == "BUY_ANIMAL":
                    qty[s][item] += n
                    days[s][item] += [t // 24] * n
                elif op == "BUY_LAND":
                    qty[s]["LAND"] += n
                    days[s]["LAND"] += [t // 24] * n
                elif op == "BUY_PRODUCT" and item not in VALID_BUY_PRODUCT:
                    waste[s] += 1
    return dict(ep=d["episode_id"], opp=d["teams"][1 - me],
                yarn=tr[-1]["shops"].count("YARN_STORE"),
                margin=d["rewards"][me] - d["rewards"][1 - me],
                oq=qty[me], tq=qty[1 - me], od=days[me], td=days[1 - me],
                owool=sells[me].get("WOOL", 0), twool=sells[1 - me].get("WOOL", 0),
                owaste=waste[me], twaste=waste[1 - me])


if __name__ == "__main__":
    recs = [r for r in (decode(p) for p in
                        sorted(glob.glob(os.path.join(ROOT, "mine/loss/*.json.gz")))) if r]
    print(f"{len(recs)} losses\n")
    print("MEDIAN UNITS BOUGHT, by YARN_STORE count in the draw")
    print(f"{'#YARN':>6}{'n':>4}{'ourSHEEP':>10}{'thSHEEP':>9}{'ourCOW':>8}{'thCOW':>7}"
          f"{'ourLAND':>9}{'thLAND':>8}{'ourWool':>9}{'thWool':>8}{'medMargin':>11}")
    by = collections.defaultdict(list)
    for r in recs:
        by[r["yarn"]].append(r)
    for k in sorted(by):
        g = by[k]
        f = lambda side, it: statistics.median(r[side].get(it, 0) for r in g)
        print(f"{k:>6}{len(g):>4}{f('oq','SHEEP'):>10.0f}{f('tq','SHEEP'):>9.0f}"
              f"{f('oq','COW'):>8.0f}{f('tq','COW'):>7.0f}"
              f"{f('oq','LAND'):>9.0f}{f('tq','LAND'):>8.0f}"
              f"{statistics.median(r['owool'] for r in g):>9.0f}"
              f"{statistics.median(r['twool'] for r in g):>8.0f}"
              f"{statistics.median(r['margin'] for r in g):>+11,.0f}")

    hi = [r for r in recs if r["yarn"] >= 3]
    print(f"\nThe {len(hi)} worst-mismatch games (3+ YARN_STOREs):")
    print(f"{'opponent':<20}{'yarn':>5}{'margin':>10}{'shp us/them':>13}{'land us/them':>14}"
          f"{'wool us/them':>14}{'their sheep days':>26}")
    for r in sorted(hi, key=lambda r: r["margin"]):
        sd = sorted(r["td"].get("SHEEP", []))
        sheep = "%d/%d" % (r["oq"].get("SHEEP", 0), r["tq"].get("SHEEP", 0))
        land = "%d/%d" % (r["oq"].get("LAND", 0), r["tq"].get("LAND", 0))
        wool = "%d/%d" % (r["owool"], r["twool"])
        print(f"{r['opp'][:18]:<20}{r['yarn']:>5}{r['margin']:>+10,.0f}"
              f"{sheep:>13}{land:>14}{wool:>14}{str(sd[:10]):>26}")

    print("\nWHEN sheep are bought (all losses; day -> total units)")
    ours, theirs = collections.Counter(), collections.Counter()
    for r in recs:
        for dd in r["od"].get("SHEEP", []):
            ours[dd] += 1
        for dd in r["td"].get("SHEEP", []):
            theirs[dd] += 1
    for dd in sorted(set(ours) | set(theirs)):
        print(f"   day {dd:>2}:  ours {ours.get(dd,0):>4}   theirs {theirs.get(dd,0):>4}")

    print(f"\nrejected BUY_PRODUCT orders (wasted slots): ours "
          f"{statistics.median(r['owaste'] for r in recs):.0f}/game, "
          f"theirs {statistics.median(r['twaste'] for r in recs):.0f}/game")
