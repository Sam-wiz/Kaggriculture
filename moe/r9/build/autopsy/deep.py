"""Deep-dive one replay: what did each side DO. Ops histogram, market order mix,
timing of key events (land buys, hires, first premium sells)."""
import gzip, json, sys
from collections import Counter

path = sys.argv[1]
r = json.load(gzip.open(path))
teams = r["teams"]
us = teams.index("Sam-wiz")
them = 1 - us
print(f"ep {r['ep']} seed {r['seed']}  {teams[us]}={r['rewards'][us]:.0f} vs {teams[them]}={r['rewards'][them]:.0f}")

for side, name in [(us, "US"), (them, "OPP")]:
    uops = Counter()
    mops = Counter()
    sell_items = Counter()
    buy_animals = Counter()
    buy_seeds = Counter()
    land_turns = []
    hire_turns = []
    first_sell = {}
    for t, pair in enumerate(r["actions"]):
        a = pair[side]
        if not isinstance(a, dict):
            continue
        f = a.get("farmer")
        if f:
            uops[f[0]] += 1
        for h in a.get("hands") or []:
            if h:
                uops["H:" + h[0]] += 1
        for o in a.get("market") or []:
            if not o:
                continue
            mops[o[0]] += 1
            if o[0] == "SELL":
                sell_items[o[1]] += o[2] if len(o) > 2 and isinstance(o[2], int) else 1
                if o[1] not in first_sell:
                    first_sell[o[1]] = t
            elif o[0] == "BUY_ANIMAL":
                buy_animals[o[1]] += o[2] if len(o) > 2 and isinstance(o[2], int) else 1
            elif o[0] == "BUY_SEED":
                buy_seeds[o[1]] += o[2] if len(o) > 2 and isinstance(o[2], int) else 1
            elif o[0] == "BUY_LAND":
                land_turns.append(t)
            elif o[0] == "HIRE":
                hire_turns.append(t)
    print(f"\n--- {name} ({teams[side]}) ---")
    print("  unit ops:", dict(uops.most_common(12)))
    print("  market ops:", dict(mops.most_common()))
    print("  sells:", dict(sell_items.most_common(10)))
    print("  animals:", dict(buy_animals), " seeds(top):", dict(buy_seeds.most_common(6)))
    print("  land buys at turns:", land_turns[:6], " hires:", len(hire_turns),
          "first:", hire_turns[:5])
    print("  first-sell turns:", dict(sorted(first_sell.items(), key=lambda x: x[1])))
