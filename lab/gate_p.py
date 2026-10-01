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
    pairs=[('subV_sirxP.py','subV_sir.py'),
           ('subV2_sirxP.py','subV2_sirx.py'),
           ('subV2_sirxP.py','subV2_sir.py'),
           ('subV_sirxP.py','rivals/kaggriculture-melon-threshold-squeeze-2749/main.py'),
           ('subV_sirxP.py','subJ_2945.py')]
    seeds=list(range(700,724))
    tasks=[(a,b,s) for a,b in pairs for s in seeds]
    res={}
    with cf.ProcessPoolExecutor(max_workers=8) as ex:
        for ap,bp,seed,m1,m2 in ex.map(pair,tasks):
            res.setdefault((ap,bp),[]).append((seed,m1,m2))
    for (c,o),rows in sorted(res.items()):
        ms=[(s_,m) for s_,a,b in rows for m in (a,b) if isinstance(m,(int,float))]
        w=sum(1 for _,m in ms if m>0);l=sum(1 for _,m in ms if m<0)
        vals=[m for _,m in ms]
        print(f'{c} vs {o}: {w}-{l} (+{sum(1 for _,a,b in rows for m in (a,b) if m==0)} ties) mean={statistics.mean(vals):+.0f} med={statistics.median(vals):+.0f} worst={min(vals):+.0f}')
        if 'sir.py' in o:
            neg=[(s_,m) for s_,m in ms if m<0]
            if neg:print('   losses:',sorted(neg)[:6])
