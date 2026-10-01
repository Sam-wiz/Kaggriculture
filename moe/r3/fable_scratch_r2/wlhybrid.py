"""Deconfounded market test: candidate's MARKET orders closed-loop from its own observation, but its UNIT ops
replaced by WLV's recorded unit ops (so the farm state tracks WLV's). Compare candidate market stream vs WLV's
recorded market stream. If WL's market wrapper is WLV's market, agreement should be ~1.0."""
import sys, os, json, gzip
sys.argv=[sys.argv[0],"2179"]
exec(open("/tmp/fable_r2/wlmarket.py").read().split("if __name__")[0])
CANDS={"publicWL":"rivals4/kaggriculture-yummers/_entry.py","shepherd":"subW_shepherd.py","hyb2965":"subX_hyb2965.py"}
def work4(job):
    ep, name, path, seed, opp, acts = job
    ag=load(path, "%d_%d"%(ep,abs(hash(name)))); g=kagsim.Game(seed=int(seed)); me=1-opp
    agree={"mkt":0,"sell":0,"sell_late":0}; first={"mkt":None,"sell":None}; nlate=0; fd=None
    for t in range(719):
        ours = acts[t+1][me] if isinstance(acts[t+1][me],dict) else PASS
        rec = acts[t+1][opp] if isinstance(acts[t+1][opp],dict) else PASS
        try: a=ag(g.observe(opp))
        except Exception: a=PASS
        if not isinstance(a,dict): a=PASS
        hyb={"farmer":rec.get("farmer",["PASS"]),"hands":rec.get("hands",[]),"market":a.get("market") or []}
        for ch,fn in (("mkt",mkt),("sell",sellset)):
            if fn(hyb)==fn(rec): agree[ch]+=1
            elif first[ch] is None:
                first[ch]=t
                if ch=="sell": fd=(t,(hyb["market"])[:5],(rec.get("market") or [])[:5])
        if t>=300:
            nlate+=1
            if sellset(hyb)==sellset(rec): agree["sell_late"]+=1
        g.step(*((ours,hyb) if opp==1 else (hyb,ours)))
    return name,ep,agree,first,nlate,fd,[float(g.reward(0)),float(g.reward(1))]
if __name__=="__main__":
    rows=json.load(open("moe/r3/fable_scratch/live_rows2.json"))
    sel=[r for r in rows if tuple(r["open_they"])==(5,0) and (r["R"] or 0)>=2179 and r["same_u"]>=0.85]
    jobs=[]; meta=[]
    for cname,cpath in CANDS.items():
        for r in sel:
            d=json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz","rt"))
            jobs.append((int(r["ep"]),cname,cpath,d["seed"],1-r["seat"],d["actions"])); meta.append(r)
    summ={}
    with ProcessPoolExecutor(max_workers=2) as ex:
        for (name,ep,agree,first,nlate,fd,rw),r in zip(ex.map(work4,jobs,chunksize=1),meta):
            s=summ.setdefault(name,{"mkt":[], "sell":[], "late":[], "m":[]})
            s["mkt"].append(agree["mkt"]/719); s["sell"].append(agree["sell"]/719); s["late"].append(agree["sell_late"]/max(1,nlate)); s["m"].append(rw[r["seat"]]-rw[1-r["seat"]])
            print(f"{name:9s} {ep} {r['opp'][:12]:12s} R={r['R']:.0f} rec_m={r['margin']:+6.0f} | first_div mkt={first['mkt']} sell={first['sell']} | agree mkt={agree['mkt']/719:.3f} sell={agree['sell']/719:.3f} sell_t>=300={agree['sell_late']/max(1,nlate):.3f} | margin(us-hyb)={(rw[r['seat']]-rw[1-r['seat']]):+.0f} | 1st sell diff @{fd[0] if fd else None}: cand={fd[1] if fd else None} REC={fd[2] if fd else None}",flush=True)
    print("\nSUMMARY (mean over 14 WLV games; candidate market on WLV's exact farm actions):")
    for name,s in summ.items():
        n=len(s["m"]); print(f"  {name:9s} mkt_exact={sum(s['mkt'])/n:.3f} sellset={sum(s['sell'])/n:.3f} sellset_t>=300={sum(s['late'])/n:.3f} mean margin(us-hyb)={sum(s['m'])/n:+.0f}  (recorded us-WLV mean {sum(r['margin'] for r in sel)/len(sel):+.0f})")
