import importlib.util,concurrent.futures as cf,statistics
from kaggle_environments import make
def loadm(p):
    spec=importlib.util.spec_from_file_location(p.replace('.','_')+str(hash(p)),p)
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
    cands=['subV_sirx2.py']
    opps=['subV_sirx.py','rivals/koshinm_kaggriculture-local-best-2026-09-21/main.py','subK_pipe16.py']
    seeds=list(range(700,724))
    tasks=[(c,o,s) for c in cands for o in opps for s in seeds]
    res={}
    with cf.ProcessPoolExecutor(max_workers=8) as ex:
        for ap,bp,seed,m1,m2 in ex.map(pair,tasks):
            res.setdefault((ap,bp),[]).append((seed,m1,m2))
    for (c,o),rows in sorted(res.items()):
        ms=[m for _,a,b in rows for m in (a,b) if isinstance(m,(int,float))]
        w=sum(1 for m in ms if m>0);l=sum(1 for m in ms if m<0)
        print(f'{c} vs {o}: {w}-{l} mean={statistics.mean(ms):+.0f} med={statistics.median(ms):+.0f} worst={min(ms):+.0f}')
        if 'sirx.py' in o:
            for seed,a,b in sorted(rows):
                if seed in (700,714):print(f'   seed{seed}: {a:+.0f} {b:+.0f}')
