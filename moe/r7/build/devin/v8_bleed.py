# v8 endgame-fade diagnostic: per-day bank/product breakdown on losing vs winning seeds.
import sys, os, json
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act
import kagsim

V8 = "subAC_v8.py"
OPP = "subW_shepherd.py"   # the reference opponent from the original trace

def run(seed):
    a, _ = load(V8, "a"); b, _ = load(OPP, "b")
    g = kagsim.Game(seed=seed)
    days = []
    for t in range(720):
        o0 = g.observe(0)
        if t % 24 == 0 and t > 0:
            days.append(snap(g, t))
        g.step(act(a, g.observe(0)), act(b, g.observe(1)))
    days.append(snap(g, 719))
    return days, g.reward(0), g.reward(1)

def snap(g, t):
    o = g.observe(0); me = o["farms"][0]
    an = [tl.get("animal") for r in me["tiles"] for tl in r if isinstance(tl, dict) and tl.get("animal")]
    cared = sum(1 for r in me["tiles"] for tl in r if isinstance(tl, dict) and tl.get("animal") and tl.get("cared_today"))
    fed = sum(1 for r in me["tiles"] for tl in r if isinstance(tl, dict) and tl.get("animal") and tl.get("fed_today"))
    held = {str(tl.get("animal")): int(tl.get("yield_units") or 0) for r in me["tiles"] for tl in r
            if isinstance(tl, dict) and tl.get("animal") and tl.get("yield_units")}
    crops = {}
    for r in me["tiles"]:
        for tl in r:
            if isinstance(tl, dict) and tl.get("kind") == "PLANT":
                crops[tl["crop"]] = crops.get(tl["crop"], 0) + 1
    shed = {k: v for k, v in o["private"]["shed"].items() if v}
    opp = g.observe(1)["farms"][1]
    return dict(day=o["day"], bank=me["money"], opp=opp["money"], animals={a: an.count(a) for a in set(an)},
                fed=fed, cared=cared, held=held, crops=crops, shed=shed, shops=list(o["town"]["unlocked_shops"]))

if __name__ == "__main__":
    for seed in (9100005, 9100008, 9100012, 9100001, 9100003):
        days, ra, rb = run(seed)
        tag = "LOSE" if ra < rb else "WIN "
        print(f"\n=== seed {seed} [{tag}] v8={ra:.0f} shep={rb:.0f} ===")
        for d in days:
            if d["day"] >= 15:
                print(f" d{d['day']:2d} bank={d['bank']:7.0f} opp={d['opp']:7.0f} an={d['animals']} fed={d['fed']} cared={d['cared']} held={d['held']} crops={d['crops']} shed={d['shed']}")
