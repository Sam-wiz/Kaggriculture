# MoE r3 — Fable 5.1 position (written 2026-09-26 ~01:00 UTC, before reading opus.md; claude.md was in my context as project instructions)

Scratch analyses live in `/tmp/fable/` (not committed): `live_pass1.py`, `fingerprint.py`,
`moneytrace.py`, `sidebyside.py`, `premdiff.py`. All ran on 1 worker at nice 10, ~6 CPU-min total
(machine load was ~10 on 8 cores throughout). Every number below that I did not compute myself is
cited to its file.

## 0. The two facts that change the plan

**F1. The pre-deadline rating is not the objective; it is only our instrument.** Kaggle staff
(`discussions.md` line 103): submissions keep playing for two weeks after the deadline, then "a
single Bradley-Terry Tournament" decides the final leaderboard; team = better of its two (staff,
line 4343); ties = half wins. A BT fit has no "start at 600 and climb" penalty — a late upload only
has fewer games in the fit (wider CI, no bias). So the brief's constraint "without losing our best
anchor" is a constraint on *reading*, not on the *final*. There is nothing to protect: a converged
2100 has zero medal value and its file is on disk. Both slots are test slots for four days; the
last two uploads on 09-30 are the final pair, chosen on evidence, not on convergence.
(Open question in the dump, lines 128/139: whether pre-deadline episodes enter the fit. Either
answer leaves the conclusion intact.)

