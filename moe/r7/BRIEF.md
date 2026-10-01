# MoE r7 — the OTHER submission: pick the hedge slot for the final pair. 2026-09-27 ~23:00 UTC. Deadline 09-30 23:59 UTC (last upload ~18:00).

Orchestrator: **devin**. Participants: **devin** (orchestrator + lanes), **devin-f** (forensics
subagent lane), **devin-q** (quant lane), **astra/codex** (may join — daemon alive; GH screen data
already in `moe/r6/build/resume/`), **opus**, **opusb**, **sonnet** (rate-limited until ~09-28
21:00 UTC; lanes reserved). You cannot submit. <=2 workers each, nice 10.
Write only `moe/r7/<you>.md`, `moe/r7/build/<you>/`, and posts appended to `moe/r7/THREAD.md`.
r6 files stay append-only; r7 references them but does not edit.

## The scoring fact that defines this round (HANDOFF.md 09-21a, Addison Howard verbatim)
**"The team score is based on the better of its two submissions (a team can't occupy two ranks).
The second slot can be viewed as a hedge with no downside."** Ties = half wins.
=> Slot-B's ONLY job is to exceed slot-A's realized rating in the runs where slot-A lands low
(noise ~±200 documented; chassis-collapse = the tail we actually fear). Downside is impossible.
The slot-B pick maximizes E[max(A, B)], NOT E[B]. Different-class beats strong-same-class.

## State (from r6 close-out)
- Staged slot-A: **M30B** `moe/r6/build/devin/harvest_m30_brx2.py` — RR map **2402 [2192,2562]**,
  held-out validated, preflight DONE. Upload blocked by user rule until live pair converges
  (Harvest ~1883, C1R2 ~1714 @~22:20, still climbing; convergence ~09-29).
- After M30B uploads: pair = [Harvest, M30B]. NEXT upload evicts Harvest => slot-B fills it.
- r34 class: v8 maps 2150, beats our chassis ~65% H2H — only different-class agent found that
  beats the monoculture. The fish's live ~2798 build is a private descendant; public files are not
  it. v8's failure = seed-clustered endgame fade (~25% of map draws).
- Codex's `github.jsonl` prescreen: 21 paths, only v8 advanced; 75 legacy load failures remain
  unevaluated (`moe/r6/build/resume/unevaluated_github.json`) — NOT proven weak.
- Top-family class exists ~2800-3050 (DECEM/DSM/Boey core + fish's private r34 build).
  Everything we've ever fielded is shepherd-lineage — monoculture risk is real.

## The asks
1. **Rank slot-B candidates** under E[max(M30B, X)]: current list = v8 (r34 public best), a
   second M30B (pure noise hedge), hyb2965 (1885, same-family), plus whatever the GH remainder /
   new research surfaces. For each: mapped rating, loss-correlation vs M30B on shared seeds,
   class difference, license status.
2. **Can slot-B be BUILT better than v8?** Options: (a) graft our BRX2/market layers onto an
   r34-chassis; (b) fix v8's endgame fade (its only measured weakness — leads then bleeds days
   17-28 on ~25% of draws); (c) a different different-class artifact from the GH remainder.
3. **Keep pushing slot-A?** Anything left that beats M30B on the map is still welcome —
   pre-registered gate stands (point > 2402, lb > 2192 to replace the staged candidate now).
4. **Debate live** in `moe/r7/THREAD.md`: reply by name, evidence with paths + numbers, <=300
   words, end with **Next action (<owner>):**.

## Pre-registered slot-B gate (proposed — debate in thread)
Candidate X advances to the staged slot-B if it maximizes E[max(M30B, X)] by the agreed model.
Default model until challenged: R_X ~ mapped rating + N(0,150) sampling noise + chassis-collapse
scenario mass estimated from X's loss-correlation with M30B on the 20 map seeds + anchors.
License/attribution must be clear before staging. **NO submission before user lifts the hold.**

## Lane starters (round 1 = your file; then thread rounds)
- **devin:** this brief + thread seed + slot-B screen of the r34 family versions (v4-v8 all map)
  — which r34 artifact is least-correlated yet strongest?
- **devin-f (subagent):** fish-tape forensics — can the fish's late-game mechanism be identified
  from ~200 tapes closely enough to estimate whether v8+fix reaches it? Output: mechanism spec,
  not code.
- **devin-q (subagent):** E[max(A,B)] quant model on the seed-level loss data we hold —
  correlation structure of v8/H/C1R2/M30B losses across seeds, realized hedge value.
- **astra (if in):** the 75 unevaluated GH load-failures — recover deps, screen for other
  different-class agents strong enough for slot-B.
- **opus/sonnet (when back):** does the decode say what fixes the r34-class endgame? Fish loses
  0.1-0.5 to the elite — is that also reachable cheaply?
