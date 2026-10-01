import importlib.util,harness,statistics,sys,collections
from concurrent.futures import ProcessPoolExecutor
def Lp(p):
    spec=importlib.util.spec_from_file_location('m'+p.replace('/','_').replace('.','_'),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m.agent
def job(a):
    f,opp,seed,swap=a
    x,y=(Lp(opp),Lp(f)) if swap else (Lp(f),Lp(opp))
    r=harness.run_episode(x,y,seed=seed,copy_obs=False)
    p,q=r['reward'][::-1] if swap else r['reward']
    return (f,opp,p-q)
if __name__=='__main__':
    cells={}
    spec=sys.argv[1]  # e.g. 'cand.py:opp1.py,opp2.py'
    pairs=[]
    for grp in sys.argv[1:]:
        f,ops=grp.split(':')
        for o in ops.split(','): pairs.append((f,o))
    seeds=list(range(int(sys.argv[2] if len(sys.argv)>2 else 9200),
                     int(sys.argv[3] if len(sys.argv)>3 else 9216))) if False else list(range(9200,9216))
    jobs=[(f,o,s,sw) for f,o in pairs for s in seeds for sw in (0,1)]
    with ProcessPoolExecutor(max_workers=8) as ex:
        res=list(ex.map(job,jobs))
    agg=collections.defaultdict(list)
    for f,o,d in res: agg[(f,o)].append(d)
    for (f,o),ds in sorted(agg.items()):
        w=sum(1 for x in ds if x>0)
        print('%-22s vs %-18s W%2d/%d avg %+6.0f'%(f,o[:18],w,len(ds),statistics.mean(ds)))
