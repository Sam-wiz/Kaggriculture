"""r6 opusb: (1) same-world contrast lane seat vs its top-8 opponent (same seed/shops/market): per-product revenue
delta, costs; (2) shop-draw reactivity: corr(demand by dawn d9, herd@d12 / seeds d10-19), lane vs C1 self-play."""
import json, collections, statistics as S
ALIAS = {"Russell Kirk": "有辣条有权", "midnq": "We wanna be tomatos", "nah id win": "We wanna be tomatos"}
T = [t["team"] for t in json.load(open("moe/r6/top20.json"))]
TOP8 = set(T[:8]); LANE = T[10:20]
C = lambda t: ALIAS.get(t, t)
recs = [json.loads(l) for l in open("moe/r6/build/opusb/lane_macro.jsonl")]
PR = ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER"]
SEEDC = dict(WHEAT=10, CARROT=20, TOMATO=40, STRAWBERRY=70, MELON=150)   # placeholder; costs recovered from fills below
def tot(se):
    rev = {p: sum(x["sell"].get(p, [0, 0])[1] for x in se["dec"]) for p in PR}
    hc = sum(x["hcost"] for x in se["dec"]); land = sum(x["land"] for x in se["dec"])
    return rev, hc, land
print("== same-world contrast vs top-8 opponents: mean (lane - opp) revenue by product, $")
for team in LANE:
    G = [(r, s) for r in recs for s in range(2) if C(r["teams"][s]) == team and r["teams"][1 - s] in TOP8]
    if len(G) < 3: continue
    d = collections.defaultdict(list)
    for r, s in G:
        a, ha, la = tot(r["seats"][s]); b, hb, lb = tot(r["seats"][1 - s])
        for p in PR: d[p].append(a[p] - b[p])
        d["hire$"].append(-(ha - hb)); d["quads"].append(la - lb); d["margin"].append(r["rewards"][s] - r["rewards"][1 - s])
        d["sold_total"].append(sum(a.values()) - sum(b.values()))
    print(f"{team:22s} n={len(G):2d} margin {S.mean(d['margin']):+7,.0f} | rev " + " ".join(f"{p[:4]}{S.mean(d[p]):+6,.0f}" for p in PR) + f" | sum {S.mean(d['sold_total']):+7,.0f} hires$ {S.mean(d['hire$']):+5,.0f} quads {S.mean(d['quads']):+.2f}")
# reactivity
DEM = dict(EGG={"BAKERY", "BRUNCH_SPOT"}, MILK={"PIZZA_SHOP", "ICE_CREAM_SHOP", "SMOOTHIE_SHOP"}, WOOL={"YARN_STORE"},
           TOMATO={"PIZZA_SHOP", "FARMERS_MARKET"}, CARROT={"PET_CAFE", "FARMERS_MARKET"})
W = dict(WOOL=2, CARROT=1)
def dem(shops, p): return sum((2 if (p == "WOOL" or (p == "CARROT" and s == "PET_CAFE")) else 1) for s in shops if s in DEM[p])
def corr(x, y):
    if len(x) < 5 or S.pstdev(x) == 0 or S.pstdev(y) == 0: return None
    return round(S.correlation(x, y), 2)
def react(G, getdawn, getdec):
    out = {}
    for p, an in (("EGG", "GOOSE"), ("MILK", "COW"), ("WOOL", "SHEEP")):
        x = [dem(getdawn(g)[9]["shops"], p) for g in G]; y = [getdawn(g)[12]["herd"].get(an, 0) for g in G]
        out[an] = corr(x, y)
    for p in ("TOMATO", "CARROT"):
        x = [dem(getdawn(g)[9]["shops"], p) for g in G]; y = [sum(getdec(g)[d]["seed"].get(p, 0) for d in range(10, 20)) for g in G]
        out[p] = corr(x, y)
    return out
print("\n== shop reactivity: corr(demand from shops at dawn d9, herd@d12 / seeds d10-19)")
for team in LANE:
    G = [(r, s) for r in recs for s in range(2) if C(r["teams"][s]) == team]
    if len(G) < 7: continue
    print(f"{team:22s} n={len(G):2d}", react(G, lambda g: g[0]["seats"][g[1]]["dawn"], lambda g: g[0]["seats"][g[1]]["dec"]))
c1 = [json.loads(l) for l in open("moe/r5/build/opus/c1macro.jsonl")]
G = [(r, 0) for r in c1]
print(f"{'C1 self-play (seat0)':22s} n={len(G):2d}", react(G, lambda g: g[0]["seats"][0]["dawn"], lambda g: g[0]["seats"][0]["dec"]))
# top family reference from opus's macro.jsonl (sample of top-8 seats)
fam = collections.defaultdict(list)
for l in open("moe/r5/build/opus/macro.jsonl"):
    r = json.loads(l)
    for s in range(2):
        if r["teams"][s] in TOP8 and len(fam[r["teams"][s]]) < 120: fam[r["teams"][s]].append((r, s))
for t, G in fam.items():
    print(f"{t[:22]:22s} n={len(G):3d}", react(G, lambda g: g[0]["seats"][g[1]]["dawn"], lambda g: g[0]["seats"][g[1]]["dec"]))
