"""Crop Dusta buys ~1750 wheat and sells ~1745. Is that an arbitrage, and when?"""
import gzip, glob, json, sys, collections, statistics
TEAM = "Crop Dusta"

buys = collections.Counter(); sells = collections.Counter()
buy_units = collections.Counter(); sell_units = collections.Counter()
n = 0
for p in sorted(glob.glob("mine/top/*.json.gz")):
    with gzip.open(p, "rt") as f:
        d = json.load(f)
    if TEAM not in d["teams"]:
        continue
    seat = d["teams"].index(TEAM)
    n += 1
    for step, pair in enumerate(d["actions"]):
        a = pair[seat]
        if not isinstance(a, dict):
            continue
        day = step // 24
        for o in (a.get("market") or []):
            if not o or len(o) < 3 or o[1] != "WHEAT":
                continue
            if o[0] == "BUY_PRODUCT":
                buys[day] += 1; buy_units[day] += int(o[2])
            elif o[0] == "SELL":
                sells[day] += 1; sell_units[day] += int(o[2])
print(f"{TEAM}: {n} episodes")
print(f"{'day':>4}{'buy units/ep':>14}{'sell units/ep':>15}{'net':>10}")
tb = ts = 0
for day in range(30):
    b = buy_units[day] / n; s = sell_units[day] / n
    tb += b; ts += s
    if b or s:
        print(f"{day:>4}{b:>14.1f}{s:>15.1f}{b-s:>10.1f}")
print(f"{'TOT':>4}{tb:>14.1f}{ts:>15.1f}{tb-ts:>10.1f}")
