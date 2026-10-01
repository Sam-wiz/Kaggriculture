"""Transfer to the REAL WLV: our seat = shepherd variant (live), their seat = recorded WLV tape (open-loop), 18 WLV games.
Reports margin and the our-bank / their-bank split vs vanilla shepherd (their-bank half is the flattered part).
usage: openwlv.py TAG name=path ... (vanilla shepherd always included)"""
import os, sys, json, gzip
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0, ROOT)
from concurrent.futures import ProcessPoolExecutor
PASS = {"farmer": ["PASS"], "hands": [], "market": []}
def tape(acts, seat):
    def ag(obs):
        t = obs["step"] + 1; a = acts[t][seat] if t < len(acts) else None
        return a if isinstance(a, dict) else PASS
    return ag
def job(args):
    ep, name, path, seat, seed, acts = args
    import harness
    me = harness.load_agent(path, name=f"ow_{name}_{ep}")
    pair = (me, tape(acts, 1 - seat)) if seat == 0 else (tape(acts, 1 - seat), me)
    r = harness.run_episode(pair[0], pair[1], seed=seed, copy_obs=True); rw = r["reward"]
    return dict(ep=ep, name=name, m=rw[seat] - rw[1 - seat], ours=rw[seat], theirs=rw[1 - seat])
if __name__ == "__main__":
    tag = sys.argv[1]; C = [("shep", "subW_shepherd.py")] + [tuple(a.split("=", 1)) for a in sys.argv[2:]]
    rows = json.load(open("moe/r3/fable_scratch/live_rows2.json"))
    sel = [r for r in rows if tuple(r["open_they"]) == (5, 0) and (r["R"] or 0) >= 2000 and r["same_u"] >= 0.85 and "Acidic" not in r["opp"]]
    jobs = []
    for r in sel:
        d = json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz", "rt"))
        for n, p in C: jobs.append((int(r["ep"]), n, p, r["seat"], d["seed"], d["actions"]))
    with ProcessPoolExecutor(max_workers=2) as ex: res = list(ex.map(job, jobs, chunksize=1))
    json.dump(res, open(f"moe/r3/build/opus/openwlv_{tag}.json", "w"))
    van = {r["ep"]: r for r in res if r["name"] == "shep"}
    for n, _ in C:
        X = [r for r in res if r["name"] == n]
        d = [r["m"] - van[r["ep"]]["m"] for r in X]; do = [r["ours"] - van[r["ep"]]["ours"] for r in X]; dt = [r["theirs"] - van[r["ep"]]["theirs"] for r in X]
        lw = sum(1 for r in X if van[r["ep"]]["m"] <= 0 < r["m"]); wl = sum(1 for r in X if r["m"] <= 0 < van[r["ep"]]["m"])
        print(f"{n:8s} W-L {sum(r['m']>0 for r in X)}-{sum(r['m']<=0 for r in X)} mean {sum(r['m'] for r in X)/len(X):+6.0f} | vs vanilla {sum(d)/len(d):+6.0f} (our-bank {sum(do)/len(do):+5.0f}, their-bank {sum(dt)/len(dt):+5.0f}) | L->W {lw} W->L {wl}", flush=True)
