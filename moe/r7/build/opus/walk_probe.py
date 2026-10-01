# Is DSM's walk = nearest-pending-work? Move rows: does step match sign(dx/dy) of nearest job?
# Stay rows: when current tile has a pending op, P(op) vs P(move).
import json,sys,collections
P=sys.argv[1]; MV={"NORTH":(0,-1),"SOUTH":(0,1),"EAST":(1,0),"WEST":(-1,0)}
WORK=["water","harvest","feed","care","cfert","dig"]
def feas(r,k):
    if k=="feed": return r["inv"]["WHEAT"]>0
    return True
S=collections.Counter()
for l in open(P):
    r=json.loads(l); y=r["y"]; d=r["d"]
    js=[(d[k][0],k,d[k][1],d[k][2]) for k in WORK if k in d and d[k][0]<99 and feas(r,k)]
    on0=[k for k in WORK if k in d and d[k][0]==0 and feas(r,k)]
    if y in MV:
        S["mv"]+=1
        if on0: S["mv_with_work_here"]+=1
        js=[j for j in js if j[0]>0]
        if not js: S["mv_nojob"]+=1; continue
        m=min(j[0] for j in js); near=[j for j in js if j[0]==m]
        ux,uy=MV[y]
        ok=any((ux and ux*j[2]>0) or (uy and uy*j[3]>0) for j in near)
        okall=any((ux and ux*j[2]>0) or (uy and uy*j[3]>0) for j in js)
        S["mv_toward_nearest"]+=ok; S["mv_toward_anyjob"]+=okall
        # toward shed?
        ds=r["dshed"]
        if ds[0]>0 and ((ux and ux*ds[1]>0) or (uy and uy*ds[2]>0)): S["mv_toward_shed"]+=1
    elif on0:
        S["work_here"]+=1
        if y!="PASS": S["op_when_work_here"]+=1
n=S["mv"]; print(P.split("/")[-1],dict(S))
print(" move rows %.1f%% of all; with work on current tile %.1f%%; toward nearest %.1f%%; toward any job %.1f%%; toward shed %.1f%%"%(
 100*n/(n+S["work_here"]+1),100*S["mv_with_work_here"]/n,100*S["mv_toward_nearest"]/(n-S["mv_nojob"]),100*S["mv_toward_anyjob"]/(n-S["mv_nojob"]),100*S["mv_toward_shed"]/n))
