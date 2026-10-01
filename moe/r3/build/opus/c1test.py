"""C1 (and C2 if present) closed-loop vs the best WLV reproductions (R2S = cand_R, WL+S2) on the 14 WLV seeds at the
recorded seat, with Fable's _V92_EP parity holdout set to each game's episode id (the game's own WLV stream excluded)."""
import sys, json, os
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/run.py").read().split('\nif __name__ == "__main__":')[0])
def cgame(job):
    xn, xp, on, op, seed, us, ep = job
    a, ma = load(xp, "x"); b, mb = load(op, "o")
    if ep is not None: ma._V92_EP = int(ep)
    g = kagsim.Game(seed=int(seed))
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        A, B = (a, b) if us == 0 else (b, a)
        g.step(act(A, o0), act(B, o1))
    r = [float(g.reward(0)), float(g.reward(1))]
    return dict(x=xn, o=on, seed=int(seed), us=us, ep=ep, m=r[us] - r[1 - us], tx=tele(ma), to=tele(mb))
if __name__ == "__main__":
    S = json.load(open(ROOT + "/moe/r3/build/opus/w1_seeds.json"))
    # Fable's session exited before building; cand_C*_rebuilt.py = Fable's mkcand.py recipe (mkc1.py), built here.
    X = [("C1", "moe/r3/build/opus/cand_C1_rebuilt.py"), ("C2", "moe/r3/build/opus/cand_C2_rebuilt.py")]
    jobs = [(xn, xp, on, op, g["seed"], g["seat"], g["ep"]) for xn, xp in X
            for on, op in (("R2S", "moe/r3/build/opus/R2S.py"), ("WL+S2", "moe/r3/build/opus/wl_S2.py")) for g in S["wlv"]]
    idx = [r["seed"] for r in json.load(open(ROOT + "/data/seedindex_900000_1400.json"))][1380:1404]
    jobs += [("C1", X[0][1], on, op, s, us, None) for on, op in (("shep", "subW_shepherd.py"), ("hyb2965", "subX_hyb2965.py"),
             ("shepR", "moe/r3/build/opus/shepR.py")) for s in idx for us in (0, 1)]
    print(len(jobs), "games", [x[0] for x in X], flush=True)
    out = ROOT + "/moe/r3/build/opus/c1test.jsonl"; open(out, "w").close(); pool(cgame, jobs, out)
