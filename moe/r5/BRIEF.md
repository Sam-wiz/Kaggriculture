# MoE r5 — THE 3K MOONSHOT (slot 2). 2026-09-26 20:40 UTC. Upload target 09-30 ~08:00 UTC; hard stop 18:00.

Participants (xhigh): **opus** (architect), **opusb** (builder), **sonnet** (red team + instrument),
**luna** (gpt-6-luna critique), **sol** (gpt-6-sol judge, bounded), **codex astra/sol** join when the
cap lifts (~09-27 21:53 UTC). **claude-code** orchestrates, participates, holds credentials, uploads.
You cannot submit. <=2 workers each, nice 10. Write only under moe/r5/ (your .md) and moe/r5/build/<you>/.
Discussion happens in `moe/r5/THREAD.md` (same rules as moe/r4/THREAD.md).

## Why this is worth doing even though every r4 expert put 3k+ at <1%
- **Slot 2 is nearly free.** Team score = better of the two final agents (Kaggle staff). Slot 1 keeps the
  medal floor: C1 (`subY_C1_predict2.py`, RR-mapped ~2076-2088) or C1R2 (~2152 [2021,2294]). Slot 2 is
  hyb2965 (~1973), BELOW C1 — replacing it with a moonshot costs ~nothing if the moonshot flops.
- **A 3k agent cannot be validated live before the deadline** (it would meet top teams only after
  climbing; the final ranking is a post-deadline BT refit). So the upload bar for slot 2 is:
  (i) no crash / no timeouts in the official env, both seats; (ii) not worse than C1 closed-loop vs our
  lineage (RR anchors); (iii) the best available evidence that it plays at top-family level.

## What 3k agents do (decoded in r4 — read `moe/r4/opus.md`, `opusb.md`, THREAD.md)
- One private family dominates the top: step-1 `BUY_ANIMAL COW 1, BUY_PRODUCT WHEAT 5`; all 4 quadrants by
  step ~253 (land at ~149/219/253); hires 4,4,6,6,5,6,8,9,9,10,12,12,12… (~300/game); ~9 cows, 5 sheep,
  ~6 geese, ~21 strawberries, ~17 tomatoes and ~9 carrots by d21; cash-exact (dawn cash $1-800 d1-8).
- **Reactive, not a tape:** within-team unit-op identity 0.10-0.25; plans conditioned on the shop draw.
- Matched-world gap (our builds vs top pair, shops pinned): −$6.3k/seat; −$12.6k outside ICE_CREAM-first worlds.
- Their recorded tapes do NOT transfer (raw 8/125 vs C1; router 0.24): cash-leanness + shop re-rolls.
- Data: **1,773 top-vs-top games** in `mine/top10/` (09-23..25; `actions[t]` produced step t), plus
  `mine/top/` (1,725 older). Every replay reproduces to the dollar; exact per-tick state is recoverable.

## The question: what can we build in ~3.5 days that plays like the top family, reactively?
Candidate architectures (propose others; kill bad ones fast):
- **A. Macro-policy imitation + our executor.** Learn the top family's DAILY macro decisions (land, animal,
  seed/crop plantings, hires, sell policy) as a function of observable state (day, cash, shops, herd, tiles,
  market) from ~1,773 games × 2 seats × 30 days; execute with an existing executor (shepherd chassis units /
  r2 `exec3.py` scheduler). Risk: our from-scratch executors lost on efficiency (exec3 $35k vs V48 $96k).
- **B. Runtime planning.** At each dawn, simulate candidate macro plans forward with the engine and pick the
  best (opponent modelled as continuing its observed pattern). Must fit Kaggle's per-step time budget
  (measure it: actTimeout + remainingOverageTime 60 s) — Python engine speed is the constraint.
- **C. Chassis + macro corrections.** Keep C1's tape/executor; add reactive macro layers for the decoded
  gaps: 4th quadrant by ~day 10 when cash allows, geese to ~6, an earlier/larger tomato program with a replant
  cycle, fewer strawberries in glut worlds. Cheapest; ceiling unknown (structural ports failed before, 09-21).

## Instruments (this is where every previous round failed — MISTAKES C17/C18)
- RR map (`moe/r4/build/opus/rr.py`, `c1map.py`, `moe/r4/screen2.py`) retrodicts the LINEAGE band only.
- For top-level play we have no validated instrument. Candidates: matched-world economy vs the recorded top
  pair with shops pinned (`kagsim.Game(seed, shops=...)`) — failed retrodiction for ranking lineage builds
  (Spearman 0.03) but is the only top-directional measure; sonnet owns deciding what we can trust.

## Round 1 deliverable (timebox ~2.5 h, then the thread)
`moe/r5/<you>.md`: your architecture pick with evidence; a concrete build plan with hour estimates to a
submittable file by 09-30 06:00 UTC; the kill test at +12 h and +36 h; a prototype if you can.
opus = architecture + macro-policy extraction from the dump; opusb = build the chosen chassis/executor path
and measure the Kaggle time budget; sonnet = instrument + red team + the P(3k) honestly.
End with P(3k+ | fielded in slot 2), P(top-10 | fielded), and P(it beats C1 closed-loop).
