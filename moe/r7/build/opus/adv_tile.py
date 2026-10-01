# For INIT missions (init_extract logic), recover the TARGET TILE (unit pos when end-op fires)
# and ask: is that tile also a water candidate at obs[t-1]? Is it the nearest water tile?
import gzip,json,glob,sys
from collections import Counter,defaultdict
sys.path.insert(0,"/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/mine/rawkeep")
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
MOVES={"NORTH","SOUTH","EAST","WEST"}
W2T={"WATER":"water","HARVEST":"harvest","FEED":"feed","CARE":"care","COLLECT_FERTILIZER":"cfert","DIG":"dig","PLANT":"plant","BUILD_COOP":"struct_free","BUILD_PASTURE":"struct_free","PICKUP":"shed","PLACE":"shed","DROP":"shed","FERTILIZE":"fert"}
co=defaultdict(Counter); near=Counter(); n_ep=0
for f in sorted(glob.glob(f"{ROOT}/mine/rawkeep/*.json.gz")):
    x=json.loads(gzip.open(f).read()); tm=(x.get("info") or {}).get("TeamNames") or []
    if "DSM" not in tm: continue
    pi=tm.index("DSM"); S=x["steps"]; n_ep+=1
    seqs=defaultdict(list)
    for t,st in enumerate(S):
        if pi>=len(st): break
        a=st[pi].get("action") or {}
        for ui,op in enumerate([a.get("farmer")]+list(a.get("hands") or [])): seqs[ui].append((t,op))
    for ui,seq in seqs.items():
        inm=False
        for i,(t,op) in enumerate(seq):
            mv=isinstance(op,list) and op and op[0] in MOVES
            if mv and not inm:
                inm=True
                for j in range(i+1,min(i+13,len(seq))):
                    tj,oj=seq[j]; c=W2T.get(oj[0]) if isinstance(oj,list) and oj else None
                    if c:
                        o0=S[t-1][pi].get("observation") or {}; oj1=S[tj-1][pi].get("observation") or {}
                        if not o0 or not oj1: break
                        pos=[oj1["farms"][pi]["farmer"]]+list(oj1["farms"][pi].get("hands") or [])
                        if ui>=len(pos): break
                        tx,ty=pos[ui]; tl=o0["farms"][pi]["tiles"][ty][tx]
                        wc=isinstance(tl,dict) and tl.get("kind")=="PLANT" and not tl.get("watered_today")
                        co[c]["also_water_tile" if wc else "not_water_tile"]+=1
                        if c=="water":
                            p0=([o0["farms"][pi]["farmer"]]+list(o0["farms"][pi].get("hands") or []))
                            if ui<len(p0):
                                ux,uy=p0[ui]; T=o0["farms"][pi]["tiles"]
                                ds=[abs(xx-ux)+abs(yy-uy) for yy,r in enumerate(T) for xx,tt in enumerate(r) if isinstance(tt,dict) and tt.get("kind")=="PLANT" and not tt.get("watered_today")]
                                if ds: near["nearest(manh)" if abs(tx-ux)+abs(ty-uy)==min(ds) else "not_nearest"]+=1
                        break
                    if not(isinstance(oj,list) and oj and oj[0] in MOVES): break
            elif not mv: inm=False
    if n_ep>=30: break
print("eps",n_ep)
for c,v in sorted(co.items(),key=lambda kv:-sum(kv[1].values())):
    n=sum(v.values()); print(f"{c:12s} n={n:6d} target tile also unwatered-plant: {100*v['also_water_tile']/n:5.1f}%")
n=sum(near.values()); print("water missions to a manhattan-nearest unwatered tile: %.1f%% (n=%d)"%(100*near["nearest(manh)"]/n,n))
