"""From recorded tapes only: (1) sell-event-set agreement us-vs-WLV (same metric as wlmarket.py, for comparison
with public-WL-vs-WLV); (2) sell-timing lag: for each premium product, pair our k-th cumulative unit with their
k-th cumulative unit and measure who sold it first; (3) at contested steps, who sells on the DROP tick."""
import json, gzip
from collections import Counter, defaultdict
rows=json.load(open("moe/r3/fable_scratch/live_rows2.json"))
sel=[r for r in rows if tuple(r["open_they"])==(5,0) and (r["R"] or 0)>=2000 and r["same_u"]>=0.85 and "Acidic" not in r["opp"]]
PREM=("MILK","WOOL","STRAWBERRY")
def sellset(a): return frozenset(o[1] for o in ((a or {}).get("market") or []) if isinstance(o,(list,tuple)) and o and o[0]=="SELL")
def sells(a):
    c=Counter()
    for o in ((a or {}).get("market") or []):
        if isinstance(o,(list,tuple)) and len(o)>=3 and o[0]=="SELL" and isinstance(o[2],(int,float)): c[o[1]]+=int(o[2])
    return c
tot_agree=0; tot_n=0; late_agree=0; late_n=0
lag_hist=Counter(); lead_units=Counter()
drop_tick=Counter()
print(" ep       opp              R     m    sellset_agree  t>=300  | units-first: us / they / same | per-product lead (they-us units sold earlier)")
for r in sel:
    d=json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz","rt")); A=d["actions"]; me=r["seat"]; op=1-me
    ag=0; n=0; la=0; ln=0
    cum={"us":defaultdict(list),"they":defaultdict(list)}  # product -> list of step per unit
    for t in range(1,len(A)):
        a=A[t][me] if isinstance(A[t][me],dict) else {}; b=A[t][op] if isinstance(A[t][op],dict) else {}
        n+=1; ag+= sellset(a)==sellset(b)
        if t>300: ln+=1; la+= sellset(a)==sellset(b)
        for p,u in sells(a).items():
            if p in PREM: cum["us"][p]+= [t]*u
        for p,u in sells(b).items():
            if p in PREM: cum["they"][p]+= [t]*u
        # DROP tick: did a side both DROP/PLACE and SELL premium the same step?
        for side,x in (("us",a),("they",b)):
            ops=[x.get("farmer")]+list(x.get("hands") or [])
            dropped=any(isinstance(o,(list,tuple)) and o and o[0] in ("DROP","PLACE") for o in ops)
            if dropped and any(p in PREM for p in sellset(x)): drop_tick[side]+=1
    tot_agree+=ag; tot_n+=n; late_agree+=la; late_n+=ln
    usf=theyf=same=0; lead=""
    for p in PREM:
        u=cum["us"][p]; v=cum["they"][p]; k=min(len(u),len(v))
        pu=pt=0
        for i in range(k):
            dl=v[i]-u[i]  # negative: they sold the i-th unit earlier
            if dl<0: theyf+=1; pt+=1
            elif dl>0: usf+=1; pu+=1
            else: same+=1
            lag_hist[max(-5,min(5,dl))]+=1
        lead+=f" {p[:1]}:{pt-pu:+d}"
    print(f" {r['ep']} {r['opp'][:16]:16s} {r['R']:.0f} {r['margin']:+6.0f}   {ag/n:.3f}       {la/max(1,ln):.3f}  | {usf:4d} / {theyf:4d} / {same:4d} |{lead}")
print(f"\nsell-set agreement us-vs-WLV: all {tot_agree/tot_n:.3f}, t>300 {late_agree/late_n:.3f}")
print("lag histogram (they_step - our_step for the k-th unit; clipped ±5):", dict(sorted(lag_hist.items())))
print("premium SELL on a DROP/PLACE tick (count of steps): ", dict(drop_tick))
