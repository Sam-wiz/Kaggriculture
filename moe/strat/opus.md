# Strategy MoE — Opus answer (2026-09-25, ~10:15 UTC; deadline 09-30 23:59 UTC = ~134 h)

**Short answer.** Nothing I can find gets us to 3k+ by 09-30, and top-10 is a long shot (~2%). Our
ceiling comes from the field: we are one member of a crowd running the same farm plan. It is not a
layer we can fix. On a fixed opponent-rating scale, our implied strength fell smoothly by ~300 from
09-20 to 09-24. Over the same days, margins against same-rated opponents collapsed from about
+$1.5k to ~$0, while our own bank did not fall. That points to "field drift", not a regression in
our code. Two moves could still produce a jump of +250 or more:

- **(a)** the pipe16 control reveals a live regression after all. I put this at ~20%.
- **(b)** a public kernel published in the last ~60 h before the lock beats our builds. We never
  pulled that window.

Every other lever is worth +30-80, which is too small to matter for a flat top-10 prize when we are
~500 short. So the week should be: read the control correctly, measure what the field actually
runs, pick the final pair on that basis, and stop churning.

---

## 0. Evidence I produced for this answer (reproducible; scratch scripts were in /tmp)

| check | method | result |
|---|---|---|
| Leaderboard drift | `data/lb.json` (09-22 19:20 UTC) vs `live_eps/lb_now.json` (09-24 20:35 UTC) | see E1 |
| Per-build strength | 742 replays (`live_eps/replays`, via `own.json`) + 91 pipe16 09-20 episodes (`data/ep_pipe16.jsonl`); fit each build's rating by maximum likelihood (Elo-400) against opponents' ratings **frozen at one snapshot** | see E2 |
| Opponent bands | Same games, grouped by the opponent's 09-22 rating | see E3 |
| Clone identity | Share of turns where the opponent's farmer+hands ops equal ours (market ops excluded); up to 25 replays per build, 75 for pipe16 | see E4 |
| Public-kernel coverage | mtimes under `rivals*/`; `data/kernels.json` | Last pull **09-21 ~10:00 UTC**. Nothing published between 09-21 10:00 and the 09-23 23:59 lock was pulled or screened |

Sanity check on the fit: when the snapshot is taken at the same time as the games, the fitted
rating matches the displayed one. L96-V1 fits 2239 on the 09-24 snapshot against a display of
~2216-2225. The method is therefore sound, and it does not depend on the order games were played.

## 1. Diagnosis — why the ceiling is ~2.8k, and why the post-09-23 builds read ~2.0-2.3k

**E1 — the whole board deflated, and one block of teams collapsed.** Between the two snapshots:

- **Rank deflation:** rank 10 went 2977→2930, rank 100 2758→2689, rank 300 2646→2568, rank 1000
  2375→2296 — a uniform −50..−80.
- **A distinct block fell further:** ~320 teams rated 2200-2600 on 09-22 dropped **400-600** in 49 h.
  The histogram of changes has a separate mode at −400..−500, not a smeared tail.
- **Public-lineage authors fell too:** Nathan Jacob 2567→2176, KoshinM 2318→2041, ToastUz −279,
  jojo −260.
- **The top barely moved:** −50..−200.
- **Only 3 teams are ≥3000** (DSM 3083, DECEM 3040, Vadim 3001). 3k+ means top-3, not top-5.

**E2 — our strength declined smoothly with submission date, not in one step at 09-23.**
Ratings below are fitted on the 09-22 snapshot scale, with 90% bootstrap intervals.

| build (submitted) | games | fitted rating | 90% CI |
|---|---|---|---|
| pipe16 (09-20) | 88 | **2658** | 2580-2756 |
| f55rec-V2 (09-22, no reclaim) | 109 | 2589 | 2527-2649 |
| f55rec-V1 (09-22) | 103 | 2536 | 2471-2606 |
| sir-V2 (09-23) | 84 | 2470 | 2396-2552 |
| sir-V1 (09-23) | 90 | 2413 | 2286-2557 |
| sirxP-V1 (09-23) | 76 | 2346 | 2242-2447 |
| L96-V1 (09-23/24) | 184 | 2341 | 2271-2405 |
| sirxP-V2 (09-23/24) | 149 | 2267 | 2190-2328 |

