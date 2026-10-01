# Train BC dispatch policy (numpy MLP), evaluate held-out episode accuracy, export weights.
import json, sys, numpy as np
from collections import Counter

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
SRC = ROOT + "/mine/rawkeep/bc2_DSM.jsonl"
WOUT = ROOT + "/mine/rawkeep/bc_weights.npz"

MK = ["water","harvest","feed","care","cfert","dig","empty","struct_free"]

def feats(r):
    on = r["on"]; G = r["G"]; inv = r["inv"]; d = r["d"]; c = G["cnts"]
    x, y = r["xy"]
    return [
        x/9., y/9., G["day"]/29., G["hour"]/23., min(G["money"],50000)/50000.,
        G["hires"]/10., G["quads"],
        min(G["shed_wheat"],50)/50., min(G["shed_fert"],50)/50., min(G["shed_animals"],10)/10.,
        min(c["water"],40)/40., min(c["harvest"],40)/40., min(c["feed"],30)/30.,
        min(c["care"],30)/30., min(c["cfert"],30)/30., min(c["dig"],30)/30.,
        min(c["empty"],60)/60., min(c["struct_free"],30)/30.,
        min(d["water"][0],20)/20., min(d["harvest"][0],20)/20., min(d["feed"][0],20)/20.,
        min(d["care"][0],20)/20., min(d["cfert"][0],20)/20., min(d["dig"][0],20)/20.,
        min(d["empty"][0],20)/20., min(d["struct_free"][0],20)/20.,
        d["water"][1], d["water"][2], d["harvest"][1], d["harvest"][2],
        d["feed"][1], d["feed"][2], d["care"][1], d["care"][2],
        d["dig"][1], d["dig"][2], d["empty"][1], d["empty"][2],
        min(r["dshed"][0],20)/20., r["dshed"][1], r["dshed"][2],
        min(inv["WHEAT"],10)/10., min(inv["FERTILIZER"],10)/10., min(inv["goods"],10)/10., min(inv["animals"],10)/10.,
        1 if on.get("empty") else 0, 1 if on.get("weed") else 0,
        1 if on.get("plant") else 0, 1 if on.get("animal") else 0,
        1 if on.get("watered") else 0, min(on.get("yield") or 0,8)/8.,
        1 if on.get("fed") else 0, 1 if on.get("cared") else 0, 1 if on.get("fert_av") else 0,
        min(r["ui"],10)/10., (r["ui"]==0)*1.,
    ]

print("loading rows..."); rows = [json.loads(l) for l in open(SRC)]
eps = sorted(set(r["ep"] for r in rows))
test_eps = set(eps[-5:])
tr = [r for r in rows if r["ep"] not in test_eps]
te = [r for r in rows if r["ep"] in test_eps]
print(f"train {len(tr)}  test {len(te)}")

labels = sorted(set(r["y2"] for r in tr))
li = {c:i for i,c in enumerate(labels)}
print(len(labels), "classes:", Counter(r["y2"] for r in tr).most_common(14))

X = np.array([feats(r) for r in tr], dtype=np.float32)
Y = np.array([li[r["y2"]] for r in tr])
Xt = np.array([feats(r) for r in te], dtype=np.float32)
Yt = np.array([li.get(r["y2"],0) for r in te])

D, K = X.shape[1], len(labels)
H1, H2 = 128, 64
rng = np.random.default_rng(1)
W1 = rng.normal(0, np.sqrt(2/D), (D,H1)).astype(np.float32); b1 = np.zeros(H1, np.float32)
W2 = rng.normal(0, np.sqrt(2/H1), (H1,H2)).astype(np.float32); b2 = np.zeros(H2, np.float32)
W3 = np.zeros((H2,K), np.float32); b3 = np.zeros(K, np.float32)
params = [W1,b1,W2,b2,W3,b3]
ms = [np.zeros_like(p) for p in params]; vs = [np.zeros_like(p) for p in params]

def fwd(x):
    a1 = np.maximum(x@W1+b1, 0)
    a2 = np.maximum(a1@W2+b2, 0)
    return a1, a2, a2@W3+b3

BS, lr, EPOCHS = 8192, 1e-3, 30
n = len(X); it = 0
for ep in range(EPOCHS):
    perm = rng.permutation(n)
    for s in range(0, n-BS, BS):
        idx = perm[s:s+BS]; it += 1
        xb, yb = X[idx], Y[idx]
        a1, a2, z = fwd(xb)
        z -= z.max(1,keepdims=True); p = np.exp(z); p /= p.sum(1,keepdims=True)
        oh = np.zeros_like(p); oh[np.arange(BS), yb] = 1
        g = (p-oh)/BS
        gW3 = a2.T@g; gb3 = g.sum(0)
        da2 = g@W3.T; da2[a2<=0] = 0
        gW2 = a1.T@da2; gb2 = da2.sum(0)
        da1 = da2@W2.T; da1[a1<=0] = 0
        gW1 = xb.T@da1; gb1 = da1.sum(0)
        grads = [gW1,gb1,gW2,gb2,gW3,gb3]
        for i,(pr,gr) in enumerate(zip(params,grads)):
            ms[i] = .9*ms[i]+.1*gr; vs[i] = .999*vs[i]+.001*gr*gr
            pr -= lr*ms[i]/(np.sqrt(vs[i])+1e-8)
    # eval
    _,_,zt = fwd(Xt)
    acc = (zt.argmax(1)==Yt).mean()
    print(f"epoch {ep}: held-out acc {acc:.3f}")

_,_,zt = fwd(Xt)
pred = zt.argmax(1)
acc = (pred==Yt).mean()
top3 = np.argsort(-zt,axis=1)[:,:3]
acc3 = (top3==Yt[:,None]).any(1).mean()
print(f"\nFINAL held-out: acc {acc:.3f} top3 {acc3:.3f} (majority {np.bincount(Yt).max()/len(Yt):.3f})")
for c in ["WATER","HARVEST","FEED","CARE","DIG","COLLECT_FERTILIZER","PASS","PICKUP:WHEAT","DROP","PLANT:WHEAT","BUILD_PASTURE","BUILD_COOP","PLACE:COW","PLACE:SHEEP","MOVE_IDLE"]:
    if c not in li: continue
    m = Yt==li[c]
    if m.sum(): print(f"  {c:20s} n={int(m.sum()):5d} acc={float((pred==Yt)[m].mean()):.3f}")

np.savez(WOUT, W1=W1,b1=b1,W2=W2,b2=b2,W3=W3,b3=b3,
         labels=np.array(labels), mu=np.zeros(D), sd=np.ones(D))
print("saved", WOUT)
