import json, collections, statistics as S, math, sys
rows=[json.loads(l) for l in open(sys.argv[1] if len(sys.argv)>1 else 'moe/r4/build/opusb/gate.jsonl')]
err=[r for r in rows if 'err' in r]; rows=[r for r in rows if 'err' not in r]
print(len(rows),'rows',len(err),'errs'); [print(' ',e['x'],e['o'],e['err']) for e in err[:3]]
cell=collections.defaultdict(dict)
for r in rows: cell[(r['x'],r['o'])][(r['seed'],r['us'])]=r
for (x,o),d in sorted(cell.items()):
    m=[r['m'] for r in d.values()]; W=sum(v>0 for v in m)
    se=S.pstdev(m)/math.sqrt(len(m)) if len(m)>1 else 0
    extra=''
    if x!='C1' and ('C1',o) in cell:
        b=cell[('C1',o)]; ks=[k for k in d if k in b]
        if ks:
            dd=[d[k]['m']-b[k]['m'] for k in ks]; sed=S.pstdev(dd)/math.sqrt(len(dd)) if len(dd)>1 else 0
            extra=f" | paired vs C1 n={len(ks)} {S.mean(dd):+7.0f} (SE {sed:.0f}) better {sum(v>0 for v in dd)}/{len(dd)} | me {S.mean(d[k]['me']-b[k]['me'] for k in ks):+6.0f} opp {S.mean(d[k]['opp']-b[k]['opp'] for k in ks):+6.0f}"
    fires=S.mean(r['tx']['P'].get('pred_fires',0)+r['tx']['Q'].get('pred_fires',0) for r in d.values())
    dcs=[r['dc'].get('errors',0) for r in d.values() if r['dc']]
    print(f"{x:6s} vs {o:6s} n={len(m):2d} W-L {W}-{len(m)-W} WR {W/len(m):.2f} mean {S.mean(m):+7.0f} (SE {se:.0f}) fires {fires:.0f}{' dcerr '+str(sum(dcs)) if dcs else ''}{extra}")
