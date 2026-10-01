import json, collections, statistics as S, sys, math
rows=[json.loads(l) for l in open(sys.argv[1])]
err=[r for r in rows if 'err' in r]; rows=[r for r in rows if 'err' not in r]
print(len(rows), 'rows', len(err), 'errs'); [print(e['err']) for e in err[:2]]
by=collections.defaultdict(list)
for r in rows: by[(r.get('tag') or r['spec'], r['live'].split('/')[-1][:18])].append(r)
for k, rs in sorted(by.items()):
    m=[r['me']-r['opp'] for r in rs]; W=sum(x>0 for x in m)
    se=S.pstdev(m)/math.sqrt(len(m)) if len(m)>1 else 0
    dead=[r['tele']['dead_actions'] for r in rs]
    print(f"{k[0]:28s} vs {k[1]:18s} n={len(rs):3d} W-L {W}-{len(rs)-W} WR {W/len(rs):.2f} | margin mean {S.mean(m):+8.0f} (SE {se:.0f}) med {S.median(m):+8.0f} | bank {S.median(r['me'] for r in rs):7.0f} opp {S.median(r['opp'] for r in rs):7.0f} | dead med {S.median(dead):.0f} >300: {sum(d>300 for d in dead)} | routed {sum(r['route']!='default' for r in rs)}")
