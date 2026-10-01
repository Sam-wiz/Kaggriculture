# MoE r4 — Sonnet 5 round 1 position (strategy / red team, Q1 lane)

Written 2026-09-26, machine clock (`date -u` at start of this session reads 09-26 ~10:30-11:00 UTC).
I read HANDOFF.md `## 09-25d`→end, MISTAKES.md C14-C18, `moe/r3/{BRIEF,claude,opus_r2,fable_r2,
DECISION_R3}.md`, `moe/r3/build/opus/RESULT.md`, `moe/opus/RESULT.md`, and TOP10_DECODE.md. All
new numbers below are checked against files on disk or fresh scripts I ran this round; everything
under `moe/r4/build/sonnet/` is mine and reproducible (`.venv/bin/python moe/r4/build/sonnet/<script>.py`).

## 0. Correction to ambient instructions before anything else

**AGENTS.md's "Active work — 2026-09-23" note is stale and should not be used.** It says the live
pair is `subV_f55rec`/`subV2_f55rec` and that the next lever is "the koshinm matchup cell." Both are
wrong as of now:
- The live pair has rotated four times since (f55rec → sir_V1/sir_V2 → shepherd/hyb2965 →
  hyb2965/C1); current per `moe/r4/BRIEF.md`: **hyb2965 (1974, 139 games) + C1 (1542, 65 games,
  56-9 overall but 4-4 vs ≥2000)**.
