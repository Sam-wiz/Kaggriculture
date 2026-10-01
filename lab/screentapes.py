"""Screen mined tapes: which of them actually win when replayed against the current meta?

A recorded tape reproduces its own episode exactly, but that says nothing about how it fares on a
different seed against a different opponent -- the shop draw it was built around is gone. So each
tape is run as a fixed-action agent against a small meta pool over several seeds, and ranked by win
rate against the same yardstick we use everywhere else.

The current base (yhay81's router) is included as the reference line: a tape is only interesting if
it beats that.
"""
import gzip
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

PASS = {"farmer": ["PASS"], "hands": [], "market": []}
POOL = [
    "rivals/leoprovorov_kaggriculture-v65/main.py",
    "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py",
    "rivals/y3uanm_kaggriculture-market-impact-router-v4/main.py",
]
REF = "rivals/yhay81_shop-router-0908/pkg/main.py"
TAPES = "data/tapes/tapes_2026-09-08.jsonl.gz"
def load_tapes(path=TAPES, meta_only=False):
    """Read the library. `meta_only` drops the action stream, which is 99% of the bytes."""
    out = []
    for line in gzip.open(path, "rt"):
        r = json.loads(line)
        if meta_only:
            r.pop("tape", None)
        out.append(r)
    return out


def load_one(i, path=TAPES):
    for k, line in enumerate(gzip.open(path, "rt")):
        if k == i:
            return json.loads(line)
    return None


def make_agent(tape):
    n = len(tape)

    def agent(obs):
        s = obs.get("step")
        if s is None:
            s = int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        if s < 0 or s >= n:
            return dict(PASS)
        a = tape[s]
        if not isinstance(a, dict):
            return dict(PASS)
        have = len(obs["farms"][obs["player"]].get("hands") or [])
        hands = list(a.get("hands") or [])[:have]
        hands += [["PASS"]] * (have - len(hands))
        return {"farmer": a.get("farmer", ["PASS"]), "hands": hands,
                "market": list(a.get("market") or [])[:10]}
    return agent


def _job(a):
    """One job = one tape against the whole pool.

    Keying jobs by (tape, opponent, seed) made every worker hold all 570 tapes -- roughly a
    gigabyte of Python objects each -- and the pool thrashed. Loading a single tape per job keeps
    each worker to one action stream at a time.
    """
    idx, seeds = a
    me = REF if idx < 0 else make_agent(load_one(idx)["tape"])
    out = []
    for opp in POOL:
        for seed in seeds:
            for swap in (0, 1):
                x, y = (opp, me) if swap else (me, opp)
                try:
                    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
                except Exception:
                    continue
                p, q = r["reward"][::-1] if swap else r["reward"]
                out.append((1 if p > q else (0.5 if p == q else 0), p - q))
    return (idx, out)


if __name__ == "__main__":
    nseed = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    recs = load_tapes(meta_only=True)
    idx = json.load(open("data/seedindex_900000_1400.json"))
    seeds = [r["seed"] for r in idx][1000:1000 + nseed]
    # Pre-filter by the tape's own recorded bank: screening all 570 takes ~35 minutes, and a tape
    # that only banked 60k in the game it was recorded in is not going to out-earn the reference.
    top = int(os.environ.get("TOP", "0"))
    order = sorted(range(len(recs)), key=lambda i: -recs[i]["bank"])
    keep = order[:top] if top else list(range(len(recs)))
    jobs = [(i, seeds) for i in [-1] + keep]
    print(f"{len(recs)} tapes + reference, "
          f"{len(jobs)*len(POOL)*len(seeds)*2} games", flush=True)
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=1))
    by = {i: v for i, v in res}
    ref = by.get(-1, [])
    ref_wr = statistics.mean(w for w, _ in ref) if ref else 0
    print(f"\nreference (yhay81 router): win rate {ref_wr:.3f}, "
          f"margin {statistics.mean(m for _, m in ref):+,.0f}\n", flush=True)
    rows = []
    for i, v in by.items():
        if i < 0:
            continue
        if not v:
            continue
        rows.append((i, statistics.mean(w for w, _ in v),
                     statistics.mean(m for _, m in v), recs[i]))
    rows.sort(key=lambda r: (-r[1], -r[2]))
    print(f"{'rank':>5}{'team':<22}{'wr':>7}{'margin':>10}{'ownBank':>10}{'yarn':>6}{'seed':>12}")
    for k, (i, wr, mg, rec) in enumerate(rows[:30], 1):
        print(f"{k:>5}{rec['team'][:20]:<22}{wr:>7.3f}{mg:>+10,.0f}"
              f"{rec['bank']:>10,.0f}{rec['shops'].count('YARN_STORE'):>6}{rec['seed']:>12}")
    beat = sum(1 for _, wr, _, _ in rows if wr > ref_wr)
    print(f"\ntapes beating the reference on win rate: {beat}/{len(rows)}")
    json.dump([{"i": i, "wr": wr, "margin": mg, "team": r["team"], "seed": r["seed"],
                "bank": r["bank"], "yarn": r["shops"].count("YARN_STORE")}
               for i, wr, mg, r in rows], open("data/tapescreen.json", "w"))
