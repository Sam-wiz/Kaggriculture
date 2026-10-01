"""Engine-gap decomposition: self-play of a build on a dump seed in the Python engine with the recorded shop
sequence pinned (monkeypatched _end_of_day) and fill hooks; emits the same per-seat record as decode.py so the
top pair (dec_top10.jsonl) and our pair can be compared product by product in the same world.
usage: engdec.py OUT.jsonl NAME=PATH WORKERS LIMIT [GLOB]
"""
import glob, gzip, json, os, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/opus"); sys.path.insert(0, ROOT + "/moe/r4/build/opus")
import harness, ledger_eps as L
K = harness.K
PIN = {"shops": None}


def _install_pin():
    if getattr(K, "_opus_pin", False): return
    orig = K._end_of_day

    def eod(state, env, day):
        orig(state, env, day)
        f = PIN["shops"]
        if f is not None:
            town = state[0].observation.town
            n = len(town["unlocked_shops"])
            town["unlocked_shops"][:] = list(f[:n])
    K._end_of_day = eod; K._opus_pin = True


BASE = dict(WHEAT=25, CARROT=35, TOMATO=60, STRAWBERRY=120, MELON=250, EGG=50, MILK=160, WOOL=200, FERTILIZER=100)


def job(arg):
    name, path, p = arg
    L._install_hooks(); _install_pin()
    d = json.load(gzip.open(p, "rt")); PIN["shops"] = list(d["shops"])
    rec = dict(fills=[], prod=[], placed=[], discard=[], herd=[], shops=None); L.G["rec"] = rec
    herd = []

    def on_step(step, state, env):
        if (step + 1) % 24 == 0:
            h = []
            for f in state[0].observation.farms:
                c = {}
                for row in f["tiles"]:
                    for t in row:
                        if isinstance(t, dict):
                            k = t.get("animal") or (("P_" + t["crop"]) if t.get("kind") == "PLANT" else t.get("kind"))
                            c[k] = c.get(k, 0) + 1
                h.append(c)
            herd.append(h)
    try:
        a = harness.load_agent(path, name="ed_a_%d" % d["episode_id"]); b = harness.load_agent(path, name="ed_b_%d" % d["episode_id"])
        r = harness.run_episode(a, b, seed=d["seed"], copy_obs=True, on_step=on_step)
    except Exception as e:
        L.G["rec"] = None; PIN["shops"] = None
        return dict(name=name, ep=d["episode_id"], err=repr(e)[:150])
    L.G["rec"] = None; PIN["shops"] = None
    shops_end = list(r["state"][0].observation.town["unlocked_shops"])
    seats = []
    for s in range(2):
        sell = {}; buyp = {}; cost = dict(seed=0, animal=0, hire=0, land=0)
        for st, pl, op, it, pr in rec["fills"]:
            if pl != s: continue
            if op == "SELL":
                q = sell.setdefault(it, dict(u=0, rev=0)); q["u"] += 1; q["rev"] += pr
            elif op == "BUY_PRODUCT":
                q = buyp.setdefault(it, [0, 0]); q[0] += 1; q[1] += pr
            elif op == "BUY_SEED": cost["seed"] += pr
            elif op == "BUY_ANIMAL": cost["animal"] += pr
            elif op == "HIRE": cost["hire"] += pr
            elif op == "BUY_LAND": cost["land"] += pr
        prod = {}
        for st, pl, k, n in rec["prod"]:
            if pl == s: prod[k] = prod.get(k, 0) + n
        seats.append(dict(bank=r["reward"][s], sell=sell, buyp=buyp, cost=cost, prod=prod, herd=[h[s] for h in herd],
                          land=[x[0] for x in rec["fills"] if x[1] == s and x[2] == "BUY_LAND"]))
    return dict(name=name, ep=d["episode_id"], shops_ok=shops_end == list(d["shops"]), seats=seats)


if __name__ == "__main__":
    out, arm = sys.argv[1], sys.argv[2].split("=", 1)
    W, LIM = int(sys.argv[3]), int(sys.argv[4]); g = sys.argv[5] if len(sys.argv) > 5 else "mine/top10/*.json.gz"
    paths = sorted(glob.glob(g))[:LIM]
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: r = json.loads(line); done.add((r["name"], r["ep"]))
            except Exception: pass
    jobs = [(arm[0], arm[1], p) for p in paths if (arm[0], int(os.path.basename(p).split(".")[0])) not in done]
    print(len(jobs), "jobs", flush=True)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
        for i, r in enumerate(ex.map(job, jobs, chunksize=1), 1):
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
