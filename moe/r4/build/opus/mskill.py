"""Market-skill decode (exact replay, Python engine + fill hooks). Per seat, per product p:
  u, rev           exact filled sell units and revenue
  hold, holdp      holding exposure: sum over steps of shed_p(after step) and shed_p * price_p (after step)
                   -> passive = holdp/hold (mean price of the goods while they sat in the shed)
  captured         = rev/u ; timing = captured/passive (>1 = sells into highs)
  steps, coll      sell-steps; sell-steps where the rival also got SELL fills of p that step
  first            collisions where our first SELL p order sat in an earlier slot than the rival's
usage: mskill.py OUT.jsonl GLOB [LIMIT]
"""
import glob, gzip, json, os, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/opus")
import harness, ledger_eps as L
PASS = {"farmer": ["PASS"], "hands": [], "market": []}
PROD = ("MILK", "WOOL", "STRAWBERRY", "MELON", "EGG", "TOMATO", "CARROT", "WHEAT", "FERTILIZER")


def slot_of(m, p):
    for i, o in enumerate(m or []):
        if isinstance(o, list) and len(o) >= 3 and o[0] == "SELL" and o[1] == p: return i
    return None


def one(p):
    L._install_hooks()
    d = json.load(gzip.open(p, "rt")); A = d["actions"]
    rec = dict(fills=[], prod=[], placed=[], discard=[], herd=[], shops=None); L.G["rec"] = rec
    hold = [{q: [0, 0] for q in PROD} for _ in range(2)]

    def mk(seat):
        def ag(obs):
            t = obs["step"] + 1
            a = A[t][seat] if t < len(A) else None
            return a if isinstance(a, dict) else PASS
        return ag

    def on_step(step, state, env):
        pr = state[0].observation.market["prices"]
        for i in range(2):
            sh = state[i].observation.private["shed"]
            for q in PROD:
                h = sh.get(q, 0)
                if h > 0: hold[i][q][0] += h; hold[i][q][1] += h * pr[q]
    r = harness.run_episode(mk(0), mk(1), seed=d["seed"], copy_obs=False, on_step=on_step)
    L.G["rec"] = None
    acc = [{q: dict(u=0, rev=0, steps=0, coll=0, first=0, hold=hold[i][q][0], holdp=hold[i][q][1]) for q in PROD} for i in range(2)]
    by = {}
    for st, pl, op, it, pr in rec["fills"]:
        if op == "SELL" and it in PROD:
            acc[pl][it]["u"] += 1; acc[pl][it]["rev"] += pr
            by.setdefault((st, it), set()).add(pl)
    for (st, it), pls in by.items():
        for pl in pls:
            acc[pl][it]["steps"] += 1
            if len(pls) == 2:
                acc[pl][it]["coll"] += 1
                a, b = slot_of((A[st + 1][pl] or {}).get("market"), it), slot_of((A[st + 1][1 - pl] or {}).get("market"), it)
                if a is not None and b is not None and a < b: acc[pl][it]["first"] += 1
    return dict(ep=d["episode_id"], teams=d["teams"], rewards=d["rewards"], replayed=r["reward"], acc=acc)


if __name__ == "__main__":
    out, gpat = sys.argv[1], sys.argv[2]; LIM = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    done = set()
    if os.path.exists(out):
        for l in open(out):
            try: done.add(json.loads(l)["ep"])
            except Exception: pass
    ps = [p for p in sorted(glob.glob(gpat)) if int(os.path.basename(p).split(".")[0].split("_")[-1]) not in done]
    if LIM: ps = ps[:LIM]
    with open(out, "a") as f:
        for p in ps:
            try: r = one(p)
            except Exception as e: r = dict(ep=p, err=repr(e)[:100])
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
