"""Real-WLV transfer check (r3 openwlv.py recipe, kagsim): our seat = candidate (live), their seat = the recorded WLV
tape open-loop, on the 18 live WLV games. Both C1 arms carry the same PREDICT2 library (which contains these 18 WLV
streams -> both flattered equally), so the PAIRED difference isolates the P-library change. Report our-bank half.
usage: openwlv_b.py OUT.json name=path ..."""
import os, sys, json, gzip
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act, PASS
import kagsim
HOLD = os.environ.get("OW_HOLD") == "1"
def tape(acts, seat):
    def ag(obs):
        t = obs["step"] + 1; a = acts[t][seat] if t < len(acts) else None
        return a if isinstance(a, dict) else PASS
    return ag
def job(args):
    ep, name, path, seat, seed = args
    d = json.load(gzip.open(f"mine/opp/{ep}.json.gz", "rt")); T = tape(d["actions"], 1 - seat)
    fn, m = load(path, "w"); A = lambda o: act(fn, o)
    if HOLD and hasattr(m, "_V92_EP"):   # PREDICT2 parity holdout on the candidate; shield the P library (ep=-1)
        m._V92_EP = int(ep); _o = m._v92_p_forecast
        def _pf(obs, st, _o=_o, _m=m):
            sv = _m._V92_EP; _m._V92_EP = None
            try: return _o(obs, st)
            finally: _m._V92_EP = sv
        m._v92_p_forecast = _pf
    g = kagsim.Game(seed=int(seed))
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        g.step(A(o0) if seat == 0 else T(o0), T(o1) if seat == 0 else A(o1))
    rw = [float(g.reward(0)), float(g.reward(1))]
    return dict(ep=ep, name=name, m=rw[seat] - rw[1 - seat], ours=rw[seat], theirs=rw[1 - seat], rec=d["rewards"][seat])
if __name__ == "__main__":
    out = sys.argv[1]; C = [tuple(a.split("=", 1)) for a in sys.argv[2:]]
    rows = json.load(open("moe/r3/fable_scratch/live_rows2.json"))
    sel = [r for r in rows if tuple(r["open_they"]) == (5, 0) and (r["R"] or 0) >= 2000 and r["same_u"] >= 0.85 and "Acidic" not in r["opp"]]
    jobs = []
    for r in sel:
        d = json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz", "rt"))
        for n, p in C: jobs.append((int(r["ep"]), n, p, r["seat"], d["seed"]))
    print(len(sel), "games", len(jobs), "jobs", flush=True)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=2) as ex: res = list(ex.map(job, jobs, chunksize=1))
    json.dump(res, open(out, "w"))
    base = {r["ep"]: r for r in res if r["name"] == C[0][0]}
    for n, _ in C:
        X = [r for r in res if r["name"] == n]
        d = [r["m"] - base[r["ep"]]["m"] for r in X]; do = [r["ours"] - base[r["ep"]]["ours"] for r in X]; dt = [r["theirs"] - base[r["ep"]]["theirs"] for r in X]
        print(f"{n:6s} W-L {sum(r['m']>0 for r in X)}-{sum(r['m']<=0 for r in X)} mean {sum(r['m'] for r in X)/len(X):+6.0f} | vs {C[0][0]} {sum(d)/len(d):+6.0f} (our-bank {sum(do)/len(do):+5.0f}, their-bank {sum(dt)/len(dt):+5.0f}) better {sum(x>0 for x in d)}/{len(d)}", flush=True)
