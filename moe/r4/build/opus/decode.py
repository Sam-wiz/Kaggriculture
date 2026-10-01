"""MoE r4 Opus — decode top-rated episodes by exact engine replay.

For each reduced episode (mine/top10/<ep>.json.gz, or any file with seed/teams/rewards/actions) replay
both seats' recorded actions through the pinned Python engine with fill hooks (moe/opus/ledger_eps.py)
and emit one compact per-seat record:
  plan    land buys (step), hires per day, seeds/animals bought per day, herd + plants at each dawn
  market  per product: units sold, revenue, avg price, price/base, sells by phase; buy-backs; discards
  money   bank at each dawn (both seats), final
  sig     opening market signature (first 3 non-empty market lists), unit-op signature hash per day
Verifies replay == recorded rewards (field `match`).
usage: decode.py OUT.jsonl [GLOB] [WORKERS]   (skips episodes already in OUT)
"""
import glob, gzip, hashlib, json, os, sys
from concurrent.futures import ProcessPoolExecutor
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/opus")
import harness
import ledger_eps as L

BASE = dict(WHEAT=25, CARROT=35, TOMATO=60, STRAWBERRY=120, MELON=250, EGG=50, MILK=160, WOOL=200,
            FERTILIZER=100)
PREM = ("STRAWBERRY", "MELON", "MILK", "WOOL")
PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def uops(a):
    if not isinstance(a, dict): return []
    return [a.get("farmer")] + list(a.get("hands") or [])


def job(path):
    L._install_hooks()
    d = json.load(gzip.open(path, "rt"))
    acts, seed, rew = d["actions"], d["seed"], d["rewards"]

    def mk(seat):
        def ag(obs):
            t = obs["step"] + 1
            a = acts[t][seat] if t < len(acts) else None
            return a if isinstance(a, dict) else PASS
        return ag

    rec = dict(fills=[], prod=[], placed=[], discard=[], herd=[], shops=None)
    L.G["rec"] = rec
    money = [[], []]; prices = []; shopsday = []

    def on_step(step, state, env):
        ob = state[0].observation
        if (step + 1) % 24 == 0:
            h = []
            for f in ob.farms:
                c = {}
                for row_ in f["tiles"]:
                    for t in row_:
                        if isinstance(t, dict):
                            if "animal" in t: c[t["animal"]] = c.get(t["animal"], 0) + 1
                            elif t.get("kind") == "PLANT": c["P_" + t["crop"]] = c.get("P_" + t["crop"], 0) + 1
                            elif t.get("kind") == "WEED": c["weed"] = c.get("weed", 0) + 1
                c["quads"] = len(f.get("unlocked_quadrants") or [])
                h.append(c)
            rec["herd"].append(h)
            for i in range(2): money[i].append(ob.farms[i]["money"])
            shopsday.append(len(ob.town["unlocked_shops"]))
        prices.append({k: ob.market["prices"].get(k) for k in PREM})

    try:
        r = harness.run_episode(mk(0), mk(1), seed=seed, copy_obs=False, on_step=on_step)
    except Exception as e:
        L.G["rec"] = None
        return dict(ep=d["episode_id"], err=repr(e)[:200])
    L.G["rec"] = None
    rp = r["reward"]
    out = dict(ep=d["episode_id"], date=d.get("date"), seed=seed, teams=d["teams"], rewards=rew,
               replayed=rp, match=[abs(a - b) < 0.5 for a, b in zip(rp, rew)],
               shops=list(r["state"][0].observation.town["unlocked_shops"]), shops150=d.get("shops150"),
               seats=[])
    for s in range(2):
        f = [x for x in rec["fills"] if x[1] == s]
        land = [x[0] for x in f if x[2] == "BUY_LAND"]
        hires = {}
        for x in f:
            if x[2] == "HIRE": hires[x[0] // 24] = hires.get(x[0] // 24, 0) + 1
        seeds, animals, buyp = {}, {}, {}
        sell = {}
        for x in f:
            st, _, op, it, pr = x; dday = st // 24
            if op == "BUY_SEED": seeds.setdefault(it, {}); seeds[it][dday] = seeds[it].get(dday, 0) + 1
            elif op == "BUY_ANIMAL": animals.setdefault(it, {}); animals[it][dday] = animals[it].get(dday, 0) + 1
            elif op == "BUY_PRODUCT":
                b = buyp.setdefault(it, [0, 0]); b[0] += 1; b[1] += pr
            elif op == "SELL":
                q = sell.setdefault(it, dict(u=0, rev=0, ph=[0, 0, 0], rph=[0, 0, 0], steps=set()))
                q["u"] += 1; q["rev"] += pr; ph = 0 if dday < 13 else (1 if dday < 25 else 2)
                q["ph"][ph] += 1; q["rph"][ph] += pr; q["steps"].add(st)
        for it, q in sell.items():
            q["avg"] = round(q["rev"] / q["u"], 1); q["pi"] = round(q["rev"] / q["u"] / BASE.get(it, 1), 3)
            q["nsteps"] = len(q.pop("steps"))
        prod = {}
        for st, p, k, n in rec["prod"]:
            if p == s: prod[k] = prod.get(k, 0) + n
        disc = sum(n for st, p, n in rec["discard"] if p == s)
        # opening signature: first 3 non-empty market lists
        sig = []
        for t in range(1, len(acts)):
            a = acts[t][s]
            m = a.get("market") if isinstance(a, dict) else None
            if m: sig.append(m)
            if len(sig) >= 3: break
        # unit-op hash per day (for plan-determinism across games)
        dh = []
        for day in range(30):
            h = hashlib.md5(json.dumps([uops(acts[t][s]) for t in range(1 + day * 24, min(len(acts), 1 + (day + 1) * 24))]).encode()).hexdigest()[:8]
            dh.append(h)
        out["seats"].append(dict(team=d["teams"][s], bank=rew[s], land=land, hires=hires, seeds=seeds,
                                 animals=animals, buyp=buyp, sell=sell, prod=prod, discard=disc,
                                 herd=[h[s] for h in rec["herd"]], money=money[s], sig=sig, dayhash=dh,
                                 nsell_steps=len({x[0] for x in f if x[2] == "SELL"})))
    out["shopsday"] = shopsday
    # premium price path summary: mean price per product per day
    pp = {}
    for k in PREM:
        pp[k] = [round(sum(prices[t][k] or 0 for t in range(d0, min(d0 + 24, len(prices)))) / 24, 1)
                 for d0 in range(0, len(prices), 24)]
    out["premprice"] = pp
    return out


if __name__ == "__main__":
    out = sys.argv[1]; g = sys.argv[2] if len(sys.argv) > 2 else "mine/top10/*.json.gz"
    W = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: done.add(json.loads(line)["ep"])
            except Exception: pass
    paths = [p for p in sorted(glob.glob(g)) if int(os.path.basename(p).split(".")[0].split("_")[-1]) not in done]
    print(len(paths), "to decode", flush=True)
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
        for i, res in enumerate(ex.map(job, paths, chunksize=1), 1):
            f.write(json.dumps(res) + "\n"); f.flush()
            if "err" in res or not all(res.get("match", [0])): print("BAD", res.get("ep"), res.get("err"), res.get("replayed"), res.get("rewards"), flush=True)
            if i % 25 == 0: print(i, "done", flush=True)
