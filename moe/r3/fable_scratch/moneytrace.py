import json, gzip, os, sys
os.chdir("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"); sys.path.insert(0, ".")
import harness
PASS={"farmer":["PASS"],"hands":[],"market":[]}
rows=json.load(open("/tmp/fable/live_rows2.json"))
sel=[r for r in rows if r["build"]=="shepherd" and r["same_u"]>=0.95 and (r["R"] or 0)>=2000 and r["opp"]!="Sam-wiz"]
def tape(acts, seat):
    def ag(obs):
        t=obs["step"]+1; a=acts[t][seat] if t<len(acts) else None
        return a if isinstance(a,dict) else PASS
    return ag
out=[]
for r in sel:
    d=json.load(gzip.open(r["path"] if "path" in r else f"mine/opp/{r['ep']}.json.gz","rt"))
    A=d["actions"]; me=r["seat"]; op=1-me
    money=[]; prices=[]
    def on_step(step, state, env):
        f=state[0].observation.farms
        money.append((f[0]["money"], f[1]["money"]))
        p=state[0].observation.market["prices"]; inv=state[0].observation.market["inventory"]
        prices.append((p["MILK"],p["WOOL"],p["STRAWBERRY"],inv["MILK"],inv["WOOL"],inv["STRAWBERRY"]))
    res=harness.run_episode(tape(A,0), tape(A,1), seed=d["seed"], on_step=on_step, copy_obs=False)
    fid = abs(res["reward"][me]-r["ours"])<1 and abs(res["reward"][op]-r["theirs"])<1
    # per-day margin delta
    daily=[]
    prev=0.0
    for day in range(30):
        s=min(len(money)-1, day*24+23)
        m=money[s][me]-money[s][op]
        daily.append(round(m-prev)); prev=m
    out.append(dict(ep=r["ep"], opp=r["opp"], R=r["R"], seat=me, margin=r["margin"], fid=fid, daily=daily,
                    open_they=r["open_they"], first_prem_diff=r["first_prem_diff"]))
    print(r["ep"], r["opp"][:18], f"R={r['R']:.0f} m={r['margin']:+.0f} fid={fid} d0-5={sum(daily[:6]):+d} d6-12={sum(daily[6:13]):+d} d13-24={sum(daily[13:25]):+d} d25-29={sum(daily[25:]):+d}", flush=True)
json.dump(out, open("/tmp/fable/moneytrace.json","w"))
