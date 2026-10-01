"""Counterfactual replay: edit one seat's recorded market orders, replay both seats open-loop, report bank deltas.

Edits (per step, seat S):
  net:ITEM   net same-turn SELL/BUY_PRODUCT ITEM round trips (S sells, B buys -> one order |S-B| at the first
             ITEM slot; other ITEM slots become NOOP so later slot positions are unchanged)
  noop       replace NOOP placeholders by nothing (compacts slot positions)
usage: cfx.py OUT.jsonl TEAM EDIT[,EDIT] [GLOB]
"""
import glob, gzip, json, os, sys, copy
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT)
import kagsim
PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def net_item(m, item):
    S = sum(int(o[2]) for o in m if isinstance(o, list) and len(o) >= 3 and o[0] == "SELL" and o[1] == item)
    B = sum(int(o[2]) for o in m if isinstance(o, list) and len(o) >= 3 and o[0] == "BUY_PRODUCT" and o[1] == item)
    if S == 0 or B == 0: return m, 0
    out, first = [], True
    for o in m:
        if isinstance(o, list) and len(o) >= 3 and o[1] == item and o[0] in ("SELL", "BUY_PRODUCT"):
            if first and S != B: out.append(["SELL", item, S - B] if S > B else ["BUY_PRODUCT", item, B - S])
            else: out.append(["NOOP"])
            first = False
        else: out.append(o)
    return out, min(S, B)


def edit(acts, seat, edits):
    a2 = copy.deepcopy(acts); n = 0
    for t in range(1, len(a2)):
        a = a2[t][seat]
        if not isinstance(a, dict): continue
        m = list(a.get("market") or [])
        for e in edits:
            if e.startswith("net:"):
                m, k = net_item(m, e[4:]); n += k
            elif e == "noop":
                m = [o for o in m if not (isinstance(o, list) and o and o[0] == "NOOP")]
        a["market"] = m
    return a2, n


def replay(acts, seed):
    s0 = kagsim.Stream([a[0] if isinstance(a[0], dict) else PASS for a in acts[1:]])
    s1 = kagsim.Stream([a[1] if isinstance(a[1], dict) else PASS for a in acts[1:]])
    return kagsim.run_episode(s0, s1, seed=int(seed))


if __name__ == "__main__":
    out, team, edits = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
    g = sys.argv[4] if len(sys.argv) > 4 else "mine/top10/*.json.gz"
    with open(out, "a") as f:
        for p in sorted(glob.glob(g)):
            d = json.load(gzip.open(p, "rt"))
            if team not in d["teams"]: continue
            s = d["teams"].index(team)
            base = replay(d["actions"], d["seed"])
            ok = [abs(base[i] - d["rewards"][i]) < 0.5 for i in range(2)]
            a2, n = edit(d["actions"], s, edits)
            cf = replay(a2, d["seed"])
            r = dict(ep=d["episode_id"], team=team, opp=d["teams"][1 - s], edits=edits, units=n, ok=ok,
                     rec=[d["rewards"][s], d["rewards"][1 - s]], cf=[cf[s], cf[1 - s]],
                     d_self=cf[s] - base[s], d_opp=cf[1 - s] - base[1 - s],
                     d_margin=(cf[s] - cf[1 - s]) - (base[s] - base[1 - s]))
            f.write(json.dumps(r) + "\n"); f.flush()
            print(json.dumps({k: r[k] for k in ("ep", "opp", "units", "ok", "d_self", "d_opp", "d_margin")}, ensure_ascii=False))