- The koshinm matchup cell was **closed on 09-24** (HANDOFF "rival-conditional routing — CLOSED":
  "route 9 pinned onto real yarn draws vs koshinm = +210, the BEST pick... the shipped map is
  per-draw optimal even vs our toughest rival"), immediately followed by a "FINAL STATE —
  architecture ceiling reached" declaration that was itself overturned within 24h by the 09-25
  field-episode re-analysis. Re-opening koshinm now would be re-litigating a closed, correctly-closed
  question. See §3 for why the general pattern here ("ceiling reached" claims that don't survive
  contact with live data) matters for how much to trust this round's build claims too.

I flag this because a stale project-instructions file is exactly the kind of thing a strategy/red-team
lane should catch before anyone re-derives 09-23's work by accident.

## 1. Q1 — How do we move to 3k+? (checked evidence)

### 1.1 The gap, quantified from the freshest LB snapshot on disk

`moe/r3/lb_0926_0500.json` (09-26 05:00 UTC, 10,028 teams). Our team (Sam-wiz): **1974.2, rank
~1596 (84th percentile)**.

| target | rank | score | gap from 1974 | % of field at/above |
|---|---|---|---|---|
| bronze | 1000 | 2211.4 | **+237** | ~10.0% (by construction) |
| silver | 500 | 2408.7 | **+435** | ~5.0% (by construction) |
| top-10 | 10 | 2899.3 | **+925** | 0.09% (9 teams) |
| 3000+ | — | 3000 | **+1026** | 0.02% (2 teams) |

(Table built by `sorted(lb.values())`, not eyeballed — see `moe/r4/build/sonnet/` history if the
orchestrator wants the one-liner re-run.)

If this rating behaves even approximately like standard Elo (K=400-scale logistic), which the
project's own numbers roughly confirm — e.g. HANDOFF 09-25g: sir_V1 (~2456 implied) beat exact
pipe16 (~2174 implied), Δ=282, predicted WR 0.835, observed flip-adjusted WR was in the 0.85-0.92
neighborhood — then a **+925 gap implies a per-game win probability against a *typical* top-10-caliber
opponent of roughly 1/(1+10^(2.31)) ≈ 0.5%.** That is not "we need to get a bit better," it is "our
current chassis loses to that population almost every time it meets it." Nothing short of a
different tier of play changes that number, and no amount of extra games converges our rating past
our true strength — more games buys precision, not altitude.

**Bronze (+237) is comparatively close**: multiple of our own builds have independently landed
implied ratings of 2100-2260 post-lock (shepherd ~2160, hyb2965 ~2135, L96 2216-2225 pre-lock,
sir_V1 offline gate mean 0.830). Bronze is a real target for the remaining runway. **Silver (+435)
has never been sustained by any post-lock public-lineage build** (f55rec's 2552 was pre-lock and is
not evidence for the current, drifted field). **Top-10/3k are a different population, not a further
point on the same curve** — see 1.3.

### 1.2 What separates 3000+ from 2800-2900, at scale (not guessed — measured)

Prior rounds decoded specific opponents from replay (WLV, the mirror band) at huge effort and hit a
hard reproduction ceiling (see §3). I took a different, cheaper angle this round: **join
`meta/episode_features.csv` (behavioural features per episode-seat: crop mix, hires, land timing,
price ranges) to `meta/agents.csv` (rating_after) across the whole pre-lock corpus** — 354k
episode-seats, thousands of distinct submissions — and bucket by rating band. Script:
`moe/r4/build/sonnet/band_features.py`, output `band_features.log`, `submission_level.csv`.

**Caveat stated up front:** this dataset runs 2026-07-30→09-20, entirely **pre-lock**. Post-lock
field drift (HANDOFF 09-25f/g: public-lineage teams fell 218-390 points in 49h) means the *rating
scale* here doesn't map onto today's LB. The *behavioural* correlates (crop mix, land timing,
tile count) are a different claim — they're about what a strategy does, not what rating that
strategy happens to earn on a given day — and I treat them as a hypothesis generator, not as fact,
which is exactly why I built a falsification test in §2 rather than just reporting the correlation.

Submission-level (one row per submission_id, median features, bucketed by peak rating_after
reached, n=27,064 / 17,633 / 9,910 / 659 / 322 / 66 / 4 submissions in the seven bands):

| band | carrot frac | melon frac | strawberry frac | tiles planted | first_land_day | peak_crew |
|---|---|---|---|---|---|---|
| ≤2000 | 0.072 | 0.106 | 0.186 | 195 | 6.26 | 12.04 |
| 2000-2400 | 0.078 | 0.065 | 0.161 | 224 | 6.04 | 12.31 |
| 2400-2800 | 0.075 | 0.074 | 0.168 | 217 | 6.11 | 12.50 |
| 2800-2900 | 0.021 | 0.115 | 0.213 | 187 | 6.43 | 13.50 |
| 2900-3000 | 0.005 | 0.123 | 0.222 | 181 | 6.51 | 13.85 |
| 3000-3100 | **0.000** | 0.131 | 0.233 | 177 | 6.79 | **14.00** |
| 3100+ (n=4) | 0.001 | 0.124 | 0.220 | 178 | 6.75 | 14.00 |

Four consistent, monotonic signals from 2400-2800 up through 3000+:
1. **Carrot goes to exactly zero.** It is not a minor crop for the top tier, it is absent.
2. **Melon/strawberry share rises** (0.074→0.131, 0.168→0.233) while **wheat share falls**
   (0.666→0.629, not tabulated above but in the log).
3. **Total tiles planted falls** (206→175) even as money and win rate presumably rise — top agents
   plant *less*, not more; consistent with shifting to strawberry (an ongoing crop that doesn't need
   replanting) and away from replant-heavy wheat/carrot churn.
4. **peak_crew converges on exactly 14.00** in the top two bands (not "about 14" — the mean is
   exactly 14.00, meaning every submission in those bands hits the same hand count) and
   **first_land_day is later**, not earlier (6.1→6.8), contradicting the "rush land" intuition.

Price-range evidence points at *why*: `range_carrot` compresses from 22.6 (2400-2800) to 6.2
(3000-3100) — top agents barely move that market because they're barely in it — while
`range_melon`/`range_strawberry` **widen** (224→270, 181→198) — top agents push those markets
harder, consistent with concentrating volume into fewer, higher-value channels rather than
spreading it across five crops.

### 1.3 What top-tier head-to-head actually looks like (tested on live dump episodes)

`mine/top10/*.json.gz` is Kaggle's official current top-episode dump (65 games on disk as of this
writing, streaming in; all 2026-09-25). I extracted `(team, rating_from_lb, final_bank)` for both
seats per game and matched against the same LB snapshot — `moe/r4/build/sonnet/top10_headtohead.py`,
log in the same directory. These are **actual current top-~20 teams playing each other**: Boey
(3097.9), DSM (3057.9), Vadim Vasilenko (2998.2), M&M&P&Q (2994.0), DECEM (2979.6), Unknown
Mother-Goose (2929.3), Majkel1337 (2905.2), 吃白饭的大肥鱼 (2891.1), and others down to ~2500.

