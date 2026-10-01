"""ENGINE gap: closed-loop self-play of a build on a dump game's seed with the recorded shop sequence pinned,
vs what the two top teams banked in that same world (seed + shops). Both sides are closed-loop, so there is no
frozen-tape breakage; this measures the economic engine (production + price capture under a symmetric rival),
not head-to-head skill.
usage: engine.py OUT.jsonl NAME=PATH[,..] WORKERS LIMIT [GLOB] [OFFSET]
"""
import glob, gzip, json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act
import kagsim


def job(arg):
    name, path, p = arg
    d = json.load(gzip.open(p, "rt")); t0 = time.time()
    try:
        a, _ = load(path, "e0"); b, _ = load(path, "e1")
        g = kagsim.Game(seed=int(d["seed"]), shops=list(d["shops"]))
        for t in range(719):
            o0, o1 = g.observe(0), g.observe(1)
            g.step(act(a, o0), act(b, o1))
        r = [float(g.reward(0)), float(g.reward(1))]
    except Exception as e:
        return dict(name=name, ep=d["episode_id"], err=repr(e)[:120])
    return dict(name=name, ep=d["episode_id"], banks=r, rec=d["rewards"], teams=d["teams"], shops=d["shops"],
                s=round(time.time() - t0, 1))


if __name__ == "__main__":
    out = sys.argv[1]; arms = [a.split("=", 1) for a in sys.argv[2].split(",")]
    W, LIM = int(sys.argv[3]), int(sys.argv[4]); g = sys.argv[5] if len(sys.argv) > 5 else "mine/top10/*.json.gz"
    OFF = int(sys.argv[6]) if len(sys.argv) > 6 else 0
    paths = sorted(glob.glob(g))[OFF:OFF + LIM]
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: r = json.loads(line); done.add((r["name"], r["ep"]))
            except Exception: pass
    jobs = [(n, a, p) for p in paths for n, a in arms if (n, int(os.path.basename(p).split(".")[0])) not in done]
    print(len(jobs), "jobs", flush=True)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
        for i, r in enumerate(ex.map(job, jobs, chunksize=1), 1):
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
            if i % 20 == 0: print(i, flush=True)
