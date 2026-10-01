"""GRPO-flavored policy optimization over islandga season-spec genomes.

Mapping to GRPO (group relative policy optimization):
  * policy pi_theta  = a distribution over genomes: the anchor genome
    plus islandga's structured macro-mutation kernel (and crossover with
    the running best-ever as a second parent).
  * group            = one generation: the anchor + K sampled mutants.
  * reward           = PAIRED in-company margin vs a fixed opponent panel
    on a shared seed panel: every member plays the identical
    (seed x opponent) cells, so differences are the genome's, not the
    world's (common random numbers).
  * advantage A_i    = R_i - mean_group(R)  (the group baseline = V(s)).
  * update           = per-coherent-block reinforcement vote: each block
    of the next anchor is drawn from member i w.p. ~ relu(A_i), the
    anchor keeping a sticky prior share. Blocks carried by above-mean
    members gain probability mass; below-mean blocks are suppressed.
    Elitism: the anchor is member 0 of its own group.
  * KL/clip analogue = blocks move at most one generation at a time,
    anchor persistence weight, and a mutation-temperature schedule
    (moves 1-2 normally, 2-5 when the anchor stalls).

Not literal GRPO (no NN, no token sequence, no KL term) — it is the
policy-gradient idea ported to a structured 720-step "action" that is a
compiled season spec. Documented as such.

Eval: exec3 row-walker executor (the strongest blueprint executor we
have), kagsim engine, opponents loaded once per worker, candidate always
seat 0 (kagsim seat-swap is measured bit-identical, so seat-1 adds no
information and halves throughput).

Usage:
    PYTHONPATH=root:root/kaggriculture-island-ga:root/moe/r3/build/opus \\
    .venv/bin/python rl/train.py [--hours 2] [--out rl/results/run1]
                                 [--workers 5] [--resume]

Outputs in <out>: gen.jsonl (one row per member per gen),
games.jsonl (one row per game), state.json (resumable checkpoint),
best.json (best genome + confirm-panel numbers).
"""
import argparse
import copy
import json
import os
import random
import sys
import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
from pathlib import Path

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
for _p in (ROOT, ROOT + "/kaggriculture-island-ga",
           ROOT + "/moe/r3/build/opus",
           ROOT + "/moe/r7/build/devin/rl"):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import policy                     # noqa: E402  (applies bound/cap patches)
from policy import (block_vote, compile_genome, gid_of, is_valid, mutate,
                    crossover, make_species, normalize)
from dsm_genome import dsm_genome  # noqa: E402

OPPS = ("m30b", "v8", "shep")

# training panel: 3 fresh seeds per generation x 3 opponents = 9 games
# per member (inside the "8-12 paired games" bound). Seeds rotate every
# generation (winner's-curse control); all members share the panel, so
# the group comparison is exactly paired.
SEED_BASE = 7700000
N_SEEDS = 3

# fixed confirm panel (disjoint from training rotation and from every
# held-out block used elsewhere in the repo) for best-ever tracking and
# the final paired report
CONFIRM_SEEDS = [9600001 + i for i in range(20)]

GROUP_MUTANTS = 6                  # mutants of the anchor per generation
STICKY = 0.75                      # anchor persistence vs max member weight
TEMP_STALL = 4                     # gens without improvement -> hot moves


def panel_for_gen(gen):
    return [(SEED_BASE + gen * 97 + j, opp)
            for j in range(N_SEEDS) for opp in OPPS]


