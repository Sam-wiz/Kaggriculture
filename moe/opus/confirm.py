"""Seat-0 paired confirmation (clone cells are seat-symmetric): agents x opponents x seeds[a:b]."""
import json, os, sys, itertools
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.getcwd()); import harness
AG = {"brx": "moe/opus/frozen_brx_v1.py", "brx2": "moe/opus/frozen_brx2_v1.py", "ctrl": "moe/opus/frozen_ctrl_sir2.py"}
OPP = {"LIVE_sir_V1": "subV_sir2.py", "LIVE_f55rec_V2": "subV2_f55rec.py",
       "koshinm": "rivals/koshinm_kaggriculture-local-best-2026-09-21/main.py", "metav4": "subL_metav4.py"}
def job(a):
    an, on, s = a
    try:
        r = harness.run_episode(AG[an], OPP[on], seed=s, catch_errors=True)
        if r["status"] != ["DONE", "DONE"]: return (an, on, s, None)
        return (an, on, s, r["reward"][0] - r["reward"][1])
    except Exception:
        return (an, on, s, None)
if __name__ == "__main__":
    lo, n = int(sys.argv[1]), int(sys.argv[2]); out = sys.argv[3]
    seeds = [r["seed"] for r in json.load(open("data/seedindex_900000_1400.json"))][lo:lo + n]
    jobs = [(a, o, s) for a in AG for o in OPP for s in seeds if not (a == "ctrl" and o == "LIVE_sir_V1")]
    print(len(jobs), "games", flush=True)
    with ProcessPoolExecutor(2) as ex:
        res = list(ex.map(job, jobs, chunksize=2))
    json.dump(res, open(out, "w"))
    M = {(a, o, s): m for a, o, s, m in res}
    w = lambda m: 1 if m > 0 else .5 if m == 0 else 0
    for o in OPP:
        line = f"{o:15s}"
        for a in AG:
            ms = [M.get((a, o, s)) for s in seeds]
            if a == "ctrl" and o == "LIVE_sir_V1": ms = [0.0] * len(seeds)
            ms = [m for m in ms if m is not None]
            line += f" | {a} WR {sum(map(w, ms))/len(ms):.3f} mean {sum(ms)/len(ms):+6.0f}"
        for a in ("brx", "brx2"):
            d = [M[(a, o, s)] - (0.0 if o == "LIVE_sir_V1" else M[("ctrl", o, s)]) for s in seeds
                 if M.get((a, o, s)) is not None and (o == "LIVE_sir_V1" or M.get(("ctrl", o, s)) is not None)]
            line += f" | {a}-ctrl {sum(d)/len(d):+5.0f} ({sum(x>0 for x in d)}+/{sum(x<0 for x in d)}-)"
        print(line)
