import sys,importlib.util,concurrent.futures as cf,statistics
from kaggle_environments import make
def loadm(p):
    spec=importlib.util.spec_from_file_location(p.replace('.','_'),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def game(ap,bp,seed):
    a=loadm(ap).agent;b=loadm(bp).agent
    env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
    env.run([a,b]);return [s.reward for s in env.steps[-1]]
def pair(args):
    ap,bp,seed=args
    try:
        r1=game(ap,bp,seed);r2=game(bp,ap,seed)
        return (ap,bp,seed,r1[0]-r1[1],r2[1]-r2[0])
    except Exception as e:
        return (ap,bp,seed,'ERR',str(e))
if __name__=='__main__':
    # sirx vs sir = isolated compaction delta; vs koshinm + pipe16 = band check
    cands=['subV_sirx.py','subV2_sirx.py']
    opps=['subV_sir.py','subV2_sir.py',
          'rivals/koshinm_kaggriculture-local-best-2026-09-21/main.py',
          'subK_pipe16.py']
    seeds=list(range(700,712))
    tasks=[(c,o,s) for c in cands for o in opps for s in seeds]
    res={}
    with cf.ProcessPoolExecutor(max_workers=8) as ex:
        for ap,bp,seed,m1,m2 in ex.map(pair,tasks):
            res.setdefault((ap,bp),[]).append((seed,m1,m2))
    for (c,o),rows in sorted(res.items()):
        ms=[m for _,a,b in rows for m in (a,b) if isinstance(m,(int,float))]
        w=sum(1 for m in ms if m>0);l=sum(1 for m in ms if m<0)
        errs=[r for r in rows if not isinstance(r[1],(int,float))]
        print(f'{c} vs {o}: {w}-{l} mean={statistics.mean(ms):+.0f} med={statistics.median(ms):+.0f} worst={min(ms):+.0f}'+(f' ERRS={len(errs)}' if errs else ''))
