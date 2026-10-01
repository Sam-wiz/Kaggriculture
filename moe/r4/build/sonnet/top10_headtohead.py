"""
Q1/Q2 evidence: direct head-to-head among the CURRENT top ~15-20 teams, from
mine/top10/*.json.gz (Kaggle's official daily top-episode dump, 2026-09-25),
cross-referenced against the freshest LB snapshot (moe/r3/lb_0926_0500.json,
2026-09-26 05:00 UTC). This is "what is recoverable from a replay" applied at
the coarsest level (teams, ratings, final banks) before any action-level
decoding -- deliberately cheap, and enough to answer "how tight is the top
tier" without burning the round on per-episode reverse engineering that
Opus's lane already owns in depth.
"""
import gzip, json, glob, statistics

LB_PATH = "moe/r3/lb_0926_0500.json"
TOP10_GLOB = "mine/top10/*.json.gz"


def main():
    lb = json.load(open(LB_PATH))
    rows = []
    for fp in sorted(glob.glob(TOP10_GLOB)):
        with gzip.open(fp) as f:
            d = json.load(f)
        t0, t1 = d["teams"]
        r0, r1 = d["rewards"]
        rows.append((d["episode_id"], t0, lb.get(t0), r0, t1, lb.get(t1), r1))

    print(f"{len(rows)} top-episode games loaded\n")
    for eid, t0, rt0, b0, t1, rt1, b1 in rows:
        win = t0 if b0 > b1 else (t1 if b1 > b0 else "TIE")
        print(f"{eid} | {t0:28s}({rt0}) {b0:8.0f}  vs  {t1:28s}({rt1}) {b1:8.0f}  -> {win}")

    margins = [abs(b0 - b1) for _, _, _, b0, _, _, b1 in rows]
    pct = [abs(b0 - b1) / min(b0, b1) * 100 for _, _, _, b0, _, _, b1 in rows]
    print(f"\nn={len(rows)} margin mean={statistics.mean(margins):.0f} "
          f"median={statistics.median(margins):.0f}")
    print(f"margin as % of loser bank: mean={statistics.mean(pct):.2f} "
          f"median={statistics.median(pct):.2f}")
    print(f"margin<2000: {sum(1 for m in margins if m<2000)}/{len(margins)}  "
          f"margin<5000: {sum(1 for m in margins if m<5000)}/{len(margins)}  "
          f"margin>20000: {sum(1 for m in margins if m>20000)}/{len(margins)}")


if __name__ == "__main__":
    main()
