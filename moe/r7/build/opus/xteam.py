# Cross-team transfer: DSM-trained causal net scored on causal rows from other top teams (<=6 eps each).
# Answers: shared dispatch style (pooled net ok) vs team-specific (router needed)?
import gzip,json,glob,sys,numpy as np
from collections import defaultdict
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
ex=open(ROOT+"/moe/r7/build/opus/bc_extract2_shift.py").read().split('if __name__')[0]
TEAMS=["mtmr_s1","Vadim Vasilenko","SpaTaro","THIRD FARM CLUB"]
rows=defaultdict(list); neps=defaultdict(int)
import tempfile,os
for f in sorted(glob.glob(ROOT+"/mine/rawkeep/*.json.gz")):
    if all(neps[t]>=6 for t in TEAMS): break
    try: x=json.load(gzip.open(f,"rt"))
    except Exception: continue
    tn=x["info"]["TeamNames"]
    for T in TEAMS:
        if T in tn and neps[T]<6:
            tmp=ROOT+f"/moe/r7/build/opus/_xt_{T.replace(' ','_')}.jsonl"
            g={"__name__":"x"}; exec(ex,g); g["TEAM"]=T; g["OUT"]=tmp
            if neps[T]==0 and os.path.exists(tmp): os.remove(tmp)
            if g["extract"](x): neps[T]+=1
sys.argv=[sys.argv[0]]
exec(open(ROOT+"/mine/rawkeep/bc_train2.py").read().split("print(\"loading rows")[0])
src=open(ROOT+"/moe/r7/build/opus/bc_dispatch_audit.py").read()
exec(src[src.index("MOVES="):src.index("grp=defaultdict")])
w=np.load(ROOT+"/moe/r7/build/opus/bc_weights_shift.npz"); L=list(w["labels"])
def score(name,te):
    X=np.array([feats(r) for r in te],np.float32)
    a=np.maximum(X@w["W1"]+w["b1"],0); a=np.maximum(a@w["W2"]+w["b2"],0); z=a@w["W3"]+w["b3"]
    P=[L[i] for i in z.argmax(1)]; g=defaultdict(lambda:[0,0,0])
    for r,p in zip(te,P):
        k="move" if r["y"] in MOVES else ("pass" if r["y"]=="PASS" else "work")
        q=nearest_rule(r) if k=="move" else (ontile_rule(r) or nearest_rule(r))
        g[k][0]+=1; g[k][1]+=p==r["y2"]; g[k][2]+=q==r["y2"]
    print(name,{k:(v[0],"mlp",round(v[1]/v[0],3),"rule",round(v[2]/v[0],3)) for k,v in g.items()},flush=True)
d=[json.loads(l) for l in open(ROOT+"/moe/r7/build/opus/bc2s_DSM.jsonl")]
eps=sorted(set(r["ep"] for r in d)); score("DSM-heldout(5ep)",[r for r in d if r["ep"] in set(eps[-5:])]); del d
for T in TEAMS:
    tmp=ROOT+f"/moe/r7/build/opus/_xt_{T.replace(' ','_')}.jsonl"
    if os.path.exists(tmp): score(f"{T}({neps[T]}ep)",[json.loads(l) for l in open(tmp)])
