import json, collections, statistics as S, sys
rows=[json.loads(l) for l in open(sys.argv[1])]
rows=[r for r in rows if 'err' not in r]
print(len(rows), 'rows')
by=collections.defaultdict(list); bytape=collections.defaultdict(list)
for r in rows: by[r['team']].append(r); bytape[(r['g'],r['seat'])].append(r)
tot=[0,0]
for tm, rs in sorted(by.items(), key=lambda kv:-len(kv[1])):
    W=sum(r['me']>r['opp'] for r in rs); held=[r for r in rs if r['tele']['dead_actions']<300]
    Wh=sum(r['me']>r['opp'] for r in held)
    print(f"{tm[:20]:20s} n={len(rs):3d} W {W:3d} ({W/len(rs):.2f}) held {len(held):3d} ({len(held)/len(rs):.2f}) heldW {Wh:3d} | margin med {S.median(r['me']-r['opp'] for r in rs):+8.0f} | bank med {S.median(r['me'] for r in rs):7.0f} opp {S.median(r['opp'] for r in rs):7.0f}")
    tot[0]+=W; tot[1]+=len(rs)
print('all tapes W', tot)
best=sorted(bytape.items(), key=lambda kv: -sum(r['me']-r['opp'] for r in kv[1])/len(kv[1]))
print('best tapes:')
for (g,s), rs in best[:25]:
    print(' ', g.split('/')[-1], s, rs[0]['team'][:16], len(rs), 'W', sum(r['me']>r['opp'] for r in rs), 'mean margin %+.0f'%(sum(r['me']-r['opp'] for r in rs)/len(rs)), 'dead', [r['tele']['dead_actions'] for r in rs])
