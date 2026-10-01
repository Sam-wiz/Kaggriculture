"""C1 minus V233, paired per world (claude-code 22:50 next action). kag_dc engine (shops decoupled from weeds).

Per seed (our seat = seed % 2; opponent = pristine C1 in both arms):
  off : C1        vs C1
  ab  : C1noV233  vs C1     (C1noV233.py = C1 with V233's world gate forced False: never eligible, never commits)
Per arm we log a hash of every action of both seats, both banks, and our/their V233 telemetry, so the
"ablation only changes native-V233 worlds" claim is checked trajectory-wide: in worlds where off's V233 makes no
commit request, both seats' 720 actions and banks must be identical.
usage: nov233.py OUT.jsonl WORKERS SEED [SEED ...]
       nov233.py OUT.jsonl WORKERS --screen SEED0 N   (enrichment: off arm first; ab arm only if V233 requested)
"""
import contextlib, hashlib, importlib.util, io, json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
B = ROOT + "/moe/r5/build/opusb"
sys.path.insert(0, ROOT); os.chdir(ROOT)
import harness as H
spec = importlib.util.spec_from_file_location("kag_dc", ROOT + "/kag_dc.py"); DC = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DC); H.K = DC
PATHS = {"C1": ROOT + "/subY_C1_predict2.py", "C1noV233": B + "/C1noV233.py"}
OPP = os.environ.get("NV_OPP", "C1")   # opponent name; path from NV_OPP_PATH (default pristine C1)
if OPP != "C1": PATHS[OPP] = ROOT + "/" + os.environ["NV_OPP_PATH"]
_N = [0]


class Quiet(Exception):
    pass


def load(which):
    _N[0] += 1
    name = "nv_%s_%d_%d" % (which, os.getpid(), _N[0])
    sp = importlib.util.spec_from_file_location(name, PATHS[which]); m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m
    with contextlib.redirect_stdout(io.StringIO()):
        sp.loader.exec_module(m)
    return m


def v233(m, farm):
    rep = dict(getattr(m, "_V233_REPORT", {}))
    se = [farm["tiles"][y][x] for y in range(5, 10) for x in range(5, 10)]
    return dict(req=rep.get("sheep_commit_requests", 0), committed=rep.get("sheep_committed", 0),
                wool=rep.get("sheep_wool_harvested", 0), budget_decl=rep.get("sheep_budget_declines", 0),
                se=("SE" in farm["unlocked_quadrants"]),
                se_sheep=sum(isinstance(t, dict) and t.get("animal") == "SHEEP" for t in se))


def game(seed, arm, stop_if_quiet=None):
    me = seed % 2
    mm = load(arm); mo = load(OPP)
    ag = [None, None]; ag[me] = mm.agent; ag[1 - me] = mo.agent
    hs = [[], []]; land = []; first_req = [None]

    def hook(step, state, env):
        for i in (0, 1):
            hs[i].append(hashlib.md5(json.dumps(state[i].action, sort_keys=True, default=str).encode()).hexdigest()[:10])
        if any(o and o[0] == "BUY_LAND" for o in (state[me].action.get("market") or [])):
            land.append(step)
        if first_req[0] is None and getattr(mm, "_V233_REPORT", {}).get("sheep_commit_requests", 0):
            first_req[0] = step
        if stop_if_quiet is not None and step == stop_if_quiet and not mm._V233_REPORT.get("sheep_commit_requests", 0):
            raise Quiet

    t0 = time.time()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            r = H.run_episode(ag[0], ag[1], seed=seed, on_step=hook, catch_errors=True)
    except Quiet:
        return dict(seed=seed, me=me, arm=arm, quiet_at=stop_if_quiet, sec=round(time.time() - t0, 1))
    f = r["state"][0].observation.farms
    return dict(seed=seed, me=me, arm=arm, opp_name=OPP, bank=f[me]["money"], opp=f[1 - me]["money"], status=r["status"],
                errors=r["errors"], land=land, first_req=first_req[0],
                v233_me=v233(mm, f[me]), v233_opp=v233(mo, f[1 - me]),
                shops=list(r["state"][0].observation.town["unlocked_shops"]),
                h_me="".join(hs[me]), h_opp="".join(hs[1 - me]), sec=round(time.time() - t0, 1))


def job(a):
    seed, arm, stop = a
    return game(seed, arm, stop)


if __name__ == "__main__":
    os.nice(10)
    out, W = sys.argv[1], int(sys.argv[2])
    from concurrent.futures import ProcessPoolExecutor
    done = set()
    if os.path.exists(out):
        for l in open(out):
            r = json.loads(l); done.add((r["seed"], r["arm"]))
    if sys.argv[3] == "--screen":
        s0, n = int(sys.argv[4]), int(sys.argv[5])
        seeds = list(range(s0, s0 + n))
        # V233 can only request at d11 h0-3 / d12 h0-1 (steps 264-289); quiet at 300 => never fires
        jobs = [(s, "C1", 300) for s in seeds if (s, "C1") not in done]
        with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as fh:
            for r in ex.map(job, jobs, chunksize=1):
                fh.write(json.dumps(r) + "\n"); fh.flush()
        fired = [json.loads(l) for l in open(out)]
        fired = [r["seed"] for r in fired if r["arm"] == "C1" and "bank" in r and r["seed"] in seeds]
        jobs = [(s, "C1noV233", None) for s in fired if (s, "C1noV233") not in done]
        print("screened", len(seeds), "fired", len(fired), flush=True)
    else:
        seeds = [int(s) for s in sys.argv[3:]]
        jobs = [(s, a, None) for s in seeds for a in ("C1", "C1noV233") if (s, a) not in done]
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as fh:
        for r in ex.map(job, jobs, chunksize=1):
            fh.write(json.dumps(r) + "\n"); fh.flush()
            print(r["seed"], r["arm"], r.get("bank"), r.get("opp"), (r.get("v233_me") or {}).get("req"), r["sec"], "s", flush=True)
