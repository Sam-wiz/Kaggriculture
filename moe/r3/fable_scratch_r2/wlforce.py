"""Is the step-57 market divergence a state artefact of the step-53 harvest? Wrap public WL so hand 0 PASSes at
53-58 and 84-91 (the WLV idle Opus found); re-measure first divergence and sell-set agreement vs recorded WLV."""
import sys, os, json, gzip
sys.argv=[sys.argv[0],"2179"]
exec(open("/tmp/fable_r2/wlmarket.py").read().split("if __name__")[0])
IDLE=set(range(53,59))|set(range(84,92))
def load_forced(path, tag):
    base=load(path, tag)
    def ag(obs):
        a=base(obs)
        if not isinstance(a,dict): return a
        st=int(obs["step"])
        if st in IDLE and a.get("hands"):
            h=[list(x) if isinstance(x,(list,tuple)) else x for x in a["hands"]]
            h[0]=["PASS"]; a=dict(a); a["hands"]=h
        return a
    return ag
def work3(job):
    ep, name, path, seed, opp, acts = job
    ag=load_forced(path, "%d_%d"%(ep,abs(hash(name)))); g=kagsim.Game(seed=int(seed)); me=1-opp
    agree={"unit":0,"mkt":0,"sell":0,"sell_late":0}; first={"unit":None,"mkt":None,"sell":None}; nlate=0
    firstdiff=None
    for t in range(719):
        ours = acts[t+1][me] if isinstance(acts[t+1][me],dict) else PASS
        rec = acts[t+1][opp] if isinstance(acts[t+1][opp],dict) else PASS
        try: a=ag(g.observe(opp))
        except Exception: a=PASS
        if not isinstance(a,dict): a=PASS
        for ch,fn in (("unit",units),("mkt",mkt),("sell",sellset)):
            if fn(a)==fn(rec): agree[ch]+=1
            elif first[ch] is None:
                first[ch]=t
                if ch=="mkt": firstdiff=(t, (a.get("market") or [])[:4], (rec.get("market") or [])[:4])
        if t>=300:
            nlate+=1
            if sellset(a)==sellset(rec): agree["sell_late"]+=1
        g.step(*((ours,a) if opp==1 else (a,ours)))
    return ep,agree,first,nlate,firstdiff,[float(g.reward(0)),float(g.reward(1))]
if __name__=="__main__":
    rows=json.load(open("moe/r3/fable_scratch/live_rows2.json"))
    sel=[r for r in rows if tuple(r["open_they"])==(5,0) and (r["R"] or 0)>=2179 and r["same_u"]>=0.85]
    jobs=[]
    for r in sel:
        d=json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz","rt"))
        jobs.append((int(r["ep"]),"WLf","rivals4/kaggriculture-yummers/_entry.py",d["seed"],1-r["seat"],d["actions"]))
    with ProcessPoolExecutor(max_workers=2) as ex:
        for (ep,agree,first,nlate,fd,rw),r in zip(ex.map(work3,jobs,chunksize=1),sel):
            print(f"{ep} {r['opp'][:14]:14s} R={r['R']:.0f} | first_div unit={first['unit']} mkt={first['mkt']} sell={first['sell']} | agree unit={agree['unit']/719:.3f} mkt={agree['mkt']/719:.3f} sell={agree['sell']/719:.3f} sell_t>=300={agree['sell_late']/max(1,nlate):.3f} | margin(us-WLf)={(rw[r['seat']]-rw[1-r['seat']]):+.0f} | 1st mkt diff @{fd[0] if fd else None}: WL={fd[1] if fd else None} REC={fd[2] if fd else None}",flush=True)
