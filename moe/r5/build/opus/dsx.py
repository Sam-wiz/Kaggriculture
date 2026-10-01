"""DSX — day-swap executor test (r5 opus instrument for architecture A's critical path).

Replays a recorded top-family game EXACTLY (official Python engine via harness) up to the dawn of day d.
During day d, seat s keeps its recorded MARKET orders (the family's own macro: hires, buys, sells) but its
UNIT ops come from a candidate executor; the opponent replays its tape.  At dawn d+1 we score seat s against
the same game with the family's own unit ops (the exact recording):
    miss_w  plants with consecutive_unwatered >= 1          (missed watering)
    miss_f  animals with consecutive_unfed >= 1              (missed feed)
    care    sum of pending_care_bonus on animals             (care banked)
    val     money + base-value of PRODUCTS in shed + unit inventories + yield sitting on tiles (unplaced animals = 0)
    new     plants planted during day d  /  placed animals
The candidate is told the family's own plan for the day (tiles the family planted / animals it placed during d),
so the test isolates EXECUTION: can our units do the family's day with the family's hands?
usage: dsx.py CAND N_GAMES DAYS [TEAM]      CAND in {family, exec3}   DAYS like 3,6,10,15,20
"""
import copy, glob, gzip, json, os, sys, statistics as st
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT)
for p in (ROOT, ROOT + "/kaggriculture-island-ga"):
    if p not in sys.path: sys.path.insert(0, p)
import harness
BASE = dict(WHEAT=25, CARROT=35, TOMATO=60, STRAWBERRY=120, MELON=250, EGG=50, MILK=160, WOOL=200, FERTILIZER=100,
            COW=400, SHEEP=500, GOOSE=300)
APROD = {"COW": "MILK", "SHEEP": "WOOL", "GOOSE": "EGG"}
PASS = {"farmer": ["PASS"], "hands": [], "market": []}


class Stop(Exception):
    pass


def score(obs, s):
    f = obs["farms"][s]; pv = obs["private"] if isinstance(obs, dict) and "private" in obs else None
    mw = mf = care = 0; tv = 0.0; plants = animals = 0
    for row in f["tiles"]:
        for t in row:
            if not isinstance(t, dict): continue
            if t.get("kind") == "PLANT":
                plants += 1
                if int(t.get("consecutive_unwatered") or 0) >= 1: mw += 1
                tv += int(t.get("yield_units") or 0) * BASE[t["crop"]]
            elif t.get("animal"):
                animals += 1
                if int(t.get("consecutive_unfed") or 0) >= 1: mf += 1
                care += int(t.get("pending_care_bonus") or 0)
                tv += int(t.get("yield_units") or 0) * BASE[APROD[t["animal"]]]
                tv += (1 if t.get("fertilizer_available") else 0) * BASE["FERTILIZER"]
    return dict(miss_w=mw, miss_f=mf, care=care, tile_val=tv, plants=plants, animals=animals, money=f["money"])


def plan_of_day(d, acts, seed, s, day):
    """family's own tiles planted / animals placed during `day` (from its dawn day+1 tiles)"""
    return None  # filled by run() from the family replay


def run(path, s, day, cand_factory):
    d = json.load(gzip.open(path, "rt")); acts = d["actions"]; seed = d["seed"]
    lo, hi = day * 24, day * 24 + 24
    out = {}
    cand = cand_factory() if cand_factory else None
    shadow = {}

    def mk(seat):
        def ag(obs):
            st_ = obs["step"]
            rec = acts[st_ + 1][seat] if st_ + 1 < len(acts) and isinstance(acts[st_ + 1][seat], dict) else PASS
            if seat == s and lo <= st_ < hi:
                if st_ == lo: out["dawn"] = score(obs, s)
                if cand is not None:
                    u = cand(obs)
                    return {"farmer": u.get("farmer") or ["PASS"], "hands": u.get("hands") or [], "market": rec.get("market") or []}
            if seat == s and st_ == hi:
                out["end"] = score(obs, s)
                f = obs["farms"][s]; pv = obs["private"]
                inv = {}
                for iv in pv.get("inventories") or []:
                    for k, v in (iv or {}).items(): inv[k] = inv.get(k, 0) + int(v or 0)
                shed = dict(pv.get("shed") or {})
                out["end"]["goods"] = sum((shed.get(k, 0) + inv.get(k, 0)) * BASE.get(k, 0) for k in set(shed) | set(inv)
                                          if k not in ("COW", "SHEEP", "GOOSE"))   # unplaced animals earn nothing
                out["end"]["val"] = out["end"]["money"] + out["end"]["goods"] + out["end"]["tile_val"]
                out["tiles"] = copy.deepcopy(f["tiles"])
                raise Stop()
            return rec
        return ag
    try:
        harness.run_episode(mk(0), mk(1), seed=seed, copy_obs=False, catch_errors=False)
    except Stop:
        pass
    return out


