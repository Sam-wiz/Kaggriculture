import json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor
def job(arg):
    from run import load, act
    import kagsim
    (na, pa, nb, pb), seed = arg
    try:
        a, _ = load(pa, "a"); b, _ = load(pb, "b")
        g = kagsim.Game(seed=int(seed))
        for t in range(719):
            g.step(act(a, g.observe(0)), act(b, g.observe(1)))
        return dict(a=na, seed=seed, ra=float(g.reward(0)), rb=float(g.reward(1)))
    except Exception as e:
        return dict(a=na, seed=seed, err=repr(e)[:100])
if __name__ == "__main__":
    os.nice(10)
    BASE = ("M30B", "moe/r6/build/devin/harvest_m30_brx2.py")
    cands = [(n, f"rivalsGH/pranav-bot_kaggriculture/{n}") for n in
             ("submissions_telemetry_policy_fix_main.py", "submissions_sovereign_apex_main.py",
              "submissions_apex_engine_main.py", "submissions_velocity_sovereign_main.py")]
    jobs = [((c, p, BASE[0], BASE[1]), s) for c, p in cands for s in range(9600001, 9600006)]
    with ProcessPoolExecutor(max_workers=4) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    for c, _ in cands:
        g = [r for r in rows if r["a"] == c and "err" not in r]
        e = [r for r in rows if r["a"] == c and "err" in r]
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"{c[:45]:45} {w}-{l}-{len(g)-w-l} err={len(e)} mean {sum(r['ra']-r['rb'] for r in g)/max(1,len(g)):+.0f}")
        if e: print("   ", e[0]["err"])
