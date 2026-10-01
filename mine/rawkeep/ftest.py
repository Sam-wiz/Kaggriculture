# F-test (opus): can a MEMORYLESS scorer predict job-type on travel decisions?
#   survive: frame-only acc >=85% held-out AND +history adds <5pp
#   die:     history adds >5pp (hidden ledger real)
import json, sys, numpy as np
from collections import defaultdict

PATH = "moe/r7/build/opus/bc2s_DSM.jsonl"
JKEYS = ["water","harvest","feed","care","cfert","dig","empty","struct_free"]
MOVES = {"NORTH","SOUTH","EAST","WEST"}

rows = [json.loads(l) for l in open(PATH)]
# index rows by (ep, ui) sorted by t to get history
by_unit = defaultdict(list)
for r in rows: by_unit[(r["ep"], r["ui"])].append(r)
for k in by_unit: by_unit[k].sort(key=lambda r: r["t"])
rowidx = {id(r): i for i, r in enumerate(rows)}

# history features per row: prev emitted class, prev intent, turns since last work
prev_op = {}; prev_int = {}; gap = {}
claims = defaultdict(lambda: defaultdict(int))  # (ep,t) -> {intent: count of other units' prev intent}
per_key = defaultdict(list)
for (ep, ui), us in by_unit.items():
    last_op = "NONE"; last_int = "NONE"; last_work_t = -99
    for r in us:
        prev_op[id(r)] = last_op; prev_int[id(r)] = last_int
        gap[id(r)] = min(24, r["t"] - last_work_t)
        claims[(ep, r["t"])][last_int] += 1
        if r["y"] not in MOVES and r["y"] not in ("PASS","ABSENT"):
            last_work_t = r["t"]
        last_op = r["y"]; last_int = r["y2"] if r["y2"] else "NONE"

# travel decisions: emitted move AND a real work intent
dec = [r for r in rows if r["y"] in MOVES and r["y2"] not in (None,"PASS","ABSENT") and r["y2"] not in MOVES]
labels = sorted(set(r["y2"] for r in dec))
li = {c:i for i,c in enumerate(labels)}
print(f"{len(dec)} travel-decision rows, {len(labels)} job classes")

def fx(r, hist):
    v = [min(r["d"][k][0],24)/24.0 for k in JKEYS]
    v += [min(r["G"]["cnts"].get(k,0),20)/20.0 for k in JKEYS]
    inv = r["inv"]
    v += [r["G"]["day"]/30.0, r["G"]["hour"]/24.0, min(r["G"]["money"],60000)/60000.0,
          min(r["dshed"][0],24)/24.0, r["ui"]/12.0,
          min(inv.get("WHEAT",0),10)/10.0, min(inv.get("FERTILIZER",0),6)/6.0,
          min(inv.get("goods",0),10)/10.0, min(inv.get("animals",0),4)/4.0]
    on = r["on"]
    v += [1.0 if on.get("empty") else 0.0, 1.0 if on.get("crop") else 0.0,
          1.0 if (on.get("crop") and not on.get("watered_today")) else 0.0,
          1.0 if on.get("animal") else 0.0]
    if hist:
        # unit history: prev emitted class, prev intent, gap; claims per job class by peers' prev intent
        v += [1.0 if prev_op[id(r)]==c else 0.0 for c in labels]
        v += [1.0 if prev_int[id(r)]==c else 0.0 for c in labels]
        v += [gap[id(r)]/24.0]
        ck = claims[(r["ep"], r["t"])]
        # claim pressure per candidate class c: peers' prev intent equals c
        v += [min(ck.get(c,0),4)/4.0 for c in labels]
    return v

# split by episode
eps = sorted(set(r["ep"] for r in dec))
tr_eps = set(eps[:-10]); te_eps = set(eps[-10:])
tr = [r for r in dec if r["ep"] in tr_eps]; te = [r for r in dec if r["ep"] in te_eps]

def fit_eval(hist):
    X = np.array([fx(r, hist) for r in tr]); Y = np.array([li[r["y2"]] for r in tr])
    Xt = np.array([fx(r, hist) for r in te]); Yt = np.array([li[r["y2"]] for r in te])
    mu, sd = X.mean(0), X.std(0)+1e-6
    X = (X-mu)/sd; Xt = (Xt-mu)/sd
    X = np.c_[X, np.ones(len(X))]; Xt = np.c_[Xt, np.ones(len(Xt))]
    K = len(labels); W = np.zeros((X.shape[1], K))
    for ep_i in range(300):
        z = X@W; z -= z.max(1, keepdims=True)
        p = np.exp(z); p /= p.sum(1, keepdims=True)
        p[range(len(Y)), Y] -= 1
        g = X.T@p/len(Y) + 1e-4*W
        W -= 0.5*g
        if ep_i in (0, 50, 150, 299):
            acc = (Xt@W).argmax(1)
            print(f"  ep{ep_i}: held-out top-1 {100*np.mean(acc==Yt):.1f}%")
    acc = (Xt@W).argmax(1)
    return np.mean(acc==Yt)

print("\n== memoryless (frame only) =="); a0 = fit_eval(False)
print("\n== +history (prev op/intent, gap, peer claims) =="); a1 = fit_eval(True)
print(f"\nFRAME {100*a0:.1f}%  +HIST {100*a1:.1f}%  delta {100*(a1-a0):+.1f}pp")
print("F survives" if (a0>=0.85 and a1-a0<0.05) else "F DIES" if a1-a0>0.05 else "F weak/mixed")
