# Probe: are DSM/Vadim market decisions memoryless functions of visible obs? (causal: obs[t-1] -> action[t])
import gzip,json,glob,sys,collections
TEAM=sys.argv[1]
AN={"GOOSE":"COOP","COW":"PASTURE","SHEEP":"PASTURE"}
sellsig=collections.Counter(); animal=collections.Counter(); hires=[]; land=[]; ex_ani=[]
eps=0
for f in sorted(glob.glob("mine/rawkeep/*.json.gz")):
    x=json.load(gzip.open(f,"rt"))
    if TEAM not in x["info"]["TeamNames"]: continue
    pi=x["info"]["TeamNames"].index(TEAM); eps+=1; S=x["steps"]
    for t in range(1,len(S)):
        o=S[t-1][pi].get("observation") or {}; a=S[t][pi].get("action") or {}
        if not o or "private" not in o: continue
        m=[q for q in (a.get("market") or []) if q]; me=o["farms"][pi]; pr=o["private"]
        sells=tuple(q[1] for q in m if q[0]=="SELL")
        sellsig[(len(sells), tuple(sorted(set(q[2] for q in m if q[0]=="SELL"))))]+=1
        free={"COOP":0,"PASTURE":0}; herd=collections.Counter()
        for row in me["tiles"]:
            for tl in row:
                if isinstance(tl,dict) and tl.get("kind") in free:
                    if tl.get("animal"): herd[tl["animal"]]+=1
                    else: free[tl["kind"]]+=1
        held=collections.Counter()
        for sp in AN:
            held[AN[sp]]+=pr["shed"].get(sp,0)+sum((iv or {}).get(sp,0) for iv in pr["inventories"])
        buy={"COOP":0,"PASTURE":0}
        for q in m:
            if q[0]=="BUY_ANIMAL": buy[AN[q[1]]]+=q[2]
        for k in free:
            gap=free[k]-held[k]
            animal[(k, "fire" if buy[k] else "none", "eq" if buy[k]==max(gap,0) else ("gap>0" if gap>0 else "gap<=0"))]+=1
            if buy[k] and buy[k]!=max(gap,0) and len(ex_ani)<6: ex_ani.append((t,k,buy[k],free[k],held[k],me["money"]))
        nh=sum(1 for q in m if q[0]=="HIRE")
        if nh: 
            nj=sum(1 for row in me["tiles"] for tl in row if isinstance(tl,dict) and tl.get("kind") in("PLANT","COOP","PASTURE"))
            hires.append((o["day"],o["hour"],nh,nj,sum(herd.values()),me["money"]))
        if any(q[0]=="BUY_LAND" for q in m): land.append((o["day"],o["hour"],me["money"],len(me["unlocked_quadrants"])))
print(TEAM,"eps",eps)
print("SELL signatures (nSELL, qty set):",sellsig.most_common(6))
print("BUY_ANIMAL vs (free struct - held animals):"); [print(" ",k,v) for k,v in sorted(animal.items())]
print(" mismatched fires (t,struct,buy,free,held,money):",ex_ani)
import statistics as st
hh=collections.Counter(h[1] for h in hires); print("HIRE hours:",hh.most_common(4))
# does hire count track jobs? bucket by day
byd=collections.defaultdict(list)
for d,h,n,nj,hd,mo in hires: byd[d].append((n,nj))
print("HIRE n by day (mean n, mean jobs, sd n):",[(d,round(st.mean(v[0] for v in L),1),round(st.mean(v[1] for v in L)),round(st.pstdev([v[0] for v in L]),1)) for d,L in sorted(byd.items())][:30:3])
# within-day residual: corr(n, jobs) after day-demeaning
import math
r=[];
for d,L in byd.items():
    if len(L)>3:
        mn=st.mean(v[0] for v in L); mj=st.mean(v[1] for v in L); r+= [(v[0]-mn,v[1]-mj) for v in L]
if r:
    sx=math.sqrt(sum(a*a for a,b in r)); sy=math.sqrt(sum(b*b for a,b in r))
    print("within-day corr(hires, jobs):", round(sum(a*b for a,b in r)/(sx*sy+1e-9),3), "n",len(r), "frac zero-var", round(sum(1 for a,b in r if a==0)/len(r),2))
print("BUY_LAND (day,hour,money,quads):",sorted(land)[:12], "... n",len(land))
