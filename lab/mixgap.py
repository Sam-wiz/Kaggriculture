"""Do we lose because our sell mix is mismatched to the shop draw?

The router commits to one of four tails at t=226 (day 9.4) on a *binary* test -- is any YARN_STORE
open -- and never revisits it. But shops keep unlocking until day 24, and a single shop that carries
one product fires twice per interval, so a draw with four YARN_STOREs is a completely different
economy from one with a single one.

For every lost episode this measures, per product: how much each side sold, how far the price fell,
and how many shops actually consume it. If the thesis is right, our losses should show us dumping a
product whose price collapses while the opponent works a product the town is still paying for.
"""
import collections
import glob
import gzip
import json
import os
import statistics

ROOT = os.path.dirname(os.path.abspath(__file__))
SHOP_ITEMS = {
    "BAKERY": ("EGG", "WHEAT"),
    "PIZZA_SHOP": ("MILK", "TOMATO", "WHEAT"),
    "BRUNCH_SPOT": ("EGG", "WHEAT", "STRAWBERRY"),
    "YARN_STORE": ("WOOL",),
    "ICE_CREAM_SHOP": ("STRAWBERRY", "MILK", "WHEAT"),
    "PET_CAFE": ("CARROT",),
    "SMOOTHIE_SHOP": ("STRAWBERRY", "MILK"),
    "FARMERS_MARKET": ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY"),
}


def demand(shops):
    """Units per firing interval the town wants of each product; single-product shops count 2x."""
    d = collections.Counter()
    for s in shops:
        items = SHOP_ITEMS.get(s, ())
        for it in items:
            d[it] += 2 if len(items) == 1 else 1
    return d


def analyse(path):
    d = json.load(gzip.open(path, "rt"))
    me, tr, acts = d["our_seat"], d["trace"], d["actions"]
    if not tr:
        return None
    sells = [collections.Counter(), collections.Counter()]
    for a in acts:
        for s in (0, 1):
            for o in ((a[s] or {}).get("market") or []):
                if o and o[0] == "SELL":
                    sells[s][o[1]] += int(o[2])
    fin = tr[-1]
    dem = demand(fin["shops"])
    px_peak, px_min = {}, {}
    for r in tr:
        for k, v in (r["px"] or {}).items():
            if v is None:
                continue
            px_peak[k] = max(px_peak.get(k, 0), v)
            if r["t"] > 240:
                px_min[k] = min(px_min.get(k, 1e9), v)
    return dict(ep=d["episode_id"], opp=d["teams"][1 - me],
                margin=d["rewards"][me] - d["rewards"][1 - me],
                ours=sells[me], theirs=sells[1 - me], dem=dem,
                px_peak=px_peak, px_min=px_min, shops=fin["shops"])


if __name__ == "__main__":
    recs = [r for r in (analyse(p) for p in sorted(glob.glob(os.path.join(ROOT, "mine/loss/*.json.gz")))) if r]
    print(f"{len(recs)} losses\n")

    print("PRICE COLLAPSE: how far each product fell after day 10, and who sold it")
    print(f"{'product':<13}{'medPeak':>9}{'medFloor':>10}{'collapsed':>11}{'ourQty':>9}{'theirQty':>10}{'delta':>8}")
    prods = ["STRAWBERRY", "MILK", "WOOL", "WHEAT", "MELON", "FERTILIZER", "CARROT", "EGG"]
    for p in prods:
        pk = [r["px_peak"].get(p) for r in recs if r["px_peak"].get(p)]
        mn = [r["px_min"].get(p) for r in recs if r["px_min"].get(p)]
        if not pk:
            continue
        coll = sum(1 for r in recs
                   if r["px_peak"].get(p, 0) > 0 and r["px_min"].get(p, 9e9) < 0.25 * r["px_peak"][p])
        ou = statistics.median(r["ours"].get(p, 0) for r in recs)
        th = statistics.median(r["theirs"].get(p, 0) for r in recs)
        print(f"{p:<13}{statistics.median(pk):>9.0f}{statistics.median(mn):>10.0f}"
              f"{coll:>8}/{len(recs):<3}{ou:>9.0f}{th:>10.0f}{ou-th:>+8.0f}")

    print("\nWOOL: our sales vs the number of YARN_STOREs in the draw")
    byn = collections.defaultdict(list)
    for r in recs:
        byn[r["shops"].count("YARN_STORE")].append(r)
    print(f"{'#YARN':>6}{'n':>5}{'ourWool':>10}{'theirWool':>11}{'ourStraw':>10}{'medMargin':>11}")
    for k in sorted(byn):
        g = byn[k]
        print(f"{k:>6}{len(g):>5}{statistics.median(r['ours'].get('WOOL',0) for r in g):>10.0f}"
              f"{statistics.median(r['theirs'].get('WOOL',0) for r in g):>11.0f}"
              f"{statistics.median(r['ours'].get('STRAWBERRY',0) for r in g):>10.0f}"
              f"{statistics.median(r['margin'] for r in g):>+11,.0f}")

    print("\nSTRAWBERRY: our sales vs number of shops that actually eat it")
    bys = collections.defaultdict(list)
    for r in recs:
        bys[r["dem"].get("STRAWBERRY", 0)].append(r)
    print(f"{'demand':>7}{'n':>5}{'ourStraw':>10}{'theirStraw':>12}{'floorPx':>9}{'medMargin':>11}")
    for k in sorted(bys):
        g = bys[k]
        print(f"{k:>7}{len(g):>5}{statistics.median(r['ours'].get('STRAWBERRY',0) for r in g):>10.0f}"
              f"{statistics.median(r['theirs'].get('STRAWBERRY',0) for r in g):>12.0f}"
              f"{statistics.median(r['px_min'].get('STRAWBERRY',0) for r in g):>9.0f}"
              f"{statistics.median(r['margin'] for r in g):>+11,.0f}")
