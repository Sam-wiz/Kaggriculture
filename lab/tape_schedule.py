"""Decode the strongest public tape and report the macro schedule it executes.

The point is to LEARN the plan, not to copy the binary: hire curve, land days,
what it buys and plants, and what it sells when. Those are the numbers our own
planner should be reproducing.
"""
import re, sys, collections

ITEMS = ["WHEAT","CARROT","TOMATO","STRAWBERRY","MELON","EGG","MILK","WOOL","FERTILIZER",
         "GOOSE","COW","SHEEP"]
OPS = ["PASS","NORTH","SOUTH","EAST","WEST","PICKUP","DROP","PLACE","PLANT","WATER","HARVEST",
       "FERTILIZE","DIG","BUILD_COOP","BUILD_PASTURE","FEED","COLLECT_FERTILIZER","CARE","INVALID"]
MOPS = ["NONE","HIRE","BUY_LAND","BUY_SEED","BUY_PRODUCT","BUY_ANIMAL","SELL"]


def load_tapes(path):
    txt = open(path).read()
    blocks = re.findall(r'\{((?:\s*"[^"]*",?)+)\s*\}', txt)
    tapes = []
    for b in blocks:
        rows = re.findall(r'"([^"]*)"', b)
        if len(rows) > 100:
            tapes.append(rows)
    return tapes


def decode(row):
    t = list(map(int, row.split()))
    if not t:
        return [], []
    nu, no = t[0], t[1]
    i = 2
    units = []
    for _ in range(nu):
        units.append(tuple(t[i:i+3])); i += 3
    orders = []
    for _ in range(no):
        orders.append(tuple(t[i:i+3])); i += 3
    return units, orders


def report(tape, label):
    unit_ops = collections.Counter()
    plants = collections.Counter()
    buys = collections.Counter()
    sells = collections.Counter()
    hires_per_day = collections.Counter()
    land_days = []
    units_per_day = collections.defaultdict(int)
    animals = collections.Counter()
    sell_by_day = collections.defaultdict(collections.Counter)
    for step, row in enumerate(tape):
        day = step // 24
        units, orders = decode(row)
        units_per_day[day] = max(units_per_day[day], len(units))
        for op, arg, n in units:
            unit_ops[OPS[op] if op < len(OPS) else op] += 1
            if OPS[op] == "PLANT":
                plants[ITEMS[arg]] += 1
        for op, item, n in orders:
            name = MOPS[op] if op < len(MOPS) else str(op)
            if name == "HIRE":
                hires_per_day[day] += 1
            elif name == "BUY_LAND":
                land_days.append(day)
            elif name == "BUY_SEED":
                buys["seed:" + ITEMS[item]] += max(1, n)
            elif name == "BUY_ANIMAL":
                animals[ITEMS[item]] += max(1, n)
            elif name == "BUY_PRODUCT":
                buys["buy:" + ITEMS[item]] += max(1, n)
            elif name == "SELL":
                sells[ITEMS[item]] += max(1, n)
                sell_by_day[day][ITEMS[item]] += max(1, n)
    print(f"\n===== {label} =====")
    print("land bought on days:", land_days)
    print("hires/day:", " ".join(f"d{d}:{hires_per_day[d]}" for d in sorted(hires_per_day)))
    print("max units/day:", " ".join(f"d{d}:{units_per_day[d]}" for d in sorted(units_per_day)))
    print("animals:", dict(animals))
    print("seeds/products bought:", dict(buys))
    print("plantings:", dict(plants))
    print("total sells by item:", dict(sells))
    print("unit-action mix:", dict(unit_ops.most_common()))
    print("first sell day per item:",
          {it: min(d for d in sell_by_day if sell_by_day[d][it]) for it in sells})


if __name__ == "__main__":
    tapes = load_tapes(sys.argv[1])
    print("tapes found:", len(tapes), "turns each:", [len(t) for t in tapes])
    for i, t in enumerate(tapes):
        report(t, "route %d" % i)
