"""Append recorded streams (w1_streams*.jsonl, x in XS) to a candidate's PREDICT library. usage: addlib.py IN.py OUT.py x[,x] [oracle]"""
import sys, json
sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus")
from lib import read_src, decode, encode, write_src, pair_index
src, blob, index = read_src(sys.argv[1]); lib = decode(blob, index); xs = sys.argv[3].split(",")
recs = [json.loads(l) for f in ("w1_streams.jsonl", "w1_streams_o.jsonl") for l in open(f)]
if len(sys.argv) > 4: recs += json.load(open("w1_oracle_streams.json"))
n = 0
for r in recs:
    if r["x"] in xs and r["pair"]:
        lib[pair_index(r["pair"])].append({tuple(map(int, k.split(","))): min(255, int(q)) for k, q in r["ev"].items()}); n += 1
b2, i2 = encode(lib); write_src(src, b2, i2, sys.argv[2]); print(sys.argv[2], "+", n, "streams, total", sum(map(len, lib)))
