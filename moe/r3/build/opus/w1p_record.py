"""cand_W1p library: fill the 37 shop pairs not yet covered with 12 R2 streams (shepherd-vs-R2, recovered by shepherd)
and 6 shepherd streams (shepherd self-play, recovered by the other seat). Seeds disjoint from every test/gate slice."""
import sys, json, random, gzip
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/w1_mirror.py").read().split('\nif __name__ == "__main__":')[0])
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/pairs.py").read().split('\nif __name__=="__main__":')[0])
from lib import NAMES
def selfrec(job):
    seed, _ = job
    a, ma = load(SH, "a"); b, mb = load(SH, "b")
    g = kagsim.Game(seed=int(seed)); pair = None
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        if t == 150: pair = tuple(o0["town"]["unlocked_shops"][:2])
        g.step(act(a, o0), act(b, o1))
    return dict(seed=int(seed), pair=pair, x="shep", ev={"%d,%d" % k: v for k, v in ma._V92_P[0]["obs"].items()})
if __name__ == "__main__":
    S = json.load(open(ROOT + "/moe/r3/build/opus/w1_seeds.json"))
    idx = [r["seed"] for r in json.load(open(ROOT + "/data/seedindex_900000_1400.json"))]
    rows = json.load(open(ROOT + "/moe/r3/fable_scratch/live_rows2.json"))
    taken = set(idx) | set(int(s) for s in S["test_pairs"]) | set(S["lib_seeds"])
    taken |= {json.loads(l)["seed"] for l in open(ROOT + "/moe/r3/build/opus/w1_streams_s2.jsonl")}
    have = {tuple(json.loads(l)["pair"]) for l in open(ROOT + "/moe/r3/build/opus/w1_mirror_streams.jsonl")}
    allp = [(a, b) for a in NAMES for b in NAMES]
    needR = {p: 12 for p in allp if p not in have}; needS = {p: 6 for p in allp if p not in have}
    rng = random.Random(20260927); rseeds, sseeds = [], []
    while any(needR.values()) or any(needS.values()):
        s = rng.randrange(10**8, 2 * 10**9)
        if s in taken: continue
        p = pair(s); taken.add(s)
        if needR.get(p, 0): needR[p] -= 1; rseeds.append(s)
        elif needS.get(p, 0): needS[p] -= 1; sseeds.append(s)
    print(len(needR), "pairs to fill;", len(rseeds), "R2 games,", len(sseeds), "self-play games", flush=True)
    pool(rec, [(s, k % 2) for k, s in enumerate(rseeds)], ROOT + "/moe/r3/build/opus/w1p_streams_r2.jsonl")
    pool(selfrec, [(s, 0) for s in sseeds], ROOT + "/moe/r3/build/opus/w1p_streams_shep.jsonl")
