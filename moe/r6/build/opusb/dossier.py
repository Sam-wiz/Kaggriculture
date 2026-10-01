"""r6 opusb: per-team dossier for ranks 11-20 from exact-replay macro records (lane_macro.jsonl) + raw tapes.
usage: dossier.py [TEAM ...]   -> prints tables; writes dossier.json
"""
import json, gzip, collections, statistics as S, hashlib, sys, os
ALIAS = {"Russell Kirk": "有辣条有权", "midnq": "We wanna be tomatos", "nah id win": "We wanna be tomatos"}
T = [t["team"] for t in json.load(open("moe/r6/top20.json"))]
RANK = {t: i + 1 for i, t in enumerate(T)}
LANE = T[10:20]
BASE = dict(WHEAT=25, CARROT=35, TOMATO=60, STRAWBERRY=120, MELON=250, EGG=50, MILK=160, WOOL=200, FERTILIZER=100)
def C(t): return ALIAS.get(t, t)
def med(x): return S.median(x) if x else 0
def mean(x): return S.mean(x) if x else 0
recs = [json.loads(l) for l in open("moe/r6/build/opusb/lane_macro.jsonl")]
recs = [r for r in recs if "err" not in r and all(r["match"])]
def raw(ep):
    for p in (f"mine/top10/{ep}.json.gz",):
        if os.path.exists(p): return json.load(gzip.open(p, "rt"))
