# Learnability check: is DSM's per-unit dispatch predictable from state features?
import json, sys
import numpy as np
from collections import Counter, defaultdict

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
SRC = ROOT + "/mine/rawkeep/bc_DSM.jsonl"

# collapse classes: moves -> DIR, rest -> kind[:arg]
def norm_label(y):
    return y

def feats(r):
    on = r["on"]; nb = r["nb"]; G = r["G"]; inv = r["inv"]
    x, y = r["xy"]
    return [
        x, y, G["day"], G["hour"], G["money"]/1000., G["hires"], G["quads"],
        G["shed_wheat"], G["shed_fert"], G["shed_goods"], G["shed_animals"],
        G["n_dry"], G["n_ripe"], G["n_hungry"], G["n_weed"], G["n_empty"],
        G["n_crop"], G["n_anim"], G["n_fertav"],
        inv["WHEAT"], inv["FERTILIZER"], inv["goods"], inv["animals"],
        on.get("empty",0), on.get("weed",0), on.get("plant",0), on.get("animal",0), on.get("struct",0),
        on.get("watered",0), on.get("yield",0), on.get("dry",0), on.get("fed",0), on.get("cared",0),
        on.get("unfed",0), on.get("age",0), on.get("crop_i",-1)+1, on.get("an_i",-1)+1, on.get("fert_av",0),
        nb["dry"], nb["ripe"], nb["hungry"], nb["empty"], nb["weed"], nb["anim"], nb["fertav"],
    ]

rows = [json.loads(l) for l in open(SRC)]
eps = sorted(set(r["ep"] for r in rows))
test_eps = set(eps[-5:])  # hold out last 5 episodes
tr = [r for r in rows if r["ep"] not in test_eps]
te = [r for r in rows if r["ep"] in test_eps]
print(f"train {len(tr)}  test {len(te)}")

labels = sorted(set(r["y"] for r in tr))
li = {c:i for i,c in enumerate(labels)}
print(f"{len(labels)} classes:", Counter(r["y"] for r in tr).most_common(12))

X = np.array([feats(r) for r in tr], dtype=np.float32)
Y = np.array([li[r["y"]] for r in te and tr or tr])  # careful
Y = np.array([li[r["y"]] for r in tr])
Xt = np.array([feats(r) for r in te], dtype=np.float32)
Yt = np.array([li.get(r["y"],0) for r in te])

mu, sd = X.mean(0), X.std(0)+1e-6
X = (X-mu)/sd; Xt = (Xt-mu)/sd
# softmax regression, adam
D, K = X.shape[1], len(labels)
W = np.zeros((D,K), dtype=np.float32); b = np.zeros(K, dtype=np.float32)
mw=np.zeros_like(W); vw=np.zeros_like(W); mb=np.zeros_like(b); vb=np.zeros_like(b)
rng = np.random.default_rng(0)
BS = 8192; lr = 3e-3
for i in range(1, 4001):
    idx = rng.integers(0, len(X), BS)
    xb, yb = X[idx], Y[idx]
    z = xb@W+b; z -= z.max(1,keepdims=True); p = np.exp(z); p/=p.sum(1,keepdims=True)
    oh = np.zeros_like(p); oh[np.arange(BS), yb]=1
    g = (p-oh)/BS
    gW, gb = xb.T@g, g.sum(0)
    mw=.9*mw+.1*gW; vw=.999*vw+.001*gW*gW; mb=.9*mb+.1*gb; vb=.999*vb+.001*gb*gb
    W -= lr*mw/(np.sqrt(vw)+1e-8); b -= lr*mb/(np.sqrt(vb)+1e-8)

pred = Xt@W+b
acc = (pred.argmax(1)==Yt).mean()
print(f"\nheld-out episode accuracy: {acc:.3f}  (prior majority = {np.bincount(Yt).max()/len(Yt):.3f})")
# top-3 accuracy
top3 = np.argsort(-pred,axis=1)[:,:3]
acc3 = (top3==Yt[:,None]).any(1).mean()
print(f"top-3 accuracy: {acc3:.3f}")
# per-class accuracy for work ops
for c in ["WATER","HARVEST","FEED","CARE","DIG","NORTH","SOUTH","EAST","WEST","PASS","PICKUP:WHEAT","DROP","PLANT:WHEAT"]:
    if c not in li: continue
    m = Yt==li[c]
    if m.sum(): print(f"  {c:16s} n={m.sum():5d} acc={ (pred.argmax(1)==Yt)[m].mean():.3f }")
