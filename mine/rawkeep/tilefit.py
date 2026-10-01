# Conditional logit v2 over candidate TILES with cargo masks.
# score(c) = A[ty] + b_d[ty]*d + W . [d,urg,yld,val,dl,wbon,risk]
# Feasibility mask (opus): feed needs inv WHEAT; fert needs FERTILIZER;
# struct_free needs a carried animal; plant needs seeds>0.
# Eval: strict (ty+xy), tile-any (xy only), class-level; stratified by slack<0.
import json, sys, numpy as np

PATH = sys.argv[1] if len(sys.argv)>1 else "mine/rawkeep/tilerows_DSM.jsonl"
TYPES = ["water","harvest","feed","care","cfert","dig","plant","build","fert","struct_free","shed"]
TI = {t:i for i,t in enumerate(TYPES)}; K=len(TYPES); F=11
rows=[]
for l in open(PATH):
    r=json.loads(l)
    if "label" in r: rows.append(r)
print(len(rows),"rows w/labels",flush=True)

NC=max(len(r["cands"]) for r in rows)
eps=sorted(set(r["ep"] for r in rows)); tre=set(eps[:-10]); tee=set(eps[-10:])
tr=[r for r in rows if r["ep"] in tre]; te=[r for r in rows if r["ep"] in tee]
print(f"train {len(tr)} test {len(te)} maxcands {NC}",flush=True)

# static per-unit home: mean of TRAIN label positions per unit index
from collections import defaultdict
acc=defaultdict(list)
for r in tr:
    if r.get("label"): acc[r["ui"]].append(r["label"]["xy"])
ZH={u:(sum(p[0] for p in v)/len(v), sum(p[1] for p in v)/len(v)) for u,v in acc.items()}
print("unit homes:",{u:tuple(round(c,1) for c in z) for u,z in sorted(ZH.items())})

def feasible(r, c):
    ty=c["ty"]
    if ty=="feed": return r["inv"].get("WHEAT",0)>0
    if ty=="fert": return r["inv"].get("FERTILIZER",0)>0
    if ty=="struct_free": return r["inv"].get("COW",0)+r["inv"].get("SHEEP",0)+r["inv"].get("GOOSE",0)>0
    if ty=="plant": return r.get("seeds_tot",0)>0
    return True

def prep(rs):
    N=len(rs)
    M=np.zeros((N,NC)); X=np.zeros((N,NC,F)); TY=np.zeros((N,NC),dtype=int)
    XY=np.zeros((N,NC,2),dtype=int)
    Y=np.full(N,-1); Yxy=np.full((N,2),-1); Sl=np.zeros(N); UI=np.zeros(N,dtype=int)
    for i,r in enumerate(rs):
        Sl[i]=r["G"].get("slack",0); UI[i]=r["ui"]
        for j,c in enumerate(r["cands"]):
            if not feasible(r,c): continue
            M[i,j]=1; TY[i,j]=TI[c["ty"]]; XY[i,j]=[c["x"],c["y"]]
            d=min(c["d"],24); dl=min(c["dl"],48)
            zd=c.get("zd",-1)
            zh=ZH.get(r["ui"])
            zd2=((c["x"]-zh[0])**2+(c["y"]-zh[1])**2)**.5 if zh else -1
            X[i,j]=[d/24.,min(c["urg"],8)/8.,min(c["yld"],10)/10.,
                    min(c["val"],400)/400.,dl/48.,min(c.get("wbon",0),300)/300.,
                    np.clip((d-dl)/24.,-1,1),
                    1.0 if zd>=0 else 0.0, max(zd,0)/14.,
                    1.0 if zh else 0.0, max(zd2,0)/14.]
        ty,txy=r["label"]["ty"],r["label"]["xy"]; Yxy[i]=txy
        for j,c in enumerate(r["cands"]):
            if c["ty"]==ty and [c["x"],c["y"]]==txy: Y[i]=j;break
    return M,X,TY,XY,Y,Yxy,Sl,UI

M,X,TY,XY,Y,Yxy,Sl,UI=prep(tr); Mt,Xt,TYt,XYt,Yt,Yxyt,Slt,UIt=prep(te)
oktr = (Y>=0) & (M[np.arange(len(Y)),np.clip(Y,0,NC-1)]>0)
okte = (Yt>=0) & (Mt[np.arange(len(Yt)),np.clip(Yt,0,NC-1)]>0)
miss = np.sum(Yt<0)
print(f"usable: train {oktr.sum()} test {okte.sum()}  label-not-offered(test) {miss}",flush=True)

