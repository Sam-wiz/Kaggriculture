"""Build a pair->route remap from route_margins*.jsonl and evaluate it.

Usage:
  route_remap.py build            # print learned map + diagnostics
  route_remap.py cv               # leave-one-pair-out CV of remap vs shipped
"""
import json
import collections
import sys

CANDIDATES = [0, 4, 8, 10, 11, 12, 101, 103, 105, 106, 107, 108,
              110, 111, 114, 115, 118, 120, 123, 126]

# shipped map picks, replicated from _entry.py router logic
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "v48", "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py")
_m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m)


def map_pick(shops2):
    t = tuple(shops2)
    if t.count("YARN_STORE") == 0:
        return _m._R108_SHOP_ROUTES.get(t, 100)
    return _m._R110_OLD_SHOPS.get(t, 0)


def load():
    rows = []
    for f in ("data/route_margins.jsonl", "data/route_margins2.jsonl"):
        try:
            rows += [json.loads(l) for l in open(f)]
        except OSError:
            pass
    # margins keys come back as str -> int
    for r in rows:
        r["margins"] = {int(k): v for k, v in r["margins"].items()}
    return rows


def pair_means(rows):
    pr = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in rows:
        for rid, v in r["margins"].items():
            pr[tuple(r["shops2"])][rid].append(v)
    return {p: {k: sum(v) / len(v) for k, v in rm.items()} for p, rm in pr.items()}


def single_means(rows):
    """mean margin per route conditioned on a single shop (either slot)."""
    sr = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in rows:
        for shop in set(r["shops2"]):
            for rid, v in r["margins"].items():
                sr[shop][rid].append(v)
    return {s: {k: sum(v) / len(v) for k, v in rm.items()} for s, rm in sr.items()}


def remap_pick(shops2, pmap, smap, min_n=1, pair_counts=None):
    """pair argmax -> additive single-shop -> global best."""
    t = tuple(shops2)
    if t in pmap and (pair_counts is None or pair_counts.get(t, 0) >= min_n):
        return max(pmap[t], key=pmap[t].get)
    if len(t) == 2 and t[0] in smap and t[1] in smap:
        combo = {}
        for rid in CANDIDATES:
            combo[rid] = smap[t[0]].get(rid, -1e9) + smap[t[1]].get(rid, -1e9)
        return max(combo, key=combo.get)
    # global argmax across pairs
    glob = collections.defaultdict(list)
    for p, rm in pmap.items():
        for rid, m in rm.items():
            glob[rid].append(m)
    means = {k: sum(v) / len(v) for k, v in glob.items()}
    return max(means, key=means.get)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    rows = load()
    print("records:", len(rows))
    pmap = pair_means(rows)
    smap = single_means(rows)
    pc = collections.Counter(tuple(r["shops2"]) for r in rows)
    if mode == "build":
        print("\nlearned remap (pair -> route, n, vs shipped pick):")
        for p, rm in sorted(pmap.items()):
            best = max(rm, key=rm.get)
            ship = map_pick(p)
            flag = "" if best == ship else "  <-- CHANGE (%s->%s)" % (ship, best)
            print("%-36s n=%-3d best=%-4s ship=%-4s m=%+7.0f vs ship_m=%+7.0f%s" % (
                p, pc[p], best, ship, rm[best], rm.get(ship, float("nan")), flag))
    elif mode == "cv":
        # leave-one-seed-out: build map on other seeds, eval on held-out record
        gains = []
        for i, r in enumerate(rows):
            train = rows[:i] + rows[i + 1:]
            pm = pair_means(train)
            sm = single_means(train)
            pcc = collections.Counter(tuple(x["shops2"]) for x in train)
            pick = remap_pick(r["shops2"], pm, sm, pair_counts=dict(pcc))
            gains.append(r["margins"].get(pick, r["ship_margin"]) - r["ship_margin"])
        import statistics
        wins = sum(1 for g in gains if g > 0)
        print("LOSO CV: mean gain %+.0f, wins %d/%d" % (
            statistics.mean(gains), wins, len(gains)))