Two things this data says that change how I'd frame the problem:
- **Median margin is ~5% of the loser's bank ($5,284 median, mean $7,981 on n=65)**, and no single
  name wins even close to every game it's in — Boey (rank 1) loses to 吃白饭的大肥鱼 (rank ~8) in
  the very first game in the dump. **The top tier is not one dominant clone family beating everyone
  else; it's several distinct, competitive builds trading wins at ~100-200 rating points apart.**
  That is a materially different picture from our own band (2200-2600), which prior rounds showed
  to be *production clones* of one public lineage decided by tiny sell-order-race margins (Opus's
  `moe/opus/RESULT.md`: 80-97% unit-op identity, median loss $199-708 on ~$100k banks — an order of
  magnitude tighter than the top tier's 5%).
- **This argues against "decode and clone the strongest single private agent" as the highest-EV
  framing for Q2/Q3, and for "build something generically more precise than a good private
  build"** — because the top tier itself doesn't look like it converged on one dominant strategy to
  copy. It looks like several different, roughly-equal-strength approaches. (I develop this as a
  critique of the decoding lane in §3.)

### 1.4 Synthesis on Q1

Bronze is reachable with the current architecture family if the PREDICT lever (see §3) delivers
even a fraction of its closed-loop promise live. Silver requires beating every post-lock
public-lineage build has ever sustained — possible but unproven, ~1-in-15. Top-10/3k require beating
a small (~10-70 team), heterogeneous, apparently well-optimized private population by a margin no
mechanism found in three MoE rounds (SIR, PREDICT, route refit, herd swaps, CXO, lockstep,
counterfactual selectors — HANDOFF's "FINAL STATE" list) has come close to producing. I do not
think 4.5 days changes that conclusion; see §5 for numbers.

## 2. What I built: a falsifiable test of the carrot hypothesis (Q1→experiment)

The §1.2 correlation ("top agents plant 0% carrot") is exactly the kind of finding this project's
own MISTAKES.md (C15) warns about taking at face value: correlation from aggregate stats is not a
verified lever until something is actually counted causally. So I built the cheapest possible
causal test rather than just reporting the correlation as a recommendation.

**Build:** `moe/r4/build/sonnet/shepherd_nocarrot.py` — imports `subW_shepherd.py`'s `agent`
unmodified and intercepts its returned action: any `["PLANT","CARROT"]` (farmer or hand op) becomes
`["PASS"]` instead. Nothing else changes. This is a crude, lower-bound test: it does not reallocate
the freed land/action-budget to melon or strawberry, it just removes carrot and leaves the tile
bare. Telemetry (`REPORT["blocked"]`) confirms it fires.

**Gate:** paired closed-loop, same seed/seat/opponent, kagsim (bit-exact, the same instrument
`moe/r3/opus_scratch/closed.py` uses) — `moe/r4/build/sonnet/run_carrot_ablation.py`, 24 fresh
seeds × 2 fixed opponents (hyb2965, shepherd-self-mirror), alternating seats, 96 games, 2 workers,
nice 10. Threshold I pre-set before running: **paired our-bank Δ ≥ +$150/game (this project's own
C16-derived power floor for a paired design) to call it positive.**

**Result — clearly negative, not noise:**

| opponent | n (paired seeds) | paired margin Δ (nocarrot − shepherd) | paired our-bank Δ |
|---|---|---|---|
| hyb2965 | 24 | **−$6,035 (SE 500)** | **−$3,332/game** |
| shepherd (mirror) | 24 | **−$6,017 (SE 439)** | **−$3,456/game** |

0/24 seeds improved in either matchup. Effect size is >6 SE in both cells — this is not a whisker
result, it is a clear kill.

**What this means, and why I'm reporting a failure instead of a recommendation:** the crude ablation
refutes the naive reading of the correlation ("just delete carrot"). The likely real explanation is
that top-tier agents don't have an isolated "carrot on/off" switch — carrot's early, fast, cheap
cash cycle is presumably load-bearing for early-game liquidity in the current chassis (buying land,
seed, and hire cost timing all depend on early cash), and a top-tier farm plan that avoids carrot
starts from a **different overall land/crop allocation from day one** (more land committed to
melon/strawberry earlier, different hire/land timing — consistent with §1.2's later `first_land_day`
and higher `peak_crew`), not a one-line deletion on top of an unchanged plan. That is a genuine
production/route redesign — exactly the category TOP10_DECODE.md §0 already flagged as "historically
where our overlays die" (item 1, confidence-gated herd swaps). I am not recommending a build here;
I am reporting that this specific, cheap, checkable version of the lever is dead, and flagging the
real version (whole-plan reallocation away from carrot) as a **build candidate for Fable's lane**,
sized correctly as a route/production change, not a patch, with the gate above as the template
(paired closed-loop Δ before anything gets an offline-gate score, let alone a live slot).

## 3. Red team: the other two lanes' assumptions

**Opus (decoding).** The lane's own r3 work already found the honest ceiling here, and I want to
make sure round 2 doesn't relitigate it: reproducing a private agent from replay alone tops out
around a **median 215-616-step match on 719 total steps, and 0/18 tapes ever reached a full-game
market-channel match** (`moe/r3/build/opus/RESULT.md` §2, "R gate: FAIL"). The d13-29 block —
where the money is — is "opponent-conditioned... cannot be reverse-engineered from 18 tapes." My
§1.3 finding sharpens why: the top tier isn't one dominant agent with a single private wrapper to
crack, it's several distinct competitive builds. Decoding buys real value for the **mid-band**
(2200-2600, where §1.3 shows near-clone dynamics and Opus's own numbers show 80-97% unit identity),
which is exactly the silver/bronze-relevant population. I'd frame Q2 explicitly as "decode the
mid-band we actually play against" rather than "decode top-10," because the latter's own evidence
(R gate) says it's not reachable in the time available, and even a full reproduction of one
private agent (WLV) would only ever explain that one agent, not the ~10-70 different builds
occupying the top tier.

**Fable (building).** C1 (`subY_C1_predict2.py`) is exactly the kind of instrument-risk MISTAKES.md
C18 already burned us on once: it passed every closed-loop gate against **reconstructed proxies**
(WLV proxy R2S, WL+S2) — 0.90 vs a shepherd proxy, 0.80 vs a hyb2965 proxy, "L→W 11/22, W→L 0" — and
those proxies were themselves built and validated only by reproducing recorded, *frozen* games, not
by predicting a *new* agent's live interaction with the field. That is precisely the gap that made
shepherd's replay-substitution overprediction fail (predicted 0.656 vs ≥2200, delivered ~0.2 —
MISTAKES C18). **C1's early live read (r4 BRIEF: 4-4 vs ≥2000 at 65 games, i.e. break-even) is
already tracking below its 0.90/0.80 gate predictions, the same shape as shepherd's collapse, just
less extreme so far.** I would not treat "4-4" as a comfortable mid-read; I'd treat it as an early
warning that deserves the same skepticism this project already learned to apply, and I'd act on it
faster than the original plan (see §4).

One specific methodological gap I'd close: shepherd's collapse was invisible in a pooled "vs ≥2200"
number (0.59 at 2000-2200, cratering to 0.15 at ≥2400) — the pool average would have looked
survivable much longer than the tail actually was. **C1's own reported number ("4-4 vs ≥2000") is
pooled the same way.** Before anyone calls promote/kill on C1, split its read the way shepherd's was
split after the fact (2000-2200 / 2200-2400 / ≥2400) — if the sub-band split isn't done pre-emptively
this time, we will find out C1 failed the same way shepherd did, one read too late again.

## 4. Live-test protocol, 09-26 → 09-30 (my ownership per the brief)

Constraints I'm building around, all sourced from files, not assumed: deadline 09-30 23:59 UTC,
**upload hard stop 09-30 18:00 UTC** (r4 BRIEF); uploads ≥8h apart (r3 consensus); each upload
evicts the *older* of the active pair (recency, not choice); final team score = better of the last
two submissions (Addison Howard, quoted in HANDOFF 09-25c); pre-deadline rating is weakly informative
of final standing (55-65% chance the final BT fit is post-deadline-games-only per opus_r2 §4's
careful sourcing — I did not re-derive this, it's already the most rigorous treatment in the repo
and I have no reason to second-guess it). **Practical upshot: churn between now and ~09-29 is cheap,
but only if each read is long enough to be trustworthy — the risk is not churning too much, it's
promoting on too short/pooled a read (§3).**

| when (UTC) | action |
|---|---|
| now – 09-26 ~18:00 | **Hold [hyb2965, C1].** Do not evict C1 or hyb2965 on a partial read. Read C1 at the ~24h mark **split by sub-band** (2000-2200/2200-2400/≥2400), not pooled. If ≥2400 WR is trending toward shepherd's 0.15 rather than the gate's predicted 0.80-0.90, that's the kill signal — treat it exactly like C18, don't wait for the full 40-h read to confirm what the tail already shows. |
| 09-26 evening – 09-29 | **This is the free-churn window.** hyb2965 is the older slot and will be evicted by the *next* upload regardless of what we do — so use it. Whatever Fable/Opus's next build is (PREDICT library growth, the carrot-reallocation redesign from §2, a genuinely different chassis), it should go into hyb2965's slot as soon as it clears: (a) `kaggle_load_check`, (b) a closed-loop gate vs the *current* live pair (not a frozen tape) at n≥40, mean Δ≥+$150 paired, and (c) — new requirement from §3 — if its validation used a reconstructed proxy of any kind, the promote bar is a live sub-band split at ≥24 games vs ≥2200, not a pooled ≥2000 number. Rotate probes every ~12-16h through this window; each rotation costs nothing under the last-two-uploads rule as long as the read before rotating was real (≥24 band games), not partial. |
| 09-29 ~18:00 | Stop probing. Freeze on whichever two builds have the best validated live reads, from genuinely different lineages/chassis if the numbers are close (the "better of two" rule means the second slot should maximize the chance that *at least one* build has a good private-tier matchup, not duplicate the first). |
| 09-30 08:00 | Re-upload finalist A (best read), after load-check + one official-env smoke test both seats. |
| 09-30 14:00 | Re-upload finalist B (best of a different family than A). This and 08:00 become the scored pair. |
| 09-30 18:00 | Hard stop. No further uploads except to replace an outright crash. |

This is close to Opus/Fable r2's own timeline (I'm not overriding a plan that already did the
sourcing work correctly) — the addition is the sub-band split requirement and treating C1's current
number as a warning rather than a mid-read, both directly downstream of §3.

## 5. Next 12 hours

1. **Watch C1's sub-band split** as it crosses ~100-150 games (~09-26 evening/09-27 morning per the
   BRIEF's own cadence) and flag immediately if the ≥2400 slice is trending shepherd-shaped.
2. **Hand the carrot-reallocation redesign (§2) to Fable's lane** as a scoped candidate: not "delete
   carrot," but "commit more land to melon/strawberry earlier, drop carrot from the rotation,
   re-time first land purchase later" — sized and gated the way §2's failed ablation was (paired
   closed-loop before any offline-pool score), since a naive version of this has now been shown to
   backfire by >$3k/game if done wrong.
