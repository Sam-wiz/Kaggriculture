"""W1 closed-loop test: shepherd (seat `us`) vs {yummers, WL+S, WL+R} on the 14 WLV seeds (recorded seat)
+ 20 fresh seeds x both seats. Telemetry: WL's PREDICT fires/units, and how many forecasts picked an appended stream."""
import sys, json
sys.argv_saved = list(sys.argv); sys.argv = [sys.argv[0]]
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/run.py").read().split("if __name__")[0])
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from lib import read_src, decode
BASE_N = [len(b) for b in decode(*read_src(ROOT + "/rivals4/kaggriculture-yummers/_entry.py")[1:])]
def w1game(job):
    xn, xp, on, op, seed, us = job
    a, ma = load(xp, "x"); b, mb = load(op, "o")
    picks = {"calls": 0, "app": 0}
    orig = mb._v92_p_forecast
    def fc(obs, st):
        best = orig(obs, st); picks["calls"] += 1
        shops = tuple(obs["town"]["unlocked_shops"][:2]); lst = mb._v92_p_pair(shops)
        k = ["BAKERY", "BRUNCH_SPOT", "FARMERS_MARKET", "ICE_CREAM_SHOP", "PET_CAFE", "PIZZA_SHOP", "SMOOTHIE_SHOP", "YARN_STORE"]
        if best and len(shops) == 2 and shops[0] in k and shops[1] in k:
            pi = k.index(shops[0]) * 8 + k.index(shops[1])
            for ev in best:
                for j, e in enumerate(lst):
                    if e[1] is ev:
                        if j >= BASE_N[pi]: picks["app"] += 1
                        break
        return best
    mb._v92_p_forecast = fc
    g = kagsim.Game(seed=int(seed))
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        A, B = (a, b) if us == 0 else (b, a)
        g.step(act(A, o0), act(B, o1))
    r = [float(g.reward(0)), float(g.reward(1))]
    return dict(x=xn, o=on, seed=int(seed), us=us, m=r[us] - r[1 - us], r=r, tx=tele(ma), to=tele(mb), picks=picks)
if __name__ == "__main__":
    S = json.load(open(ROOT + "/moe/r3/build/opus/w1_seeds.json"))
    OPP = [("yummers", "rivals4/kaggriculture-yummers/_entry.py"), ("WL+S", "moe/r3/build/opus/wl_S.py"), ("WL+R", "moe/r3/build/opus/wl_R.py"),
           ("WL+O", "moe/r3/build/opus/wl_O.py")]
    if len(sys.argv_saved) > 1: OPP = [o for o in OPP if o[0] in sys.argv_saved[1:]]
    jobs = []
    for on, op in OPP:
        for g in S["wlv"]: jobs.append(("shep", "subW_shepherd.py", on, op, g["seed"], g["seat"]))
        for s in S["fresh"]:
            for us in (0, 1): jobs.append(("shep", "subW_shepherd.py", on, op, s, us))
    out = ROOT + "/moe/r3/build/opus/w1_test.jsonl"
    pool(w1game, jobs, out)
