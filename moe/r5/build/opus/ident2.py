"""r5 opus: is the top family a branching tape (deterministic in shop prefix) or reactive?
For each family team and day d, group that team's seats by the shop prefix revealed by day d
(shops unlock every 3 days: n_revealed = d//3) and measure, within groups of >=2 seats,
the share of steps whose unit ops (farmer+hands) / market list equal the group's modal one.
Also: first step at which each seat diverges from its team's modal day-0 tape.
Pure action-file scan, no replay.  usage: ident2.py
"""
import gzip, json, glob, collections, sys
FAM = {"Vadim Vasilenko", "DECEM", "Unknown Mother-Goose", "DSM", "mtmr_s1", "M & M & P & Q"}
seats = collections.defaultdict(list)   # team -> list of (shops, acts_seat)
for f in sorted(glob.glob("mine/top10/*.json.gz")):
    d = json.load(gzip.open(f, "rt"))
    for s in range(2):
        t = d["teams"][s]
        if t in FAM:
            a = [(d["actions"][k][s] if isinstance(d["actions"][k][s], dict) else {}) for k in range(1, len(d["actions"]))]
            seats[t].append((d["shops"], a, d["date"], d["teams"][1 - s]))
def U(a): return json.dumps([a.get("farmer")] + list(a.get("hands") or []))
def M(a): return json.dumps(a.get("market") or [])
out = {}
for t, L in seats.items():
    print(f"== {t} n={len(L)}")
    rows = []
    for day in range(0, 30, 1):
        k = min(day // 3, 8)   # shops revealed at dawn of `day` (approx: 1 per 3 days)
        grp = collections.defaultdict(list)
        for shops, a, dt, opp in L: grp[tuple(shops[:k])].append(a)
        su = sm = n = 0
        for g in grp.values():
            if len(g) < 2: continue
            for st in range(day * 24, min(day * 24 + 24, 719)):
                cu = collections.Counter(U(a[st]) for a in g); cm = collections.Counter(M(a[st]) for a in g)
                su += cu.most_common(1)[0][1]; sm += cm.most_common(1)[0][1]; n += len(g)
        rows.append((day, k, len(grp), round(su / max(n, 1), 3), round(sm / max(n, 1), 3)))
    print(" day k groups unit_id mkt_id")
    for r in rows:
        if r[0] in (0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 21, 24, 27, 29): print("  ", r)
    out[t] = rows
    # first divergence from modal tape (whole team, unconditioned)
    fd = []
    for shops, a, dt, opp in L:
        pass
    firstdiv = []
    for st in range(0, 719):
        pass
json.dump(out, open("moe/r5/build/opus/ident2.json", "w"))
