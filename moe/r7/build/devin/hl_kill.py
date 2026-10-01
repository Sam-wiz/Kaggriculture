import json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor
from collections import Counter
def job(arg):
    from run import load, act
    import kagsim
    (na, pa), seed = arg
    try:
        a, _ = load(pa, "a"); b, _ = load("subAB_m30b.py", "b")
        g = kagsim.Game(seed=int(seed)); buys=Counter()
        for t in range(719):
            an = act(a, g.observe(0)); g.step(an, act(b, g.observe(1)))
            for o in an.get("market") or []:
                if isinstance(o,(list,tuple)) and o and o[0]=="BUY_ANIMAL": buys[o[1]]+=o[2] if len(o)>2 else 1
        return dict(a=na, seed=seed, ra=float(g.reward(0)), rb=float(g.reward(1)), buys=dict(buys))
    except Exception as e:
        return dict(a=na, seed=seed, err=repr(e)[:150])
if __name__ == "__main__":
    os.nice(10)
    cands = [(v, f"moe/r7/build/devin/agents_v8_{v}.py") for v in ("hl6", "hd4")]
    jobs = [(c, s) for c in cands for s in range(9700001, 9700021)]
    with ProcessPoolExecutor(max_workers=4) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/hl_kill.json", "w"), indent=1)
    for n, _ in cands:
        g = [r for r in rows if r["a"] == n and "err" not in r]
        w = sum(r["ra"] > r["rb"] for r in g)
        import statistics
        bc = statistics.mean(r["buys"].get("COW",0) for r in g); bs=statistics.mean(r["buys"].get("SHEEP",0) for r in g); bg=statistics.mean(r["buys"].get("GOOSE",0) for r in g)
        print(f"{n}: {w}-{len(g)-w} mean {sum(r['ra']-r['rb'] for r in g)/len(g):+.0f} | avg buys C{bc:.1f} S{bs:.1f} G{bg:.1f}")
