"""Opponent profile of the C1 chassis (lineage class): C1 vs C1 self-play, shadow deltas recover seat 1's per-step
net market effect. Used only to BOUND the value of opponent-class identification in TS (the test opponent is C1).
usage: c1prof.py OUT.json NGAMES SEED0
"""
import copy, io, contextlib, json, os, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r5/build/opusb")
os.chdir(ROOT)
import harness as H
import ts

out, n, s0 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
acc = [dict() for _ in range(720)]
for g in range(n):
    with contextlib.redirect_stdout(io.StringIO()):
        a = H.load_agent(ROOT + "/subY_C1_predict2.py", "pa%d" % g); b = H.load_agent(ROOT + "/subY_C1_predict2.py", "pb%d" % g)
    st = {"prev": None, "act": None}

    def wa(o):
        if st["prev"] is not None:
            for k, v in ts.shadow_delta(st["prev"], st["act"], o).items():
                acc[st["prev"]["step"]][k] = acc[st["prev"]["step"]].get(k, 0) + v
        r = a(o); st["prev"] = copy.deepcopy(o); st["act"] = copy.deepcopy(r)
        return r
    with contextlib.redirect_stdout(io.StringIO()):
        H.run_episode(wa, b, seed=s0 + g, copy_obs=True)
mean = [{k: v / n for k, v in d.items()} for d in acc]
tot = {}
for d in mean:
    for k, v in d.items():
        tot[k] = tot.get(k, 0) + v
json.dump(dict(n=n, mean=mean), open(out, "w"))
print("C1 seat season net", {k: round(v) for k, v in tot.items()})
