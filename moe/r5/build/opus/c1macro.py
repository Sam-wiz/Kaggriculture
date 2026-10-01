"""r5 opus turn 3: C1's own macro in the same schema as macro.py (family decode), so options.json can state
each option as a delta vs the executor.  C1 vs C1 self-play, fresh seeds, official Python engine + ledger hooks.
usage: c1macro.py N [WORKERS]   -> c1macro.jsonl (one line per seed, seat 0 and seat 1)
"""
import json, os, sys
from concurrent.futures import ProcessPoolExecutor
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT)
for p in (ROOT, ROOT + "/moe/opus", ROOT + "/moe/r5/build/opus"):
    if p not in sys.path: sys.path.insert(0, p)
import harness
import ledger_eps as L
from macro import tmap
C1 = ROOT + "/subY_C1_predict2.py"


def dawn_rec(obs, seat):
    f = obs["farms"][seat]; day = obs["day"]
    herd, plants = {}, {}; empty = weeds = 0
    for row in f["tiles"]:
        for t in row:
            if t is None: empty += 1
            elif isinstance(t, dict):
                k = t.get("kind")
                if k == "WEED": weeds += 1
                elif k == "PLANT": plants[t["crop"]] = plants.get(t["crop"], 0) + 1
                elif t.get("animal"): herd[t["animal"]] = herd.get(t["animal"], 0) + 1
    return dict(day=day, money=f["money"], quads=len(f.get("unlocked_quadrants") or []),
                shops=list(obs["town"]["unlocked_shops"]), herd=herd, plants=plants, empty=empty, weeds=weeds,
                map=tmap(f["tiles"]))


def job(seed):
    import uuid
    L._install_hooks()
    base = [harness.load_agent(C1, "c1a_" + uuid.uuid4().hex), harness.load_agent(C1, "c1b_" + uuid.uuid4().hex)]
    dawn = [[], []]

    def mk(seat):
        def ag(obs):
            if obs["hour"] == 0: dawn[seat].append(dawn_rec(obs, seat))
            return base[seat](obs)
        return ag
    rec = dict(fills=[], prod=[], placed=[], discard=[], herd=[], shops=None)
    L.G["rec"] = rec
    r = harness.run_episode(mk(0), mk(1), seed=seed, copy_obs=True, catch_errors=False)
    L.G["rec"] = None
    out = dict(seed=seed, rewards=r["reward"], shops=list(r["state"][0].observation.town["unlocked_shops"]), seats=[])
    for s in range(2):
        dec = [dict(seed={}, animal={}, land=0, land_step=[], hire=0, sell={}) for _ in range(30)]
        for st, p, op, it, pr in rec["fills"]:
            if p != s: continue
            x = dec[min(st // 24, 29)]
            if op == "BUY_SEED": x["seed"][it] = x["seed"].get(it, 0) + 1
            elif op == "BUY_ANIMAL": x["animal"][it] = x["animal"].get(it, 0) + 1
            elif op == "BUY_LAND": x["land"] += 1; x["land_step"].append(st)
            elif op == "HIRE": x["hire"] += 1
            elif op == "SELL":
                q = x["sell"].setdefault(it, [0, 0]); q[0] += 1; q[1] += pr
        prod = [dict() for _ in range(30)]
        for st, p, k, n in rec["prod"]:
            if p == s: prod[min(st // 24, 29)][k] = prod[min(st // 24, 29)].get(k, 0) + n
        out["seats"].append(dict(bank=r["reward"][s], dawn=dawn[s], dec=dec, prod=prod))
    return out


if __name__ == "__main__":
    N = int(sys.argv[1]); W = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    seeds = [9530001 + i for i in range(N)]
    with ProcessPoolExecutor(W, max_tasks_per_child=1) as ex, open(ROOT + "/moe/r5/build/opus/c1macro.jsonl", "w") as fo:
        for res in ex.map(job, seeds):
            fo.write(json.dumps(res, separators=(",", ":")) + "\n"); fo.flush()
            s0 = res["seats"][0]
            print(res["seed"], [round(x) for x in res["rewards"]], "quads d12", s0["dawn"][12]["quads"], "herd d12",
                  s0["dawn"][12]["herd"], "land", [st for d in s0["dec"] for st in d["land_step"]], flush=True)
