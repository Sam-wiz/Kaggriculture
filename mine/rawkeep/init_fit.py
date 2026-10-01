# Conditional logit on INIT rows, VECTORIZED: pad candidate sets to max, mask absent.
import json, sys, numpy as np

PATH = sys.argv[1] if len(sys.argv)>1 else "mine/rawkeep/init_DSM.jsonl"
TYPES = ["water","harvest","feed","care","cfert","dig","plant","fert","struct_free","shed"]
rows = [json.loads(l) for l in open(PATH) if json.loads(l)["label"]]
print(len(rows), "INIT rows w/labels", flush=True)

def shared_feats(r):
    G=r["G"]; inv=r["inv"]
    goods = sum(inv.get(c,0) for c in ("WHEAT","CARROT","TOMATO","STRAWBERRY","MELON","MILK","WOOL","EGG"))
    anims = sum(inv.get(a,0) for a in ("COW","SHEEP","GOOSE"))
    return [G["day"]/30., G["hour"]/24., min(G["money"],60000)/60000., r["ui"]/12.,
            min(goods,10)/10., min(inv.get("FERTILIZER",0),6)/6., min(anims,4)/4.]

K=len(TYPES); NS=len(shared_feats(rows[0])); NF=6
def prep(rs):
    N=len(rs)
    M=np.zeros((N,K)); Tf=np.zeros((N,K,NF)); Sf=np.zeros((N,NS)); Y=np.full(N,-1)
    for i,r in enumerate(rs):
        for k,ty in enumerate(TYPES):
            t=r["types"].get(ty)
            if t and t.get("n",0)>0:
                M[i,k]=1
                d=t["d"]; d1=d[0] if d else 30; d2=d[1] if len(d)>1 else 30
                Tf[i,k]=[min(d1,24)/24.,min(d2,24)/24.,min(t["n"],20)/20.,min(t["urg"],8)/8.,min(t.get("urg2",0),8)/8.,min(t.get("urg_sum",0),40)/40.]
        Sf[i]=shared_feats(r)
        if r["label"] in TYPES: Y[i]=TYPES.index(r["label"])
    return M,Tf,Sf,Y

eps=sorted(set(r["ep"] for r in rows))
tre=set(eps[:-10]);tee=set(eps[-10:])
tr=[r for r in rows if r["ep"] in tre];te=[r for r in rows if r["ep"] in tee]
print(f"train {len(tr)} / test {len(te)}", flush=True)
M,Tf,Sf,Y = prep(tr); Mt,Tft,Sft,Yt = prep(te)

# baseline: nearest-first -> argmin min-dist over present
pred_nf = np.where(Mt>0, Tft[:,:,0], 99).argmin(1)
lab_ok = (Yt>=0) & (Mt[np.arange(len(Yt)), np.clip(Yt,0,K-1)]>0)
print(f"nearest-first: {100*np.mean(pred_nf[lab_ok]==Yt[lab_ok]):.1f}% (n={lab_ok.sum()})", flush=True)

# score_k = A_k + (B_k . shared) + (C . typefeats_k)
A=np.zeros(K); B=np.zeros((K,NS)); C=np.zeros(NF)
lr=0.5
N=len(Y)
for ep in range(300):
    S = A[None,:] + np.einsum('ns,ks->nk',Sf,B) + np.einsum('nkf,f->nk',Tf,C)
    S = np.where(M>0, S, -1e9)
    S -= S.max(1,keepdims=True); P=np.exp(S); P/=P.sum(1,keepdims=True)
    valid = Y>=0
    P[range(N),np.clip(Y,0,K-1)] -= valid.astype(float)
    P *= M
    gA = P.mean(0)
    gB = np.einsum('nk,ns->ks',P,Sf)/N
    gC = np.einsum('nk,nkf->f',P,Tf)/N
    A-=lr*gA; B-=lr*gB; C-=lr*gC
    if ep%60==59:
        St = A[None,:] + np.einsum('ns,ks->nk',Sft,B) + np.einsum('nkf,f->nk',Tft,C)
        St = np.where(Mt>0,St,-1e9); pred=St.argmax(1)
        print(f"  ep{ep}: held-out {100*np.mean(pred[lab_ok]==Yt[lab_ok]):.1f}%", flush=True)
St = A[None,:] + np.einsum('ns,ks->nk',Sft,B) + np.einsum('nkf,f->nk',Tft,C)
St = np.where(Mt>0,St,-1e9); pred=St.argmax(1)
print(f"\nFINAL held-out top-1: {100*np.mean(pred[lab_ok]==Yt[lab_ok]):.1f}%  (vs nearest-first ~{47}-{73}%)")
print("weights C (dist1,dist2,count,urg):", np.round(C,2))
print("type priors A:", {TYPES[k]:round(A[k],2) for k in range(K)})
