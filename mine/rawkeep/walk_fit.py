# Walker fitter: multinomial logit over {N,S,E,W,TILE_OP,PASS}.
# Move-row direction gate (opus): acc >= max(nearest-dir, momentum) + 10pp.
import json, sys, numpy as np
from collections import defaultdict

PATH=sys.argv[1] if len(sys.argv)>1 else "mine/rawkeep/walkrows_DSM.jsonl"
rows=[json.loads(l) for l in open(PATH)]
eps=sorted(set(r["ep"] for r in rows)); tre=set(eps[:-10]); tee=set(eps[-10:])
tr=[r for r in rows if r["ep"] in tre]; te=[r for r in rows if r["ep"] in tee]
print(f"{len(rows)} rows | train {len(tr)} test {len(te)}",flush=True)

def prep(rs):
    N=len(rs); FD=np.zeros((N,4,3)); G=np.zeros((N,7)); Y=np.zeros(N,dtype=int)
    PV=np.zeros(N,dtype=int); MV=np.zeros(N,dtype=bool)
    for i,r in enumerate(rs):
        for d in range(4):
            m,nj,u=r["f"][d]; FD[i,d]=[min(m,24)/24.,min(nj,30)/30.,min(u,8)/8.]
        G[i]=[r["g"][0]/30.,r["g"][1]/24.,min(r["g"][2],16)/16.,
              min(r["g"][3],10)/10.,min(r["g"][4],6)/6.,r["g"][5],min(r["g"][6],200)/200.]
        Y[i]=r["y"]; PV[i]=r["pv"] if r["pv"]>=0 else 5
        MV[i]=r["y"]<=3
    return FD,G,Y,PV,MV

FD,G,Y,PV,MV=prep(tr); FDt,Gt,Yt,PVt,MVt=prep(te)

# baselines on move rows
pv_mv=PVt[MVt]; yt_mv=Yt[MVt]
print("move-row share:",f"{100*MVt.mean():.1f}%")
print(f"momentum baseline (repeat prev move): {100*np.mean(pv_mv==yt_mv):.1f}%")
nd=np.argmin(np.where(FDt[:, :, 0]>0, FDt[:,:,0], 99),axis=1)   # dir of nearest job
print(f"nearest-job-direction baseline: {100*np.mean(nd[MVt]==yt_mv):.1f}%")
# set-valued + NWES-priority tiebreak baselines (opus/astra correction)
sethit=[r["y"] in r["best"] for r in te if r["y"]<=3]
NWES=[0,3,2,1]  # N>W>E>S fixed priority guess
priohit=[r["y"]==next((d for d in NWES if d in r["best"]),r["y"]) for r in te if r["y"]<=3]
print(f"any-shortest-dir agreement (set): {100*np.mean(sethit):.1f}%")
print(f"NWES-priority argmax:             {100*np.mean(priohit):.1f}%")

C=6
B=np.zeros(C); MOM=np.zeros(C); WD=np.zeros(3); GC=np.zeros((C,7))
lr=0.5; N=len(Y)
onepv=np.zeros((N,C)); onepv[np.arange(N),PV]=1
onepvt=np.zeros((len(te),C)); onepvt[np.arange(len(te)),PVt]=1
for ep in range(300):
    Sdir=np.einsum('ndf,f->nd',FD,WD)                 # N x 4 directional scores
    S=np.zeros((N,C)); S[:,:4]=Sdir
    S+=B+MOM*onepv+G@GC.T
    S-=S.max(1,keepdims=True); P=np.exp(S);P/=P.sum(1,keepdims=True)
    P[np.arange(N),Y]-=1
    B-=lr*P.mean(0); MOM-=lr*(P*onepv).mean(0)
    WD-=lr*np.einsum('nd,ndf->f',P[:,:4],FD)/N*4
    GC-=lr*np.einsum('nc,nf->cf',P,G)/N
    if ep%60==59:
        Sdir=np.einsum('ndf,f->nd',FDt,WD)
        St=np.zeros((len(te),C));St[:,:4]=Sdir;St+=B+MOM*onepvt+Gt@GC.T
        pr=St.argmax(1)
        print(f"  ep{ep}: all {100*np.mean(pr==Yt):.1f}% | move-row dir {100*np.mean(pr[MVt]==Yt[MVt]):.1f}%",flush=True)
print(f"\nFINAL all-turn {100*np.mean(pr==Yt):.1f}%  move-row {100*np.mean(pr[MVt]==Yt[MVt]):.1f}%")
print("gate: >=",f"{max(53.7,100*np.mean(pv_mv==yt_mv))+10:.1f}%")
print("dir bias B[N,S,E,W]:",np.round(B[:4],2),"| work:",round(B[4],2),"pass:",round(B[5],2))
print("dir feat W[mind,njobs,urg]:",np.round(WD,2))
print("momentum per class:",np.round(MOM,2))
EOF_MARKER=None
