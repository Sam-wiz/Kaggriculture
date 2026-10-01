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
    return (f,opp,p-q,r['status'])
if __name__=='__main__':
    pairs=[]
    for grp in sys.argv[1].split(';'):
        f,ops=grp.split(':')
        for o in ops.split(','): pairs.append((f,o))
    n=int(sys.argv[2]) if len(sys.argv)>2 else 16
    s0=int(sys.argv[3]) if len(sys.argv)>3 else 9200
    jobs=[(f,o,s,sw) for f,o in pairs for s in range(s0,s0+n) for sw in (0,1)]
    with ProcessPoolExecutor(max_workers=8) as ex:
        res=list(ex.map(job,jobs))
    agg=collections.defaultdict(list)
    errs=collections.Counter()
    for f,o,d,st in res:
        agg[(f,o)].append(d)
        for s in st:
            if s!='DONE': errs[(f,o,s)]+=1
    for (f,o),ds in sorted(agg.items()):
        w=sum(1 for x in ds if x>0);t=sum(1 for x in ds if x==0)
        print('%-22s vs %-40s W%2d T%d L%2d avg %+6.0f'%(f.split('/')[-1],o.split('/')[-2][:38] if '/' in o else o,w,t,len(ds)-w-t,statistics.mean(ds)))
    for k,v in errs.items(): print('ERR',k,v)
