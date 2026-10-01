"""shepherd / hyb2965 market on WLV's exact farm: first market divergence AFTER step 1 (ignore the opening),
first 6 differing steps with both order lists, and count of differing steps per phase."""
import sys, os, json, gzip
sys.argv=[sys.argv[0],"2179"]
exec(open("/tmp/fable_r2/wlmarket.py").read().split("if __name__")[0])
CANDS={"shepherd":"subW_shepherd.py","hyb2965":"subX_hyb2965.py"}
def phase(t):
    d=t//24
    return "d0-5" if d<=5 else "d6-12" if d<=12 else "d13-24" if d<=24 else "d25-29"
def work5(job):
    ep, name, path, seed, opp, acts = job
    ag=load(path, "%d_%d"%(ep,abs(hash(name)))); g=kagsim.Game(seed=int(seed)); me=1-opp
    diffs=[]; per={"d0-5":0,"d6-12":0,"d13-24":0,"d25-29":0}; first2=None
    for t in range(719):
        ours = acts[t+1][me] if isinstance(acts[t+1][me],dict) else PASS
        rec = acts[t+1][opp] if isinstance(acts[t+1][opp],dict) else PASS
        try: a=ag(g.observe(opp))
        except Exception: a=PASS
        if not isinstance(a,dict): a=PASS
        hyb={"farmer":rec.get("farmer",["PASS"]),"hands":rec.get("hands",[]),"market":a.get("market") or []}
        if mkt(hyb)!=mkt(rec):
            if t>=2:
                per[phase(t)]+=1
                if first2 is None: first2=t
                if len(diffs)<6: diffs.append((t,[o for o in hyb["market"]][:4],[o for o in (rec.get("market") or [])][:4]))
        g.step(*((ours,hyb) if opp==1 else (hyb,ours)))
    return name,ep,first2,per,diffs
if __name__=="__main__":
    rows=json.load(open("moe/r3/fable_scratch/live_rows2.json"))
    sel=[r for r in rows if tuple(r["open_they"])==(5,0) and (r["R"] or 0)>=2179 and r["same_u"]>=0.85]
    jobs=[]; meta=[]
    for cname,cpath in CANDS.items():
        for r in sel:
            d=json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz","rt"))
            jobs.append((int(r["ep"]),cname,cpath,d["seed"],1-r["seat"],d["actions"])); meta.append(r)
    with ProcessPoolExecutor(max_workers=2) as ex:
        for (name,ep,first2,per,diffs),r in zip(ex.map(work5,jobs,chunksize=1),meta):
            print(f"{name:8s} {ep} {r['opp'][:12]:12s} first_mkt_div(t>=2)={first2} diffs/phase={per}",flush=True)
            for t,c,rc in diffs[:4]: print(f"      t={t} (d{t//24} h{t%24}) cand={c} REC={rc}")
