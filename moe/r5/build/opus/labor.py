"""r5 opus: family labour budget.  Per day: unit-turns, and op mix (move / PASS / productive by op).
Tells how much slack a greedy executor has vs the family."""
import gzip, json, glob, collections, pickle
F = pickle.load(open("moe/r5/build/opus/fam.pkl", "rb"))["fam"]
want = {(r["ep"], r["seat"]) for r in F if r["team"] in ("DSM", "Vadim Vasilenko", "DECEM")}
MOV = {"NORTH", "SOUTH", "EAST", "WEST"}
agg = [collections.Counter() for _ in range(30)]; n = 0
for f in sorted(glob.glob("mine/top10/*.json.gz"))[::4]:
    d = json.load(gzip.open(f, "rt"))
    for s in range(2):
        if (d["episode_id"], s) not in want: continue
        n += 1
        for t in range(1, len(d["actions"])):
            a = d["actions"][t][s]
            if not isinstance(a, dict): continue
            day = (t - 1) // 24
            for u in [a.get("farmer")] + list(a.get("hands") or []):
                op = (u or ["PASS"])[0]
                agg[day]["MOVE" if op in MOV else op] += 1; agg[day]["_units"] += 1
print("seats", n)
keys = ["_units", "MOVE", "PASS", "WATER", "HARVEST", "PLANT", "FEED", "CARE", "COLLECT_FERTILIZER", "FERTILIZE", "PICKUP", "PLACE", "DROP", "DIG", "BUILD_PASTURE", "BUILD_COOP"]
print("day " + " ".join(f"{k[:6]:>6s}" for k in keys))
for d in range(30):
    c = agg[d]; u = c["_units"]
    print(f"d{d:2d} " + f"{u/n:6.0f} " + " ".join(f"{c[k]/u:6.2f}" for k in keys[1:]))
