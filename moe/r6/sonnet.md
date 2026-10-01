# sonnet.md — r6 round 1: red team + synthesis

Scope note: round 1 is parallel — `opus.md`, `opusb.md`, `astra.md` did not exist yet when this was
written (checked `moe/r6/build/{opus,opusb,astra}/`, all empty except opusb's `count.py`). So "which
decoded differences are plausibly causal" below leans on the **existing** r4/r5 decode (HANDOFF
09-26d, `moe/r5/build/opus/options.json`), not a fresh top-20 read, plus one fresh check I ran myself
(§3). I'll re-read opus/opusb/astra's files in the thread round and update.

## 1. Which decoded differences are plausibly causal

The r4/r5 decode already gives one family-vs-C1 macro delta table (`opus.md` r5 §1, `options.json`):
tomato seeds 16.8 vs 1.5, geese 6.2 vs 2.7, cows 9.0 vs 7.1, carrot 60 vs 45, SE 77% vs 5%, C1 idle
cash $15-20k at d11-14 vs family $3-14k. The obvious read is "family wins because it plants/herds/
expands more." **That read is refuted by r5's own experiments**, not by me:

- Grafting the SE package (O1) onto C1's executor: sheep −$14.6k, cow −$16.9k, goose −$9.2k/g,
  oracle ceiling +$220/g vs a +$1k bar. 0-1/40 arms positive.
- Grafting herd targets (O2): same arm, same failure — cow arm IS O2's herd, corr with milk shops −0.38.
- Grafting the tomato/SE package (O3, V219): selector clears (r 0.965) but the *ceiling* doesn't
  (+$109/g margin); C1's own CXTB gate is already right in 58/64 worlds.
- Mechanism (opusb 22:40, opus 23:19): **C1's labour is not idle — 9-12 hires/day, wool at the $1
  floor, extra milk cannibalises its own.** The family's macro only pays with the family's *executor*.

So the causal variable is very likely **unit-level labour allocation** (how tile-ops are assigned to
farmer+hands without collision), not the resource mix. This reads on independently: Georgy Mamarin's
toy carrot-bot test (`discussions.md` ~9481, new tail) found 12 tiles/3 hands sharing one job list at
**−$601±320** vs the *same* 12 tiles/3 hands each owning a slice at **+$3,871±990** — an ~$4.5k swing
from allocation alone, no macro change. That is exactly the axis r5 could not touch: every
whole-game/day-splice replanner that would let us rewrite C1's unit-ops is dead (TS 3/32, NN 0/8, DS
0/20, router 0.24, raw tapes 8/125). **We cannot address the causal variable by 09-30.** What's left is
whatever doesn't require rewriting the executor — see §3.

## 2. Forum claims (partial sample of discussions.md; astra owns the full ledger)

