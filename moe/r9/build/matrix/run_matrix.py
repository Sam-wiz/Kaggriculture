"""MoE r9 lane `matrix` runner: pairwise episodes via harness.py, parallel.

Usage:
  .venv/bin/python moe/r9/build/matrix/run_matrix.py \
      --pairs "subAB_m30b.py:agents/v8hh.py,..." \
      --seeds 9300-9311 --workers 4 --out moe/r9/build/matrix/results.jsonl

Appends one JSON record per episode to --out (crash-safe, resumable-ish:
existing records for the same (a,b,seed,swapped) are skipped).
"""
import argparse, json, os, sys
from concurrent.futures import ProcessPoolExecutor, as_completed

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
os.chdir(ROOT)
sys.path.insert(0, ROOT)
import harness  # noqa: E402


def job(t):
    a, b, seed, swapped = t
    x, y = (b, a) if swapped else (a, b)
    try:
        r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    except Exception as e:  # noqa: BLE001
        return {"a": a, "b": b, "seed": seed, "swapped": swapped,
                "ra": None, "rb": None, "err": repr(e)[:200]}
    ra, rb = r["reward"]
    if r["status"][0] != "DONE":
        ra = None
    if r["status"][1] != "DONE":
        rb = None
    if swapped:
        ra, rb = rb, ra
    return {"a": a, "b": b, "seed": seed, "swapped": swapped,
            "ra": ra, "rb": rb,
            "status": r["status"], "errors": r["errors"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", required=True, help="comma-sep A:B file pairs")
    ap.add_argument("--seeds", required=True, help="e.g. 9300-9311 or 9300,9301")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    pairs = [tuple(p.split(":")) for p in args.pairs.split(",")]
    if "-" in args.seeds:
        lo, hi = args.seeds.split("-")
        seeds = list(range(int(lo), int(hi) + 1))
    else:
        seeds = [int(s) for s in args.seeds.split(",")]

    done = set()
    if os.path.exists(args.out):
        for line in open(args.out):
            try:
                r = json.loads(line)
                done.add((r["a"], r["b"], r["seed"], r["swapped"]))
            except Exception:  # noqa: BLE001
                pass

    jobs = []
    for a, b in pairs:
        for s in seeds:
            for sw in (False, True):
                if (a, b, s, sw) not in done:
                    jobs.append((a, b, s, sw))

    print(f"{len(jobs)} episodes to run ({len(done)} already done), workers={args.workers}", flush=True)
    fout = open(args.out, "a", buffering=1)
    n = 0
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(job, t): t for t in jobs}
        for fut in as_completed(futs):
            rec = fut.result()
            fout.write(json.dumps(rec) + "\n")
            n += 1
            if n % 8 == 0 or n == len(jobs):
                print(f"  {n}/{len(jobs)}", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
