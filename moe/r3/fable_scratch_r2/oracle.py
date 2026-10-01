"""Oracle / holdout PREDICT2 test on the 18 WLV tapes. Our seat = live shepherd variant; their seat = WLV tape
(open-loop). Arms: vanilla (must reproduce the recorded margin), oracle (library = all 18 WLV streams incl. this
game's own), holdout (parity holdout: same-parity episodes excluded, so this game's own stream is excluded)."""
import os, sys, json, gzip, time
os.chdir("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"); sys.path.insert(0,".")
from concurrent.futures import ProcessPoolExecutor
PASS={"farmer":["PASS"],"hands":[],"market":[]}
def tape(acts, seat):
    def ag(obs):
        t=obs["step"]+1; a=acts[t][seat] if t<len(acts) else None
        return a if isinstance(a,dict) else PASS
    return ag
def job(args):
    ep, arm, seat, seed, acts = args
    import harness, sys as _s
    env={"vanilla":{}, "oracle":{"FABLE_STREAMS":"/tmp/fable_r2/wlv_streams.json"},
         "holdout":{"FABLE_STREAMS":"/tmp/fable_r2/wlv_streams.json","FABLE_EP":str(ep)}}[arm]
    for k in ("FABLE_STREAMS","FABLE_EP"): os.environ.pop(k,None)
    os.environ.update(env)
    path="subW_shepherd.py" if arm=="vanilla" else "/tmp/fable_r2/shep_oracle.py"
    name=f"arm_{arm}_{ep}"
    t0=time.time(); me=harness.load_agent(path, name=name)
    pair=(me, tape(acts,1-seat)) if seat==0 else (tape(acts,1-seat), me)
    r=harness.run_episode(pair[0], pair[1], seed=seed, copy_obs=True)
    rw=r["reward"]; mod=_s.modules.get(name)
    rep=getattr(mod,"_V92_Q_REPORT",None) if mod else None
    nstreams=len(getattr(mod,"_V92_Q_CACHE",{}).get("streams",[])) if mod else None
    return ep, arm, rw[seat]-rw[1-seat], rw[seat], rw[1-seat], (dict(rep) if rep else None), nstreams, round(time.time()-t0,1)
if __name__=="__main__":
    rows=json.load(open("moe/r3/fable_scratch/live_rows2.json"))
    sel=[r for r in rows if tuple(r["open_they"])==(5,0) and (r["R"] or 0)>=2000 and r["same_u"]>=0.85 and "Acidic" not in r["opp"]]
    arms=sys.argv[1].split(",") if len(sys.argv)>1 else ["vanilla","oracle","holdout"]
    jobs=[]
    for r in sel:
        d=json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz","rt"))
        for arm in arms: jobs.append((int(r["ep"]),arm,r["seat"],d["seed"],d["actions"]))
    res={}
    with ProcessPoolExecutor(max_workers=2) as ex:
        for ep,arm,m,ours,theirs,rep,ns,secs in ex.map(job,jobs,chunksize=1):
            res.setdefault(ep,{})[arm]=(m,ours,theirs,rep,ns)
            print(f"{ep} {arm:8s} margin={m:+7.0f} ours={ours:.0f} theirs={theirs:.0f} pred2={rep} nstreams={ns} {secs}s",flush=True)
    print("\nSUMMARY")
    print(" ep        opp            R    recorded | vanilla  | oracle  d(oracle-van)  | holdout d(hold-van)")
    tot={"oracle":[], "holdout":[]}; flips={"oracle":[0,0],"holdout":[0,0]}
    for r in sel:
        ep=int(r["ep"]); v=res[ep].get("vanilla",(None,))[0]
        line=f" {ep} {r['opp'][:14]:14s} {r['R']:.0f} {r['margin']:+7.0f} | {v if v is None else f'{v:+7.0f}':>8s} |"
        for arm in ("oracle","holdout"):
            if arm in res[ep] and v is not None:
                m=res[ep][arm][0]; dlt=m-v; tot[arm].append(dlt)
                if v<=0<m: flips[arm][0]+=1
                if m<=0<v: flips[arm][1]+=1
                line+=f" {m:+7.0f} {dlt:+7.0f} |"
        print(line)
    for arm in ("oracle","holdout"):
        if tot[arm]:
            n=len(tot[arm]); print(f"{arm}: mean delta vs vanilla {sum(tot[arm])/n:+.0f}/game over {n}; losses->wins {flips[arm][0]}, wins->losses {flips[arm][1]}")
    json.dump({str(k):{a:list(v[:3])+[v[3]] for a,v in d.items()} for k,d in res.items()}, open("/tmp/fable_r2/oracle_out.json","w"))