# nearest-tile baseline
pred_nf=np.where(Mt>0,Xt[:,:,0],99).argmin(1)
print(f"nearest-tile: strict {100*np.mean(pred_nf[okte]==Yt[okte]):.1f}%")

A=np.zeros(K); BD=np.zeros(K); W=np.zeros(F)
lr=0.3; N=len(Y)
for ep in range(250):
    S = A[TY] + BD[TY]*X[:,:,0] + np.einsum('ncf,f->nc',X,W)
    S = np.where(M>0,S,-1e9); S-=S.max(1,keepdims=True)
    P=np.exp(S);P/=P.sum(1,keepdims=True)
    Yv=np.clip(Y,0,NC-1); P[np.arange(N),Yv]-=(Y>=0)
    P*=M
    P*=oktr[:,None]  # astra fix: rows with absent/masked labels contribute no gradient
    gA=np.zeros(K);gBD=np.zeros(K)
    np.add.at(gA,TY.ravel(),P.ravel())
    np.add.at(gBD,TY.ravel(),(P*X[:,:,0]).ravel())
    gW=np.einsum('nc,ncf->f',P,X)
    A-=lr*gA/N*10;BD-=lr*gBD/N*10;W-=lr*gW/N*10
    if ep%50==49:
        St=A[TYt]+BD[TYt]*Xt[:,:,0]+np.einsum('ncf,f->nc',Xt,W)
        St=np.where(Mt>0,St,-1e9);pred=St.argmax(1)
        print(f"  ep{ep}: strict {100*np.mean(pred[okte]==Yt[okte]):.1f}%",flush=True)

St=A[TYt]+BD[TYt]*Xt[:,:,0]+np.einsum('ncf,f->nc',Xt,W)
St=np.where(Mt>0,St,-1e9);pred=St.argmax(1)
pxy=XYt[np.arange(len(te)),pred]           # predicted tile coords
tile_any = okte & (pxy==Yxyt).all(1)         # right tile, any type
lab_ty=np.array([TI[te[i]["label"]["ty"]] for i in range(len(te))])
pred_ty=TYt[np.arange(len(te)),pred]
# type-marginal: sum softmax mass per type, argmax type (fair vs coarse model)
P2=np.exp(St-St.max(1,keepdims=True)); P2=np.where(Mt>0,P2,0); P2/=P2.sum(1,keepdims=True)
Pm=np.zeros((len(te),K))
for k in range(K): Pm[:,k]=(P2*(TYt==k)).sum(1)
marg_ty=Pm.argmax(1)
print(f"type-marginal class: {100*np.mean(marg_ty[okte]==lab_ty[okte]):.1f}%")
# zone-masked argmax: restrict candidates to radius R of unit's static home
zh_arr=np.array([ZH.get(u,(-99,-99)) for u in UIt])
dhome=np.sqrt(((XYt-zh_arr[:,None,:])**2).sum(2))   # N x NC dist to unit home
for R in (3,4,5):
    Sm=np.where((Mt>0)&(dhome<=R),St,-1e9); pm=Sm.argmax(1)
    print(f"zone-mask R<={R}: strict {100*np.mean(pm[okte]==Yt[okte]):.1f}%  "
          f"tile-any {100*np.mean((okte)&((XYt[np.arange(len(te)),pm]==Yxyt).all(1))):.1f}%")
neg=Slt<0
print(f"\nFINAL strict(ty+xy): {100*np.mean(pred[okte]==Yt[okte]):.1f}%")
print(f"tile-any-type:       {100*np.mean(tile_any[okte]):.1f}%")
print(f"class-level:         {100*np.mean(pred_ty[okte]==lab_ty[okte]):.1f}%")
if neg.sum()>10:
    okn=okte&neg; okp=okte&~neg
    print(f"slack<0  ({okn.sum()} rows): strict {100*np.mean(pred[okn]==Yt[okn]):.1f}%")
    print(f"slack>=0 ({okp.sum()} rows): strict {100*np.mean(pred[okp]==Yt[okp]):.1f}%")
print("W[d,urg,yld,val,dl,wbon,risk]:",np.round(W,2))
print("BD:",{TYPES[k]:round(BD[k],2) for k in range(K)})
