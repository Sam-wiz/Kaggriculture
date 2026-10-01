# Round C Q1: what picks the distant committed target? For each move row, T = tile of the
# unit's next non-move op (same ep/ui/day). Compare DISTANT moves (not toward nearest job)
# vs NEAR moves (control) on: T op class; T == nearest-of-its-type; k == scarcest type;
# another unit closer to T (backfill); same ui worked T yesterday (dawn queue/ownership).
import json,sys,collections,itertools
MV={"NORTH":(0,-1),"SOUTH":(0,1),"EAST":(1,0),"WEST":(-1,0)}
WORK=["water","harvest","feed","care","cfert","dig"]
OPK={"WATER":"water","HARVEST":"harvest","FEED":"feed","CARE":"care","COLLECT_FERTILIZER":"cfert","DIG":"dig",
     "PLANT":"empty","BUILD_PASTURE":"empty","BUILD_COOP":"empty","FERTILIZE":"fert"}
SHED={(4,4),(5,4),(4,5),(5,5)}
MAXEP=int(sys.argv[2]) if len(sys.argv)>2 else 40
S=collections.Counter()
def ep_rows(path):
    cur=None;buf=[]
    for l in open(path):
        r=json.loads(l)
        if r["ep"]!=cur:
            if buf: yield buf
            cur=r["ep"];buf=[]
        buf.append(r)
    if buf: yield buf
def cls(r):
    y=r["y"].split(":")[0]
    if y in MV or y=="PASS": return None
    if y in("PICKUP","DROP") or (y=="PLACE" and tuple(r["xy"]) in SHED and r["on"].get("empty",False) is not True and False): return "shed"
    if y in("PICKUP","DROP"): return "shed"
    if y=="PLACE": return "shed" if tuple(r["xy"]) in SHED and not r["on"].get("struct") else "struct_free"
    return OPK.get(y,"other")
for rows in itertools.islice(ep_rows(sys.argv[1]),MAXEP):
    S["eps"]+=1
    by=collections.defaultdict(list); at=collections.defaultdict(dict); worked=collections.defaultdict(lambda:collections.defaultdict(set))
    for r in rows:
        day=r["G"]["day"]; by[(r["ui"],day)].append(r); at[r["t"]][r["ui"]]=tuple(r["xy"])
        if cls(r): worked[day][tuple(r["xy"])].add(r["ui"])
    for (ui,day),rs in by.items():
        nxt=None
        for r in reversed(rs):             # backward pass: next op target
            c=cls(r)
            if c: nxt=(tuple(r["xy"]),c,r["t"])
            r["_T"]=nxt
        for r in rs:
            y=r["y"]
            if y not in MV or r["_T"] is None: continue
            d=r["d"]; xy=tuple(r["xy"])
            js=[(d[k][0],k,d[k][1],d[k][2]) for k in WORK if k in d and 0<d[k][0]<99 and (k!="feed" or r["inv"]["WHEAT"]>0)]
            if not js: continue
            m=min(j[0] for j in js); ux,uy=MV[y]
            near=any((ux and ux*j[2]>0) or (uy and uy*j[3]>0) for j in js if j[0]==m)
            g="NEAR" if near else "DIST"
            T,c,tt=r["_T"]; S[(g,"n")]+=1; S[(g,"c",c)]+=1
            dT=abs(T[0]-xy[0])+abs(T[1]-xy[1]); S[(g,"dT")]+=dT; S[(g,"dnear")]+=m
            if c in d and d[c][0]<99:
                S[(g,"typed")]+=1
                if (xy[0]+d[c][1],xy[1]+d[c][2])==T or d[c][0]==dT: S[(g,"T_nearest_of_type")]+=1
                cn={k:v for k,v in r["G"]["cnts"].items() if k in WORK and v>0 and (k!="feed" or r["inv"]["WHEAT"]>0)}
                if c in cn:
                    S[(g,"scar_n")]+=1; S[(g,"scar_hit")]+=cn[c]==min(cn.values()); S[(g,"scar_base")]+=sum(v==min(cn.values()) for v in cn.values())/len(cn)
            oth=[p for u,p in at[r["t"]].items() if u!=ui]
            if oth:
                S[(g,"oth_n")]+=1
                if min(abs(T[0]-p[0])+abs(T[1]-p[1]) for p in oth)<dT: S[(g,"other_closer")]+=1
            if day>0 and c!="shed":
                prev=worked[day-1].get(T,set())
                if prev: S[(g,"yday_n")]+=1; S[(g,"yday_same_ui")]+=ui in prev
            S[(g,"h<3")]+= r["G"]["hour"]<3
for g in("NEAR","DIST"):
    n=S[(g,"n")]; p=lambda a,b: 100*S[(g,a)]/max(1,S[(g,b)])
    print(f"{g}: n={n}  mean dist to T {S[(g,'dT')]/n:.2f} vs nearest job {S[(g,'dnear')]/n:.2f}  hour<3 {100*S[(g,'h<3')]/n:.1f}%")
    print("  T class:", " ".join(f"{k[2]}={100*v/n:.1f}%" for k,v in sorted(S.items(),key=lambda kv:-kv[1]) if len(k)==3 and k[0]==g and k[1]=="c"))
    print(f"  T==nearest-of-its-type {p('T_nearest_of_type','typed'):.1f}% | type==scarcest {p('scar_hit','scar_n'):.1f}% (chance {p('scar_base','scar_n'):.1f}%) | other unit closer to T {p('other_closer','oth_n'):.1f}% | same ui worked T yesterday {p('yday_same_ui','yday_n'):.1f}% (n={S[(g,'yday_n')]})")
print("eps",S["eps"])
