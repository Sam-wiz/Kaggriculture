"""Find C1's 8 >=2000 live games (claude-code 06:55 table) in mine/opp by team+margin; print opp step-1 market."""
import gzip, json, os, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
WANT = {"Clement Lau": -98, "Fanch": -381, "kazuhiro3381": -338, "tamref": -2216, "Juste Me": 4733,
        "我的AI是豆包": 2423, "hinemos": 4977, "SatoGo": -448}
files = sorted(os.listdir("mine/opp"), key=lambda f: -os.path.getmtime("mine/opp/" + f))[:400]
out = []
for f in files:
    d = json.load(gzip.open("mine/opp/" + f, "rt"))
    t = d["teams"]
    if "Sam-wiz" not in t: continue
    me = t.index("Sam-wiz"); op = 1 - me
    if t[op] not in WANT or d["rewards"][me] is None: continue
    m = d["rewards"][me] - d["rewards"][op]
    if abs(m - WANT[t[op]]) > 1: continue
    a1 = d["actions"][1][op]
    out.append(dict(ep=d["episode_id"], opp=t[op], seat=me, m=m, seed=d["seed"], path="mine/opp/" + f,
                    open=a1.get("market") if isinstance(a1, dict) else a1))
for o in out: print(o["ep"], o["opp"], "our_seat", o["seat"], "m", o["m"], "open", o["open"])
json.dump(out, open("moe/r4/build/opus/c1opp.json", "w"), ensure_ascii=False)
print(len(out), "found")
