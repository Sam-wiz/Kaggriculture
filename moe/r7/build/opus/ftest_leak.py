# Leak audit of mine/rawkeep/ftest.py: prev_int = y2[t-1] is a hindsight label.
# Split rows into INIT (prev row was a work op / none) vs CONT (prev row was a move),
# and refit with CAUSAL history only (prev emitted op, last COMPLETED work op, gap, peers' last completed op).
import json, numpy as np
from collections import defaultdict
PATH="moe/r7/build/opus/bc2s_DSM.jsonl"
JKEYS=["water","harvest","feed","care","cfert","dig","empty","struct_free"]
MOVES={"NORTH","SOUTH","EAST","WEST"}
rows=[json.loads(l) for l in open(PATH)]
by=defaultdict(list)
for r in rows: by[(r["ep"],r["ui"])].append(r)
H={}
peer=defaultdict(lambda: defaultdict(int))
for (ep,ui),us in by.items():
    us.sort(key=lambda r:r["t"])
    lop="NONE"; lint="NONE"; ldone="NONE"; lw=-99; lt=-9
    for r in us:
        contig = (r["t"]==lt+1)
        H[id(r)]=dict(prev_op=lop if contig else "NONE", leak=lint if contig else "NONE",
                      done=ldone, gap=min(24,r["t"]-lw), cont=contig and lop in MOVES)
        peer[(ep,r["t"])][ldone]+=1
        if r["y"] not in MOVES and r["y"] not in ("PASS","ABSENT"): lw=r["t"]; ldone=r["y"]
        lop=r["y"]; lint=r["y2"] or "NONE"; lt=r["t"]
dec=[r for r in rows if r["y"] in MOVES and r["y2"] not in (None,"PASS","ABSENT") and r["y2"] not in MOVES]
labels=sorted(set(r["y2"] for r in dec)); li={c:i for i,c in enumerate(labels)}
cont=[H[id(r)]["cont"] for r in dec]
eq=[H[id(r)]["leak"]==r["y2"] for r in dec]
print(f"{len(dec)} rows; CONT share {np.mean(cont):.3f}; leak==label on CONT {np.mean([e for e,c in zip(eq,cont) if c]):.4f}, on INIT {np.mean([e for e,c in zip(eq,cont) if not c]):.4f}")
def fx(r,mode):
    v=[min(r["d"][k][0],24)/24 for k in JKEYS]+[min(r["G"]["cnts"].get(k,0),20)/20 for k in JKEYS]
    inv=r["inv"]; on=r["on"]
    v+=[r["G"]["day"]/30,r["G"]["hour"]/24,min(r["G"]["money"],6e4)/6e4,min(r["dshed"][0],24)/24,r["ui"]/12,
        min(inv["WHEAT"],10)/10,min(inv["FERTILIZER"],6)/6,min(inv["goods"],10)/10,min(inv["animals"],4)/4,
        float(bool(on.get("empty"))),float(bool(on.get("plant"))),float(bool(on.get("plant") and not on.get("watered"))),float(bool(on.get("animal")))]
    h=H[id(r)]
    if mode=="leak":
        v+=[float(h["prev_op"]==c) for c in labels]+[float(h["leak"]==c) for c in labels]+[h["gap"]/24]
    if mode=="causal":
        pops=sorted(MOVES)
        v+=[float(h["prev_op"]==c) for c in pops]+[float(h["done"]==c) for c in labels]+[h["gap"]/24,float(h["cont"])]
        pk=peer[(r["ep"],r["t"])]; v+=[min(pk.get(c,0),4)/4 for c in labels]
    return v
eps=sorted(set(r["ep"] for r in dec)); te_e=set(eps[-10:])
tr=[r for r in dec if r["ep"] not in te_e]; te=[r for r in dec if r["ep"] in te_e]
tc=np.array([H[id(r)]["cont"] for r in te])
def run(mode):
    X=np.array([fx(r,mode) for r in tr]);Y=np.array([li[r["y2"]] for r in tr])
    Xt=np.array([fx(r,mode) for r in te]);Yt=np.array([li[r["y2"]] for r in te])
    mu,sd=X.mean(0),X.std(0)+1e-6;X=np.c_[(X-mu)/sd,np.ones(len(X))];Xt=np.c_[(Xt-mu)/sd,np.ones(len(Xt))]
    W=np.zeros((X.shape[1],len(labels)))
    for _ in range(300):
        z=X@W;z-=z.max(1,keepdims=True);p=np.exp(z);p/=p.sum(1,keepdims=True);p[range(len(Y)),Y]-=1
        W-=0.5*(X.T@p/len(Y)+1e-4*W)
    ok=(Xt@W).argmax(1)==Yt
    print(f"{mode:7s} all {100*ok.mean():.1f}%  INIT {100*ok[~tc].mean():.1f}% (n={(~tc).sum()})  CONT {100*ok[tc].mean():.1f}% (n={tc.sum()})",flush=True)
for m in ("frame","leak","causal"): run(m)