- **Same-day pairs differ by ≤80:** f55rec V1/V2, sirxP V1/V2, L96 V1/V2. The differences between
  periods are ~300. Adding a layer shows up as a small effect; the passage of time shows up as a
  large one.
- **pipe16's displayed 2787 was a freshness overshoot.** Its fitted strength is 2658, so even at its
  best it was **~320 below the 09-22 top-10 cutoff**. Closing that needs ~86% head-to-head against
  the same field.
- **sir-V1's "0.88 band profile" (09-25b) is not evidence of strength.** The median 09-22 rating of
  its opponents was **1770**; it was retired mid-climb while still playing weak teams. This is the
  MISTAKES C6 trap: a record without conditioning on opponent strength. Fitted, sir-V1 is middling.

**E3 — against opponents of the same 09-22 rating, margins collapsed while our bank held.**

| opponent band (09-22) | build | games | win rate | median margin | our median bank | opponent median bank |
|---|---|---|---|---|---|---|
| 2300-2500 | pipe16 (09-20) | 13 | 0.81 | **+1,473** | 87.8k | **79.8k** |
| 2300-2500 | sir-V2 (09-23) | 38 | 0.58 | +140 | 95.7k | 95.8k |
| 2300-2500 | sirxP-V2 (09-23/24) | 46 | 0.41 | −200 | 97.8k | 99.3k |
| 2300-2500 | L96-V1 (09-23/24) | 44 | 0.48 | −24 | 100.2k | **102.3k** |
| ≥2700 | pipe16 (09-20) | 24 | **0.42** | −516 | | |
| ≥2700 | all post-09-22 builds | 30 | **0.17** (5/30) | | | |

- **Our bank did not fall** (87.8k → 100.2k); the opponents' bank rose ~22k. Bank medians carry
  ~±5k seed noise at these sample sizes, but the direction is the one field drift predicts.
- A code regression predicts the opposite: our revenue falling, or our money leaking to the opponent.

**E4 — by 09-22 our rating band was ~95% production clones.**

| build (date) | opponents with ≥70% identical farm ops | opponents with <50% identical |
|---|---|---|
| pipe16 (09-20) | 67% | **28%** — pipe16 won 0.68 against these, at big margins |
| f55rec (09-22) | 95-100% | ~0% |
| sirxP / L96 (09-23/24) | 75-88% | ~0% |

This matches the Opus build-expert's ledger of 197 games: same wheat, herd, hires and land, and
74/118 losses within $1k.

**The mechanism, in one paragraph.**

1. pipe16's 2.8k came from **freshness**. Its farm plan out-produced the older lineages at its
   rating level (+$1.5k median margin). The 17.7% clone rate (09-20k) meant it rarely met itself.
2. By 09-22 the band had adopted the pipe16/metav4 farm plan: the lock-time rush to the best public
   kernels. The production edge was arbitraged away. The rating then settles at the crowd centre
   plus whatever market microstructure (sell ordering and timing) is worth: a few hundred dollars
   per game, won or lost in index races (build expert: ~18 contested SELL-vs-SELL turns per game).
3. Above the crowd sit the private adaptive/RL policies:
   - destbreso's #1 x-ray: +$13k median margin, divergent from t=0.
   - Sayaka Miki's #4/#6 RL agent, and 2nd place confirmed RL.
   - hwe owe's (#8) ML sell-timing model.