def uops(a): return json.dumps([a.get("farmer")] + list(a.get("hands") or [])) if isinstance(a, dict) else "null"
def mops(a): return json.dumps(a.get("market") or []) if isinstance(a, dict) else "[]"
only = set(sys.argv[1:])
OUT = {}
for team in LANE:
    if only and team not in only: continue
    G = [(r, s) for r in recs for s in range(2) if C(r["teams"][s]) == team]
    print("=" * 110); print(f"#{RANK[team]} {team}: n={len(G)}")
    if not G: OUT[team] = dict(n=0); continue
    D = {}
    alias = collections.Counter(r["teams"][s] for r, s in G); dates = collections.Counter(r["date"] for r, s in G)
    W = sum(r["rewards"][s] > r["rewards"][1 - s] for r, s in G); Lo = sum(r["rewards"][s] < r["rewards"][1 - s] for r, s in G)
    bank = [r["rewards"][s] for r, s in G]; ob = [r["rewards"][1 - s] for r, s in G]; mg = [a - b for a, b in zip(bank, ob)]
    print(f"  names {dict(alias)} dates {dict(dates)} seats0/1 {sum(s==0 for r,s in G)}/{sum(s==1 for r,s in G)}")
    print(f"  W-L-T {W}-{Lo}-{len(G)-W-Lo}  bank mean {mean(bank):,.0f} med {med(bank):,.0f}  opp {mean(ob):,.0f}  margin mean {mean(mg):+,.0f} med {med(mg):+,.0f}")
    h2h = collections.defaultdict(list)
    for (r, s), m in zip(G, mg): h2h[C(r["teams"][1 - s])].append(m)
    print("  H2H:", "; ".join(f"{('#%d ' % RANK[o]) if o in RANK else ''}{o[:18]} {sum(x>0 for x in v)}-{sum(x<0 for x in v)} {mean(v):+,.0f}" for o, v in sorted(h2h.items(), key=lambda kv: RANK.get(kv[0], 99))))
    D["h2h"] = {o: [sum(x > 0 for x in v), sum(x < 0 for x in v), round(mean(v))] for o, v in h2h.items()}
    # opening
    op1 = collections.Counter(json.dumps(r["op1"][s]) for r, s in G)
    print("  step-1 market:", op1.most_common(3))
    # land
    lands = collections.Counter(tuple(st for d in r["seats"][s]["dec"] for st in d.get("land_step", [])) for r, s in G)
    print("  land steps:", lands.most_common(5))
    # hires per day
    hp = [[r["seats"][s]["dec"][d]["hire"] for r, s in G] for d in range(30)]
    hc = [sum(r["seats"][s]["dec"][d]["hcost"] for d in range(30)) for r, s in G]
    print("  hires/day med:", " ".join(str(int(med(x))) for x in hp), f"| total med {med([sum(r['seats'][s]['dec'][d]['hire'] for d in range(30)) for r,s in G])} cost med ${med(hc):,.0f}")
    # herd / plants
    for d in (3, 6, 10, 15, 20, 25, 29):
        hh = collections.Counter(); pl = collections.Counter(); q = []; mo = []; emp = []; wd = []
        for r, s in G:
            dw = r["seats"][s]["dawn"]
            if len(dw) > d:
                hh.update(dw[d]["herd"]); pl.update(dw[d]["plants"]); q.append(dw[d]["quads"]); mo.append(dw[d]["money"]); emp.append(dw[d]["empty"]); wd.append(dw[d]["weeds"])
        n = len(q)
        print(f"  dawn d{d:2d}: $ {med(mo):>7,.0f} q {mean(q):.2f} herd " + " ".join(f"{k[0]}{v/n:.1f}" for k, v in sorted(hh.items())) + " | plants " + " ".join(f"{k[:2]}{v/n:.1f}" for k, v in sorted(pl.items())) + f" | empty {mean(emp):.1f} weeds {mean(wd):.1f}")
    an = collections.Counter(); sd = collections.defaultdict(lambda: [0, 0, 0])
    for r, s in G:
        for d, x in enumerate(r["seats"][s]["dec"]):
            an.update(x["animal"])
            for k, v in x["seed"].items(): sd[k][0 if d < 10 else (1 if d < 20 else 2)] += v
    print("  animals bought mean:", {k: round(v / len(G), 1) for k, v in an.items()}, " seeds mean (d0-9/10-19/20-29):", {k: [round(x / len(G), 1) for x in v] for k, v in sd.items()})
    # market
    rows = []
    for it in BASE:
        u = [sum(x["sell"].get(it, [0, 0])[0] for x in r["seats"][s]["dec"]) for r, s in G]
        rv = [sum(x["sell"].get(it, [0, 0])[1] for x in r["seats"][s]["dec"]) for r, s in G]
        late = [sum(x["sell"].get(it, [0, 0])[0] for x in r["seats"][s]["dec"][25:]) for r, s in G]
        if sum(u) == 0: continue
        pr = [sum(x.get(it, 0) for x in r["seats"][s]["prod"]) for r, s in G]
        rows.append(f"{it[:5]} prod={mean(pr):.0f} u={mean(u):.0f} rev={mean(rv)/1000:.1f}k pi={sum(rv)/sum(u)/BASE[it]:.2f} late={sum(late)/sum(u):.2f}")
    print("  sells:", "; ".join(rows))
    bp = collections.Counter()
    for r, s in G:
        for x in r["seats"][s]["dec"]: bp.update(x["buyp"])
    print("  buy-backs mean:", {k: round(v / len(G)) for k, v in bp.items()}, " discard mean", round(mean([r["seats"][s]["discard"] for r, s in G]), 1))
    # collisions: same product same day, both seats selling
    col = collections.defaultdict(lambda: [0, 0]); cap = collections.defaultdict(lambda: [0, 0, 0, 0])
    for r, s in G:
        me, op = r["seats"][s]["dec"], r["seats"][1 - s]["dec"]
        for it in BASE:
            um = sum(x["sell"].get(it, [0, 0])[0] for x in me)
            if not um: continue
            ov = sum(min(me[d]["sell"].get(it, [0, 0])[0], op[d]["sell"].get(it, [0, 0])[0]) for d in range(30))
            col[it][0] += ov; col[it][1] += um
            c = cap[it]; c[0] += sum(x["sell"].get(it, [0, 0])[1] for x in me); c[1] += um
            c[2] += sum(x["sell"].get(it, [0, 0])[1] for x in op); c[3] += sum(x["sell"].get(it, [0, 0])[0] for x in op)
    print("  same-day overlap w/ opp:", {k: round(v[0] / v[1], 2) for k, v in col.items() if v[1] > 20 * len(G) / 10}, " captured $/u me:opp", {k: f"{v[0]/max(1,v[1]):.0f}:{v[2]/max(1,v[3]):.0f}" for k, v in cap.items() if v[1] > 2 * len(G)})
    # daily sell-revenue profile (median $k by day)
    rev = [[sum(v[1] for v in r["seats"][s]["dec"][d]["sell"].values()) for r, s in G] for d in range(30)]
    print("  sell rev/day med $k:", " ".join(f"{med(x)/1000:.1f}" for x in rev))
    # tape identity (raw actions)
    tapes = []
    for r, s in G:
        d = raw(r["ep"])
        if d is None: continue
        acts = d["actions"]
        tapes.append(([uops(acts[t][s]) for t in range(1, len(acts))], [mops(acts[t][s]) for t in range(1, len(acts))], r["shops"], r["seed"]))
    if len(tapes) >= 2:
        ident = []
        for day in range(30):
            cu = collections.Counter(hashlib.md5("".join(tp[0][day * 24:(day + 1) * 24]).encode()).hexdigest() for tp in tapes)
            ident.append(cu.most_common(1)[0][1] / len(tapes))
        print("  unit-op day-hash modal share d0..29:", " ".join(f"{x:.2f}" for x in ident))
        # first divergence from modal step-wise tape (full action)
        fd = []
        for i, tp in enumerate(tapes):
            k = 0
            while k < 719:
                col_ = collections.Counter(t2[0][k] + t2[1][k] for t2 in tapes)
                if tp[0][k] + tp[1][k] != col_.most_common(1)[0][0]: break
                k += 1
            fd.append(k)
        fdu = []
        for tp in tapes:
            k = 0
            while k < 719 and collections.Counter(t2[0][k] for t2 in tapes).most_common(1)[0][0] == tp[0][k]: k += 1
            fdu.append(k)
        print(f"  first divergence from modal (full) steps: med {med(fd)} min {min(fd)} max {max(fd)} | units-only med {med(fdu)} min {min(fdu)}")
        D["fd"] = fd; D["ident"] = ident
    OUT[team] = D
json.dump(OUT, open("moe/r6/build/opusb/dossier.json", "w"), ensure_ascii=False)
