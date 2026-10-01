import json, gzip, statistics as st
from collections import Counter, defaultdict
ids = json.load(open("moe/r3/live_episode_ids.json"))
lb = json.load(open("moe/r3/lb_0925_1612.json"))
scores = sorted(lb.values(), reverse=True)
print("teams", len(scores), "rank10", scores[9], "rank30", scores[29], "rank100", scores[99], "rank500", scores[499], "rank1000", scores[999], "rank1359", scores[1358])
print("Sam-wiz", lb.get("Sam-wiz"))
def ops(a):
    if not isinstance(a, dict): return ()
    return tuple(tuple(x) if isinstance(x, list) else x for x in [a.get("farmer")] + list(a.get("hands") or []))
def mk(a):
    if not isinstance(a, dict): return ()
    return tuple(tuple(x) for x in (a.get("market") or []))
rows = []
for sub, eps in ids.items():
    name = {"56549546": "shepherd", "56551754": "hyb2965"}[sub]
    for e in eps:
        d = json.load(gzip.open(f"mine/opp/{e}.json.gz", "rt"))
        t = d["teams"]; me = t.index("Sam-wiz"); op = 1 - me
        R = lb.get(t[op])
        A = d["actions"]
        same_u = sum(1 for x in A if ops(x[me]) == ops(x[op])) / len(A)
        same_m = sum(1 for x in A if mk(x[me]) == mk(x[op])) / len(A)
        # opening market fingerprint: first 12 steps opp market orders
        opening = [mk(x[op]) for x in A[:12]]
        rows.append(dict(build=name, ep=e, opp=t[op], R=R, seat=me, ours=d["rewards"][me], theirs=d["rewards"][op],
                         margin=d["rewards"][me]-d["rewards"][op], same_u=same_u, same_m=same_m, opening=opening))
json.dump(rows, open("/tmp/fable/live_rows.json","w"))
for b in ["shepherd","hyb2965"]:
    rs=[r for r in rows if r["build"]==b]
    print(f"\n=== {b} n={len(rs)}")
    for lo,hi in [(0,2000),(2000,2200),(2200,2400),(2400,2600),(2600,9999)]:
        g=[r for r in rs if r["R"] is not None and lo<=r["R"]<hi]
        if not g: continue
        w=sum(r["margin"]>0 for r in g); 
        print(f"  R[{lo},{hi}) n={len(g)} W={w} WR={w/len(g):.2f} medmargin={st.median([r['margin'] for r in g]):.0f} clone>=.95:{sum(r['same_u']>=.95 for r in g)}")
    g=[r for r in rs if r["R"] is None]; print("  unrated", len(g))
    print("  seat0 n=%d W=%d  seat1 n=%d W=%d" % (sum(r['seat']==0 for r in rs), sum(r['seat']==0 and r['margin']>0 for r in rs), sum(r['seat']==1 for r in rs), sum(r['seat']==1 and r['margin']>0 for r in rs)))
    print("  >=2200 games:")
    for r in sorted([r for r in rs if (r["R"] or 0)>=2200], key=lambda r:-r["R"]):
        print(f"    {r['ep']} {r['opp'][:28]:28s} R={r['R']:.0f} seat={r['seat']} ours={r['ours']:.0f} theirs={r['theirs']:.0f} m={r['margin']:+.0f} u={r['same_u']:.2f} m={r['same_m']:.2f}")
