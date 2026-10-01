"""W1: record x's premium-sale stream as recovered by public WL (yummers) via its own _v92_p_update, on library seeds."""
import sys, json
sys.argv_saved = list(sys.argv); sys.argv = [sys.argv[0]]
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/run.py").read().split("if __name__")[0])
Y = "rivals4/kaggriculture-yummers/_entry.py"
def record(job):
    xn, xp, seed, xs = job
    a, ma = load(xp, "x"); b, mb = load(Y, "y")
    g = kagsim.Game(seed=int(seed)); pair = None
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        if t == 150: pair = tuple(o0["town"]["unlocked_shops"][:2])
        A, B = (a, b) if xs == 0 else (b, a)
        g.step(act(A, o0), act(B, o1))
    r = [float(g.reward(0)), float(g.reward(1))]
    ev = {"%d,%d" % k: v for k, v in mb._V92_P[1 - xs]["obs"].items()}
    return dict(x=xn, seed=int(seed), xs=xs, pair=pair, m=r[xs] - r[1 - xs], ev=ev)
if __name__ == "__main__":
    S = json.load(open("moe/r3/build/opus/w1_seeds.json"))
    jobs = []
    for k, s in enumerate(S["lib_seeds"]):
        for xn, xp in (("o2802", "rivals/jaxa623_2802/_entry.py"),):
            jobs.append((xn, xp, s, k % 2))
    pool(record, jobs, "moe/r3/build/opus/w1_streams_o.jsonl")
