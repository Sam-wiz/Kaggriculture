import sys, os, json
sys.argv_saved=list(sys.argv)
exec(open('/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/opus_scratch/closed.py').read().split('if __name__')[0])
import kagsim
def game2(job):
    xname, xpath, pname, ppath, seed, us = job
    tag="x%d_%d_%s"%(abs(hash(xname))%10**8,seed,us)
    a=load(xpath, tag); b=load(ppath, "p%d_%d_%s"%(abs(hash(pname))%10**8,seed,us))
    m=sys.modules["C_"+tag]
    g=kagsim.Game(seed=int(seed))
    for t in range(720):
        o0,o1=g.observe(0),g.observe(1)
        A,B=(a,b) if us==0 else (b,a)
        try: a0=A(o0)
        except Exception: a0=PASS
        try: a1=B(o1)
        except Exception: a1=PASS
        g.step(a0,a1)
    r=[float(g.reward(0)),float(g.reward(1))]
    rep=dict(P=dict(getattr(m,'_V92_P_REPORT',{})),Q=dict(getattr(m,'_V92_Q_REPORT',{})))
    return xname,pname,seed,us,r[us]-r[1-us],rep
if __name__=="__main__":
    games=json.load(open('/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/opus_scratch/wl_games.json'))
    X={'shep':'subW_shepherd.py','shep_nopred':'/tmp/opus_r3b/shep_nopred.py'}
    jobs=[(xn,xp,'yummers','rivals4/kaggriculture-yummers/_entry.py',g['seed'],g['seat']) for g in games for xn,xp in X.items()]
    with ProcessPoolExecutor(max_workers=2) as ex, open('/tmp/opus_r3b/ablate.jsonl','w') as f:
        for res in ex.map(game2, jobs, chunksize=1):
            f.write(json.dumps(res)+"\n"); f.flush()
