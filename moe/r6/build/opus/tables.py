"""r6 opus: render per-team tables (markdown) for LB ranks 1-10 -> teams_1_10.md
Inputs: dossier.json (09-23..25 decode), rawscan.pkl (tape scan), macro26.jsonl (09-26 decode so far).
H2H matrix pools 09-23..26 and excludes Boey's broken submission (day-0 unit tape 30886, 30 games, 0 wins).
"""
import collections, json, pickle, statistics as st, zlib
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
B = ROOT + "/moe/r6/build/opus/"
DJ = json.load(open(B + "dossier.json"))
TOP20 = [x["team"] for x in json.load(open(ROOT + "/moe/r6/top20.json"))]
LB = json.load(open(ROOT + "/moe/r6/lb_0927.json"))
R = pickle.load(open(B + "rawscan.pkl", "rb"))
bad = {(r["ep"], r["seat"]) for r in R if r["team"] == "Boey" and hash(tuple(r["uh"][:24])) % 100000 == 30886}
games = []  # (ep, date, teams, rewards)
seen = set()
D = pickle.load(open(ROOT + "/moe/r5/build/opus/fam.pkl", "rb"))
byep = collections.defaultdict(dict)
for r in D["fam"] + D["other"]: byep[r["ep"]][r["seat"]] = r
for ep, s in byep.items():
    games.append((ep, s[0]["date"], [s[0]["team"], s[1]["team"]], [s[0]["bank"], s[1]["bank"]])); seen.add(ep)
for l in open(B + "macro26.jsonl"):
    r = json.loads(l)
    if "seats" in r and r["ep"] not in seen: games.append((r["ep"], r["date"], r["teams"], r["rewards"]))
ROWS = TOP20[:8] + ["mtmr_s1", "THIRD FARM CLUB", "吃白饭的大肥鱼", "Kaggledew Valley 🏆"]
H = collections.defaultdict(list)
for ep, dt, T, W in games:
    for s in range(2):
        if (ep, s) in bad or (ep, 1 - s) in bad: continue
        H[(T[s], T[1 - s])].append(W[s] - W[1 - s])
L = []
L.append("# r6 opus — per-team tables, LB ranks 1-10 (build/opus/tables.py)\n")
L.append(f"Data: 09-23..25 top dump (1,773 games, exact replay) + {len(games)-len(seen)} games of 09-26 decoded so far. "
         "Ranks 9 (Just A game on your lips) and 10 (Anton Tikhonov) have **0 games** in either.\n")
L.append("## H2H matrix (row team's WR vs column, n), 09-23..26, Boey's broken submission excluded\n")
short = lambda t: {"M & M & P & Q": "MMPQ", "Vadim Vasilenko": "Vadim", "Unknown Mother-Goose": "MGoose", "Fourth Quadrant": "4thQ",
                   "Majkel1337": "Majkel", "THIRD FARM CLUB": "TFC", "吃白饭的大肥鱼": "chibai", "Kaggledew Valley 🏆": "Kdew"}.get(t, t)
L.append("| row \\ col | " + " | ".join(short(c) for c in ROWS) + " | all top-20 | all |")
L.append("|" + "---|" * (len(ROWS) + 3))
for a in TOP20[:8]:
    cells = []
    for b in ROWS:
        v = H.get((a, b), [])
        cells.append("—" if a == b or not v else f"{sum(x > 0 for x in v)/len(v):.2f} ({len(v)})")
    v20 = [x for b in TOP20 if b != a for x in H.get((a, b), [])]
    va = [x for (p, q), xs in H.items() if p == a for x in xs]
    cells.append(f"{sum(x > 0 for x in v20)/max(1,len(v20)):.2f} ({len(v20)})"); cells.append(f"{sum(x > 0 for x in va)/max(1,len(va)):.2f} ({len(va)})")
    L.append(f"| **{short(a)}** (#{TOP20.index(a)+1}, {LB.get(a)}) | " + " | ".join(cells) + " |")
L.append("")
PROD = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER")
for i, t in enumerate(TOP20[:10], 1):
    d = DJ.get(t, {})
    L.append(f"## #{i} {t} (LB {LB.get(t)}) — seats {d.get('n', 0)} (09-23..25)\n")
    if not d.get("n"): L.append("No games in the top dump (09-23..25) nor in the 09-26 files decoded so far.\n"); continue
    rc = d["record"]
    L.append(f"- record W-L {rc['W']}-{rc['L']}, bank median ${rc['bank_med']:,.0f}, mean margin {rc['margin_mean']:+,.0f}; dates {rc['dates']}")
    L.append(f"- step-1 market (top): " + "; ".join(f"x{v} `{k[:120]}`" for k, v in d["op1"][:2]))
    L.append(f"- land-step tuples: " + ", ".join(f"{k} x{v}" for k, v in d["land"][:4]))
    L.append(f"- hires/day: " + " ".join(f"{x:.1f}" for x in d["hires_day"]) + f" (total {d['hires_total']:.0f}, ${d['hire_cost']:,.0f})")
    L.append(f"- dawn cash (median) d1..d10: " + " ".join(f"{d['dawn_cash_med'][k]:,.0f}" for k in range(1, 11)) + f"; d15 {d['dawn_cash_med'][15]:,.0f}; d29 {d['dawn_cash_med'][29]:,.0f}")
    L.append("\n| dawn | cows | sheep | geese | wheat | carrot | tomato | straw | melon |\n|---|---|---|---|---|---|---|---|---|")
    for day in ("3", "6", "10", "15", "20", "25"):
        hh = d["herd"].get(day) or d["herd"].get(int(day)); pp = d["plants"].get(day) or d["plants"].get(int(day))
        L.append(f"| d{day} | {hh['COW']:.1f} | {hh['SHEEP']:.1f} | {hh['GOOSE']:.1f} | " + " | ".join(f"{pp[c]:.0f}" for c in ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON")) + " |")
    L.append("\nSeeds bought per phase (d0-5 | 6-11 | 12-17 | 18-23 | 24-29): " + "; ".join(f"{c.lower()} " + "|".join(f"{x:.0f}" for x in v) for c, v in d["seeds_phase"].items()))
    L.append(f"\nAnimals bought/game: {', '.join(f'{k.lower()} {v:.1f}' for k, v in d['animals_bought'].items())}. Buy-backs/game: {', '.join(f'{k.lower()} {v:.0f}' for k, v in d['buyback'].items())}. Discards {d['discard']:.1f}.\n")
    L.append("| product | units sold | revenue | captured $/u | share sold d25+ | share d29 | $/u edge vs opp same game (n) |\n|---|---|---|---|---|---|---|")
    for p in PROD:
        m = d["market"][p]; e = d["px_edge_vs_opp"].get(p)
        L.append(f"| {p.lower()} | {m['units']:.0f} | ${m['rev']:,.0f} | {m['px']:.0f} | {m['late_share']:.2f} | {m['d29_share']:.2f} | " + (f"{e[0]:+.1f} ({e[1]})" if e and e[1] else "—") + " |")
    L.append("\n| reactivity target | mean ± sd | CV R² shop demand | + opponent covariates (≤d6) |\n|---|---|---|---|")
    for k, v in d["reactivity"].items():
        L.append(f"| {k} | {v['mean']:.1f} ± {v['sd']:.1f} | {v['r2_shop']:.2f} | {v['r2_shop_opp']:.2f} |")
    L.append("")
open(B + "teams_1_10.md", "w").write("\n".join(L))
print("\n".join(L[:20]))
