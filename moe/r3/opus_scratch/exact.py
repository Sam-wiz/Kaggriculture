"""Exact identification: candidate in opponent seat vs our recorded tape; first divergence step."""
import sys, os, json, gzip, importlib.util, signal
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
def load(path, tag):
    ap=os.path.join(ROOT,path); cwd=os.getcwd(); os.chdir(os.path.dirname(ap))
    try:
        spec=importlib.util.spec_from_file_location("X_"+tag, ap); m=importlib.util.module_from_spec(spec)
        sys.modules["X_"+tag]=m; spec.loader.exec_module(m)
    finally: os.chdir(cwd)
    f=None
    for k,v in list(vars(m).items()):
        if callable(v) and not isinstance(v,type) and getattr(v,'__module__',None)==m.__name__: f=v
    return getattr(m,'agent',None) or f
def work(job):
    ep, name, path, seed, opp, acts = job
    def h(*a): raise TimeoutError()
    signal.signal(signal.SIGALRM,h); signal.alarm(120)
    try:
        ag=load(path, "%d_%d"%(ep,abs(hash(name))))
        g=kagsim.Game(seed=int(seed)); me=1-opp
        for t in range(719):
            ours = acts[t+1][me] if isinstance(acts[t+1][me],dict) else PASS
            try: a=ag(g.observe(opp))
            except Exception: a=PASS
            if norm(a)!=norm(acts[t+1][opp]):
                signal.alarm(0); return ep,name,t,None
            g.step(*( (ours,a) if opp==1 else (a,ours) ))
        signal.alarm(0); return ep,name,719,[float(g.reward(0)),float(g.reward(1))]
    except BaseException as e:
        signal.alarm(0); return ep,name,-1,repr(e)[:60]
if __name__=="__main__":
    lib=json.load(open('/tmp/opus_r3/libopen.json'))
    opps=json.load(open('/tmp/opus_r3/opps_c.json'))
    minR=float(sys.argv[1]); maxc=int(sys.argv[2])
    jobs=[]
    for o in opps:
        if (o['R'] or 0)<minR or not o['cands'] or len(o['cands'])>maxc: continue
        d=json.load(gzip.open(o['path'],'rt'))
        for c in o['cands']:
            jobs.append((o['ep'],c,lib[c][0],d['seed'],1-o['seat'],d['actions']))
    print(len(jobs),"jobs",flush=True)
    best={}
    with ProcessPoolExecutor(max_workers=2) as ex:
        for ep,name,t,rw in ex.map(work, jobs, chunksize=2):
            best.setdefault(ep,[]).append((t,name,rw))
    out={}
    for o in opps:
        if o['ep'] in best:
            b=sorted(best[o['ep']],key=lambda x:-x[0])
            out[o['ep']]=b
            print(f"R={o['R']:.0f} {o['opp'][:18]:18} m={o['m']:+6.0f} top: "+"; ".join(f"{n.split('/')[-1][:30]}@{t}" for t,n,_ in b[:3]), flush=True)
    json.dump(out,open('/tmp/opus_r3/exact_%s_%d.json'%(sys.argv[1],maxc),'w'))
