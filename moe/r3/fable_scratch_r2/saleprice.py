"""Exact replay (python harness) of the WL-opening games; per side, per premium product: units sold,
unit-weighted mean quoted price at the step of sale, mean sale step. Off-by-one: actions[t] produced step t,
so the market orders acted on at observation step t are actions[t+1]."""
import json, gzip, os, sys
os.chdir("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"); sys.path.insert(0, ".")
import harness
from collections import defaultdict
PASS={"farmer":["PASS"],"hands":[],"market":[]}
PREM=("MILK","WOOL","STRAWBERRY","MELON")
rows=json.load(open("moe/r3/fable_scratch/live_rows2.json"))
minR=float(sys.argv[1]) if len(sys.argv)>1 else 2179
sel=[r for r in rows if tuple(r["open_they"])==(5,0) and (r["R"] or 0)>=minR and r["same_u"]>=0.85]
def tape(acts, seat):
    def ag(obs):
        t=obs["step"]+1; a=acts[t][seat] if t<len(acts) else None
        return a if isinstance(a,dict) else PASS
    return ag
agg=defaultdict(lambda: defaultdict(lambda: [0,0.0,0.0]))  # side -> product -> [units, sum(price*u), sum(step*u)]
print(" ep       opp              R    m     | MILK us/they units, meanP, meanStep | WOOL ... | STRAW ...")
for r in sel:
    d=json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz","rt")); A=d["actions"]; me=r["seat"]; op=1-me
    prices=[]
    def on_step(step, state, env):
        p=state[0].observation.market["prices"]; prices.append(dict(p))
    res=harness.run_episode(tape(A,0), tape(A,1), seed=d["seed"], on_step=on_step, copy_obs=False)
    fid = abs(res["reward"][me]-r["ours"])<1 and abs(res["reward"][op]-r["theirs"])<1
    per={"us":defaultdict(lambda:[0,0.0,0.0]),"they":defaultdict(lambda:[0,0.0,0.0])}
    for t in range(min(len(prices),len(A)-1)):
        p=prices[t]
        for side,seat in (("us",me),("they",op)):
            a=A[t+1][seat]
            if not isinstance(a,dict): continue
            for o in (a.get("market") or []):
                if isinstance(o,(list,tuple)) and len(o)>=3 and o[0]=="SELL" and o[1] in PREM and isinstance(o[2],(int,float)):
                    u=o[2]; per[side][o[1]][0]+=u; per[side][o[1]][1]+=p.get(o[1],0)*u; per[side][o[1]][2]+=t*u
                    agg[side][o[1]][0]+=u; agg[side][o[1]][1]+=p.get(o[1],0)*u; agg[side][o[1]][2]+=t*u
    def f(side,prod):
        u,sp,ss=per[side][prod]; return f"{u:4d} {sp/u if u else 0:6.1f} {ss/u if u else 0:5.0f}"
    print(f" {r['ep']} {r['opp'][:16]:16s} {r['R']:.0f} {r['margin']:+6.0f} fid={int(fid)} | M {f('us','MILK')} / {f('they','MILK')} | W {f('us','WOOL')} / {f('they','WOOL')} | S {f('us','STRAWBERRY')} / {f('they','STRAWBERRY')}", flush=True)
print("\nAGGREGATE over", len(sel), "games (units, unit-weighted mean quoted price at sale, mean sale step):")
for prod in PREM:
    for side in ("us","they"):
        u,sp,ss=agg[side][prod]
        print(f"  {prod:10s} {side:4s} units={u:5d} meanP={sp/u if u else 0:6.1f} meanStep={ss/u if u else 0:5.0f}  revenue~={sp:8.0f}")
