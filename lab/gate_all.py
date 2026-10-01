import importlib.util,concurrent.futures as cf,statistics
from kaggle_environments import make
def loadm(p):
    spec=importlib.util.spec_from_file_location(p.replace('.','_')+str(abs(hash(p))%9999),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def game(ap,bp,seed):
    env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
    env.run([loadm(ap).agent,loadm(bp).agent]);return [s.reward for s in env.steps[-1]]
def pair(args):
    ap,bp,seed=args
    try:
        r1=game(ap,bp,seed);r2=game(bp,ap,seed)
        return (ap,bp,seed,r1[0]-r1[1],r2[1]-r2[0])
    except Exception as e:
        return (ap,bp,seed,'ERR',str(e))
if __name__=='__main__':
    pairs=[('subV_sirx.py','subV_sir.py'),      # stacked compaction+deadlock
           ('subV_sirx2.py','subV_sirx.py'),   # tomato gate alone
           ('subV_sirxP.py','subV_sirx.py'),   # projected shed alone
           ('subV2_sirx.py','subV2_sir.py'),   # stacked on v2 chassis
           ('subV_sirxP.py','rivals/koshinm_kaggriculture-local-best-2026-09-21/main.py'),
           ('subV_sirxP.py','subK_pipe16.py')]
    seeds=list(range(700,724))
    tasks=[(a,b,s) for a,b in pairs for s in seeds]
    res={}
    with cf.ProcessPoolExecutor(max_workers=8) as ex:
        for ap,bp,seed,m1,m2 in ex.map(pair,tasks):
            res.setdefault((ap,bp),[]).append((seed,m1,m2))
    for (c,o),rows in sorted(res.items()):
        ms=[m for _,a,b in rows for m in (a,b) if isinstance(m,(int,float))]
        e=sum(1 for r in rows if not isinstance(r[1],(int,float)))
        w=sum(1 for m in ms if m>0);l=sum(1 for m in ms if m<0)
        print(f'{c} vs {o}: {w}-{l} mean={statistics.mean(ms):+.0f} med={statistics.median(ms):+.0f} worst={min(ms):+.0f}'+(f' ERRS={e}' if e else ''))
