"""Closed-loop proxy test: agent X (our seat) vs proxy P (their seat) on recorded seed+seat; kagsim."""
import sys, os, json, gzip, importlib.util, signal
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0,ROOT)
sys.path.insert(0, ROOT+"/kaggriculture-cppsim")
import kagsim
from concurrent.futures import ProcessPoolExecutor
PASS={"farmer":["PASS"],"hands":[],"market":[]}
def load(path, tag):
    ap=os.path.join(ROOT,path); cwd=os.getcwd(); os.chdir(os.path.dirname(ap))
    try:
        spec=importlib.util.spec_from_file_location("C_"+tag, ap); m=importlib.util.module_from_spec(spec)
        sys.modules["C_"+tag]=m; spec.loader.exec_module(m)
    finally: os.chdir(cwd)
    f=None
    for k,v in list(vars(m).items()):
        if callable(v) and not isinstance(v,type) and getattr(v,'__module__',None)==m.__name__: f=v
    return getattr(m,'agent',None) or f
def game(job):
    xname, xpath, pname, ppath, seed, us = job
    a=load(xpath, "x%d_%d"%(abs(hash(xname))%10**8,seed)); b=load(ppath, "p%d_%d"%(abs(hash(pname))%10**8,seed))
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
    return xname,pname,seed,us,r[us]-r[1-us]
if __name__=="__main__":
    spec=json.load(open(sys.argv[1])); out=sys.argv[2]
    jobs=[tuple(j) for j in spec]
    with ProcessPoolExecutor(max_workers=2) as ex, open(out,'w') as f:
        for res in ex.map(game, jobs, chunksize=1):
            f.write(json.dumps(res)+"\n"); f.flush()
