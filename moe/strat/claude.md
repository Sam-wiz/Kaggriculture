# Claude Code (Opus 5.5) — round 1 position, written before reading codex.md / opus.md

## 1. Diagnosis: why the ceiling is ~2.8k

Our agent is a public, plan-bound tape (pipe16 = V39 + nathanjacob layers). Three mechanisms
set its ceiling, in order of size:

1. **Clone saturation of the matchmaking band.** Near 2.6-2.8k, a large share of opponents run
   the same public tape or a close descendant. Opus build-expert's replay of 197 band games:
   identical wheat, herd, hires and land; 74/118 losses within $1k; median loss ~-$200. Against
   a clone we are a coin flip settled by market microstructure. pipe16 *peaked* at 2843 because
   it was fresh (few clones yet — 09-20e: 2 mirrors in its first 34 games) and decayed to 2787 as
   copies appeared. A public tape converges toward the centre of its own clone cluster.
2. **Private reactive agents above the cluster.** The top-11 emit a different buy signature per
   game; they win by production mix and sell timing, not by market tricks. Every attempt to port
   their structure onto our tape failed (HANDOFF 09-21 PM) because the tape commits a route at
   day ~6 and cannot re-plan.
3. **Our own regressions since 09-23 (probable, being tested).** Every build submitted from 09-23
   converged 1.8-2.3k; every build <=09-22 converged 2.4-2.8k. The f55rec files specifically went
   2552/2489 -> 1930/1793 when resubmitted with the reclaim layer. Codex build-expert found reclaim
   stalls sheep workers ~12 endgame turns. Field drift is the alternative; the exact-pipe16 live
   control (ref 56547613) decides it.

## 2. Ranked plan

| # | move | expected gain | conf. | days | 24h kill/confirm test |
|---|---|---|---|---|---|
| 1 | **Revert to the pre-09-23 stack** if the control converges >=2.5k: pipe16 (+clamp +prem) in slot 1, no reclaim/SIR | +500..+900 vs today's 1.9k (back to 2.6-2.8k) | 0.6 | 0 | the control itself |
| 2 | **Best-response SELL permutation vs clones** (Opus lane): rival keeps our native order 88% -> predict its list, simulate the turn, pick our permutation | whisker losses -> wins in clone games: if clone games are ~40% of band and go 0.45->0.65, +0.08 WR ~ **+55** | 0.35 | 1-2 | offline vs exact-clone opponents is valid HERE (the population is literally clones) — must also be neutral vs non-clones |
| 3 | **Endgame delivery fix** (Codex `cand_capture`) — only if the chosen base still carries reclaim; on a pre-09-23 base the stall may not exist | 0..+80 | 0.3 | 0.5 | check whether the stall occurs on pipe16-without-reclaim; if not, moot |
| 4 | **Freshness / uniqueness**: our modified private build cannot be cloned by others, so it avoids the tie band that public pipe16 falls into | small, but it is why private edits beat public copies live | 0.4 | 0 | compare clone-rate of our private builds vs public pipe16 in live eps |
| 5 | A reactive replanner (production mix, strawberry d2, ~10 cows) | the real +200-300 | 0.05 by 09-30 | >5 | — |

## 3. Slot policy
- Now: [sir_V2, exact pipe16]. Let pipe16 run >=60 games (~4-8h) before any decision.
- If control >=2.5k: next submission = best pre-09-23 build with a *different* chassis (subP2
  metav4+prem, 2602) replacing sir_V2 -> pair = two pre-regression lineages.
- Any candidate (moves 2/3) enters ONLY after beating the slot it replaces in a paired test that
  includes exact-clone opponents, and only once. **Freeze all submissions 09-28 00:00 UTC** so the
  final pair converges and accumulates games before the BT window.

## 4. Next 12 hours
Wait for the control; in parallel have the Opus build-expert finish the best-response permutation
and test it against exact clones of pipe16 AND against non-clones (neutrality), on pipe16 without
reclaim. Do not submit anything else until the control reads.

## 5. Strongest argument 3k+ is NOT reachable by 09-30
+200 over our best needs ~75-80% head-to-head vs the same field. The only measured large gains in
the project came from adopting newer public bases — and the public pool is frozen. Every overlay
since has been worth tens of Elo, not hundreds, and several were negative live. The top agents'
advantage is structural (reactive production and sell timing) and needs a replanner we cannot
build and validate in 5 days. So 3k+ is unlikely; the rational goal is P(top-10) via the best
converged pre-regression pair, plus variance from a distinct second slot. Top-10 needs ~2940,
~150 above our best-ever — plausible only if the post-deadline BT refit, run on fewer clone
mirrors, favours a private unique build more than the ladder did.

CONFIDENCE 3k+ by 09-30: 5%
CONFIDENCE top-10: 12%