3. **Extend the top10-dump head-to-head table** as more episodes stream into `mine/top10/`
   (`fetch_epindex.py` is still running per its log) — 65 games is enough to see the shape, not
   enough to fully characterize each top team; this is cheap to keep re-running
   (`moe/r4/build/sonnet/top10_headtohead.py`) and costs no worker budget beyond a few seconds.
4. **Flag AGENTS.md's stale "Active work" section to the orchestrator** (§0) so it gets refreshed —
   low effort, avoids a repeat of this round's few minutes spent confirming the koshinm lever was
   already dead.
5. I do not have Kaggle credentials and am not proposing any upload myself; everything above is
   input to Claude Code's decisions and Fable's build queue.

## 6. Probabilities

Grounded in §1.1's percentile math, §1.3's top-tier heterogeneity finding, and the project's own
demonstrated ceiling (every mechanism in HANDOFF's "FINAL STATE" list plus PREDICT/SIR/BRX,
none of which has sustained a post-lock live rating above ~2200-2260):

**P(3k+): 0.1%  P(top-10): 0.5%  P(silver): 7%  P(bronze): 40%**

(3k+/top-10 essentially unchanged from r3's consensus, 0.3-1%/0.2-2% — the top-tier heterogeneity
finding in §1.3 is a reason the *framing* should shift toward "generic precision" over "clone the
leader," not a reason the odds should move much in 4.5 days. Bronze/silver match r3's Opus/Fable
convergence (38-40%/7-8%); I see nothing in this round's evidence that should move either, and the
early C1 warning in §3 is a reason not to round bronze upward on PREDICT's promise alone.)
