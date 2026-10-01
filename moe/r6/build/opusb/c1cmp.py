"""r6 opusb: C1 self-play macro (moe/r5/build/opus/c1macro.jsonl, 40 seeds x 2 seats) in the dossier's metrics."""
import json, statistics as S, collections
BASE = dict(WHEAT=25, CARROT=35, TOMATO=60, STRAWBERRY=120, MELON=250, EGG=50, MILK=160, WOOL=200, FERTILIZER=100)
R = [json.loads(l) for l in open("moe/r5/build/opus/c1macro.jsonl")]
G = [(r, s) for r in R for s in range(2)]
med = lambda x: S.median(x) if x else 0; mean = lambda x: S.mean(x) if x else 0
print("C1 self-play n seats", len(G), "bank mean", round(mean([r["seats"][s]["bank"] for r, s in G])))
hp = [[r["seats"][s]["dec"][d]["hire"] for r, s in G] for d in range(30)]
print("  hires/day med:", " ".join(str(int(med(x))) for x in hp), "| total med", med([sum(r["seats"][s]["dec"][d]["hire"] for d in range(30)) for r, s in G]))
for d in (3, 6, 10, 15, 20, 25, 29):
    hh = collections.Counter(); pl = collections.Counter(); q = []; mo = []; emp = []
    for r, s in G:
        dw = r["seats"][s]["dawn"][d]; hh.update(dw["herd"]); pl.update(dw["plants"]); q.append(dw["quads"]); mo.append(dw["money"]); emp.append(dw["empty"])
    n = len(G)
    print(f"  dawn d{d:2d}: $ {med(mo):>7,.0f} q {mean(q):.2f} herd " + " ".join(f"{k[0]}{v/n:.1f}" for k, v in sorted(hh.items())) + " | plants " + " ".join(f"{k[:2]}{v/n:.1f}" for k, v in sorted(pl.items())) + f" | empty {mean(emp):.1f}")
an = collections.Counter(); sd = collections.defaultdict(lambda: [0, 0, 0])
for r, s in G:
    for d, x in enumerate(r["seats"][s]["dec"]):
        an.update(x["animal"])
        for k, v in x["seed"].items(): sd[k][0 if d < 10 else (1 if d < 20 else 2)] += v
print("  animals bought mean:", {k: round(v / len(G), 1) for k, v in an.items()}, " seeds mean:", {k: [round(x / len(G), 1) for x in v] for k, v in sd.items()})
rows = []
for it in BASE:
    u = [sum(x["sell"].get(it, [0, 0])[0] for x in r["seats"][s]["dec"]) for r, s in G]
    rv = [sum(x["sell"].get(it, [0, 0])[1] for x in r["seats"][s]["dec"]) for r, s in G]
    late = [sum(x["sell"].get(it, [0, 0])[0] for x in r["seats"][s]["dec"][25:]) for r, s in G]
    pr = [sum(x.get(it, 0) for x in r["seats"][s]["prod"]) for r, s in G]
    if sum(u): rows.append(f"{it[:5]} prod={mean(pr):.0f} u={mean(u):.0f} rev={mean(rv)/1000:.1f}k pi={sum(rv)/sum(u)/BASE[it]:.2f} late={sum(late)/sum(u):.2f}")
print("  sells:", "; ".join(rows))
bp = collections.Counter()
for r, s in G:
    for x in r["seats"][s]["dec"]: bp.update(x.get("buyp", {}))
print("  buy-backs mean:", {k: round(v / len(G)) for k, v in bp.items()})
lands = collections.Counter(tuple(st for d in r["seats"][s]["dec"] for st in d.get("land_step", [])) for r, s in G)
print("  land:", lands.most_common(4))
rev = [[sum(v[1] for v in r["seats"][s]["dec"][d]["sell"].values()) for r, s in G] for d in range(30)]
print("  sell rev/day med $k:", " ".join(f"{med(x)/1000:.1f}" for x in rev))
