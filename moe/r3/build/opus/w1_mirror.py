"""W1 mirror (C1-prime direction check): arm SHEPHERD with 12/pair streams of the WLV proxy R2 (recovered by shepherd's
own _v92_p_update in shepherd-vs-R2 games on the W1 library seeds), then shepR vs R2S / R2 on WLV14 + fresh40."""
import sys, json
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/run.py").read().split('\nif __name__ == "__main__":')[0])
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from lib import read_src, decode, encode, write_src, pair_index, NAMES
R2 = "moe/r3/build/opus/R2.py"; SH = "subW_shepherd.py"; SHR = "moe/r3/build/opus/shepR.py"
BASE_N = [len(b) for b in decode(*read_src(ROOT + "/" + SH)[1:])]
def rec(job):
    seed, rs = job                      # rs = R2's seat
    a, ma = load(SH, "s"); b, mb = load(R2, "r")
    g = kagsim.Game(seed=int(seed)); pair = None
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        if t == 150: pair = tuple(o0["town"]["unlocked_shops"][:2])
        A, B = (b, a) if rs == 0 else (a, b)
        g.step(act(A, o0), act(B, o1))
    return dict(seed=int(seed), rs=rs, pair=pair, ev={"%d,%d" % k: v for k, v in ma._V92_P[1 - rs]["obs"].items()})
def mgame(job):
    xn, xp, on, op, seed, us = job
    a, ma = load(xp, "x"); b, mb = load(op, "o"); picks = {"calls": 0, "app": 0}
    orig = ma._v92_p_forecast
    def fc(obs, st):
        best = orig(obs, st); picks["calls"] += 1
        shops = tuple(obs["town"]["unlocked_shops"][:2])
        if best and len(shops) == 2 and shops[0] in NAMES and shops[1] in NAMES:
            lst = ma._v92_p_pair(shops); pi = NAMES.index(shops[0]) * 8 + NAMES.index(shops[1])
            for ev in best:
                for j, e in enumerate(lst):
                    if e[1] is ev:
                        picks["app"] += j >= BASE_N[pi]; break
        return best
    ma._v92_p_forecast = fc
    g = kagsim.Game(seed=int(seed))
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        A, B = (a, b) if us == 0 else (b, a)
        g.step(act(A, o0), act(B, o1))
    r = [float(g.reward(0)), float(g.reward(1))]
    return dict(x=xn, o=on, seed=int(seed), us=us, m=r[us] - r[1 - us], tx=tele(ma), to=tele(mb), picks=picks)
if __name__ == "__main__":
    S = json.load(open(ROOT + "/moe/r3/build/opus/w1_seeds.json"))
    seeds = S["lib_seeds"] + [json.loads(l)["seed"] for l in open(ROOT + "/moe/r3/build/opus/w1_streams_s2.jsonl")]
    out = ROOT + "/moe/r3/build/opus/w1_mirror_streams.jsonl"; open(out, "w").close()
    pool(rec, [(s, k % 2) for k, s in enumerate(seeds)], out)
    src, blob, index = read_src(ROOT + "/" + SH); L = decode(blob, index); n = 0
    for l in open(out):
        r = json.loads(l)
        if r["pair"]: L[pair_index(r["pair"])].append({tuple(map(int, k.split(","))): min(255, int(q)) for k, q in r["ev"].items()}); n += 1
    b2, i2 = encode(L); write_src(src, b2, i2, ROOT + "/" + SHR); print("shepR +", n, "streams", flush=True)
    jobs = []
    for xn, xp in (("shepR", SHR), ("shep", SH)):
        for on, op in (("R2S", "moe/r3/build/opus/R2S.py"), ("R2", R2)):
            for g in S["wlv"]: jobs.append((xn, xp, on, op, g["seed"], g["seat"]))
            if xn == "shepR":
                for s in S["fresh"]:
                    for us in (0, 1): jobs.append((xn, xp, on, op, s, us))
    out2 = ROOT + "/moe/r3/build/opus/w1_mirror.jsonl"; open(out2, "w").close(); pool(mgame, jobs, out2)