def evaluate(pool, members, games, gid_of_member):
    """members: [genome,...]; returns (gid -> rec, [per-game rows])."""
    tasks = []
    seen = set()
    for g in members:
        gid = gid_of(g)
        if gid in seen:
            continue
        seen.add(gid)
        try:
            bp = compile_genome(g)             # validity gate
        except Exception as e:
            print(f"  INVALID genome {gid}: {e!r}"[:140], flush=True)
            continue
        tasks.append((gid, json.dumps(bp), games))
    out = {}
    rows_all = []
    if tasks:
        for rows in pool.map(_eval_star, tasks):
            rows_all.extend(rows)
            for r in rows:
                if "margin" not in r:
                    continue
                s = out.setdefault(r["gid"], dict(margin=0.0, wins=0.0,
                                                  n=0, banks=[], cerr=0))
                s["margin"] += r["margin"]
                s["wins"] += r["win"]
                s["n"] += 1
                s["banks"].append(round(r["r0"]))
                s["cerr"] += r.get("cerr", 0)
    return out, rows_all


def _eval_star(task):
    import worker
    return worker.eval_member(task)


def score(rec):
    return rec["margin"] / max(1, rec["n"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=2.0)
    ap.add_argument("--out", default=str(Path(__file__).parent
                                         / "results" / "run1"))
    ap.add_argument("--workers", type=int, default=5)
    ap.add_argument("--seed", type=int, default=20260928)
    ap.add_argument("--anchor", default="dsm",
                    choices=["dsm", "envelope", "boundmix", "intensity"])
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    os.nice(10)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    anchor = dsm_genome() if args.anchor == "dsm" \
        else make_species(args.anchor, rng)
    anchor = normalize(anchor)
    assert is_valid(anchor), "anchor genome failed validity check"

    best_ever = {"genome": copy.deepcopy(anchor), "confirm": None}
    gen = 0
    stall = 0
    hist = []

    state_path = out / "state.json"
    if args.resume and state_path.exists():
        st = json.loads(state_path.read_text())
        anchor = st["anchor"]
        best_ever = st["best_ever"]
        gen = st["gen"]
        stall = st.get("stall", 0)
        hist = st.get("hist", [])
        print(f"RESUME gen {gen} best confirm {best_ever['confirm']}",
              flush=True)

    ctx = mp.get_context("fork")
    pool = ProcessPoolExecutor(max_workers=args.workers,
                               mp_context=ctx,
                               initializer=_init_w)
    log_f = open(out / "gen.jsonl", "a")
    games_f = open(out / "games.jsonl", "a")
    t_start = time.time()
    t_end = t_start + args.hours * 3600

    def confirm(genome, seeds=CONFIRM_SEEDS):
        recs, rows = evaluate(pool, [genome],
                              [(s, o) for s in seeds for o in OPPS],
                              gid_of)
        for r in rows:
            r2 = dict(r)
            r2["gen"] = -1
            games_f.write(json.dumps(r2) + "\n")
        games_f.flush()
        return recs.get(gid_of(genome), dict(margin=0, wins=0, n=0,
                                            banks=[], cerr=0))

    try:
        while time.time() < t_end:
            gen += 1
            t0 = time.time()
            seeds = panel_for_gen(gen)
            moves = (2, 5) if stall >= TEMP_STALL else (1, 2)

            # ---- group = anchor + mutants + best_ever cross + immigrant
            group = [anchor]
            for _ in range(GROUP_MUTANTS):
                group.append(mutate(anchor, rng, moves=moves))
            if best_ever["genome"] is not None and \
                    gid_of(best_ever["genome"]) != gid_of(anchor):
                group.append(mutate(
                    crossover(anchor, best_ever["genome"], rng),
                    rng, moves=(1, 2)))
            group.append(make_species("random", rng))   # immigrant

            group = [normalize(g) for g in group]
            recs, rows = evaluate(pool, group, seeds, gid_of)
            for r in rows:
                r2 = dict(r)
                r2["gen"] = gen
                games_f.write(json.dumps(r2) + "\n")
            games_f.flush()

            # ---- rewards + group baseline (GRPO advantage)
            members = [g for g in group if gid_of(g) in recs]
            R = {gid_of(g): score(recs[gid_of(g)]) for g in members}
            base = sum(R.values()) / max(1, len(R))
            adv = {gid: R[gid] - base for gid in R}

            # log members
            for g in members:
                gid = gid_of(g)
                rec = recs[gid]
                log_f.write(json.dumps(dict(
                    gen=gen, gid=gid, anchor=(g is group[0]),
                    score=R[gid], adv=adv[gid], wins=rec["wins"],
                    n=rec["n"], bank=sum(rec["banks"]) / max(1, len(rec["banks"])),
                    cerr=rec["cerr"])) + "\n")
            log_f.flush()

            # ---- advantage-weighted block vote -> next anchor
            order = [gid_of(g) for g in members]
            w = [max(0.0, adv.get(gid, 0.0)) for gid in order]
            wmax = max(w) if w else 0.0
            if order and order[0] == gid_of(anchor):
                w[0] = max(w[0], STICKY * wmax)
            if wmax <= 0:
                # nobody above the group mean except ties: keep anchor,
                # count a stall
                stall += 1
                child = anchor
            else:
                child = block_vote(anchor, members, w, rng)
            improved = gid_of(child) != gid_of(anchor)

            # track best by TRAINING score (paired panel), confirm later
            cur = max(members, key=lambda g: R.get(gid_of(g), -1e18))
            cur_gid = gid_of(cur)
            hist.append(dict(gen=gen, anchor_score=R.get(gid_of(anchor)),
                             top=R.get(cur_gid, 0.0), top_gid=cur_gid))
            anc = hist[-1]["anchor_score"]
            hist = hist[-40:]

            anchor_score = R.get(gid_of(anchor), 0.0)
            anchor = child
            stall = 0 if improved else stall + 1

            # ---- periodic confirm for best-ever tracking
            if gen % 8 == 0 or gen == 1:
                c = confirm(anchor, CONFIRM_SEEDS[:8])
                cs = score(c)
                if best_ever["confirm"] is None or \
                        cs > best_ever["confirm"]:
                    best_ever = {"genome": copy.deepcopy(anchor),
                                 "confirm": cs}
                print(f"  confirm: anchor {cs:,.0f}  "
                      f"best {best_ever['confirm']:,.0f}", flush=True)

            top_line = max(R.values()) if R else 0.0
            print(f"gen {gen:3d}  anchor {anc:9,.0f}  top {top_line:9,.0f}  "
                  f"mean {base:9,.0f}  stall {stall}  moves {moves}  "
                  f"{time.time()-t0:.0f}s", flush=True)
            state_path.write_text(json.dumps(dict(
                gen=gen, anchor=anchor, best_ever=best_ever,
                stall=stall, hist=hist), default=str))
    finally:
        # ---- final confirm: anchor + best_ever on the full 20-seed panel
        finals = {}
        for tag, g in (("anchor", anchor),
                       ("best_ever", best_ever["genome"]),
                       ("dsm_seed", dsm_genome())):
            try:
                rec = confirm(g, CONFIRM_SEEDS)
                finals[tag] = dict(genome=normalize(g),
                                   margin=score(rec),
                                   wins=rec["wins"], n=rec["n"],
                                   bank=(sum(rec["banks"])
                                         / max(1, len(rec["banks"]))),
                                   cerr=rec.get("cerr"))
            except Exception as e:
                finals[tag] = dict(err=repr(e)[:200])
        (out / "best.json").write_text(json.dumps(
            dict(finals=finals, gens=gen, args=vars(args)),
            indent=1, default=str))
        log_f.close()
        games_f.close()
        pool.shutdown(wait=True)
        print("\n=== FINAL ===")
        for tag, f in finals.items():
            print(f"  {tag:10s} margin {f.get('margin', 0):>10,.0f}  "
                  f"wins {f.get('wins', 0):>5.1f}/{f.get('n', 0)}  "
                  f"bank {f.get('bank', 0):>9,.0f}  cerr {f.get('cerr')}")


def _init_w():
    import worker
    worker.init_worker()


if __name__ == "__main__":
    main()
