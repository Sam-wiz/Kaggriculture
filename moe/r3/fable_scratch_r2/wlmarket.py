"""Public WL closed-loop in the opponent seat vs our recorded tape (kagsim), per-channel agreement with the
recorded WLV stream: unit ops, exact market list, and sell-event set (products sold that step).
Also first-divergence step per channel. Usage: python wlmarket.py <minR> [candpath]"""
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
def units(a): return norm((a.get("farmer"), a.get("hands")))
def mkt(a): return norm(a.get("market") or [])
def sellset(a): return frozenset((o[1]) for o in (a.get("market") or []) if isinstance(o,(list,tuple)) and o and o[0]=="SELL")
def work(job):
    ep, name, path, seed, opp, acts = job
    def h(*a): raise TimeoutError()
    signal.signal(signal.SIGALRM,h); signal.alarm(300)
    try:
        ag=load(path, "%d_%d"%(ep,abs(hash(name))))
        g=kagsim.Game(seed=int(seed)); me=1-opp
        agree={"unit":0,"mkt":0,"sell":0,"sell_late":0}; first={"unit":None,"mkt":None,"sell":None}; nlate=0
        for t in range(719):
            ours = acts[t+1][me] if isinstance(acts[t+1][me],dict) else PASS
            rec = acts[t+1][opp] if isinstance(acts[t+1][opp],dict) else PASS
            try: a=ag(g.observe(opp))
            except Exception: a=PASS
            if not isinstance(a,dict): a=PASS
            for ch,fn in (("unit",units),("mkt",mkt),("sell",sellset)):
                if fn(a)==fn(rec): agree[ch]+=1
                elif first[ch] is None: first[ch]=t
            if t>=300:
                nlate+=1
                if sellset(a)==sellset(rec): agree["sell_late"]+=1
            # closed loop: the candidate's own action drives its seat
            g.step(*((ours,a) if opp==1 else (a,ours)))
        signal.alarm(0)
        rw=[float(g.reward(0)),float(g.reward(1))]
        return ep,name,agree,first,nlate,rw
    except BaseException as e:
        signal.alarm(0); return ep,name,None,None,None,repr(e)[:80]
if __name__=="__main__":
    minR=float(sys.argv[1]); cand=sys.argv[2] if len(sys.argv)>2 else "rivals4/kaggriculture-yummers/_entry.py"
    rows=json.load(open("moe/r3/fable_scratch/live_rows2.json"))
    sel=[r for r in rows if tuple(r["open_they"])==(5,0) and (r["R"] or 0)>=minR and r["same_u"]>=0.85]
    jobs=[]
    for r in sel:
        d=json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz","rt"))
        jobs.append((int(r["ep"]),"WL",cand,d["seed"],1-r["seat"],d["actions"]))
    print(len(jobs),"jobs",flush=True)
    out=[]
    with ProcessPoolExecutor(max_workers=2) as ex:
        for (ep,name,agree,first,nlate,rw),r in zip(ex.map(work,jobs,chunksize=1),sel):
            if agree is None: print(ep,"ERR",rw,flush=True); continue
            print(f"{ep} {r['opp'][:16]:16s} R={r['R']:.0f} m={r['margin']:+6.0f} seat={r['seat']} | first_div unit={first['unit']} mkt={first['mkt']} sell={first['sell']} | agree unit={agree['unit']/719:.3f} mkt={agree['mkt']/719:.3f} sell={agree['sell']/719:.3f} sell_t>=300={agree['sell_late']/max(1,nlate):.3f} | closed-loop margin(us-them)={(rw[r['seat']]-rw[1-r['seat']]):+.0f}",flush=True)
            out.append(dict(ep=ep,opp=r["opp"],R=r["R"],m=r["margin"],first=first,agree=agree,nlate=nlate,rw=rw))
    json.dump(out,open(f"/tmp/fable_r2/wlmarket_{int(minR)}.json","w"))
