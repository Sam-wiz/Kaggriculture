"""Build a shop-matched tape router from one top-10 team's own library.

Mined tapes from different players share nothing, so they cannot be switched between mid-game --
splicing incoherent tapes destroys the farm. But tapes from a single team often DO share a long
prefix, because that team is itself running a tape router. Measured across 2026-09-08:

    自己找差距      62 tapes, every pair identical for at least 150 turns
    Mengfei Li     55 tapes, at least 168
    Atakan Aldemir 32 tapes, at least 184
    SpaTaro        93 tapes, 0 -- reactive, no shared prefix, unusable this way

So a router over one such library is sound as long as it commits before that team's own divergence
point. Shops unlock on days 3 and 6, so at turn 144 exactly two are known -- which is both the last
safe dawn boundary for 自己找差距 and exactly the information their own router was branching on.

The rule here is nearest-neighbour on that pair: run the shared prefix to turn 144, compare the two
unlocked shops against what each tape saw, and commit to the best match (ties broken by the bank
that tape actually earned). No mid-game splice, so no coherence risk beyond the measured prefix.
"""
import collections
import gzip
import json
import os
import sys

SRC = "data/tapes/tapes_2026-09-08.jsonl.gz"


def load(team=None):
    out = []
    for line in gzip.open(SRC, "rt"):
        r = json.loads(line)
        if team is None or r["team"] == team:
            out.append(r)
    return out


def min_divergence(tapes):
    lo = 10 ** 9
    for i in range(len(tapes)):
        for j in range(i + 1, len(tapes)):
            a, b = tapes[i]["tape"], tapes[j]["tape"]
            d = next((t for t in range(min(len(a), len(b))) if a[t] != b[t]), min(len(a), len(b)))
            lo = min(lo, d)
            if lo == 0:
                return 0
    return lo


def pick_library(team, switch, max_tapes):
    """One representative tape per distinct (first-two-shops) draw, best bank wins."""
    tapes = load(team)
    best = {}
    for r in tapes:
        key = tuple(r["shops"][:2])
        if len(key) < 2:
            continue
        if key not in best or r["bank"] > best[key]["bank"]:
            best[key] = r
    lib = sorted(best.values(), key=lambda r: -r["bank"])[:max_tapes]
    return tapes, lib


if __name__ == "__main__":
    team = sys.argv[1] if len(sys.argv) > 1 else "自己找差距"
    switch = int(sys.argv[2]) if len(sys.argv) > 2 else 144
    maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 16
    tapes, lib = pick_library(team, switch, maxn)
    print(f"team {team}: {len(tapes)} tapes")
    d = min_divergence(tapes)
    print(f"minimum pairwise divergence: turn {d}  -> switching at {switch} is "
          f"{'SAFE' if switch < d else 'UNSAFE'}")
    draws = collections.Counter(tuple(r["shops"][:2]) for r in tapes)
    print(f"distinct first-two-shop draws seen: {len(draws)}")
    print(f"\nlibrary ({len(lib)} tapes, one per draw, best bank):")
    print(f"{'#':>3}{'first two shops':<44}{'bank':>10}{'seed':>12}")
    for i, r in enumerate(lib):
        print(f"{i:>3}{' + '.join(r['shops'][:2]):<44}{r['bank']:>10,.0f}{r['seed']:>12}")
    # verify the chosen library really is prefix-identical up to the switch
    bad = 0
    for i in range(len(lib)):
        for j in range(i + 1, len(lib)):
            if lib[i]["tape"][:switch] != lib[j]["tape"][:switch]:
                bad += 1
    print(f"\nlibrary pairs disagreeing before turn {switch}: {bad} (must be 0)")
    os.makedirs("data/lib", exist_ok=True)
    out = "data/lib/%s_%d.json" % (team.encode('ascii', 'replace').decode()[:12].replace('?', 'x'),
                                   switch)
    json.dump(dict(team=team, switch=switch,
                   tapes=[r["tape"] for r in lib],
                   draws=[r["shops"][:2] for r in lib],
                   banks=[r["bank"] for r in lib]), open(out, "w"))
    print(f"wrote {out} ({os.path.getsize(out)/1e6:.1f} MB)")