4. Against these we win 0.17 now and won 0.42 at our best. That is the hard ceiling.
5. Le Quang Canh (V3, a replayed tape settling at 2432 against its source's 2888) and destbreso
   (V5, "a clone does not appear to have the potential to reach the original") describe exactly
   this.

**What this means for the pending pipe16 control.**

- It predicts **no revert**: exact pipe16 now meets its own crowd — exact ties plus whisker losses
  to pipe16-plus-overlay teams. Offline it loses to our overlays 0.17-0.25 and to koshinm 0.45.
- **My pre-registered prediction:** at ≥80 rated games its fitted rating is **within ±150 of
  sir_V2's, or below**. Its display lands at ~1950-2300 (70%).
- **P(control − sir_V2 ≥ +150 fitted) ≈ 20%.** If that happens, the drift reading is wrong for our
  lineage and a live defect exists. The only layer in every post-09-22 build is reclaim, and Codex
  found a real reclaim stall.

## 2. Ranked plan (for P(top-10), only moves with a +250 tail matter)

| # | move | expected gain | tail | confidence | days | confirm/kill within 24 h | mirage risk |
|---|---|---|---|---|---|---|---|
| 1 | **Read the control against a fixed scale and act on it** | ~+50 (0.2 × +250) | **yes** — the only path back to ~2650 strength | medium; I predict "no revert" | 0 build + ~12 h wait | see below | none (live); ±80 noise per arm |
| 2 | **Field fingerprint + live-weighted gate, library extended with lock-time kernels** | +40-80 (better final pick) | **yes** if a lock-time kernel dominates the band, or a counter-agent farms the dominant family | medium | 0.5-1 | see below | medium, cut by the back-prediction test |
| 3 | **Codex `cand_capture` on the pipe16 chassis**, gated alongside a "sir_V1 minus reclaim" control | +30-60 (sheep-ranch draws only; whisker flips) | no | medium: bit-verified mechanism, dev n=12 (+$944 vs koshinm, 10W/2L) | 0 (built; held-out gate [906:930] running) | see below | moderate — winner's curse on a 12-game dev panel |
| 4 | **Counter-slot, only if move 2 shows a dominant family with a known counter** (e.g. band mostly vanilla pipe16 + koshinm clones → melon-class beats both 0.95/1.00 offline) | 0 to +150 | yes | low | 0.5 | Weighted win rate ≥ our best + 0.05 on a fresh slice | **high** — counters are brittle (melon loses 0.94-0.98 to metav4/clamp builds) |
| 5 | Best-response SELL permutation (Opus build lane) | +0-40 | no | low | 1-2 | Gate ≥0.60 vs both live builds by 09-27 12:00 UTC | **high** — siblings CF −46 and lockstep −46 died the same way |

**Move 1 — confirm/kill.** At readout, take one fresh LB snapshot and fit both arms against it.
sir_V2 and the control were submitted 7 minutes apart, so they face the same field.

- **Decision threshold:** fitted Δ ≥ |150| with ≥80 rated games each. The standard error of the
  difference is ~55-60.
- **Do not act on the display** before ~24 h. Identical files have landed 250-500 apart
  (C10; forum V5).

**Move 2 — what it is, and how to validate it.** The public-pool gate weights every agent equally;
the live field weights them by prevalence. That is why the gate ranked pipe16 7th of 9, when pipe16
was our best agent live.

- **Build:** run `fingerprint_loss2.py`-style exact replay on ~150 post-lock opponents from our
  replays. Classify each against the 354-agent library, extended with every kernel published
  09-21 10:00 → 09-23 23:59 UTC. That window was never pulled, and it is exactly the window the
  lock-time crowd cloned from.
- **Score:** each candidate's weighted win rate = Σ share_i × WR(candidate vs agent_i), taken from
  48-game cells.
- **Validation test for the instrument:** it must back-predict the observed live ordering. On the
  09-20 field pipe16 should come out well above f55rec; on the 09-24 band, L96-V1, sirxP-V2 and
  sir-V2 should come out ~0.5. If it fails, do not use it.
- **Kill if:** the band is ≥80% our own lineage in native sell order AND no library or lock-time
  agent beats sir_V1 on weighted win rate.
- **Confirm if:** a lock-time kernel is ≥10% of the band and beats sir_V1 ≥0.65 over 48 games.

**Move 3 — confirm/kill, and why the no-reclaim control matters.**

- **Confirm if:** held-out ≥0.60 vs the sir_V1 parent, and pool mean ≥ sir_V1's 0.830.
- **Kill if:** <0.55 vs the parent.
- **The control:** reclaim is the one layer common to every build since 09-23. If simply removing
  it scores as well as the capture fix, ship the removal — it is less code.

**Do not reopen** the replanner, route refits, rescue grafts, sell-phase shifts, prem floors or
alpha sweeps — all closed in §5 and the timeline. A +30-60 edge does not move P(top-10) when the
gap is ~500. Only moves 1, 2 and 4 have a tail that does.

## 3. Slot policy (only the last 2 submissions play; each restart costs ~12-24 h)

| when (UTC) | action |
|---|---|
| now → 09-25 22:00 | **Hold [sir_V2 56547525, pipe16 control].** Zero submissions. Run moves 2 and 3 offline. |
| 09-25 ~22:00 (≥80 games each) | **Readout R1** by fitted rating (move 1). |
| 09-26 ~12:00 | **Readout R2:** the new arm vs the incumbent, same method. |
| 09-27 12:00 | Last discretionary rotation. Needs a fitted Δ ≥150 live, or a weighted-gate winner by ≥0.05 that passed the back-prediction test. |
| **09-28 12:00** | **Final pair frozen** (~60 h to converge and seed post-deadline matchmaking). |
| 09-28 → 09-30 | Submit only to replace a crashed or timed-out agent. Never both slots on one day. Never re-submit an identical file to re-roll the rating — the final Bradley-Terry refit uses only post-deadline games. |

**What to submit at R1, by outcome:**

- **Control ≥ sir_V2 + 150** (regression). Keep the control. Replace sir_V2 with the best
  **no-reclaim** build as picked by move 2: "sir_V1 minus reclaim", or the exact 09-22 f55rec bytes.
- **|Δ| < 150** (field-driven; my expected case). Replace the control with the pipe16-chassis
  winner of move 3 (sir_V1+capture if it passes, else sir_V1). The pair becomes pipe16-chassis +
  metav4-chassis, a real hedge.
- **Control ≤ sir_V2 − 150.** Same as the previous branch, with more confidence.

**Final pair principle.** Take the best measured build, plus the most *different* build with a
credible right tail (move 2 or 4 winner if one exists). The team score is the better of the two,
so slot 2 costs nothing. A copy of slot 1 buys almost nothing: ~2 weeks of post-deadline games per
agent (~700 at ~2/h) shrink the Bradley-Terry noise to ±25, so there is no noise lottery to win.

## 4. The single thing for the next 12 hours

**Build the live-weighted gate (move 2), and write down its prediction for the control before
readout R1.**

1. **Pull the lock-time kernels** (`listkernels.py`, publications 09-21 10:00 → 09-23 23:59 UTC).
   This step needs Kaggle session credentials, so the orchestrator has to run it; ~40 min.
2. **Extract and screen** them vs sir_V1, pipe16 and koshinm: 48 games each, fresh slice,
   `--workers 1`.
3. **Fingerprint the opponents** of our post-lock games (L96-V2, the late L96-V1 and sirxP-V2
   episodes, then sir_V2 and the control as they arrive).
4. **Reweight the existing gate matrix** by the band's composition and run the back-prediction test.

Within 12 hours this answers three questions:

- What the field we are rated against actually runs.
- Whether an unscreened public base beats us — the only kind of change that has ever moved us
  +250 or more.
- Which final pair to field, using an instrument checked against live results rather than a
  saturated public pool.

## 5. The strongest argument that 3k+ is not reachable by 09-30

3k+ means top-3: DSM, DECEM, Vadim. The agents seen at that level:

- destbreso's #1 x-ray: +$13k median margins, adaptive from t=0.
- An RL policy at #2/#4.

Our fitted strength at its all-time best was 2658, ~350 short of 3000 on the same scale; today it
is ~2340-2470. Every large gain in this project came from adopting a fresher public base, and that
pool froze at the lock. The forum's replay data and our own data agree that clones converge to the
crowd average, and pipe16 is now the crowd.

The rating maths:

- **+350 needs ~88% head-to-head** against the whole field, including agents we beat 0.17 today.
- **Our largest measured live-relevant edges** (SIR, capture, clamp) are worth $200-1,000 per game,
  i.e. +30-100.
- **The only architecture that beats the crowd** is a reactive replanner. Two round-tables judged it
  unbuildable and unvalidatable by 09-30, and nothing here changes that.
- **Live verification is too slow:** we can only detect differences ≥150 at ~12 h per arm. That
  leaves ~4 readouts, not enough to iterate towards +350 even if the levers existed.

**What then.** Treat P(top-10) as a lottery ticket held by moves 1, 2 and 4. Protect the downside
by freezing a strong, diverse pair by 09-28 12:00 UTC and ending the churn: 10 restarts in 72 h is
what put the board at ~1,920. Put remaining effort into the instrument (move 2) rather than new
layers, so the final pick rests on how the live field actually behaves.

CONFIDENCE 3k+ by 09-30: 0.3%
CONFIDENCE top-10: 2%
