"""Tape -> strategy spec. Aggregates per-team behavior from reduced episode tapes."""
import gzip, json, glob, os, sys
from collections import Counter, defaultdict

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
FILES = sorted(glob.glob(ROOT + "/mine/top/*.json.gz")) + sorted(glob.glob(ROOT + "/mine/top10/*.json.gz")) + sorted(glob.glob(ROOT + "/mine/loss/*.json.gz"))

def prof(actions, seat):
    buys = Counter(); sells = Counter(); ops = Counter()
    day0m = []
    for i, a in enumerate(actions):
        if not isinstance(a, (list, tuple)) or len(a) <= seat: continue
        act = a[seat]
        if not isinstance(act, dict): continue
        if i < 48:
            for o in act.get("market") or []:
                if isinstance(o, (list, tuple)) and o: day0m.append(tuple(o[:3] if len(o) > 2 else o))
        for o in act.get("market") or []:
            if not isinstance(o, (list, tuple)) or len(o) < 2: continue
            try: n = int(o[2]) if len(o) > 2 else 1
            except Exception: continue
            if o[0] == "SELL": sells[o[1]] += n
            elif str(o[0]).startswith("BUY"): buys[o[0] + ":" + str(o[1])] += n
            elif o[0] == "HIRE": buys["HIRE"] += 1
        for u in [act.get("farmer")] + list(act.get("hands") or []):
            if isinstance(u, (list, tuple)) and u: ops[u[0]] += 1
    return buys, sells, ops, day0m

teams = defaultdict(lambda: dict(n=0, w=0, margin=0.0, buys=Counter(), sells=Counter(), ops=Counter(), openers=Counter()))
for f in FILES:
    try: d = json.load(gzip.open(f, "rt"))
    except Exception: continue
    t = d.get("teams") or []
    if len(t) != 2 or not d.get("rewards"): continue
    for seat in (0, 1):
        name = t[seat]
        g = teams[name]
        g["n"] += 1
        m = d["rewards"][seat] - d["rewards"][1-seat]
        g["margin"] += m
        g["w"] += m > 0
        b, s, o, dm = prof(d["actions"], seat)
        g["buys"] += b; g["sells"] += s; g["ops"] += o
        g["openers"][tuple(dm)] += 1

res = []
for name, g in teams.items():
    if g["n"] < 4: continue
    n = g["n"]
    res.append(dict(team=name, n=n, wr=round(g["w"]/n, 2), margin=round(g["margin"]/n),
        cows=round(g["buys"]["BUY_ANIMAL:COW"]/n, 1), sheep=round(g["buys"]["BUY_ANIMAL:SHEEP"]/n, 1),
        geese=round(g["buys"]["BUY_ANIMAL:GOOSE"]/n, 1), feed=round(g["buys"]["BUY_PRODUCT:WHEAT"]/n, 1),
        hires=round(g["buys"]["HIRE"]/n, 1),
        eggs=round(g["sells"]["EGG"]/n, 1), milk=round(g["sells"]["MILK"]/n, 1),
        wool=round(g["sells"]["WOOL"]/n, 1), tomato=round(g["sells"]["TOMATO"]/n, 1),
        sb=round(g["sells"]["STRAWBERRY"]/n, 1), melon=round(g["sells"]["MELON"]/n, 1),
        wheat=round(g["sells"]["WHEAT"]/n, 1), carrot=round(g["sells"]["CARROT"]/n, 1),
        fert=round(g["sells"]["FERTILIZER"]/n, 1)))
res.sort(key=lambda r: -r["margin"])
json.dump(res, open(ROOT + "/moe/r7/build/devin/team_specs.json", "w"), indent=1)
for r in res[:25]:
    print(f"{r['team'][:30]:32} n={r['n']:3} wr={r['wr']:.2f} m={r['margin']:+6.0f} | C{r['cows']:>4} S{r['sheep']:>4} G{r['geese']:>4} feedW{r['feed']:>4} | egg{r['eggs']:>4} milk{r['milk']:>4} wool{r['wool']:>4} tom{r['tomato']:>4} sb{r['sb']:>4} mel{r['melon']:>4} whe{r['wheat']:>4} car{r['carrot']:>4} fer{r['fert']:>4}")
