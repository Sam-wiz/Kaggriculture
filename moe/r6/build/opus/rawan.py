"""r6 opus: analyses on rawscan.pkl (09-23..25 only unless ALLDATES=1).
lineage (day-0 tape sharing + cross-team first-divergence), market style, unit op mix, premium sell hours,
same-step collisions, within-team identity.  usage: rawan.py > rawan.log
"""
import collections, itertools, json, os, pickle, random, statistics as st

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
R = pickle.load(open(ROOT + "/moe/r6/build/opus/rawscan.pkl", "rb"))
if not os.environ.get("ALLDATES"): R = [r for r in R if r["date"] != "2026-09-26"]
TOP20 = [x["team"] for x in json.load(open(ROOT + "/moe/r6/top20.json"))]
TEAMS = [t for t in TOP20[:10] if any(r["team"] == t for r in R)] + ["mtmr_s1", "THIRD FARM CLUB", "吃白饭的大肥鱼", "Kaggledew Valley 🏆"]
FAM = {"Vadim Vasilenko", "DECEM", "Unknown Mother-Goose", "DSM", "mtmr_s1", "M & M & P & Q"}
by = collections.defaultdict(list)
for r in R: by[r["team"]].append(r)
random.seed(7)
out = {}


def fdiv(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y: return i + 1
    return len(a)


print("== LINEAGE: day-0 unit tape (steps 1-24) — distinct tapes, modal share; cross-team sharing")
d0 = {t: collections.Counter(tuple(r["uh"][:24]) for r in by[t]) for t in TEAMS}
for t in TEAMS:
    c = d0[t]; print(f"  {t[:22]:22s} n={len(by[t]):3d} distinct day-0 unit tapes {len(c):3d}, modal share {c.most_common(1)[0][1]/len(by[t]):.2f}")
print("  cross-team: share of col-team seats whose day-0 unit tape appears in row-team's seats")
hdr = "".join(f"{t[:7]:>8s}" for t in TEAMS); print(" " * 24 + hdr)
for a in TEAMS:
    line = f"  {a[:22]:22s}"
    for b in TEAMS:
        line += f"{sum(1 for r in by[b] if tuple(r['uh'][:24]) in d0[a]) / len(by[b]):8.2f}"
    print(line)
print("\n  median first-divergence step (unit ops) between random seat pairs, row x col (200 pairs):")
print(" " * 24 + hdr)
fd = {}
for a in TEAMS:
    line = f"  {a[:22]:22s}"
    for b in TEAMS:
        P = [(random.choice(by[a]), random.choice(by[b])) for _ in range(200)]
        v = st.median(fdiv(x["uh"], y["uh"]) for x, y in P if x is not y); fd[(a, b)] = v
        line += f"{v:8.0f}"
    print(line)
print("  same for the market channel:")
for a in TEAMS:
    line = f"  {a[:22]:22s}"
    for b in TEAMS:
        P = [(random.choice(by[a]), random.choice(by[b])) for _ in range(200)]
        line += f"{st.median(fdiv(x['mh'], y['mh']) for x, y in P if x is not y):8.0f}"
    print(line)

print("\n== MARKET STYLE: orders/step, op mix (share of orders), SELL size, 1-unit sells, same-step buy+sell churn steps")
for t in TEAMS:
    G = by[t]; mo = collections.Counter()
    for r in G: mo.update(r["mops"])
    tot = sum(mo.values())
    print(f"  {t[:22]:22s} ord/step {st.mean(r['ord_per_step'] for r in G):.2f}  sellord/g {st.mean(r['sell_orders'] for r in G):.0f} "
          f"size {st.mean(r['sell_sz_mean'] for r in G):.1f} 1-unit {st.mean(r['sell_sz1'] for r in G):.2f} churn {st.mean(r['churn_steps'] for r in G):.0f} | "
          + " ".join(f"{k}:{v/tot:.2f}" for k, v in mo.most_common(8)) + f" | orders/g {tot/len(G):.0f}")
    out.setdefault(t, {})["mops"] = {k: v / len(G) for k, v in mo.items()}

print("\n== UNIT OP MIX (share of unit-turns)")
for t in TEAMS:
    G = by[t]; o = collections.Counter()
    for r in G: o.update(r["ops"])
    tot = sum(o.values()); mv = sum(o[k] for k in ("NORTH", "SOUTH", "EAST", "WEST"))
    print(f"  {t[:22]:22s} unit-turns/g {tot/len(G):.0f}  move {mv/tot:.2f} PASS {o['PASS']/tot:.2f} " +
          " ".join(f"{k[:6]}:{o[k]/tot:.3f}" for k in ("WATER", "HARVEST", "PLANT", "FEED", "CARE", "COLLECT_FERTILIZER", "FERTILIZE", "PICKUP", "PLACE", "DROP", "DIG")))

print("\n== PREMIUM SELL HOURS: share of SELL orders by hour-of-day (top 4 hours) and share of units")
for t in TEAMS:
    G = by[t]; line = f"  {t[:22]:22s}"
    for p in ("STRAWBERRY", "MILK", "WOOL", "EGG", "MELON", "TOMATO"):
        c = collections.Counter(); u = collections.Counter()
        for r in G:
            c.update({int(k): v for k, v in r["hours"].get(p, {}).items()}); u.update({int(k): v for k, v in r["uhours"].get(p, {}).items()})
        n = sum(c.values()); nu = sum(u.values())
        if not n: continue
        top = c.most_common(3)
        line += f" | {p[:4]} " + ",".join(f"h{h}:{v/n:.2f}" for h, v in top) + f" (u/ord {nu/n:.1f})"
    print(line)

print("\n== COLLISIONS: share of own premium SELL steps where opp SELLs same product same step [pre = opp sold it in prior 1-3 steps]")
for t in TEAMS:
    G = by[t]; line = f"  {t[:22]:22s}"
    for cls, f in (("mirror", lambda r: r["opp"] == r["team"]), ("fam", lambda r: r["opp"] in FAM and r["opp"] != r["team"]),
                   ("nonfam", lambda r: r["opp"] not in FAM and r["opp"] != r["team"])):
        S = [r for r in G if f(r)]
        if not S: continue
        own = sum(r["coll"][p][0] for r in S for p in ("STRAWBERRY", "MILK", "WOOL", "EGG", "MELON", "TOMATO"))
        both = sum(r["coll"][p][1] for r in S for p in ("STRAWBERRY", "MILK", "WOOL", "EGG", "MELON", "TOMATO"))
        pre = sum(r["coll"][p][2] for r in S for p in ("STRAWBERRY", "MILK", "WOOL", "EGG", "MELON", "TOMATO"))
        line += f" | {cls} n={len(S)} coll {both/max(1,own):.2f} pre {pre/max(1,own):.2f}"
    print(line)

print("\n== WITHIN-TEAM IDENTITY (unit ops / market), same-date seat pairs; by day block; same vs different first-2 shops")
for t in TEAMS:
    G = by[t]; pairs = [(a, b) for a, b in itertools.combinations(G, 2) if a["date"] == b["date"]]
    random.shuffle(pairs); pairs = pairs[:1500]
    if not pairs: continue
    def idb(a, b, lo, hi, key="uh"): return sum(1 for i in range(lo, hi) if a[key][i] == b[key][i]) / (hi - lo)
    same = [(a, b) for a, b in pairs if a["shops150"] == b["shops150"]]; diff = [(a, b) for a, b in pairs if a["shops150"] != b["shops150"]]
    line = f"  {t[:22]:22s} pairs {len(pairs)}  unit d0 {st.mean(idb(a,b,0,24) for a,b in pairs):.2f} d1-2 {st.mean(idb(a,b,24,72) for a,b in pairs):.2f} " \
           f"d3-9 {st.mean(idb(a,b,72,240) for a,b in pairs):.2f} d10-29 {st.mean(idb(a,b,240,719) for a,b in pairs):.2f} | mkt d0 {st.mean(idb(a,b,0,24,'mh') for a,b in pairs):.2f} " \
           f"d10-29 {st.mean(idb(a,b,240,719,'mh') for a,b in pairs):.2f} | first-div med {st.median(fdiv(a['uh'],b['uh']) for a,b in pairs)}"
    if same and diff:
        line += f" | d3-9 same-shops {st.mean(idb(a,b,72,240) for a,b in same):.2f} (n{len(same)}) vs diff {st.mean(idb(a,b,72,240) for a,b in diff):.2f}"
    print(line)
json.dump(out, open(ROOT + "/moe/r6/build/opus/rawan.json", "w"), indent=1)
