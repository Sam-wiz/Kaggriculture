import json, sys, statistics as st, gzip
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/rdiv.py").read().split("\ndef work")[0].split("exec(open")[0])
rows = json.load(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/fable_scratch/live_rows2.json"))
sel = [r for r in rows if tuple(r["open_they"]) == (5, 0) and (r["R"] or 0) >= 2000 and r["same_u"] >= 0.85 and "Acidic" not in r["opp"]]
seed = {json.load(gzip.open(f"/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/mine/opp/{r['ep']}.json.gz", "rt"))["seed"]: r for r in sel}
wl14 = {g["seed"] for g in json.load(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/opus_scratch/wl_games.json"))}
R = [json.loads(l) for f in ARGS[1:] for l in open(f)]
print(f"recorded live (shepherd/hyb seat vs WLV): 18: W-L {sum(r['margin']>0 for r in sel)}-{sum(r['margin']<=0 for r in sel)} mean {st.mean(r['margin'] for r in sel):+.0f} | 14: mean {st.mean(r['margin'] for s, r in seed.items() if s in wl14):+.0f}")
for o in dict.fromkeys(r["o"] for r in R):
    X = [r for r in R if r["o"] == o]; X14 = [r for r in X if r["seed"] in wl14]
    d = [r["m"] - seed[r["seed"]]["margin"] for r in X]
    fires = st.mean(r["to"]["P"].get("pred_fires", 0) for r in X)
    print(f"shep vs {o:8s} 18: W-L {sum(r['m']>0 for r in X)}-{sum(r['m']<=0 for r in X)} mean {st.mean(r['m'] for r in X):+6.0f} med {st.median(r['m'] for r in X):+6.0f} | 14: W-L {sum(r['m']>0 for r in X14)}-{sum(r['m']<=0 for r in X14)} mean {st.mean(r['m'] for r in X14):+6.0f} | sim-minus-recorded {st.mean(d):+6.0f} | cand PREDICT fires/g {fires:.1f}")
def spear(a, b):
    ra = {v: i for i, v in enumerate(sorted(range(len(a)), key=lambda k: a[k]))}; rb = {v: i for i, v in enumerate(sorted(range(len(b)), key=lambda k: b[k]))}
    x = [ra[i] for i in range(len(a))]; y = [rb[i] for i in range(len(b))]
    mx, my = st.mean(x), st.mean(y)
    return sum((p - mx) * (q - my) for p, q in zip(x, y)) / (sum((p - mx) ** 2 for p in x) * sum((q - my) ** 2 for q in y)) ** .5
print("per-game agreement with recorded live margins (18):")
for o in dict.fromkeys(r["o"] for r in R):
    X = [r for r in R if r["o"] == o]
    sim = [r["m"] for r in X]; rec = [seed[r["seed"]]["margin"] for r in X]
    sign = sum((a > 0) == (b > 0) for a, b in zip(sim, rec))
    print(f"  {o:10s} spearman {spear(sim, rec):+.2f}  same-sign {sign}/18  mean|sim-rec| {st.mean(abs(a-b) for a, b in zip(sim, rec)):.0f}")
