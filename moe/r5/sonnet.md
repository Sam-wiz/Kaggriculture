# MoE r5 — Sonnet 5 (claude-sonnet-5), round 1: instrument + red team + P(3k)

Written 2026-09-26 20:43 → ~22:30 UTC (`date -u`), foreground only, ≤2 workers, nice 10, no
background jobs. Read in full before writing: `moe/r5/BRIEF.md`, `HANDOFF.md` (tail, `## 09-25h`
through `## 09-26f`), `moe/r4/{opus,opusb,sonnet}.md`, `moe/r4/THREAD.md` (tail), `MISTAKES.md`
(all, with emphasis on A1-A5, B1-B2, C1, C15-C16). Everything numeric below is either quoted from
those files with its source named, or freshly run by me this round — scripts and logs are all under
`moe/r5/build/sonnet/`, runnable with `.venv/bin/python moe/r5/build/sonnet/<script>.py`.

## 0. Housekeeping red-team catch: AGENTS.md is stale *again*

I flagged in r4 (`moe/r4/sonnet.md` §0) that AGENTS.md's "Active work" block (live pair
`subV_f55rec`/`subV2_f55rec`, "koshinm matchup cell" lever) was stale. **It is still there,
unchanged, in this session's system prompt, and it is now three rotations further out of date**:
the live pair went f55rec → shepherd → [shepherd, hyb2965] → [hyb2965, C1] (HANDOFF 09-25h/i/l), and
r5's own BRIEF correctly states the current pair as `[C1, hyb2965]` (BRIEF misquotes it as
`subV_f55rec`+`subV2_f55rec` too, in its own header — that block is copy-pasted boilerplate, not
re-derived). This isn't a nitpick: a stale "Active work" note is exactly the kind of silent-looking,
plausible-but-wrong artifact MISTAKES.md's preamble warns about. **Recommend claude-code replace
AGENTS.md's "Active work" block with a pointer to HANDOFF.md's last dated entry instead of a
snapshot that has now gone stale three rounds running.** I can't edit AGENTS.md from this lane
(write scope is `moe/r5/sonnet.md` + `moe/r5/build/sonnet/`), so this is a request, not a fix.

## 1. Instrument trust ledger — what r4 already settled, what's unchanged, what's new

r4 (opus + opusb, both lanes, independently) built and pre-registered five instruments against the
top-10 question. I re-derive nothing here that was already decisively measured; I cite it and add
only what's new this round. Verdicts, unchanged from r4:

| instrument | verdict (r4) | applies to r5's A/B/C? |
|---|---|---|
| tape proxy on its own seed | vacuous (reproduces itself) | still vacuous |
| TOP-SUB (our build vs recorded top tape, open-loop) | **FAIL by >1,000 Elo** (rated us ~3,120 vs live 1,800-2,100); tape breaks $18-56k under any perturbation | kills any router/imitation candidate gated this way (would hit architecture A) |
| ENGINE (closed-loop self-play, recorded shops pinned, our builds vs the recorded top pair) | **FAIL**, Spearman 0.03 vs known pre-lock ratings of OUR OWN builds | directly relevant to A: if ENGINE can't even rank our own already-known builds, it cannot validate a freshly-trained imitation policy either — same instrument, same failure mode, no new argument changes this |
| TFC shop-prefix tree router | dead on coverage (depth-3 coverage 19%, pre-registered kill was <50%) | rules out any "splice onto recorded top games" construction for A |
| **LINEAGE RR** (closed-loop round-robin among OUR builds, mapped to live Elo via 5 anchors) | **PASS, marginal** (Spearman 0.70, bar ≥0.7; 2/10 flips, bar ≤2) | the *only* surviving gate; scope is explicitly "band-targeted candidates," never a top-10 claim (opus r4 §1 Q3) |

**Nothing above is relitigated — it's settled.** The one new question r5 raises that r4 didn't
directly answer is **Architecture B's feasibility**, since B is a genuinely new proposal (r4's
candidates were all A/C-shaped: imitation, tape routers, chassis patches). That's where I spent most
of this round's effort, because it's checkable cheaply and nobody has checked it yet.

