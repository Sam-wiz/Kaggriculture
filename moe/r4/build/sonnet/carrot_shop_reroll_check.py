"""Sonnet r4: does shepherd_nocarrot's changed tile occupancy reroll town shops vs shepherd,
same seed/opponent/seat? Direct test of luna's confound claim on the actual 24 ablation seeds."""
import sys, os, json, importlib.util
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/kaggriculture-cppsim")
import kagsim
from concurrent.futures import ProcessPoolExecutor


def load(path, tag):
    ap = os.path.join(ROOT, path)
    spec = importlib.util.spec_from_file_location("CAND_" + tag, ap)
    m = importlib.util.module_from_spec(spec)
    sys.modules["CAND_" + tag] = m
    spec.loader.exec_module(m)
    return m.agent


PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def run(cand_path, opp_path, seed, us, tag):
    a = load(cand_path, "x_%d_%s" % (seed, tag))
    b = load(opp_path, "o_%d_%s" % (seed, tag))
    g = kagsim.Game(seed=int(seed))
    shop_hist = []
    empty_hist = []
    last_shops = None
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
        oo = o0 if us == 0 else o1
        shops = tuple(oo["town"]["unlocked_shops"])
        if shops != last_shops:
            shop_hist.append((t, shops))
            last_shops = shops
        if t % 24 == 0:
            me = oo["farms"][oo["player"]]
            empties = sum(1 for row in me["tiles"] for c in row if c is None)
            empty_hist.append((t, empties))
    r = [float(g.reward(0)), float(g.reward(1))]
    return shop_hist, empty_hist, r[us] - r[1 - us]


def job(a):
    seed, us, opp_name, opp_path = a
    sh_a, em_a, m_a = run("subW_shepherd.py", opp_path, seed, us, "shep")
    sh_b, em_b, m_b = run("moe/r4/build/sonnet/shepherd_nocarrot.py", opp_path, seed, us, "noc")
    diverge_step = None
    for i in range(min(len(sh_a), len(sh_b))):
        if sh_a[i] != sh_b[i]:
            diverge_step = sh_a[i][0]
            break
    if diverge_step is None and len(sh_a) != len(sh_b):
        diverge_step = "len_mismatch(%d vs %d)" % (len(sh_a), len(sh_b))
    return dict(seed=seed, us=us, opp=opp_name, diverge_step=diverge_step,
                n_shop_events_shep=len(sh_a), n_shop_events_noc=len(sh_b),
                margin_shep=m_a, margin_noc=m_b, empty_shep=em_a[-1], empty_noc=em_b[-1])


if __name__ == "__main__":
    seeds = list(range(9101, 9101 + 24))
    opponents = [("hyb2965", "subX_hyb2965.py"), ("shepherd", "subW_shepherd.py")]
    jobs = [(s, i % 2, oname, opath) for oname, opath in opponents for i, s in enumerate(seeds)]
    out = "moe/r4/build/sonnet/carrot_shop_reroll_check.jsonl"
    with ProcessPoolExecutor(max_workers=2) as ex, open(out, "w") as f:
        for res in ex.map(job, jobs, chunksize=1):
            f.write(json.dumps(res) + "\n")
            f.flush()
            print(res, flush=True)
