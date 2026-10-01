"""E-shop summary. NOTE: with the full shop sequence pinned, kagsim games are ~deterministic (weeds land on unused
tiles), so the P cells of one tape are one world: count distinct (tape) for P/OWNP, not rows."""
import json, collections, statistics as S, math, sys
fn = sys.argv[1] if len(sys.argv) > 1 else 'moe/r4/build/opusb/eshop.jsonl'
rows=[json.loads(l) for l in open(fn)]
err=[r for r in rows if 'err' in r]; rows=[r for r in rows if 'err' not in r]
print(len(rows),'rows',len(err),'errs')
by=collections.defaultdict(lambda: collections.defaultdict(list))
for r in rows: by[r['team']][r['arm']].append(r)
arms=sorted({r['arm'] for r in rows}, key=lambda a:(a!='U', a))
def line(rs, dedupe):
    if not rs: return '      -       '
    if dedupe:
        d={}
        for r in rs: d.setdefault((r['g'],r['seat']), r)
        rs=list(d.values())
    m=[r['me']-r['opp'] for r in rs]; W=sum(x>0 for x in m)
    return f"{W:2d}/{len(rs):2d} {S.median(m):+7.0f}"
print('team                 | ' + ' | '.join(f"{a:14s}" for a in arms))
tot=collections.defaultdict(list)
for tm,a in by.items():
    print(f"{tm[:20]:20s} | " + ' | '.join(line(a[x], x in ('P','OWNP')) for x in arms))
    for k,v in a.items(): tot[k]+=v
print(f"{'ALL':20s} | " + ' | '.join(line(tot[x], x in ('P','OWNP')) for x in arms))
