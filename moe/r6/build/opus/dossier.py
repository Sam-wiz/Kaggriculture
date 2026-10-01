"""r6 opus: per-team dossier for LB ranks 1-10 from the exact-replay decode of the 09-23..25 top dump
(moe/r5/build/opus/fam.pkl <- macro.jsonl, 1,773 games, 1,773/1,773 bank-exact).
Sections per team: record + H2H vs the top-20, lineage (op1, land tuple), macro schedule (hires, herd,
plants, seeds, dawn cash), market (units / revenue / captured price, late share, buy-backs, discards,
price edge vs opponent same game), reactivity (shop-demand R^2, opponent-covariate R^2 gain).
usage: dossier.py  -> dossier.json, prints the text dossier (tee to dossier.log)
"""
import collections, json, pickle, statistics as st, sys
import numpy as np

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
D = pickle.load(open(ROOT + "/moe/r5/build/opus/fam.pkl", "rb"))
ALL = D["fam"] + D["other"]
TOP20 = [x["team"] for x in json.load(open(ROOT + "/moe/r6/top20.json"))]
TOP10 = TOP20[:10]
LB = json.load(open(ROOT + "/moe/r6/lb_0927.json"))
byep = collections.defaultdict(dict)
for r in ALL: byep[r["ep"]][r["seat"]] = r
FAMSET = {"Vadim Vasilenko", "DECEM", "Unknown Mother-Goose", "DSM", "mtmr_s1", "M & M & P & Q"}
PROD = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER")
PREM = ("STRAWBERRY", "MELON", "MILK", "WOOL", "EGG", "TOMATO")
DEM = {"BAKERY": ["EGG", "WHEAT"], "PIZZA_SHOP": ["MILK", "TOMATO", "WHEAT"], "BRUNCH_SPOT": ["EGG", "WHEAT", "STRAWBERRY"],
       "YARN_STORE": ["WOOL", "WOOL"], "ICE_CREAM_SHOP": ["STRAWBERRY", "MILK", "WHEAT"], "PET_CAFE": ["CARROT", "CARROT"],
       "SMOOTHIE_SHOP": ["STRAWBERRY", "MILK"], "FARMERS_MARKET": ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY"]}
DP = ["EGG", "MILK", "WOOL", "WHEAT", "TOMATO", "STRAWBERRY", "CARROT"]


def dem(shops):
    c = collections.Counter()
    for s in shops:
        for p in DEM.get(s, []): c[p] += 1
    return [c[p] for p in DP]


def r2cv(X, y, groups, k=5):
    X = np.c_[np.ones(len(y)), X]; pred = np.zeros(len(y)); g = np.array(groups) % k
    for f in range(k):
        tr, te = g != f, g == f
        if tr.sum() < X.shape[1] + 2 or te.sum() == 0: return float("nan")
        b, *_ = np.linalg.lstsq(X[tr], y[tr], rcond=None); pred[te] = X[te] @ b
    v = ((y - y.mean()) ** 2).sum()
    return float(1 - ((y - pred) ** 2).sum() / v) if v > 0 else float("nan")


def m(x): return st.mean(x) if x else float("nan")
def md(x): return st.median(x) if x else float("nan")


def sells(r, lo=0, hi=30):
    u = collections.Counter(); v = collections.Counter()
    for x in r["dec"][lo:hi]:
        for k, (a, b) in x["sell"].items(): u[k] += a; v[k] += b
    return u, v


def seeds(r, lo, hi, crop):
    return sum(x["seed"].get(crop, 0) for x in r["dec"][lo:hi])


TARGETS = {
    "cows_d12": (12, lambda r: r["dawn"][12]["herd"].get("COW", 0)),
    "sheep_d12": (12, lambda r: r["dawn"][12]["herd"].get("SHEEP", 0)),
    "geese_d12": (12, lambda r: r["dawn"][12]["herd"].get("GOOSE", 0)),
    "straw_seed_d6_15": (9, lambda r: seeds(r, 6, 16, "STRAWBERRY")),
    "tomato_seed_d9_20": (12, lambda r: seeds(r, 9, 21, "TOMATO")),
    "carrot_seed_d9_27": (15, lambda r: seeds(r, 9, 28, "CARROT")),
    "melon_seed_d0_29": (6, lambda r: seeds(r, 0, 30, "MELON")),
    "hires_d10_29": (12, lambda r: sum(x["hire"] for x in r["dec"][10:30])),
}


def opp_feats(r, d):
    o = byep[r["ep"]][1 - r["seat"]]
    h = o["dawn"][d]["herd"]; p = o["dawn"][d]["plants"]
    return [h.get("COW", 0), h.get("SHEEP", 0), h.get("GOOSE", 0), p.get("STRAWBERRY", 0), p.get("TOMATO", 0),
            1.0 if o["team"] in FAMSET else 0.0]


out = {}
for team in TOP10:
    G = [r for r in ALL if r["team"] == team]
    print("=" * 110)
    print(f"#{TOP10.index(team)+1} {team}  LB {LB.get(team)}  seats in dump: {len(G)}")
    if not G:
        print("   NO GAMES in the 09-23..25 dump"); out[team] = dict(n=0); continue
    T = out[team] = dict(n=len(G))
    # ---------- record ----------
    W = sum(r["bank"] > r["obank"] for r in G); L_ = sum(r["bank"] < r["obank"] for r in G)
    T["record"] = dict(W=W, L=L_, T=len(G) - W - L_, bank_med=md([r["bank"] for r in G]), bank_mean=m([r["bank"] for r in G]),
                       margin_mean=m([r["bank"] - r["obank"] for r in G]), dates=dict(collections.Counter(r["date"] for r in G)),
                       family_share=m([r["fam"] for r in G]))
    print(f"   record W-L-T {W}-{L_}-{len(G)-W-L_} (WR {W/len(G):.2f})  bank med ${md([r['bank'] for r in G]):,.0f}  margin mean {m([r['bank']-r['obank'] for r in G]):+,.0f}"
          f"  dates {dict(collections.Counter(r['date'] for r in G))}  family-opening share {m([r['fam'] for r in G]):.2f}")
    # ---------- H2H ----------
    h2h = {}
    for o in TOP20 + ["mtmr_s1", "THIRD FARM CLUB", "Kaggledew Valley 🏆", "吃白饭的大肥鱼", "*rest"]:
        if o == team: continue
        if o == "*rest": S = [r for r in G if r["opp"] not in TOP20]
        else: S = [r for r in G if r["opp"] == o]
        if not S: continue
        h2h[o] = dict(n=len(S), wr=m([(r["bank"] > r["obank"]) + 0.5 * (r["bank"] == r["obank"]) for r in S]),
                      margin=m([r["bank"] - r["obank"] for r in S]), bank=m([r["bank"] for r in S]), obank=m([r["obank"] for r in S]))
    T["h2h"] = h2h
    print("   H2H: " + "; ".join(f"{o[:14]} {v['wr']:.2f}({v['n']}) {v['margin']:+,.0f}" for o, v in h2h.items()))
    S20 = [r for r in G if r["opp"] in TOP20]
    if S20:
        T["vs_top20"] = dict(n=len(S20), wr=m([(r["bank"] > r["obank"]) + 0.5 * (r["bank"] == r["obank"]) for r in S20]),
                             margin=m([r["bank"] - r["obank"] for r in S20]))
        print(f"   vs rest of top-20 pooled: WR {T['vs_top20']['wr']:.2f} (n={len(S20)}) margin {T['vs_top20']['margin']:+,.0f}")
    # ---------- lineage ----------
    op1 = collections.Counter(json.dumps(r["op1"]) for r in G)
    lands = collections.Counter(tuple(s for x in r["dec"] for s in x.get("land_step", [])) for r in G)
    T["op1"] = [(k, v) for k, v in op1.most_common(4)]
    T["land"] = [(list(k), v) for k, v in lands.most_common(5)]
    print("   step-1 market: " + " || ".join(f"x{v} {k[:110]}" for k, v in op1.most_common(3)))
    print("   land-step tuples: " + ", ".join(f"{list(k)} x{v}" for k, v in lands.most_common(5)))
    nq = collections.Counter(r["dawn"][29]["quads"] for r in G)
    print(f"   quadrants at d29: {dict(sorted(nq.items()))}")
    # ---------- macro ----------
    H = [m([r["dec"][d]["hire"] for r in G]) for d in range(30)]
    T["hires_day"] = H; T["hires_total"] = m([sum(x["hire"] for x in r["dec"]) for r in G]); T["hire_cost"] = m([sum(x["hcost"] for x in r["dec"]) for r in G])
    print("   hires/day mean: " + " ".join(f"{h:.1f}" for h in H) + f"  | total {T['hires_total']:.0f}, ${T['hire_cost']:,.0f}")
    cash = [md([r["dawn"][d]["money"] for r in G]) for d in range(30)]
    T["dawn_cash_med"] = cash
    print("   dawn cash med: " + " ".join(f"d{d}:{cash[d]:,.0f}" for d in (1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 29)))
    herd = {}
    for d in (1, 3, 6, 7, 10, 12, 15, 20, 25, 29):
        herd[d] = {a: m([r["dawn"][d]["herd"].get(a, 0) for r in G]) for a in ("COW", "SHEEP", "GOOSE")}
    T["herd"] = herd
    print("   herd dawn (cow/sheep/goose): " + " ".join(f"d{d}:{v['COW']:.1f}/{v['SHEEP']:.1f}/{v['GOOSE']:.1f}" for d, v in herd.items()))
    an = collections.Counter()
    for r in G:
        for x in r["dec"]:
            for k, v in x["animal"].items(): an[k] += v
    T["animals_bought"] = {k: v / len(G) for k, v in an.items()}
    plants = {}
    for d in (3, 6, 10, 15, 20, 25, 28):
        plants[d] = {c: m([r["dawn"][d]["plants"].get(c, 0) for r in G]) for c in ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON")}
    T["plants"] = plants
    print("   plants dawn W/C/T/S/M: " + " ".join(f"d{d}:" + "/".join(f"{v[c]:.0f}" for c in ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON")) for d, v in plants.items()))
    ph = [(0, 6), (6, 12), (12, 18), (18, 24), (24, 30)]
    sd = {c: [m([seeds(r, a, b, c) for r in G]) for a, b in ph] for c in ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON")}
    T["seeds_phase"] = sd
    print("   seeds by phase d0-5|6-11|12-17|18-23|24-29: " + "; ".join(f"{c[:3]} " + "|".join(f"{x:.0f}" for x in v) for c, v in sd.items()))
    print(f"   animals bought/game: {dict((k, round(v, 1)) for k, v in T['animals_bought'].items())}  empty d15 {m([r['dawn'][15]['empty'] for r in G]):.1f} weeds d20 {m([r['dawn'][20]['weeds'] for r in G]):.1f}")
    # ---------- market ----------
    mk = {}
    for p in PROD:
        U = [sells(r)[0][p] for r in G]; V = [sells(r)[1][p] for r in G]
        late = [sells(r, 25, 30)[0][p] for r in G]; d29 = [sells(r, 29, 30)[0][p] for r in G]
        mk[p] = dict(units=m(U), rev=m(V), px=(sum(V) / sum(U) if sum(U) else 0), late_share=(sum(late) / sum(U) if sum(U) else 0),
                     d29_share=(sum(d29) / sum(U) if sum(U) else 0))
    T["market"] = mk
    T["rev_total"] = m([sum(sells(r)[1].values()) for r in G])
    bp = collections.Counter()
    for r in G:
        for x in r["dec"]:
            for k, v in x["buyp"].items(): bp[k] += v
    T["buyback"] = {k: v / len(G) for k, v in bp.items()}
    T["discard"] = m([r["discard"] for r in G])
    print(f"   revenue/game ${T['rev_total']:,.0f}; buy-backs {dict((k, round(v)) for k, v in T['buyback'].items())}; discards {T['discard']:.1f}")
    print("   sold u / $ / px / late(d25+) / d29: " + "; ".join(f"{p[:4]} {v['units']:.0f}/{v['rev']/1000:.1f}k/{v['px']:.0f}/{v['late_share']:.2f}/{v['d29_share']:.2f}" for p, v in mk.items()))
    # price edge vs opponent in same game
    edge = {}
    for p in PREM:
        e = []
        for r in G:
            o = byep[r["ep"]][1 - r["seat"]]
            u1, v1 = sells(r); u2, v2 = sells(o)
            if u1[p] >= 5 and u2[p] >= 5: e.append(v1[p] / u1[p] - v2[p] / u2[p])
        edge[p] = (m(e), len(e))
    T["px_edge_vs_opp"] = edge
    print("   captured-price edge vs opp same game ($/u, n): " + "; ".join(f"{p[:4]} {v[0]:+.1f} ({v[1]})" for p, v in edge.items()))
    # ---------- reactivity ----------
    rx = {}
    grp = [r["ep"] for r in G]
    for name, (d, f) in TARGETS.items():
        y = np.array([f(r) for r in G], float)
        Xs = np.array([dem(r["dawn"][d]["shops"]) for r in G], float)
        Xo = np.array([opp_feats(r, min(d, 6)) for r in G], float)
        a = r2cv(Xs, y, grp) if len(G) >= 30 else float("nan")
        b = r2cv(np.c_[Xs, Xo], y, grp) if len(G) >= 30 else float("nan")
        rx[name] = dict(mean=float(y.mean()), sd=float(y.std()), r2_shop=a, r2_shop_opp=b)
    T["reactivity"] = rx
    print("   reactivity (mean sd | R2 shop | R2 shop+opp@<=d6): " + "; ".join(f"{k} {v['mean']:.1f}±{v['sd']:.1f} | {v['r2_shop']:.2f} | {v['r2_shop_opp']:.2f}" for k, v in rx.items()))

json.dump(out, open(ROOT + "/moe/r6/build/opus/dossier.json", "w"), indent=1, default=str)
