# Causal rows + causal weights: does the MLP carry information beyond on-tile-first + nearest-job rules?
# Scores held-out 5 eps; splits by whether MLP and hand rule agree, and who is right when they disagree.
import json,sys,numpy as np
from collections import Counter,defaultdict
sys.argv=[sys.argv[0]]; ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
exec(open(ROOT+"/mine/rawkeep/bc_train2.py").read().split("print(\"loading rows")[0])
src=open(ROOT+"/moe/r7/build/opus/bc_dispatch_audit.py").read()
exec(src[src.index("MOVES="):src.index("grp=defaultdict")])
rows=[json.loads(l) for l in open(ROOT+"/moe/r7/build/opus/bc2s_DSM.jsonl")]
eps=sorted(set(r["ep"] for r in rows)); te=[r for r in rows if r["ep"] in set(eps[-5:])]
w=np.load(ROOT+"/moe/r7/build/opus/bc_weights_shift.npz"); L=list(w["labels"])
X=np.array([feats(r) for r in te],np.float32)
a=np.maximum(X@w["W1"]+w["b1"],0); a=np.maximum(a@w["W2"]+w["b2"],0); z=a@w["W3"]+w["b3"]
P=[L[i] for i in z.argmax(1)]
def rule(r):
    if r["y"] in MOVES: return nearest_rule(r)
    return ontile_rule(r) or nearest_rule(r)
g=defaultdict(Counter); dis=Counter()
for r,p in zip(te,P):
    k="move" if r["y"] in MOVES else ("pass" if r["y"]=="PASS" else "work")
    q=rule(r); y=r["y2"]
    g[k]["n"]+=1; g[k]["mlp"]+=p==y; g[k]["rule"]+=q==y; g[k]["agree"]+=p==q
    if p!=q:
        g[k]["dis_mlp_right"]+=p==y; g[k]["dis_rule_right"]+=q==y; g[k]["dis_n"]+=1
        if p==y: dis[(k,y,q)]+=1
for k,c in g.items():
    n=c["n"]; print(k,n,"mlp",round(c["mlp"]/n,3),"rule",round(c["rule"]/n,3),"agree",round(c["agree"]/n,3),
      "| disagree n",c["dis_n"],"mlp right",c["dis_mlp_right"],"rule right",c["dis_rule_right"])
print("top MLP-right-rule-wrong (group,true,rule_said):",dis.most_common(12))
# urgency proxy: when several job kinds are in reach, does DSM pick the NEAREST kind? and does MLP?
