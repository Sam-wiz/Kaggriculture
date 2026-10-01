import glob, gzip, json, os, statistics as st, math
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
lb=json.load(open('moe/r3/lb_0925_1612.json'))
SIG={8:'shepherd',20:'hyb2965'}
rows=[]
for p in glob.glob('mine/opp/*.json.gz'):
    if os.path.getmtime(p) < os.path.getmtime('moe/r3/BRIEF.md')-60: continue
    d=json.load(gzip.open(p,'rt')); t=d['teams']
    if 'Sam-wiz' not in t or t[0]==t[1]: continue
    me=t.index('Sam-wiz'); a=d['actions']
    try: q=a[1][me]['market'][0][2]
    except Exception: q=None
    b=SIG.get(q,'?')
    opp=t[1-me]; R=lb.get(opp)
    m=d['rewards'][me]-d['rewards'][1-me]
    rows.append(dict(ep=d['episode_id'],build=b,seat=me,opp=opp,R=R,m=m,ours=d['rewards'][me],theirs=d['rewards'][1-me],
                     res=1 if m>0 else (0.5 if m==0 else 0),seed=d['seed'],path=p))
json.dump(rows,open('/tmp/opus_r3/rows.json','w'))
print(len(rows), {b:sum(r['build']==b for r in rows) for b in ('shepherd','hyb2965','?')})
B=[(0,2000),(2000,2200),(2200,2400),(2400,2600),(2600,9999)]
def mle(g):
    # Elo-400 MLE of our rating vs fixed opponent ratings
    lo,hi=1000,3500
    for _ in range(60):
        mid=(lo+hi)/2
        s=sum(r['res']-1/(1+10**((r['R']-mid)/400)) for r in g)
        if s>0: lo=mid
        else: hi=mid
    return mid
for b in ('shepherd','hyb2965'):
    g0=[r for r in rows if r['build']==b and r['R'] is not None]
    line=f"{b:9}"
    for lo,hi in B:
        g=[r for r in g0 if lo<=r['R']<hi]
        line+= f" | {lo}-{hi}: WR {st.mean(r['res'] for r in g):.2f} n={len(g)} med$ {st.median(r['m'] for r in g):+.0f} ours {st.median(r['ours'] for r in g)/1e3:.1f}k opp {st.median(r['theirs'] for r in g)/1e3:.1f}k" if g else f" | {lo}-{hi}: --"
    print(line)
    print('   overall', round(st.mean(r['res'] for r in g0),3), len(g0), 'MLE', round(mle(g0)), ' MLE>=2000', round(mle([r for r in g0 if r['R']>=2000])))
