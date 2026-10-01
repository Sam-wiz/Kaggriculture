"""WLV premium-sale streams from the 18 WLV tapes, in the _v92_q_streams format:
[{"ep": <episode>, "ev": [[tick, item_index, qty], ...]}] over MILK/WOOL/STRAWBERRY (index 0,1,2).
tick = the observation step at which the sale was VISIBLE in the inventory delta = the step the order was
issued (actions[t+1] answers obs t; the fill shows in obs t+1's inventory; _v92_q_update stores it under step-1 = t).
Quantities are order quantities capped at 100 (in-shed sellers: order ~= fill)."""
import json, gzip
rows=json.load(open("moe/r3/fable_scratch/live_rows2.json"))
sel=[r for r in rows if tuple(r["open_they"])==(5,0) and (r["R"] or 0)>=2000 and r["same_u"]>=0.85 and "Acidic" not in r["opp"]]
ITEMS=("MILK","WOOL","STRAWBERRY")
out=[]
for r in sel:
    d=json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz","rt")); A=d["actions"]; op=1-r["seat"]
    ev={}
    for t in range(len(A)-1):
        a=A[t+1][op]
        if not isinstance(a,dict): continue
        for o in (a.get("market") or []):
            if isinstance(o,(list,tuple)) and len(o)>=3 and o[0]=="SELL" and o[1] in ITEMS and isinstance(o[2],(int,float)) and o[2]>=2:
                k=(t,ITEMS.index(o[1])); ev[k]=ev.get(k,0)+min(100,int(o[2]))
    out.append({"ep":int(r["ep"]),"opp":r["opp"],"shops2":None,"ev":[[t,i,q] for (t,i),q in sorted(ev.items())]})
json.dump(out,open("/tmp/fable_r2/wlv_streams.json","w"))
print(len(out),"streams; events per stream:",[len(x["ev"]) for x in out])
