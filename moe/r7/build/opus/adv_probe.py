# Where does the INIT 61% miss live? Confusion + cargo-gating + fit with cargo/hour interactions.
import json, numpy as np
from collections import Counter
P="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/mine/rawkeep/init_DSM.jsonl"
T=["water","harvest","feed","care","cfert","dig","plant","fert","struct_free","shed"]; K=len(T)
rows=[r for r in map(json.loads,open(P)) if r["label"] in T]
GOODS=("WHEAT","CARROT","TOMATO","STRAWBERRY","MELON","MILK","WOOL","EGG","EGGS")
print("N",len(rows),"labels",Counter(r["label"] for r in rows).most_common())
f=[r for r in rows if r["label"]=="feed"]; print("feed w/ WHEAT carried %.1f%%"%(100*np.mean([r["inv"].get("WHEAT",0)>0 for r in f])))
s=[r for r in rows if r["label"]=="shed"]; print("shed w/ empty inv %.1f%%, w/ goods %.1f%%"%(100*np.mean([sum(r["inv"].values())==0 for r in s]),100*np.mean([any(r["inv"].get(g,0) for g in GOODS if g!="WHEAT") for r in s])))
fd=[r for r in rows if r["types"]["feed"]["n"]>0 and r["inv"].get("WHEAT",0)==0]
print("feed-present & no wheat: label", Counter(r["label"] for r in fd).most_common(4))
def feats(r,cargo):
    inv=r["inv"]; wh=inv.get("WHEAT",0)>0; fe=inv.get("FERTILIZER",0)>0
    gd=any(inv.get(g,0) for g in GOODS if g!="WHEAT"); an=any(inv.get(a,0) for a in("COW","SHEEP","GOOSE"))
    h=r["G"]["hour"]/24.; M=np.zeros(K); X=np.zeros((K,9))
    for k,ty in enumerate(T):
        t=r["types"][ty]
        if t["n"]<=0: continue
        M[k]=1; d=t["d"]; d1=d[0] if d else 30; d2=d[1] if len(d)>1 else 30
        g= {"feed":wh,"fert":fe,"shed":(gd or an or not wh)}.get(ty,1.0) if cargo else 0
        X[k]=[min(d1,24)/24,min(d2,24)/24,min(t["n"],20)/20,min(t["urg"],8)/8,float(g),float(g)*min(d1,24)/24,h*min(t["urg"],8)/8,h,float(gd and ty=="shed")]
    return M,X
def run(cargo):
    eps=sorted({r["ep"] for r in rows}); te=set(eps[-10:])
    def prep(rs):
        M=np.zeros((len(rs),K)); X=np.zeros((len(rs),K,9)); Y=np.array([T.index(r["label"]) for r in rs])
        for i,r in enumerate(rs): M[i],X[i]=feats(r,cargo)
        ok=M[np.arange(len(Y)),Y]>0; return M[ok],X[ok],Y[ok]
    M,X,Y=prep([r for r in rows if r["ep"] not in te]); Mt,Xt,Yt=prep([r for r in rows if r["ep"] in te])
    A=np.zeros(K); C=np.zeros(9); H=np.zeros(K); N=len(Y)
    for it in range(400):
        S=A+X@C+H*X[:,:,7]; S=np.where(M>0,S,-1e9); S-=S.max(1,keepdims=True); p=np.exp(S); p/=p.sum(1,keepdims=True)
        p[np.arange(N),Y]-=1; p*=M
        A-=0.5*p.mean(0); C-=0.5*np.einsum('nk,nkf->f',p,X)/N; H-=0.5*(p*X[:,:,7]).mean(0)
    St=np.where(Mt>0,A+Xt@C+H*Xt[:,:,7],-1e9); pr=St.argmax(1)
    print(f"cargo={cargo}: held-out {100*np.mean(pr==Yt):.1f}% n={len(Yt)}")
    cm=Counter((T[a],T[b]) for a,b in zip(Yt,pr) if a!=b); print("  top confusions (true,pred):",cm.most_common(6))
    print("  err share by true label:",{k:round(v/max(1,(pr!=Yt).sum()),2) for k,v in Counter(T[a] for a,b in zip(Yt,pr) if a!=b).most_common(5)})
run(False); run(True)
