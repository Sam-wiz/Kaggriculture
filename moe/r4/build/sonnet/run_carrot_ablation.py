"""
Paired closed-loop test: shepherd vs shepherd_nocarrot, each vs a fixed opponent,
same seeds, same seat, kagsim (bit-exact, fast). <=2 workers.
"""
import sys, os, json, importlib.util
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT)
sys.path.insert(0, ROOT)
sys.path.insert(0, ROOT + "/kaggriculture-cppsim")
import kagsim
from concurrent.futures import ProcessPoolExecutor

PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def load(path, tag):
    ap = os.path.join(ROOT, path)
    spec = importlib.util.spec_from_file_location("CAND_" + tag, ap)
    m = importlib.util.module_from_spec(spec)
    sys.modules["CAND_" + tag] = m
    spec.loader.exec_module(m)
    return m.agent


def game(job):
    xname, xpath, oppname, opppath, seed, us = job
    a = load(xpath, "x_%d_%s" % (seed, xname))
    b = load(opppath, "o_%d_%s" % (seed, oppname))
    g = kagsim.Game(seed=int(seed))
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        A, B = (a, b) if us == 0 else (b, a)
        try:
            a0 = A(o0)
        except Exception:
            a0 = PASS
        try:
            a1 = B(o1)
        except Exception:
            a1 = PASS
        g.step(a0, a1)
    r = [float(g.reward(0)), float(g.reward(1))]
    return xname, oppname, int(seed), us, r[us], r[1 - us]


if __name__ == "__main__":
    N = 24
    seeds = list(range(9101, 9101 + N))
    opponents = [
        ("hyb2965", "subX_hyb2965.py"),
        ("shepherd", "subW_shepherd.py"),
    ]
    candidates = [
        ("shepherd", "subW_shepherd.py"),
        ("shepherd_nocarrot", "moe/r4/build/sonnet/shepherd_nocarrot.py"),
    ]
    jobs = []
    for oname, opath in opponents:
        for cname, cpath in candidates:
            for i, s in enumerate(seeds):
                us = i % 2  # alternate seats
                jobs.append((cname, cpath, oname, opath, s, us))
    out = "moe/r4/build/sonnet/carrot_ablation.jsonl"
    with ProcessPoolExecutor(max_workers=2) as ex, open(out, "w") as f:
        for res in ex.map(game, jobs, chunksize=1):
            f.write(json.dumps(res) + "\n")
            f.flush()
            print(res)