`discussions.md` grew from 8,736 to **10,022 lines** while I was reading it (new tail, unmarked as a
"Version - 6" header but dated "today/yesterday/a few days ago" against 2026-09-27 — flag this for
astra, the version boundary grep (`^Version`) won't catch it).

| claim | source | status |
|---|---|---|
| Team score = better of two submissions; ties = half-win each side | Addison Howard (Kaggle staff), discussions.md ~4335 | **CONFIRMED**, matches our "slot 2 = free hedge" practice (HANDOFF 09-26f) |
| "Are top policies exploiting the 1-unit-at-a-time concurrent market queue to force opponent sells to the $1 floor?" | discussions.md:3234 | **Untested by name, but we already built and shelved the exact mechanism** — see §3 |
| "A mirror matchup is decided by sale timing... wool 226→31→1 when both dumped at once" (days 17-25) | Yujin Cha, discussions.md ~8969 | Independent corroboration of §3's mechanism and of our own "≥2400 losses are band/WLV mirrors, whiskers −$98/−$338/−$381" (HANDOFF 09-26d) |
| Splitting a bulk endgame SELL into per-turn slices made things worse (−$1k vs two lineages) | Yujin Cha, discussions.md ~8974 | Consistent with our Falsified #14 (elastic sell-to-stock, −$11.8k) — different manipulation, same direction. No action. |
| SE/4th-quadrant only pays with per-hand tile ownership, not raw land | Georgy Mamarin, discussions.md ~9479 | Consistent with §1; already subsumed by O1's kill (labour-saturation mechanism), not a new lever |
| RL plateaus against strong players even after ~1M games / 90% vs public scripts | dzjiann, discussions.md ~8743, ~8993 (posted twice) | Consistent with our own tape/BC non-generalization findings (Falsified #18, TS/NN/DS kills). No action — corroboration, not a new idea. |
| hybrid2965 (public notebook) plays a different opening depending on the opponent's turn-0 orders | Yujin Cha, discussions.md ~8966 | Same name as our own evicted `hyb2965` candidate (built from "2965 Master Hybrid Engine"), but hyb2965 is out of our live pair and not part of C1's lineage. **Low priority, flag only** — worth astra checking whether any surviving C1 layer traces to that notebook. |

## 3. Headline finding — a measured, dominant mechanism was shelved at the C1 pivot and never retested

`moe/opus/cand_brx2.py` / `frozen_brx2_v1.py` (frozen 2026-09-25 17:16, **before** C1 existed —
`subY_C1_predict2.py` appeared 2026-09-26 02:48) implements a wrapper: on any turn where the wrapped
agent emits ≥2 distinct-item SELL orders, it (a) tries every permutation of which SELL slot gets which
item/qty, scored by a per-item lockstep market sim against a predicted rival order (native vs a
"SIR"-sorted alternative), and (b) online-updates a log-odds of "rival plays native order" from the
surprise between predicted and realized cashflow each turn (`_brx2_predict`/`_brx2_agent`,
lines ~6965-7117).

**Measured result** (`moe/opus/gate_brx2_1000_50.log`, 800 games, 9 agents, seeds [1000:1050]): BRX2
mean win rate **0.844** across the pool, beating `LIVE_f55rec_V2` 0.99, `LIVE_sir_V1` 0.77, koshinm
0.65, melon 0.63, metav4 0.85 — the two agents that were *actually our live pair at the time* lost to
it badly. This is memorialized in `[[band-native-sell-order]]` (opponent's relative SELL order matches
its native list 88% of the time in the 2400-2900 band) but the memory's own verdict — "a whisker edge
(~+20-35 Elo), not a ceiling breaker" — was written for the *old* pool and **has never been re-checked
against C1 or C1R2**. Neither `moe/r4/THREAD.md` nor `moe/r5/THREAD.md` mentions "brx" (checked). The
"Known next levers" line in `AGENTS.md` (koshinm cell, reactive replanner) doesn't mention it either —
it fell out of scope exactly at the architecture pivot, not because it was tested and failed.

**I checked the one precondition myself before recommending it** (`moe/r6/build/sonnet/multisell_check.py`,
harness.py self-play, 3 seeds each, foreground, nice 10): both C1 and C1R2 batch ≥2 distinct-item SELL
orders on **6.8-7.6% of turns** (49-55 of 719 turns/game, max 4-6 simultaneous items). That's real
surface area, same order of magnitude as the old pool, and it concentrates on exactly the contested
multi-item turns Yujin Cha describes deciding mirror matchups. koshinm's own edge over our old live
pair (per `[[koshinm-mechanism]]`) is itself `sell_impact_reorder(alpha=0.25)` — a weaker, static
cousin of BRX2 — and BRX2 already beats koshinm 65% in the old pool, so porting BRX2 may retire
"the koshinm matchup cell" lever as a free byproduct rather than needing separate work.

**Why this could matter now specifically:** our own measured weakness is narrow losses to band/WLV
mirrors at ≥2400 (whiskers −$98/−$338/−$381, HANDOFF 09-26d) — small-margin, market-layer losses, not
macro losses. BRX2's mechanism is a pure market-layer wrapper; it does not touch unit-ops, so it
doesn't inherit the "grafting the family macro onto C1's executor loses money" failure mode from §1 —
it's orthogonal to the executor.

## 4. Ranked ways, with kill tests and hours

1. **Port BRX2 onto C1/C1R2, gate directly, then re-run vs koshinm** — highest priority, cheap,
   orthogonal to the dead executor-rewrite routes.
   - Build: replace `_sir_parent` with a call to C1's own `agent(obs, cfg)`; keep `_sir_price` /
     `_SIR_PARAMS` / the lockstep sim as engine-truth (verify they match AGENTS.md's price function,
     not sir-specific beliefs) — **1.5-2h**.
   - Gate C1+BRX2 vs bare C1, 60 paired seeds, harness.py (~0.8s/episode) — **1h**.
   - Replay-substitute (`[[replay-substitution-instrument]]`, open-loop, our seat swapped in) into the
     recorded ≥2400 band/WLV loss games to see if the specific whisker losses flip — **1.5-2h**.
   - Re-run vs decoded koshinm (`rivals/koshinm_kaggriculture-local-best-2026-09-21/_entry.py`),
     40-60 seeds — **1h** (reuses the build).
   - **Kill test:** paired margin ≤ $0/g vs C1 on 60 seeds, OR no improvement on the recorded whisker
     losses. Gate hygiene: this round's own testing convention (`[[v92-ep-holdout-trap]]`) — don't set
     `_V92_EP` globally in the gate script, or C1's own P-library gets silently disarmed on odd
     episode ids and the comparison is biased against the *baseline*, not the candidate.
   - **Total: 4-6h build/measure.**

2. **Methodology fix, not a lever:** don't promote a BRX2-scale (whisker) change on the RR map alone.
   `moe/r4/build/opus/PREREG_rr_retro.txt` shows the RR map's own pre-registered pass was **marginal at
   both bars** (Spearman exactly 0.70 vs the ≥0.70 bar, 2/10 pairwise disagreements vs the ≤2 bar), its
   5 anchors span live ratings ~1800-2100, and it explicitly states "closed-loop-vs-lineage may rank
   band-targeted candidates (**not top-10 claims**)." A ±20-35 Elo effect (BRX2's old-pool size) sits
   inside that instrument's own noise. Use replay-substitution (in-band, direct) as the primary gate
   for whisker-sized levers; keep the RR map for macro-scale go/no-go calls. **0h extra** — fold into
   item 1's kill test design.

3. **Sanity-check that C1R2 didn't change the O1-O3 kill's premise.** r5's kills (O1/O2/O3) were
   measured against `subY_C1_predict2.py`, not `subZ_C1R2.py` (submitted 09-27, after the kills).
   `screen2_C1noV233.log`-style evidence suggests C1R2 is a close variant (RR map 2152 vs C1's 2076,
   overlapping CIs), so this is low-expectation, but it's a 1-hour checkbox against re-litigating a
   stale kill: confirm C1R2's hires/day (bar: 9-12/day, matching opusb's C1 measurement) and idle-tile
   fraction haven't moved enough to reopen O1. **1h, low priority.**

4. **Do not re-open, for the record (red-team confirms these are correctly dead):** O1/O2 macro grafts
   (labour-saturation mechanism, independently corroborated by Georgy Mamarin's forum toy example,
   §1); O3/V219 scale-up (Fibonacci labour arithmetic already closes it, opus 09-27a "Fibonacci labour
   closes scale-up"); tape/router/TS/NN/DS replanners (all measured dead, §1); elastic/split sell
   quantities (Falsified #14, corroborated by Yujin Cha's independent negative result). None of these
   need a fresh test before 09-30.

## 5. P(bronze), P(silver), P(top-10) for the final pair under this plan

Given: current mapped position C1 ~2076 [2040,2145], C1R2 ~2152 [2021,2294]; bronze ~2210, silver
~2410, #10 2884 (r6 BRIEF state); team score = best-of-two (confirmed §2); BRX2-on-C1 is a whisker-size
lever (+20-35 Elo old-pool estimate, unverified on C1) aimed at exactly the band where our recorded
losses sit; every macro/executor route to a bigger jump is measured dead.

- **P(bronze) ≈ 0.55** — C1R2's CI already reaches into bronze range; a verified BRX2 whisker edge
  pushes the point estimate further in, but the RR map itself is a marginal-pass instrument, so this
  isn't a high-confidence number either way.
- **P(silver) ≈ 0.12** — would need something beyond a whisker edge; nothing on the table clears that
  bar today.
- **P(top-10) ≈ 0.03** — requires the executor-architecture rebuild that r5 closed off; unchanged by
  anything in this file.
