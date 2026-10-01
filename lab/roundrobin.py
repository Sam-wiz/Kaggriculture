"""Round-robin the candidates that beat our base, to pick the single strongest.

sobameshi's study (discussions.md V2) found the public field is a **transitive ladder**: across 14
implementations on 96 fresh seeds there was no intransitive triple, the newer implementation beat
the older in 86 of 91 chronological pairs, and the ordering tracked average final money. If that
holds here, a round-robin will produce a clean total order and we simply take the top of it -- no
counter-picking, no hedging against a rock-paper-scissors cycle.

Worth testing rather than assuming: if we DO find an intransitive triple among our candidates, that
is a finding in itself and changes how the final two slots should be chosen.
"""
import itertools
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

AGENTS = [
    ("pipe15", "rivals/nathanjacob_kaggriculture-pipe15-two-layers/main.py"),
    ("pipe16", "rivals/nathanjacob_kaggriculture-pipe16-idle-workers/main.py"),
    ("metav4-v13", "rivals/thomastschinkel_the-metav4-farm-submission-v13/main.py"),
    ("gods-mode", "rivals/leoprovorov_god-s-mode-hacked-stores/gods_mode_hacked_stores/base_agent.py"),
    ("subJ_2945", "subJ_2945.py"),
]


def _job(a):
    la, pa, lb, pb, seed, swap = a
    x, y = (pb, pa) if swap else (pa, pb)
    try:
        r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    except Exception:
        return None
    p, q = (r["reward"][::-1] if swap else r["reward"])
    return (la, lb, 1 if p > q else (0.5 if p == q else 0), p - q)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    idx = json.load(open("data/seedindex_900000_1400.json"))
    seeds = [r["seed"] for r in idx][200:200 + n]
    jobs = []
    for (la, pa), (lb, pb) in itertools.combinations(AGENTS, 2):
        for s in seeds:
            for sw in (0, 1):
                jobs.append((la, pa, lb, pb, s, sw))
    print(f"{len(jobs)} games, {len(AGENTS)} agents, {n} seeds both seats", flush=True)
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = [r for r in ex.map(_job, jobs, chunksize=4) if r]

    names = [l for l, _ in AGENTS]
    wr = {}
    for la, lb, w, m in res:
        wr.setdefault((la, lb), []).append(w)
    print(f"\nrow beats column (win rate):\n")
    print(f"{'':<12}" + "".join(f"{n2:>12}" for n2 in names))
    score = {n2: [] for n2 in names}
    for a in names:
        row = f"{a:<12}"
        for b in names:
            if a == b:
                row += f"{'-':>12}"
                continue
            v = wr.get((a, b))
            if v is None:
                v = [1 - x for x in wr.get((b, a), [])]
            if not v:
                row += f"{'?':>12}"
                continue
            m = statistics.mean(v)
            score[a].append(m)
            row += f"{m:>12.3f}"
        print(row)
    print(f"\n{'agent':<14}{'mean win rate vs field':>24}")
    for a, v in sorted(score.items(), key=lambda kv: -statistics.mean(kv[1]) if kv[1] else 0):
        if v:
            print(f"{a:<14}{statistics.mean(v):>24.3f}")

    # transitivity check
    order = sorted(names, key=lambda a: -statistics.mean(score[a]) if score[a] else 0)
    bad = []
    for a, b, c in itertools.permutations(order, 3):
        def beats(x, y):
            v = wr.get((x, y))
            if v is None:
                v = [1 - t for t in wr.get((y, x), [])]
            return statistics.mean(v) > 0.5 if v else None
        if beats(a, b) and beats(b, c) and beats(c, a):
            bad.append((a, b, c))
    print(f"\nintransitive triples: {len(bad)}" + (f"  e.g. {bad[0]}" if bad else "  (clean ladder)"))