**F2. Medal thresholds, verified on `moe/r3/lb_0925_1612.json` (10,008 teams):** rank 10 = 2923,
rank 30 = 2813, rank 100 = 2666, rank 500 = 2437, rank 1000 = 2239, us 2090 (rank 1359). Kaggle's
standard rule for >1000 teams is gold = top 10 + 0.2% (≈30), silver = top 5% (500), bronze = top 10%
(1000); the forum corroborates in passing (line 1825: cloning a recent public kernel "has been enough
to sit around the top 10%"; a 26th-ranked poster calls their zone "silver", line 317). I could not
find an official threshold statement in the dump. Rank thresholds are what carry to the final BT;
the score numbers will re-scale.

## 1. Diagnosis (checked)

**1a. Where the rating is lost.** 89 shepherd games joined to the LB snapshot (`/tmp/fable/live_pass1.py`):

| opp rating | n | W | WR | ≥0.95 unit-op mirrors |
|---|---|---|---|---|
| <2000 | 22 | 21 | 0.95 | 8 |
| 2000-2200 | 33 | 20 | 0.61 | 27 |
| 2200-2400 | 20 | 5 | 0.25 | 17 |
| 2400-2600 | 12 | 2 | 0.17 | 11 |
| ≥2600 | 2 | 0 | 0.00 | 0 (Joseph Adamski, Erfan: −$6.7k, −$5.4k) |

Mirrors (unit ops ≥95% identical to ours) rated 2000-2200: **18-9**. Mirrors rated ≥2200: **6-22**.
Same farm plan on both sides in all 55 games; what separates a 2100 mirror from a 2450 mirror is
its market code alone. Our implied ~2160 means "below-median market policy inside the shepherd-farm
cluster". Seats are symmetric (24/42 vs 24/47). hyb2965 (77 games): 10-7 vs 2000-2200, 3-2 vs ≥2200
mirrors, 0-2 vs the ~2700 private tier (−$20k, −$17k, 0% identity). Too early to read.

**1b. Where the money is lost, by day.** I replayed all 54 shepherd-mirror games (≥2000) with BOTH
recorded action tapes open-loop on the recorded seed (`/tmp/fable/moneytrace.py`; harness ~1 s/game).
**54/54 reproduce both final banks to the dollar** — the tapes and the engine are exact. Per-phase
margin (ours − theirs):

| phase | losses ≥2200 (n=22) mean / negative share | wins ≥2000 (n=24) mean |
|---|---|---|
| d0-5 (opening, hires, herd) | −33 / 9 of 22 | −11 |
| d6-12 (first premium sales) | **+85** / 10 of 22 | +17 |
| d13-24 | **−486 / 18 of 22** | +309 |
| d25-29 | **−407 / 18 of 22** | +357 |

Day-level deltas are ±$50-200/day, every day, from day 13 on. The margin is a **drip of many small
mid/late-game premium (milk, wool, strawberry) sell-timing races** against a producer with identical
output. Not the opening (≈$0), not the first sales (we are slightly ahead there), not one endgame
event. This matches the Opus build-expert's "~18 contested SELL-vs-SELL turns/game".

**1c. Who the mirrors are.** Opening fingerprint (`/tmp/fable/fingerprint.py`; step-1 wheat
BUY/SELL) among ≥2200 mirrors:

| opening | n | W-L | mean margin | d13-24 mean |
|---|---|---|---|---|
| (5, 0) | 9 | **1-8** | −871 | −651 |
| (20, 15) | 11 | 2-9 | −335 | −123 |
| (8, 3) = shepherd's own | 5 | 1-4 | −186 | −137 |
| (10,5) / (40,35) | 3 | 2-1 | | |

I ran the public candidates one game each: **hybu, pipe18, v15stack, V57 and hyb2965 all open
(20, 15)** — that is the pipe16-lineage default; shepherd's (8, 3) is haideptry's own edit. The
(5, 0) family, which beats us hardest, matches **no public agent we hold** (consistent with the
identify pilot's 0.74-0.90 partial matches, all diverging at step 0-1). It is private.

**1d. Our two live agents are one lineage, and their opponent model is stale.**
`subW_shepherd.py` and `subX_hyb2965.py` share the identical haideptry v9 stack, including a
**"v9/2 PREDICT" layer** (line ~3395): it recovers the rival's premium sales each turn from the
market-inventory delta, matches them against a **library of 2,398 recorded rival sale streams keyed
by the first two shops (24-63 per world; I decoded the index)**, and when the best-matching stream
sells ≥4 units of a product in the next two turns it sells our planned lots of that product NOW —
i.e. it pre-empts. It is inert before step 150 and scores over the last 240 turns. hyb2965 adds
CTRTABLE (rival-specific wheat counters), OVERFLOW, and the VE/VT six-sheep expansion. So:

- our "different-chassis hedge" is two snapshots of the same author's lineage; hedge value is low;
- shepherd is already an *opponent-conditioned sell policy*, whose library was recorded before the
  lock. The post-lock band is v9 forks and a private (5,0) family whose sale schedules are not in
  that library, so the forecast mis-fires exactly in d13-29 where we lose;
- shepherd has been public since ~09-22. Any fork built after that can have **our** stream in its
  library and pre-empt us by construction, while we cannot pre-empt them. That asymmetry predicts
  the rating gradient we see (newer forks above us, older ones below). Hypothesis, testable (§2).

Shepherd self-play is an exact tie on 4/4 seeds (both PREDICT/RACE layers are symmetric), so every
dollar in a mirror game comes from asymmetric market code, not seat order.

**1e. Why both instruments failed, precisely.** The unit-op channel replays exactly and is identical
on both sides; it contributes nothing to the ranking. The whole ranking sits in the market channel
over ~100 contested turns/game, and that is the one channel neither instrument can model: the
public pool contains market policies that are not the field's (shepherd beats every public overlay
0.75-0.84 offline and loses 0.21 live), and open-loop tapes cannot decline to sell into a glut we
create. C18 is a special case of this: any layer whose value is pre-emption is flattered by a rival
that cannot move.

## 2. Instrument: semi-closed-loop replay (SCL)

We hold **no** opponent code (identify pilot negative), so the "closed-loop against their agent"
branch of question (a) is empty. What we do hold: 860 post-lock tapes (694 indexed in
`moe/opus/eps_index.json` + 166 in `moe/r3/live_episode_ids.json`; 461 vs ≥2000, 291 vs ≥2200),
each replaying exactly, and the rival's *full private state* at every tick (shed, money, seeds) is
recoverable from the exact replay.

**Principle.** Keep what replays exactly and is insensitive to our market actions — the rival's
unit ops (97-100% identical across games whose market streams differ on 100+ turns) — open-loop.
Replace **only the rival's market channel** with a reactive model. Three tiers, cheapest first:

1. **Price-conditioned tape.** From the exact replay we know the price index at which every recorded
   rival SELL filled. The rival re-issues its recorded lots in order, but a lot *waits* (up to W
   ticks) while the current price index of that product is below (1−δ)× its recorded fill index.
   δ=0, W=0 is exactly open-loop replay, so the instrument is a strict generalisation and the
   sensitivity of a candidate's WR to (δ, W) is itself diagnostic: a candidate that only wins at
   δ=0 wins by exploiting a rival that cannot move.
2. **Behaviourally cloned family rules.** Per opening family ((5,0), (20,15), (8,3)), fit per
   product a threshold rule for (sell?, qty) on (own shed, price index, market inventory, day, hour,
   our visible premium stock on tiles, rival's last observed sale). Accept only if it reproduces
   ≥95% of the rival's market actions on held-out games of the same family.
3. **The v9 overlay itself with its library refreshed with post-lock streams** — the best-informed
   model of what a v9 fork does, and the direct test of the 1d asymmetry hypothesis.

**Validation, pre-registered, in this order; the instrument ranks nothing until it passes.**

- V1 exactness: δ=0 reproduces 54/54 banks (done).
- V2 back-prediction of shepherd: shepherd in our seat vs SCL rivals on the 28 ≥2200 mirror tapes
  must give WR in [0.10, 0.35] (live 6/28 = 0.21; 95% CI ≈ 0.08-0.41). Open-loop gave ~0.66 on the
  L96-era tapes (HANDOFF 09-25h/j). If tier 1 still says ≥0.5 at any reasonable (δ, W), tier 1 is
  not reacting enough → tier 2.
- V3 cross-build order: on the same tapes the instrument must order pipe16-control (~1800 live) <
  sir_V1 (1897) < shepherd (2100) ≈ hyb2965 (~2135 implied), gaps within ±$300/game (≈±100 Elo).
  Four live reads, one ordering to hit.
- V4 family split: reproduce (5,0) 1-8, (20,15) 2-9, and 2000-2200 mirrors 18-9 within binomial
  noise.
- V5 out-of-sample: the first candidate it ranks top goes live with a written WR prediction vs
  ≥2200 mirrors; the instrument is graded on that game (the C18 rule).

**Limits, stated.** Tier 1 models only price-reactive behaviour. A rival that forecasts *us* from a
library containing our stream reacts to our schedule, not to price; tier 3 is the only tier that can
represent that. If V2 fails under all three tiers, the instrument is dead and only live remains —
§3 is designed to work in that case. Cost: harness ~1 s/game; 28 tapes × 4 builds × 3 tiers ≈ 340
games ≈ 6 min on 1 worker.

## 3. Live-test protocol (uses F1)

Measured rates: shepherd 89 games in ~13 h, hyb2965 77 in ~12 h ≈ **7 games/h/slot**; a fresh upload
meets ≥2200 opponents after ~15-20 games (~3 h: shepherd was 17-1 vs <2300 in its first 18), then
collects ~25-35 games vs ≥2200 in the next ~10 h.

**The fast read is the paired mirror record, not the displayed rating.** Metric: W-L vs opponents
rated ≥2200 on an LB snapshot taken *at read time* (`mine/fetch_ours.py` episode list + fresh
`lb_*.json`), unit identity ≥0.95. Baseline shepherd 6-22 (0.21). Pre-registered rule after ≥24
such games: **≥12 wins → PROMOTE** (binomial p<0.003 vs 0.21); 8-11 → extend 12 h; **≤7 → KILL**.
Sanity gates: ≥0.85 vs <2000 (a broken farm loses those), zero ERROR/timeouts. No concurrent control
is needed because the metric is opponent-class-normalised; field drift over 4 days is the residual
risk and is bounded by re-reading a finalist when it is re-uploaded.

**Choreography** (pair now: shepherd 56549546 older, hyb2965 56551754 newer; eviction by recency):

| when (UTC) | action | pair after |
|---|---|---|
| 09-26 ~02:00 | upload probe P (§4 C6, 0 h to build) — evicts shepherd, whose read is complete | [hyb2965, P] |
| 09-26 ~14:00 | read P; upload C1 (if it passed its offline kill tests) — evicts hyb2965 at ~170 games (read complete) | [P, C1] |
| every ~12 h | one upload, evicting the older (already read) member; PROMOTEd builds are noted, not kept live | |
| 09-30 ~10:00 | re-upload finalist A (best read); `kaggle_load_check` + official-env smoke first | |
| 09-30 ~14:00 | re-upload finalist B (second best, preferring a different market family) | final pair |

Budget: ~100 h → ~8 candidate reads using ~9 of ~25 uploads; keep 2 uploads/day unused for crash
replacement; never both slots within 4 h (operating rule); 6-h buffer before 23:59 on 09-30. If
fewer than two candidates PROMOTE, the finalists are the best-read builds we have (hyb2965 and the
best of shepherd/C-builds by mirror record).

What this gives up: a converged pre-deadline display. It has no final value (F1). If the user wants
the display for other reasons, the alternative is re-uploading the anchor every second upload, which
halves throughput to ~4 reads; I recommend against.

## 4. Ranked candidates

Calibration: ~$300/game ≈ 100 Elo inside the clone band (memory `route-oracle-confound`). Bronze needs
~+150 (WR vs ≥2200 mirrors ~0.40-0.45); silver ~+280 (≈0.55-0.60).

| # | candidate | expected gain if it works | conf | hours | kill test |
|---|---|---|---|---|---|
| C1 | **shepherd + PREDICT library refreshed with the 860 post-lock rival streams** (drop or down-weight the 2,398 pre-lock streams; ~7 post-lock streams per shop world; optionally start at step 140 and use the PREDICT2 whole-library variant) | recovers pre-emption in d13-29 where we lose −$450/−$400: half of it (+$400/g) ≈ +130 → ~2290 (bronze) | 0.30 | 3-5 (encoder is delta-coded (tick, item, qty) per stream; `_v92_p_pair` documents it) | (1) leave-one-episode-out forecast hit-rate of rival ≥4-unit sales in the next 2 turns on post-lock tapes: refreshed must beat stale by ≥10 pp; (2) SCL tier-1 WR vs ≥2200 mirror tapes ≥ vanilla +0.15; (3) live ≥12/24 |
| C2 | **hyb2965 + the same refresh** (its CTRTABLE/OVERFLOW/VE layers are the newer v9; live 11-6 vs mirrors so far) | same mechanism on the stronger base | 0.30 | +1 on C1 | same; natural second finalist, though correlated with C1 |
| C6 | **Probe: exact public hybu** (opens (20,15); beat shepherd +$385 on one seed in both seats; +$1,741 vs pipe16; only +0.046 vs sir_V1 open-loop) | information on whether a non-v9 market family beats the band; if it reads ≥0.4 it is a finalist candidate itself | 0.15 | 0 | mirror read; costs one 12-h slot that is otherwise idle while C1 is built |
| C3 | **Anti-glut premium discipline** (public info only): never sell milk/wool/strawberry while that product's inventory is > I0+0.5T; hold up to W ticks for the town drain; always sell the whole lot in one order (the engine quotes the entire order at pre-sell inventory) | targets the same d13-29 drip | 0.20 | 2-3 | SCL tier 1 no gain, or shed-cap overflow (OVERFLOW layer covers hyb2965) |
| C4 | **Mirror-aware forecast without a library**: in a mirror the rival's premium stock equals ours until it sells and its sells are visible in the inventory delta (RACE already computes this); replace the stream lookup with the tier-2 family rule as the online forecaster | generalises off-tape; bigger ceiling than C1 | 0.15 | 6-10 | tier-2 rule reproduction <90% held-out |
| C5 | hyb2965 as is | control; read completes ~09-26 14:00 | — | 0 | — |
| — | reactive replanner / RL vs the private ~2700 tier | the top-10 lever | <0.03 by 09-30 | >5 days | not this deadline |

Failure risks: C1/C2 — the strong mirrors may already run refreshed libraries containing our stream;
then pre-emption is symmetric and both dump on the same tick (tie, which is still better than 0.21).
C3 — the tape's timing is author-tuned; deferring can walk into the rival's dump; must be tested
against tier-1 rivals at several (δ, W), not at δ=0. C6 — one seed, one game; treat as a probe.

## 5. Next 12 hours

1. 01:00-02:00 — `kaggle_load_check` on hybu; upload as probe P (evicts shepherd). Record the LB
   snapshot time.
2. 01:00-05:00 — build C1: decode/encode the PREDICT library; extract post-lock rival premium-sale
   streams from the 860 tapes by exact replay (the rival's SELL ticks of MILK/WOOL/STRAWBERRY keyed by
   first two shops); run kill test (1) (leave-one-out forecast hit-rate, stale vs refreshed).
3. 03:00-06:00 (parallel, 1 worker) — build SCL tier 1; run V1-V4 on the 28 ≥2200 mirror tapes for
   pipe16-control, sir_V1, shepherd, hyb2965 at (δ, W) ∈ {0, 0.1, 0.2} × {0, 12, 48}. Write the
   predictions to `moe/r3/scl_preregistered.md` before looking at candidates.
4. 06:00-08:00 — C1 and C3 through SCL tier 1 (kill test (2)); C2 = C1's library on hyb2965.
5. ~12:00-14:00 — read P (~70 games, ~20 vs ≥2200); upload the best of {C1, C2} that passed (1)
   and (2), with its live WR prediction written down; hyb2965's read (~170 games) closes the same hour.

## 6. Stop

- Stop using the public-pool gate and open-loop replay-substitution to rank anything that touches
  market timing (agreed by all; restated because C1-C4 all touch it). Use them only for V1-style
  exactness checks and for farm-channel changes.
- Stop treating the pre-deadline rating as the objective: "hold to converge" and "freeze 09-28" have
  no final-scoring rationale (F1). The only freeze is a 6-h load-failure buffer on 09-30.
- Stop trying to identify the mirrors as exact public agents (pilot negative; the (5,0) family is
  private).
- Stop calling shepherd/hyb2965 a chassis hedge; pick finalists by market family, not by author tag.
- Stop building on the pipe16/sir stack (sir_V1 1897 live; v9 supersedes it), and stop tuning the
  opening (d0-5 ≈ $0 in every mirror game).
- Stop endgame capture, prem floors, route refits, RL/replanner talk for this deadline (all closed).

## What I did not do / could not verify

I did not build SCL or C1; tier 1 and the library re-encoder are proposals with the format traced
but not exercised end to end. Medal thresholds are the standard Kaggle rule plus two forum
remarks, not an official statement for this competition. The (5,0)-family claim rests on
five public agents run once each; other public files may open (5,0). The "rivals hold our stream"
asymmetry (1d) is a hypothesis; kill test (1) on C1 is also its test.

P(top-10): 0.5%  P(silver): 5%  P(bronze): 28%
