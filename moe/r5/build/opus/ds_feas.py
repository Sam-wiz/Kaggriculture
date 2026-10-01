"""r5 opus, THREAD turn 2: DS (day-granular splicing) feasibility, answering claude-code 21:35.
Q1: dawn-state distance (100-tile map Hamming, macro.tmap) to the nearest FAMILY day-tape (other game, same day),
    for (a) family seats, (b) non-family top seats, (c) C1 self-play seats.
Q2: splice the nearest family donor's WHOLE day (unit ops + market orders) into the state at dawn d, official
    Python engine, and score at dawn d+1 against the state's own day: dead unit ops (op on a tile it cannot act on),
    our animals unfed / plants unwatered at dawn d+1, value (money + goods at base + tile yield) delta.
usage: ds_feas.py fam N  |  ds_feas.py c1 NSEEDS
"""
import copy, gzip, json, os, pickle, random, statistics as st, sys
from concurrent.futures import ProcessPoolExecutor
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT)
for p in (ROOT, ROOT + "/kaggriculture-island-ga", ROOT + "/moe/r5/build/opus"):
    if p not in sys.path: sys.path.insert(0, p)
import harness
from dsx import score, BASE, PASS
from macro import tmap

DAYS = [6, 10, 15, 21]
TILE_OPS = {"WATER", "HARVEST", "FEED", "CARE", "COLLECT_FERTILIZER", "FERTILIZE", "PLANT", "DIG", "BUILD_COOP",
            "BUILD_PASTURE"}


