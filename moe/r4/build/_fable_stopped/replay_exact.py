"""Exact open-loop replay of reduced episodes in kagsim. Verifies final banks against the recording and
records per-day money, per-day sale revenue (money delta from SELL fills), min cash, shops.
usage: replay_exact.py OUT.jsonl FILE [FILE ...]
Convention (BRIEF): actions[t] PRODUCED step t; the reply to obs t is actions[t+1].
"""
import sys, os, json, gzip
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0, ROOT)
sys.path.insert(0, ROOT + "/kaggriculture-cppsim")
import kagsim
PASS = {"farmer": ["PASS"], "hands": [], "market": []}

def A(acts, t, seat):
    a = acts[t + 1][seat] if t + 1 < len(acts) else None
    return a if isinstance(a, dict) else PASS

def replay(d, trace=True):
    acts = d["actions"]; g = kagsim.Game(seed=int(d["seed"]))
    money = [[], []]; minc = [1e9, 1e9]; shops_at = {}
    for t in range(720):
        o0 = g.observe(0)
        if trace:
            for s in (0, 1):
                m = o0["farms"][s]["money"]; minc[s] = min(minc[s], m)
                if t % 24 == 0: money[s].append(m)
            if t % 24 == 0: shops_at[t // 24] = list(o0["town"]["unlocked_shops"])
        g.step(A(acts, t, 0), A(acts, t, 1))
    r = [float(g.reward(0)), float(g.reward(1))]
    return dict(ep=d.get("episode_id"), seed=d["seed"], teams=d["teams"], rec=d["rewards"], sim=r,
                exact=[abs(r[s] - float(d["rewards"][s])) < 0.5 for s in (0, 1)],
                money_by_day=money, min_cash=minc, shops_final=shops_at.get(29))

if __name__ == "__main__":
    out = sys.argv[1]
    with open(out, "a") as f:
        for p in sys.argv[2:]:
            d = json.load(gzip.open(p, "rt"))
            r = replay(d)
            f.write(json.dumps(r) + "\n"); f.flush()
            print(r["ep"], r["teams"], "rec", r["rec"], "sim", r["sim"], "exact", r["exact"], "min_cash", [round(x) for x in r["min_cash"]])
            for s in (0, 1):
                print("   ", r["teams"][s][:18].ljust(18), " ".join("%5d" % (m / 1000) for m in r["money_by_day"][s]))
