"""Offline transfer check: best same-pair library stream vs each live WLV stream (MILK/WOOL/STRAWBERRY, qty>=2, +-1 tick).
Score = F1 of event match. Groups: R2 (shepR's appended), S (shepherd), O (2802), BASE (our shipped f9af library)."""
import json, sys, gzip, statistics as st
sys.argv = [sys.argv[0]]
exec(open("pairs.py").read().split('\nif __name__=="__main__":')[0])
from lib import read_src, decode, pair_index
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
wlv = json.load(open(ROOT + "/moe/r3/fable_scratch_r2/wlv_streams.json"))
seed_of = {}
for s in wlv:
    d = json.load(gzip.open(f"{ROOT}/mine/opp/{s['ep']}.json.gz", "rt")); seed_of[s["ep"]] = d["seed"]
def ev_rec(r): return {tuple(map(int, k.split(","))) for k, q in r["ev"].items() if int(k.split(",")[1]) <= 2 and q >= 2}
G = {"R2": [(r["pair"], ev_rec(r)) for r in map(json.loads, open("w1_mirror_streams.jsonl"))],
     "S": [(r["pair"], ev_rec(r)) for f in ("w1_streams.jsonl", "w1_streams_s2.jsonl") for r in map(json.loads, open(f)) if r.get("x", "shep") == "shep"],
     "O": [(r["pair"], ev_rec(r)) for r in map(json.loads, open("w1_streams_o.jsonl"))]}
base = decode(*read_src(ROOT + "/subW_shepherd.py")[1:])
def f1(a, b):
    if not a or not b: return 0.0
    ma = sum(1 for (t, i) in a if (t, i) in b or (t - 1, i) in b or (t + 1, i) in b)
    mb = sum(1 for (t, i) in b if (t, i) in a or (t - 1, i) in a or (t + 1, i) in a)
    p, r = mb / len(b), ma / len(a)
    return 2 * p * r / (p + r) if p + r else 0.0
res = {g: [] for g in ("R2", "S", "O", "BASE")}; npair = {g: [] for g in res}
for s in wlv:
    p = pair(seed_of[s["ep"]]); w = {(t, i) for t, i, q in s["ev"] if i <= 2}
    for g, L in G.items():
        c = [e for pp, e in L if tuple(pp) == p]; npair[g].append(len(c))
        res[g].append(max((f1(w, e) for e in c), default=0.0))
    c = [{k for k, q in e.items() if k[1] <= 2 and q >= 2} for e in base[pair_index(p)]]; npair["BASE"].append(len(c))
    res["BASE"].append(max((f1(w, e) for e in c), default=0.0))
for g in res:
    cov = sum(1 for n in npair[g] if n)
    v = [x for x, n in zip(res[g], npair[g]) if n]
    print(f"{g:5s} tapes with same-pair streams {cov}/18  best-stream F1 vs live WLV: mean {st.mean(v):.3f}  median {st.median(v):.3f}")
