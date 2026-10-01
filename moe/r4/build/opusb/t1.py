"""T1 — does a top team's recorded unit+market stream (a "tape") transfer? kagsim, closed-loop opponent.

Arms per (game G, top seat k, team X):
  rec     X tape vs the recorded opponent tape on seed(G)            -> must reproduce recorded banks
  own     X tape vs a live agent (default C1) on seed(G)             -> opponent sensitivity only
  xseed   X tape vs the live agent on seed(H), H = another game       -> seed + opponent sensitivity
  live    live agent vs live agent? no — `ref`: live agent in X's seat vs the same live agent (mirror) on seed(H)
          gives the live agent's own bank on seed(H) for a like-for-like comparison.
Per run: both banks, X-seat kagsim telemetry (dead actions, refused buys, escapes, dry plants ...), final shops,
per-dawn farm signature divergence vs X's recorded game (own seed only).
usage: t1.py OUT.jsonl JOBS.json WORKERS
"""
import gzip, json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act, PASS
import kagsim

TELE = ("dead_actions", "refused_buy_seed", "refused_buy_animal", "refused_hire", "refused_buy_land",
        "refused_buy_product", "sell_zero_fill", "plant_dead", "harvest_dead", "water_dead", "place_dead",
        "pickup_dead", "animals_escaped", "plants_dry", "silent_loss_coins", "shed_discarded_units",
        "sell_revenue", "total_spend", "weed_tile_days", "phantom_hand_actions")


def ep(path):
    return json.load(gzip.open(path, "rt"))


def tape(acts, seat):
    def f(o):
        t = o["step"] + 1
        a = acts[t][seat] if t < len(acts) else None
        return a if isinstance(a, dict) else PASS
    return f


def farmsig(f):
    out = []
    for row in f["tiles"]:
        for t in row:
            if t is None: out.append(".")
            elif t == "LOCKED": out.append("L")
            elif t.get("kind") == "PLANT": out.append("P" + t["crop"][:2])
            elif t.get("kind") == "WEED": out.append("W")
            else: out.append(t["kind"][:1] + (t.get("animal") or "-")[:2])
    return out


def play(seed, A, B, sigseat=None):
    g = kagsim.Game(seed=int(seed)); sigs = []
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        if sigseat is not None and t % 24 == 23: sigs.append(farmsig(o0["farms"][sigseat]))
        g.step(A(o0), B(o1))
    o = g.observe(0)
    return dict(r=[float(g.reward(0)), float(g.reward(1))], shops=list(o["town"]["unlocked_shops"]),
                tele=[{k: g.telemetry(i).get(k) for k in TELE} for i in range(2)], sigs=sigs)


def job(j):
    t0 = time.time()
    try:
        G = ep(j["g"]); k = j["seat"]; X = tape(G["actions"], k)
        arm = j["arm"]
        if arm == "rec":
            O = tape(G["actions"], 1 - k); seed = G["seed"]
        else:
            fn, m = load(j["live"], "lv"); O = lambda o, fn=fn: act(fn, o)
            seed = G["seed"] if arm == "own" else ep(j["h"])["seed"]
        if arm == "ref":   # live agent in both seats on seed(H): the live agent's own bank there
            fn2, m2 = load(j["live"], "lv2"); X = lambda o, fn=fn2: act(fn, o)
        A, B = (X, O) if k == 0 else (O, X)
        res = play(seed, A, B, sigseat=k if arm in ("rec", "own") else None)
        out = dict(j, seed=seed, me=res["r"][k], opp=res["r"][1 - k], rec_me=G["rewards"][k],
                   rec_opp=G["rewards"][1 - k], team=G["teams"][k], rec_opp_team=G["teams"][1 - k],
                   shops=res["shops"], rec_shops=G.get("shops"), tele=res["tele"][k], tele_opp=res["tele"][1 - k],
                   s=round(time.time() - t0, 1))
        if arm in ("rec", "own"): out["sigs"] = res["sigs"]
        return out
    except Exception as e:
        return dict(j, err=repr(e)[:200])


if __name__ == "__main__":
    out, jobs, W = sys.argv[1], json.load(open(sys.argv[2])), int(sys.argv[3])
    done = set()
    if os.path.exists(out):
        for line in open(out):
            r = json.loads(line); done.add((r["g"], r["seat"], r["arm"], r.get("h"), r.get("live")))
    jobs = [j for j in jobs if (j["g"], j["seat"], j["arm"], j.get("h"), j.get("live")) not in done]
    print(len(jobs), "jobs", flush=True)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
        for i, r in enumerate(ex.map(job, jobs, chunksize=1), 1):
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
            if i % 10 == 0: print(i, flush=True)
