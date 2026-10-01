"""Is the router's second decision harmful on the games that reach it from tape 1?

The shipped model picks tape 0 or 1 at step 144, then tape 2 or 3 at step 648. Tape 1 diverges from
tapes 2 and 3 at turn 168, so on any game that went to tape 1 the second decision splices a tail
recorded against tape 0's history onto a farm that tape 1 built for the preceding 480 turns. Roughly
20% of games take that path.

`choose()` documents that a leaf of -1 retains the current tape, so a fix is expressible in
model.json alone -- but only if the splice is actually costing something. This measures it by
comparing the shipped model against one with the second stage removed, reported separately for the
games that reach step 648 on tape 0 (where the switch is sound) and on tape 1 (where it is not).
"""
import json
import os
import shutil
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

SRC = "rivals/yhay81_shop-router-0908/pkg"
FILES = ("main.py", "observation.py", "model.json", "actions.json")
POOL = [
    "rivals/leoprovorov_kaggriculture-v65/main.py",
    "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py",
    "rivals/avioon_kaggriculture-apex-v7-god-emperor/main.py",
]


def build_no_stage2(outdir):
    if os.path.isdir(outdir):
        shutil.rmtree(outdir)
    os.makedirs(outdir)
    for f in FILES:
        shutil.copy(os.path.join(SRC, f), os.path.join(outdir, f))
    model = json.load(open(os.path.join(SRC, "model.json")))
    model["stages"] = [s for s in model["stages"] if int(s["step"]) == 144]
    json.dump(model, open(os.path.join(outdir, "model.json"), "w"))
    return os.path.join(outdir, "main.py")


def first_choice(seed):
    """Which tape the shipped model selects at step 144, decided on public state only."""
    import importlib.util
    name = "sp_probe"
    spec = importlib.util.spec_from_file_location(name, os.path.join(SRC, "main.py"))
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    m._ROUTER = None
    harness.run_episode(m.agent, POOL[0], seed=seed, catch_errors=True)
    d = [x["choice"] for x in (m._ROUTER.decisions if m._ROUTER else [])]
    return d[0] if d else None


def _job(a):
    cand, opp, seed, swap = a
    x, y = (opp, cand) if swap else (cand, opp)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    p, q = r["reward"][::-1] if swap else r["reward"]
    return (cand, (opp, seed, swap), 1 if p > q else (0.5 if p == q else 0), p - q)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    shipped = os.path.join(SRC, "main.py")
    nostage2 = build_no_stage2("bench_frozen/nostage2")
    idx = json.load(open("data/seedindex_900000_1400.json"))
    seeds = [r["seed"] for r in idx][850:850 + n]

    with ProcessPoolExecutor(max_workers=7) as ex:
        firsts = list(ex.map(first_choice, seeds))
    tape1 = [s for s, f in zip(seeds, firsts) if f == 1]
    tape0 = [s for s, f in zip(seeds, firsts) if f == 0]
    print(f"of {len(seeds)} seeds: {len(tape1)} go to tape 1 at step 144, {len(tape0)} stay on 0",
          flush=True)

    for label, ss in (("PATH 1 (splice is unsound)", tape1), ("PATH 0 (switch is sound)", tape0)):
        if not ss:
            continue
        jobs = [(c, o, s, sw) for c in (shipped, nostage2) for o in POOL for s in ss
                for sw in (0, 1)]
        with ProcessPoolExecutor(max_workers=7) as ex:
            res = list(ex.map(_job, jobs, chunksize=4))
        cell = {}
        for c, k, w, m in res:
            cell.setdefault(k, {})[c] = (w, m)
        print(f"\n{label}: {len(ss)} seeds x {len(POOL)} opps x 2 seats = {len(ss)*len(POOL)*2} games")
        print(f"{'model':<26}{'winrate':>9}{'margin':>10}{'dWR':>9}{'SE':>7}{'z':>7}")
        for c, lab in ((shipped, "shipped (2 stages)"), (nostage2, "stage 2 removed")):
            pairs = [(v[shipped][0], v[c][0]) for v in cell.values() if shipped in v and c in v]
            wr = statistics.mean(b for _, b in pairs)
            mg = statistics.mean(v[c][1] for v in cell.values() if c in v)
            d = statistics.mean(b - a for a, b in pairs)
            se = (statistics.pstdev([b - a for a, b in pairs]) / len(pairs) ** 0.5) if len(pairs) > 1 else 0
            print(f"{lab:<26}{wr:>9.4f}{mg:>+10,.0f}{d:>+9.4f}{se:>7.4f}"
                  f"{(d/se if se else 0):>+7.2f}", flush=True)
