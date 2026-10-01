# Decompose DIST moves: (a) T is a non-candidate class (fert/plant/shed); (b) T typed & dT==nearest (tie);
# (c) T typed & dT>nearest by 1-2; (d) >2 (truly distant). Also: does step reduce dist to T?
import json,sys,collections,itertools
exec(open("opus/target_probe.py").read().split("for rows in itertools")[0])
S=collections.Counter()
for rows in itertools.islice(ep_rows(sys.argv[1]),MAXEP):
    S["eps"]+=1; by=collections.defaultdict(list)
    for r in rows: by[(r["ui"],r["G"]["day"])].append(r)
    for rs in by.values():
        nxt=None
        for r in reversed(rs):
            c=cls(r)
            if c: nxt=(tuple(r["xy"]),c)
            r["_T"]=nxt
        for r in rs:
            y=r["y"]
            if y not in MV or r["_T"] is None: continue
            d=r["d"]; xy=tuple(r["xy"])
            js=[(d[k][0],k,d[k][1],d[k][2]) for k in WORK if k in d and 0<d[k][0]<99 and (k!="feed" or r["inv"]["WHEAT"]>0)]
            if not js: continue
            m=min(j[0] for j in js); ux,uy=MV[y]
            if any((ux and ux*j[2]>0) or (uy and uy*j[3]>0) for j in js if j[0]==m): continue
            T,c=r["_T"]; dT=abs(T[0]-xy[0])+abs(T[1]-xy[1]); S["n"]+=1
            nx=(xy[0]+ux,xy[1]+uy); S["step_reduces_dT"]+= abs(T[0]-nx[0])+abs(T[1]-nx[1])<dT
            if c not in WORK: b="a_nonWORK_"+("shed" if c=="shed" else "fert/plant/other")
            elif dT<=m: b="b_tie_or_closer"
            elif dT<=m+2: b="c_+1..2"
            else: b="d_>+2"
            S[b]+=1
            if c=="shed": S["shed_goods>0"]+=r["inv"]["goods"]>0; S["shed_wheat0"]+=r["inv"]["WHEAT"]==0
n=S["n"]; print("eps",S["eps"],"DIST n",n, "step reduces dist to T %.1f%%"%(100*S["step_reduces_dT"]/n))
for k in sorted(k for k in S if k[:2] in("a_","b_","c_","d_")): print(f"  {k}: {100*S[k]/n:.1f}%")
sh=sum(v for k,v in S.items() if k=="a_nonWORK_shed"); print("  shed-bound: carrying goods %.0f%%, wheat==0 %.0f%%"%(100*S["shed_goods>0"]/max(1,sh),100*S["shed_wheat0"]/max(1,sh)))
