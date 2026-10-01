"""Decode a mined opponent's macro schedule from their recorded actions."""
import gzip, glob, json, sys, collections


def schedule(actions):
    plants = collections.Counter(); sells = collections.Counter()
    buys = collections.Counter(); animals = collections.Counter()
    hires = collections.Counter(); land = []
    ops = collections.Counter(); units_day = collections.defaultdict(int)
    first_sell = {}
    for step, a in enumerate(actions):
        if not isinstance(a, dict):
            continue
        day = step // 24
        acts = [a.get("farmer") or ["PASS"]] + list(a.get("hands") or [])
        units_day[day] = max(units_day[day], len(acts))
        for op in acts:
            if not op:
                continue
            ops[op[0]] += 1
            if op[0] == "PLANT" and len(op) > 1:
                plants[op[1]] += 1
        for o in (a.get("market") or []):
            if not o:
                continue
            k = o[0]
            if k == "HIRE":
                hires[day] += 1
            elif k == "BUY_LAND":
                land.append(day)
            elif k == "SELL" and len(o) > 2:
                sells[o[1]] += int(o[2]); first_sell.setdefault(o[1], day)
            elif k == "BUY_ANIMAL" and len(o) > 2:
                animals[o[1]] += int(o[2])
            elif k in ("BUY_SEED", "BUY_PRODUCT") and len(o) > 2:
                buys[("seed:" if k == "BUY_SEED" else "buy:") + str(o[1])] += int(o[2])
    return dict(plants=dict(plants), sells=dict(sells), buys=dict(buys),
                animals=dict(animals), land=land, ops=dict(ops.most_common(9)),
                hires=" ".join("d%d:%d" % (d, hires[d]) for d in sorted(hires)),
                maxunits=max(units_day.values()) if units_day else 0,
                first_sell=first_sell)


if __name__ == "__main__":
    want = set(sys.argv[1:])
    best = {}
    for p in sorted(glob.glob("mine/tapes/*.json.gz")):
        with gzip.open(p, "rt") as f:
            r = json.load(f)
        if r.get("opp_bank") is None:
            continue
        k = r["opponent"]
        if k not in best or r["opp_bank"] > best[k]["opp_bank"]:
            best[k] = r
    rows = sorted(best.values(), key=lambda r: -r["opp_bank"])
    for r in rows:
        if want and r["opponent"] not in want:
            continue
        s = schedule(r["opp_actions"])
        print("=" * 78)
        print(f"{r['opponent']}   theirBank {r['opp_bank']:.0f}   ourBank {r['our_bank']:.0f}"
              f"   seed {r['seed']}   ep {r['episode_id']}")
        print("  land days:", s["land"], "  max units/day:", s["maxunits"])
        print("  hires:", s["hires"][:150])
        print("  animals:", s["animals"], " plantings:", s["plants"])
        print("  bought:", s["buys"])
        print("  sells:", s["sells"])
        print("  first sell day:", s["first_sell"])
        print("  action mix:", s["ops"])
