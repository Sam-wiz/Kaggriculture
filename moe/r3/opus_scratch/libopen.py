import sys, os, glob, json, importlib.util, signal
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0,ROOT)
sys.path.insert(0, ROOT+"/kaggriculture-cppsim")
import kagsim
from concurrent.futures import ProcessPoolExecutor
PASS={"farmer":["PASS"],"hands":[],"market":[]}
def norm(a):
    if isinstance(a, dict): return tuple((k, norm(v)) for k, v in sorted(a.items()))
    if isinstance(a, (list, tuple)): return tuple(norm(x) for x in a)
    if isinstance(a, float) and a == int(a): return int(a)
    return a
def lib():
    c={}
    for p in sorted(glob.glob("rivals*/*/_entry.py")):
        c[p.split('/')[0]+'/'+os.path.basename(os.path.dirname(p))]=p
    for p in sorted(glob.glob("data/donors/agents/*.py")): c["donor/"+os.path.basename(p)[:-3]]=p
    for p in sorted(glob.glob("sub*.py"))+sorted(glob.glob("moe/cand_*.py"))+sorted(glob.glob("moe/opus/cand_*.py"))+sorted(glob.glob("moe/codex/cand_*.py")):
        c["ours/"+p]=p
    return c
def load(path, tag):
    spec=importlib.util.spec_from_file_location("L_"+tag, path); m=importlib.util.module_from_spec(spec)
    sys.modules["L_"+tag]=m; spec.loader.exec_module(m)
    f=None
    for k,v in list(vars(m).items()):
        if callable(v) and not isinstance(v,type) and getattr(v,'__module__',None)==m.__name__: f=v  # last callable
    return getattr(m,'agent',None) or f
def work(item):
    name,path=item
    def h(*a): raise TimeoutError()
    signal.signal(signal.SIGALRM,h); signal.alarm(40)
    try:
        ap=os.path.join(ROOT,path); cwd=os.getcwd(); os.chdir(os.path.dirname(ap))
        try: ag=load(ap, str(abs(hash(name))))
        finally: os.chdir(cwd)
        g=kagsim.Game(seed=777); out=[]
        for i in range(3):
            try: a=ag(g.observe(0))
            except Exception as e: a=PASS
            out.append(norm(a)); g.step(a,PASS)
        signal.alarm(0)
        return name,path,json.dumps(out)
    except BaseException as e:
        signal.alarm(0); return name,path,"ERR "+repr(e)[:80]
if __name__=="__main__":
    c=lib(); print(len(c),flush=True)
    res={}
    with ProcessPoolExecutor(max_workers=2) as ex:
        for name,path,sig in ex.map(work, list(c.items()), chunksize=4):
            res[name]=[path,sig]
    json.dump(res,open('/tmp/opus_r3/libopen.json','w'))
    print("done", sum(1 for v in res.values() if not v[1].startswith("ERR")))