def ham(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def dead(tile, op):
    if op not in TILE_OPS: return 0
    if tile == "LOCKED": return 1
    if op in ("PLANT", "BUILD_COOP", "BUILD_PASTURE"): return int(tile is not None)
    if not isinstance(tile, dict): return 1
    k = tile.get("kind")
    if op == "WATER": return int(k != "PLANT" or bool(tile.get("watered_today")))
    if op == "FERTILIZE": return int(k != "PLANT")
    if op == "HARVEST": return int(int(tile.get("yield_units") or 0) <= 0)
    if op == "DIG": return int(bool(tile.get("animal")))
    a = tile.get("animal")
    if not a: return 1
    if op == "FEED": return int(bool(tile.get("fed_today")))
    if op == "CARE": return int(bool(tile.get("cared_today")))
    if op == "COLLECT_FERTILIZER": return int(not tile.get("fertilizer_available"))
    return 0


def count_dead(obs, s, act):
    f = obs["farms"][s]; n = 0; tot = 0
    units = [f["farmer"]] + list(f.get("hands") or [])
    ops = [act.get("farmer") or ["PASS"]] + list(act.get("hands") or [])
    for pos, op in zip(units, ops):
        if not op or op[0] not in TILE_OPS: continue
        x, y = pos; tot += 1
        n += dead(f["tiles"][y][x], op[0])
    return n, tot


def load_acts(ep):
    d = json.load(gzip.open("mine/top10/%s.json.gz" % ep, "rt"))
    return d


def rec_act(acts, st_, seat):
    a = acts[st_ + 1][seat] if st_ + 1 < len(acts) and isinstance(acts[st_ + 1][seat], dict) else PASS
    return a


def run_day(agent_factory, seed, s, day, donor):
    """agent_factory() -> (agent0, agent1). During `day`, seat s plays donor=(acts, dseat) if given. Score dawn day+1."""
    lo, hi = day * 24, day * 24 + 24
    a0, a1 = agent_factory()
    base = [a0, a1]; out = dict(dead=0, tot=0)

    class Stop(Exception): pass

    def mk(seat):
        def ag(obs):
            st_ = obs["step"]
            if seat == s and st_ == hi:
                e = score(obs, s)
                pv = obs["private"]; inv = {}
                for iv in pv.get("inventories") or []:
                    for k, v in (iv or {}).items(): inv[k] = inv.get(k, 0) + int(v or 0)
                sh = dict(pv.get("shed") or {})
                e["goods"] = sum((sh.get(k, 0) + inv.get(k, 0)) * BASE.get(k, 0) for k in set(sh) | set(inv)
                                 if k not in ("COW", "SHEEP", "GOOSE"))
                e["val"] = e["money"] + e["goods"] + e["tile_val"]
                out["end"] = e
                raise Stop()
            if seat == s and st_ == lo:
                out["map"] = tmap(obs["farms"][s]["tiles"]); out["dawn"] = score(obs, s)
            if seat == s and lo <= st_ < hi and donor is not None:
                act = rec_act(donor[0], st_, donor[1])
            else:
                act = base[seat](obs)
            if seat == s and lo <= st_ < hi:
                d_, t_ = count_dead(obs, s, act); out["dead"] += d_; out["tot"] += t_
            return act
        return ag
    try:
        harness.run_episode(mk(0), mk(1), seed=seed, copy_obs=True, catch_errors=False)
    except Stop:
        pass
    return out


def tape_factory(acts):
    return lambda: (lambda o: rec_act(acts, o["step"], 0), lambda o: rec_act(acts, o["step"], 1))


C1 = ROOT + "/subY_C1_predict2.py"


def c1_factory():
    import uuid
    return lambda: (harness.load_agent(C1, "c1a_" + uuid.uuid4().hex), harness.load_agent(C1, "c1b_" + uuid.uuid4().hex))


FAMD = None


def fam_index():
    global FAMD
    if FAMD is None:
        FAMD = pickle.load(open(ROOT + "/moe/r5/build/opus/fam.pkl", "rb"))
    return FAMD


def nearest(mp, day, exclude_ep=None):
    best = None
    for r in fam_index()["fam"]:
        if r["ep"] == exclude_ep: continue
        m = r["maps"].get(day)
        if not m: continue
        h = ham(mp, m)
        if best is None or h < best[0]: best = (h, r["ep"], r["seat"])
    return best


def job_fam(arg):
    ep, s, seed, day = arg
    own = load_acts(ep)["actions"]
    mp = fam_index()["fam"]
    my = next(r for r in mp if r["ep"] == ep and r["seat"] == s)
    h, dep, ds = nearest(my["maps"][day], day, exclude_ep=ep)
    donor = (load_acts(dep)["actions"], ds)
    a = run_day(tape_factory(own), seed, s, day, None)
    b = run_day(tape_factory(own), seed, s, day, donor)
    return dict(kind="fam", ep=ep, seat=s, day=day, ham=h, own=a, spl=b)


def job_c1(arg):
    seed, day = arg
    fac = c1_factory()
    a = run_day(fac, seed, 0, day, None)
    h, dep, ds = nearest(a["map"], day)
    donor = (load_acts(dep)["actions"], ds)
    b = run_day(c1_factory(), seed, 0, day, donor)
    return dict(kind="c1", seed=seed, day=day, ham=h, own=a, spl=b)


def summarize(rows):
    for day in DAYS:
        R = [r for r in rows if r["day"] == day]
        if not R: continue
        f = lambda k, w: st.mean(r[w]["end"][k] for r in R)
        print(f" d{day:2d} n={len(R):2d} ham med {st.median(r['ham'] for r in R):5.1f} | dead own {st.mean(r['own']['dead'] for r in R):5.1f}/"
              f"{st.mean(r['own']['tot'] for r in R):5.0f} spl {st.mean(r['spl']['dead'] for r in R):5.1f}/{st.mean(r['spl']['tot'] for r in R):5.0f}"
              f" (<5 dead: {sum(r['spl']['dead'] < 5 for r in R)}/{len(R)}) | miss_f own {f('miss_f','own'):4.1f} spl {f('miss_f','spl'):4.1f}"
              f" | miss_w own {f('miss_w','own'):4.1f} spl {f('miss_w','spl'):4.1f} | dval {st.mean(r['spl']['end']['val'] - r['own']['end']['val'] for r in R):+7.0f}"
              f" (med {st.median(r['spl']['end']['val'] - r['own']['end']['val'] for r in R):+6.0f})", flush=True)


if __name__ == "__main__":
    mode = sys.argv[1]; N = int(sys.argv[2])
    out = ROOT + "/moe/r5/build/opus/ds_feas_%s.jsonl" % mode
    if mode == "dist":   # Q1 for family and non-family top seats (no engine)
        F = fam_index(); rng = random.Random(1)
        for grp in ("fam", "other"):
            S = rng.sample(F[grp], min(N, len(F[grp])))
            for day in (3, 6, 10, 15, 21, 27):
                hs = [nearest(r["maps"][day], day, exclude_ep=r["ep"])[0] for r in S if r["maps"].get(day)]
                print(grp, "day", day, "n", len(hs), "NN ham median", st.median(hs), "p10", sorted(hs)[len(hs) // 10],
                      "p90", sorted(hs)[9 * len(hs) // 10], flush=True)
        raise SystemExit
    if mode == "fam":
        F = fam_index()["fam"]; rng = random.Random(7)
        S = rng.sample(F, N)
        args = [(r["ep"], r["seat"], r["seed"], day) for r in S for day in DAYS]
        fn = job_fam
    else:
        args = [(9520001 + i, day) for i in range(N) for day in DAYS]
        fn = job_c1
    rows = []
    with ProcessPoolExecutor(2, max_tasks_per_child=1) as ex, open(out, "w") as fo:
        for r in ex.map(fn, args):
            rows.append(r); fo.write(json.dumps(r) + "\n"); fo.flush()
            print(r["kind"], r.get("ep", r.get("seed")), r["day"], "ham", r["ham"], "dead", r["own"]["dead"], "->", r["spl"]["dead"],
                  "miss_f", r["own"]["end"]["miss_f"], "->", r["spl"]["end"]["miss_f"], "dval",
                  r["spl"]["end"]["val"] - r["own"]["end"]["val"], flush=True)
    print("SUMMARY", mode, N); summarize(rows)
