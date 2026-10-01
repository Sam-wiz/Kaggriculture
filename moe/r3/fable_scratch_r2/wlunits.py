"""Herd-loss check: public WL closed-loop in the opp seat vs our tape — its premium units sold and final bank,
vs the recorded WLV's premium units and bank. If WL's units << WLV's, the missing herd layer is the delta."""
import sys, os, json, gzip
sys.argv=[sys.argv[0],"2179"]
exec(open("/tmp/fable_r2/wlmarket.py").read().split("if __name__")[0])
from collections import Counter
def sells(a):
    c=Counter()
    for o in ((a or {}).get("market") or []):
        if isinstance(o,(list,tuple)) and len(o)>=3 and o[0]=="SELL" and isinstance(o[2],(int,float)): c[o[1]]+=int(o[2])
    return c
def work2(job):
    ep, name, path, seed, opp, acts = job
    ag=load(path, "%d_%d"%(ep,abs(hash(name)))); g=kagsim.Game(seed=int(seed)); me=1-opp
    cu=Counter(); cr=Counter(); animals_end=None
    for t in range(719):
        ours = acts[t+1][me] if isinstance(acts[t+1][me],dict) else PASS
        rec = acts[t+1][opp] if isinstance(acts[t+1][opp],dict) else PASS
        try: a=ag(g.observe(opp))
        except Exception: a=PASS
        if not isinstance(a,dict): a=PASS
        cu.update(sells(a)); cr.update(sells(rec))
        g.step(*((ours,a) if opp==1 else (a,ours)))
    o=g.observe(opp); tiles=o["farms"][opp]["tiles"]
    an=sum(1 for row in tiles for x in row if isinstance(x,dict) and x.get("animal"))
    return ep, dict(cu), dict(cr), an, [float(g.reward(0)),float(g.reward(1))]
if __name__=="__main__":
    rows=json.load(open("moe/r3/fable_scratch/live_rows2.json"))
    sel=[r for r in rows if tuple(r["open_they"])==(5,0) and (r["R"] or 0)>=2179 and r["same_u"]>=0.85]
    jobs=[]
    for r in sel:
        d=json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz","rt"))
        jobs.append((int(r["ep"]),"WL","rivals4/kaggriculture-yummers/_entry.py",d["seed"],1-r["seat"],d["actions"]))
    P=("MILK","WOOL","STRAWBERRY","MELON")
    with ProcessPoolExecutor(max_workers=2) as ex:
        for (ep,cu,cr,an,rw),r in zip(ex.map(work2,jobs,chunksize=1),sel):
            pu=sum(cu.get(p,0) for p in P); pr=sum(cr.get(p,0) for p in P)
            print(f"{ep} {r['opp'][:14]:14s} R={r['R']:.0f} | publicWL closed-loop: prem units={pu:4d} (M{cu.get('MILK',0)} W{cu.get('WOOL',0)} S{cu.get('STRAWBERRY',0)}) animals_end={an} bank={rw[1-r['seat']]:.0f} | WLV recorded: prem units={pr:4d} (M{cr.get('MILK',0)} W{cr.get('WOOL',0)} S{cr.get('STRAWBERRY',0)}) bank={r['theirs']:.0f} | our tape bank={rw[r['seat']]:.0f} (rec {r['ours']:.0f})",flush=True)
