"""r6 opusb: spread of the COW1+WHEAT5 opening (either order) across all archives: first appearance, # teams, ranks."""
import json, gzip, glob, collections, os
lb = json.load(open("moe/r6/lb_0927.json")); rk = {t: i + 1 for i, (t, s) in enumerate(sorted(lb.items(), key=lambda kv: -kv[1]))}
KEY = ({"BUY_ANIMAL COW 1", "BUY_PRODUCT WHEAT 5"})
first = {}; teams = collections.defaultdict(lambda: [0, 10**12, 0]); allseen = collections.Counter(); byday = collections.Counter()
for g in ["mine/opp/*.json.gz", "mine/top/*.json.gz", "mine/top10/*.json.gz"]:
    for p in glob.glob(g):
        try: d = json.load(gzip.open(p, "rt"))
        except Exception: continue
        ep = int(d["episode_id"])
        for s in range(2):
            a = d["actions"][1][s] if len(d["actions"]) > 1 else None
            m = a.get("market") if isinstance(a, dict) else None
            if not m: continue
            allseen[g.split("/")[1]] += 1
            ops = {" ".join(str(x) for x in o) for o in m[:3]}
            if KEY <= ops:
                t = d["teams"][s]; x = teams[t]; x[0] += 1; x[1] = min(x[1], ep); x[2] = max(x[2], ep)
                byday[(g.split("/")[1], ep // 1000000)] += 1
rows = sorted(teams.items(), key=lambda kv: kv[1][1])
print("teams with COW1+WHEAT5 in first 3 step-1 market ops:", len(rows))
for t, (n, a, b) in rows: print(f"  first ep {a} last {b} n={n:3d} rank_now {rk.get(t)} {t}")
print("by (archive, ep/1e6):", sorted(byday.items()))