class Exec3Cand:
    """exec3 row-walker told the family's own plan for the day."""
    def __init__(self, plan):
        import exec3
        self.plan = plan
        self.ex = exec3.Executor3({"market": {}, "days": {}, "meta": {"herd_goal": {}}})

    def __call__(self, obs):
        day = int(obs["day"])
        self.ex.bp["days"][str(day)] = self.plan
        self.ex.goal = {}
        a = self.ex.act(obs)
        return a


def fam_plan(tiles_end, day):
    plants, animals = [], []
    for y, row in enumerate(tiles_end):
        for x, t in enumerate(row):
            if isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("planted_day") == day:
                plants.append((x, y, t["crop"]))
            if isinstance(t, dict) and t.get("animal") and t.get("placed_day") == day:
                animals.append((x, y, t["animal"], "COOP" if t["animal"] == "GOOSE" else "PASTURE"))
    return {"plants": plants, "animals": animals, "buildings": []}


if __name__ == "__main__":
    cname = sys.argv[1]; N = int(sys.argv[2]); days = [int(x) for x in sys.argv[3].split(",")]
    team = sys.argv[4] if len(sys.argv) > 4 else "DSM"
    fam = pickle = None
    paths = []
    for p in sorted(glob.glob("mine/top10/*.json.gz")):
        d = json.load(gzip.open(p, "rt"))
        if team in d["teams"]:
            paths.append((p, d["teams"].index(team)))
        if len(paths) >= N: break
    rows = []
    for p, s in paths:
        for day in days:
            base = run(p, s, day, None)                       # family's own execution (exact)
            plan = fam_plan(base["tiles"], day)
            if cname == "family":
                c = run(p, s, day, None)
            elif cname == "exec3":
                c = run(p, s, day, lambda: Exec3Cand(plan))
            else:
                raise SystemExit("unknown cand")
            b, e = base["end"], c["end"]
            r = dict(ep=os.path.basename(p), seat=s, day=day, n_plant=len(plan["plants"]), n_anim=len(plan["animals"]),
                     fam=dict(miss_w=b["miss_w"], miss_f=b["miss_f"], care=b["care"], val=b["val"], plants=b["plants"], animals=b["animals"]),
                     cand=dict(miss_w=e["miss_w"], miss_f=e["miss_f"], care=e["care"], val=e["val"], plants=e["plants"], animals=e["animals"]),
                     dval=e["val"] - b["val"])
            rows.append(r)
            print(json.dumps(r), flush=True)
    print("\nSUMMARY", cname, team, "n=", len(rows))
    for day in days:
        R = [r for r in rows if r["day"] == day]
        if not R: continue
        print(f" d{day:2d} fam miss_w {st.mean(r['fam']['miss_w'] for r in R):5.1f} miss_f {st.mean(r['fam']['miss_f'] for r in R):4.1f} "
              f"care {st.mean(r['fam']['care'] for r in R):5.1f} | cand miss_w {st.mean(r['cand']['miss_w'] for r in R):5.1f} "
              f"miss_f {st.mean(r['cand']['miss_f'] for r in R):4.1f} care {st.mean(r['cand']['care'] for r in R):5.1f} "
              f"plants {st.mean(r['cand']['plants']-r['fam']['plants'] for r in R):+5.1f} animals {st.mean(r['cand']['animals']-r['fam']['animals'] for r in R):+5.1f} "
              f"| dval {st.mean(r['dval'] for r in R):+8.0f}")
