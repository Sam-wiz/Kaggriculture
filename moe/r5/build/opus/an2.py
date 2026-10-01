"""r5 opus an2: where does DSM's 0.88 WR come from when all family teams bank ~the same?
Head-to-head: per (team, opp-team) pair, mean own bank, opp bank, margin; product revenue/units/avg price
own vs opp in family-vs-family games."""
import pickle, collections, statistics as st
D = pickle.load(open("moe/r5/build/opus/fam.pkl", "rb")); F = D["fam"]; O = D["other"]
byep = collections.defaultdict(dict)
for r in F + O: byep[r["ep"]][r["seat"]] = r
P = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER")
def sells(r):
    u = collections.Counter(); v = collections.Counter()
    for x in r["dec"]:
        for k, (a, b) in x["sell"].items(): u[k] += a; v[k] += b
    return u, v
def cost(r):
    c = 0
    return c
teams = ["DSM", "DECEM", "Unknown Mother-Goose", "M & M & P & Q", "Vadim Vasilenko", "mtmr_s1"]
print("pairwise: row team vs col opp — WR (n) mean margin")
for t in teams:
    line = f"{t[:10]:10s}"
    for o in teams + ["Boey", "Fourth Quadrant", "Kaggledew Valley 🏆"]:
        G = [(r, byep[r["ep"]][1 - r["seat"]]) for r in F if r["team"] == t and r["opp"] == o]
        if not G: line += f" | {o[:6]:6s}    -    "; continue
        wr = st.mean(a["bank"] > b["bank"] for a, b in G); m = st.mean(a["bank"] - b["bank"] for a, b in G)
        line += f" | {o[:6]:6s} {wr:.2f}({len(G):3d}){m:+6.0f}"
    print(line)
print("\nDSM vs family-clone opponents: revenue / units / avg price by product (own vs opp)")
G = [(r, byep[r["ep"]][1 - r["seat"]]) for r in F if r["team"] == "DSM" and byep[r["ep"]][1 - r["seat"]]["fam"] and byep[r["ep"]][1 - r["seat"]]["team"] != "DSM"]
print("n games", len(G))
tot = collections.Counter()
for p in P:
    ou = st.mean(sells(a)[0][p] for a, b in G); orv = st.mean(sells(a)[1][p] for a, b in G)
    pu = st.mean(sells(b)[0][p] for a, b in G); prv = st.mean(sells(b)[1][p] for a, b in G)
    tot["own"] += orv; tot["opp"] += prv
    print(f" {p:11s} own u={ou:6.1f} rev={orv:7.0f} avg={orv/max(ou,1e-9):6.1f} | opp u={pu:6.1f} rev={prv:7.0f} avg={prv/max(pu,1e-9):6.1f} | drev={orv-prv:+6.0f}")
print(" total rev own", round(tot["own"]), "opp", round(tot["opp"]), "bank own", round(st.mean(a["bank"] for a, b in G)), "opp", round(st.mean(b["bank"] for a, b in G)))
for t in ("mtmr_s1", "Vadim Vasilenko", "DECEM"):
    G2 = [(r, byep[r["ep"]][1 - r["seat"]]) for r in F if r["team"] == t and byep[r["ep"]][1 - r["seat"]]["fam"] and byep[r["ep"]][1 - r["seat"]]["team"] != t]
    d = {p: round(st.mean(sells(a)[1][p] - sells(b)[1][p] for a, b in G2)) for p in P}
    print(f"\n{t} vs family clones n={len(G2)}: drev by product {d}; dbank {st.mean(a['bank']-b['bank'] for a,b in G2):+.0f}")