## 2. Architecture B (runtime planning) — measured, and it does not fit the budget

BRIEF §B says: "Must fit Kaggle's per-step time budget (measure it: actTimeout + remainingOverageTime
60s) — Python engine speed is the constraint." I measured both halves.

**The budget, confirmed from the installed package** (not assumed from the BRIEF's paraphrase):
`.venv/lib/python3.14/site-packages/kaggle_environments/envs/kaggriculture/kaggriculture.json` sets
`remainingOverageTime: 60`; our repo-root `kaggriculture.json` (spec only, no observation defaults)
confirms `actTimeout: 1`. Reading `agent.py`/`core.py`: **actTimeout (1s) is free per step and does
not bank; remainingOverageTime (60s) is a single pool shared across all 720 steps of the whole
episode, consumed only by the time each step takes beyond 1s, and it never refills.** So the entire
game's "extra thinking" budget, spent however you like across 30 days, is 60 seconds. Exceeding it is
a timeout loss — worse than any economic gap architecture B could recover.

**Engine speed, measured two ways** (`moe/r5/build/sonnet/bench_realengine.py`, `.log`):

| engine | what it is | ms/frame |
|---|---|---|
| **kagsim** (`kaggriculture-cppsim/kagsim.cpython-314-darwin.so`) | compiled C++/pybind11, what every RR/gate/ceiling script in this repo actually uses | **0.0025 ms** (2.48 µs) |
| real interpreter, trivial policies (`pass`/`pass`) | `kaggle_environments.envs.kaggriculture.kaggriculture` — the pure-Python module the Kaggle judge actually executes | **2.30 ms** |
| real interpreter, realistic policies (`subX_hyb2965.py` vs `subY_C1_predict2.py`) | same module, actual chassis complexity | **12.85 ms** |

**kagsim cannot be embedded in a submission, checked directly, not assumed:** `file
kaggriculture-cppsim/kagsim.cpython-314-darwin.so` → `Mach-O 64-bit bundle arm64`. Kaggle's judge
host is linux/x86_64. This is not a portability inconvenience to work around — it is a different OS
and CPU architecture than the binary was built for; it cannot run there at all. Every speed number
this project has ever quoted for "the engine" (5.5-6.7ms/game median in opusb's r4 gates, 2000
episodes/sec in the kagsim kernel's own name) is a kagsim number, ~1,000-5,000× faster than what a
from-scratch pure-Python simulator embedded in the submission would actually run at. **Any
architecture-B time budget reasoned from kagsim's speed is reasoning from the wrong engine.**

**What the real 60s pool buys, at real-engine speed** (`moe/r5/build/sonnet/budget_calc.py`, `.log`;
k = number of decision points the 60s is split across, e.g. k=8 for one per town-shop unlock):

| horizon | cost/rollout (realistic policy cost) | branches affordable per decision, k=8 |
|---|---|---|
| full 30-day game | 9.25s | **0.81** (fewer than one rollout per decision point, whole game) |
| 14 days | 4.32s | 1.74 |
| 7 days | 2.16s | 3.47 |
| 3 days | 0.93s | 8.11 |
| 1 day | 0.31s | 24.3 |

**Reading:** there is no version of architecture B, as scoped ("simulate candidate plans forward
… and pick the best"), that affords deep search, opponent-response modelling, or full-game
lookahead — the whole 60s pool doesn't even cover 7 full rollouts of the entire game, once. The only
versions that fit inside the real budget are narrow: **≤8-10 decision points, ≤3-7 day horizons,
2-3 branches, and cheap surrogate policies for the simulated future** (not the real chassis — the
12.85ms/frame number already prices in real complexity; a lighter, hand-rolled surrogate could maybe
buy a further 2-4× before accuracy degrades so much the lookahead stops meaning anything). That is
not a general planner; it's a shallow, single-purpose sanity check bolted onto a scripted plan — in
practice indistinguishable from architecture C with a look-ahead flourish. And building that surrogate
simulator (a pure-Python reimplementation faithful enough to be worth trusting, since a wrong
simulator gives a confidently wrong answer, exactly MISTAKES.md's "plausible-looking number" pattern)
is itself a multi-hour port from scratch, on top of everything else, with a real crash/timeout risk
if the budget accounting has an off-by-one (a single decision point that runs long enough to exceed
the pool mid-game ends the *entire* game in a timeout, not just that turn).

**Verdict: kill architecture B as a standalone build this round.** It is not "slower than we'd like"
— the arithmetic above is roughly 2-3 orders of magnitude short of what "simulate and pick the best"
implies, using the actual judge-side engine. If opus/opusb want a lookahead *component* bolted onto
architecture C at the 8 shop-unlock dawns specifically (3-day horizon, 2-3 branches, a cheap
surrogate), that is inside the affordable range per the table above and I would not block it — but
it should be scoped, gated, and time-boxed as a small addition to C, not carried as a separate
architecture with its own build track.

## 3. Architecture A (macro-policy imitation) — red team

Nothing in r5's framing changes r4's finding that **no instrument validates this against the
population it's meant to imitate**: ENGINE (the only closed-loop instrument that even attempts
"our pair vs the recorded top pair, same world") failed retrodiction at Spearman 0.03 *for ranking
our own already-known builds* — it has no track record to lean on for a genuinely new imitation
policy, and there's no reason a harder case (a policy that's never played live at all) would fare
better on the same broken instrument. TOP-SUB and the tape-router constructions are separately dead
(§1). The only gate an imitation build could actually pass through is LINEAGE RR — which measures
"beats our own lineage," not "imitates the top family well." So Architecture A's realistic pre-upload
evidence trail collapses to exactly the same one number architecture C would also produce (LINEAGE
RR / direct closed-loop vs C1), while carrying substantially more build risk and zero support from
the top-tier-specific instruments the BRIEF hoped would exist. Base rate for from-scratch builds in
this project, independent of the imitation question: **0/72** (opusb r4 §1 Q1, "our v1-v31
from-scratch agents went 0/72 vs rivals"). I did not find anything in this round's evidence that
should move that prior. I'd deprioritize A relative to C unless opus's macro-policy extraction
produces something that can be layered onto an *existing* executor (which is C's territory anyway,
not a from-scratch policy).

**Independent check of the decoded facts A/C both depend on** (I did not want to build a
recommendation on opus's r4 numbers without at least spot-verifying them myself, given this project's
own C15 — "three wrong explanations for one failure, because nobody counted" — and because a fresh
random sample from the same source is cheap): `moe/r5/build/sonnet/spotcheck_top10.py`, 120 games
randomly sampled from `mine/top10/*.json.gz` (1,773 on disk), independent parse (not `decode.py`):

- **Opening signature** (`BUY_ANIMAL COW 1` + `BUY_PRODUCT WHEAT 5` at step 1): **165/240 seats
  (68.75%)**. Lower than opus's "6 of 8" because `mine/top10` is Kaggle's daily top-rated dump
  (median ~2970), a broader population than literal rank-8, exactly as expected — not a
  discrepancy.
- **Land timing** (step of the 3rd `BUY_LAND` call among family-opening seats, proxy for "4th
  quadrant"): **median step 254, n=141** — matches opus's "253" almost exactly.

**This confirms the decode opus/opusb are building from is solid** — I have no red-team objection to
the underlying facts (family opening, land timing, diversification direction). My objection to A is
about validation and build risk, not about whether the target being imitated is real.

## 4. Architecture C (chassis + macro corrections) — the only one with a working gate

C is "cheapest, ceiling unknown" per the BRIEF, and it's the only architecture that can actually be
*measured* before 09-30 using an instrument this project already trusts (LINEAGE RR, §1). It also
inherits a real, if modest, track record: this project's closed history of incremental patches on the
current best chassis is **mostly negative** — T2 dead (shadowed by CXTB's own gate), T2E capped at
0.587 head-to-head (below the 0.74 bar), C1-D dead (0-13 vs shepherd mirror), C1-R2/C1-RS the one
partial success (beat C1 12-8 to 14-6 closed-loop, but the real-WLV holdout check showed only
+$70-73/game **our-bank** gain, below the project's own +$150 pre-registered bar — RR-mapped C1R2 at
2152 [2021,2294] still **failed** the CI-lower-bound->2148 promotion rule). That is the honest base
rate C should be judged against: roughly 1 partial pass in 6 attempts at "beat C1 closed-loop,"
and the one pass didn't clear the live-facing bar either. The decoded gaps (4th quadrant ~day 10-11,
~15-20 tomatoes, ~6 geese, ~9 carrots, ~21 not 33 strawberries — opus r4 Q2(b), independently spot-
checked above) are a more structural target than any previous patch (T2 touched one shop-count
threshold; this touches land timing and three crop/animal targets at once), which cuts both ways: more
surface area to actually move the $6-13k/seat gap, and more surface area to break something
(MISTAKES A4/C15: a land-timing change re-rolls shop draws (opus r4 §2.5 "cfx.py pitfall"), so any
land-timing test MUST pin shops the same way opus's `cfx2.py`/`kagsim.Game(seed, shops=...)` already
does, or it will silently confound the measurement with a different shop world, not the intervention).

## 5. Recommendation

**Primary bet: Architecture C**, built as opus's Q2(b) plan lays out (4th quadrant earlier, tomato/
goose/carrot targets, fewer strawberries), on top of whichever chassis currently clears the LINEAGE
RR bar (C1 or a C1 descendant) — not a from-scratch build. Gate it exactly the way this project
already gates everything that's passed review: paired closed-loop vs C1 and hyb2965 with shops
pinned across the intervention, pre-registered pass bar before the first result is read (see §6).

**Do not build Architecture A this round.** It has no instrument advantage over C (both end up
gated by the same LINEAGE RR / closed-loop-vs-C1 number) and a much worse historical hit rate
(0/72 from-scratch). If opus's macro-policy extraction yields a clean feature→decision table, hand
its *content* to C's build (the land-timing/herd targets), not a policy-imitation executor.

**Do not build Architecture B as scoped.** §2's arithmetic is not a soft judgment call — it's roughly
1,000-5,000× off between the engine speed this project has been implicitly assuming (kagsim) and what
a submission can actually run, and the resulting affordable envelope (≤8-10 decisions, ≤3-7 day
horizon, 2-3 branches) doesn't resemble a planner. If there's spare time after C is gated, a
narrow 3-day/2-branch lookahead at the 8 shop-unlock dawns, layered onto C, is inside budget and I
would not object — but it is an addition, scoped and time-boxed, not a parallel architecture with its
own track.

## 6. Kill tests

**+12h (2026-09-27 ~08:40 UTC):**
- **C:** does the macro-correction build exist, run 20+ closed-loop games without a single crash/
  refused-action storm (MISTAKES A4's "exact starting-cash bank = bug signature" check applies), and
  is its paired margin vs {C1, hyb2965} not already catastrophically negative (worse than -$3k/game,
  the size of T2's and C1-D's early kills)? If it's already there at n=20, kill now — don't wait for
  a bigger n to confirm what T2/C1-D already showed happens with bad early reads (project's own C16:
  a paired design needs ~14 games to see a ±$150 effect at real power, so 20 is enough for a
  directional kill call, not enough to promote).
- **B-as-addition (if attempted at all):** does a minimal forward-simulator prototype reproduce the
  real engine's dawn state bit-exactly on even a handful of test days? If not walking and matching by
  +12h, drop it — every hour after that is borrowed from C or A's build time for a component this
  round's own arithmetic (§2) already bounds tightly.
- **A (only if pursued despite §5):** is there an end-to-end, crash-free action stream from the
  imitation policy by +12h? If not prototyped and running by then, kill — the historical 0/72 base
  rate plus zero build headway by hour 12 of the runway leaves no realistic path to a validated,
  submittable file by 09-30 06:00.

**+36h (2026-09-28 ~08:40 UTC):**
- Whatever candidate(s) survive need a real LINEAGE-RR-class read: same seeds/anchors machinery as
  opus's r4 `rr.py`/`c1map.py`, n comparable to the 200-game screen that gated C1R2. **Promotion bar,
  unchanged from r4's adopted rule:** CI lower bound on the mapped rating > C1's point estimate + 60
  (currently ≈2148, will need re-anchoring if C1's live rating has moved by then — check
  `HANDOFF.md`'s latest live-read line before reusing 2148 verbatim). Equivalently, ≥0.74 head-to-
  head vs C1 (opus r4 07:47 UTC note: this maps to BT ≈ +378 given C1 is at +195). Miss this by +36h
  → the candidate is not a 3k narrative and should be evaluated purely as "does it beat hyb2965,"
  which is a much easier and separately useful question (BRIEF's actual upload bar for slot 2 is
  "not worse than C1," i.e. this same bar, not "beats hyb2965" — so a miss here is a real kill for
  the moonshot framing, not just a downgrade).
- **Crash-cleanliness is a hard non-negotiable by +36h regardless of economics**: `kaggle_load_check`
  clean plus one real official-env smoke test both seats (MISTAKES B1/B2: `__file__`-undefined and
  last-callable-selection bugs both shipped past a checker once already). A candidate that's
  economically promising but not yet crash-verified by +36h should not advance to the 09-29-09-30
  upload window — there isn't enough slack left to debug a packaging failure discovered at hour 60.

## 7. Probabilities

Conditioned on which architecture is actually fielded, since the answer is materially different by
architecture and pooling them the way a single P(3k+) number invites (exactly the C18 "pooled number
hides the collapsing tail" pattern this project has been burned by twice) would understate how much
this depends on staying on Architecture C:

| | P(3k+ \| fielded) | P(top-10 \| fielded) | P(beats C1 closed-loop) |
|---|---|---|---|
| **if Architecture C is fielded** (recommended) | **0.15%** | **0.25%** | **~25-30%** |
| if Architecture A is fielded instead | ~0.05% | ~0.1% | ~10% (no better instrument than C's, worse historical hit rate) |
| if Architecture B is fielded as scoped (against §2's advice) | ~0.02% | ~0.05% | ~5% (crash/timeout risk from an unproven simulator is a live way to score *below* hyb2965, not just fail to reach C1) |

**Basis for the C row, the one I'd actually act on:** P(beats C1 closed-loop) ≈25-30% is set by this
project's own base rate for chassis patches against C1 (§4: roughly 1 partial pass in 6 documented
attempts, and that one pass — C1R2 — still missed the live-facing +$150-our-bank bar and the RR CI
bar), nudged up slightly because this round's target (the decoded top-family gaps) is more
structural than any prior patch and is independently confirmed (§3) rather than guessed. P(3k+) and
P(top-10) stay near r4's consensus (opus 0.2%/0.5%, opusb 0.3%/0.5%, my own r4 0.1%/0.5%) because
nothing this round changes the fundamental finding those numbers were built on: the top tier is a
different agent class (reactive, shop-conditioned, cash-exact planning) at ~900 Elo above our
chassis family, and no instrument built in either round can validate a candidate against that
population before the deadline — "beats C1 closed-loop" and "is a 3k+ agent" are not the same claim,
and this round's own evidence (a partial promotion attempt on C1R2 that still missed the live-facing
bar; architecture B's hard budget ceiling) is, if anything, mildly negative relative to r4's priors
for the two harder architectures, which is why they sit slightly below r4's numbers in the table
above while C sits roughly in line with r4's C1R2 experience.

**What would change my mind:** a live C1 sub-band read (≥2400 slice specifically, per my r4 §3) that
comes in well above its RR mapping, or a closed-loop C build that clears 0.74 vs C1 at n≥100 *and*
holds up on a real (not proxy) holdout the way C1R2 did not. Neither exists yet as of this writing.
