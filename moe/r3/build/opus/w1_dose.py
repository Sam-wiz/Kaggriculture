"""W1 dose-response: 6 more shepherd streams per test pair (new library seeds) -> WL+S2 (12/pair); test on WLV14 + fresh40."""
import sys, json, random
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/w1_record.py").read().split('\nif __name__ == "__main__":')[0])
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/w1_test.py").read().split('\nif __name__ == "__main__":')[0])
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/pairs.py").read().split('\nif __name__=="__main__":')[0])
from lib import read_src, decode, encode, write_src, pair_index
if __name__ == "__main__":
    S = json.load(open(ROOT + "/moe/r3/build/opus/w1_seeds.json"))
    need = {tuple(p): 0 for p in S["test_pairs"].values()}; taken = set(int(s) for s in S["test_pairs"]) | set(S["lib_seeds"])
    rng = random.Random(20260926); lib2 = []
    while any(v < 6 for v in need.values()):
        s = rng.randrange(10**8, 2 * 10**9)
        if s in taken: continue
        p = pair(s)
        if p in need and need[p] < 6: need[p] += 1; lib2.append(s); taken.add(s)
    jobs = [("shep", "subW_shepherd.py", s, k % 2) for k, s in enumerate(lib2)]
    out = ROOT + "/moe/r3/build/opus/w1_streams_s2.jsonl"; open(out, "w").close(); pool(record, jobs, out)
    src, blob, index = read_src(ROOT + "/moe/r3/build/opus/wl_S.py"); L = decode(blob, index); n = 0
    for l in open(out):
        r = json.loads(l)
        if r["pair"]: L[pair_index(r["pair"])].append({tuple(map(int, k.split(","))): min(255, int(q)) for k, q in r["ev"].items()}); n += 1
    b2, i2 = encode(L); write_src(src, b2, i2, ROOT + "/moe/r3/build/opus/wl_S2.py"); print("WL+S2 +", n, flush=True)
    tj = [("shep", "subW_shepherd.py", "WL+S2", "moe/r3/build/opus/wl_S2.py", g["seed"], g["seat"]) for g in S["wlv"]]
    tj += [("shep", "subW_shepherd.py", "WL+S2", "moe/r3/build/opus/wl_S2.py", s, us) for s in S["fresh"] for us in (0, 1)]
    pool(w1game, tj, ROOT + "/moe/r3/build/opus/w1_test.jsonl")
