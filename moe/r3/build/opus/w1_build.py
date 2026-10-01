"""W1: WL+S = public yummers + shepherd streams; WL+R = yummers + the same count of hyb2965 streams
(both recorded vs yummers on the same library seeds, disjoint from all test seeds)."""
import json, sys
sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus")
from lib import read_src, decode, encode, write_src, pair_index
Y = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/rivals4/kaggriculture-yummers/_entry.py"
import os
recs = [json.loads(l) for f in ("w1_streams.jsonl", "w1_streams_o.jsonl") if os.path.exists(f) for l in open(f)]
S = json.load(open("w1_seeds.json")); test = set(int(s) for s in S["test_pairs"])
src, blob, index = read_src(Y); base = decode(blob, index)
for x, out in (("shep", "wl_S.py"), ("hyb", "wl_R.py"), ("o2802", "wl_O.py")):
    if not any(r["x"] == x for r in recs): continue
    lib = [list(b) for b in base]; n = 0
    for r in recs:
        if r["x"] != x or r["seed"] in test or not r["pair"]: continue
        ev = {}
        for k, q in r["ev"].items():
            t, i = map(int, k.split(",")); ev[(t, i)] = min(255, int(q))
        lib[pair_index(r["pair"])].append(ev); n += 1
    b2, i2 = encode(lib); assert decode(b2, i2) == lib
    write_src(src, b2, i2, out)
    print(out, "added", n, "streams; total", sum(len(b) for b in lib))
