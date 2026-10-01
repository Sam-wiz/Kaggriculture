# Solo seeds for BC-shifted clones vs clone_dsm baseline. Kill criterion (opus):
# clone_dsm_bc_shift must reach ~60k solo to keep the lane alive.
import sys, os, json
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor

NOP = {"farmer": ["PASS"], "hands": [], "market": []}

def job(arg):
    from run import load, act
    import kagsim
    pa, seed = arg
    a, _ = load(pa, "a")
    g = kagsim.Game(seed=int(seed))
    for t in range(719):
        g.step(act(a, g.observe(0)), NOP)
    return (pa.split("/")[-1], seed, float(g.reward(0)))

if __name__ == "__main__":
    os.nice(10)
    agents = ["clone_dsm.py", "clone_dsm_bc.py", "clone_bc.py"]
    jobs = [("moe/r7/build/devin/" + a, s) for a in agents for s in (1, 2, 3)]
    with ProcessPoolExecutor(max_workers=6) as ex:
        for r in ex.map(job, jobs):
            print(r, flush=True)
