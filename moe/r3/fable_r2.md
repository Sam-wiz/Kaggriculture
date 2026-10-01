# MoE r3 — Fable 5.1 round 2 (cross-examination)

Written 2026-09-25 ~19:50 UTC by the machine clock (`date -u`). My round-1 header said "09-26 ~01:00
UTC"; that was local time (IST). Deadline 09-30 23:59 UTC is ~124 h away, cut-off for uploads per
ROUND2 is 09-30 18:00 UTC (~118 h).

Scratch for this round: `/tmp/fable_r2/` (`wlmarket.py`, `wlunits.py`, `wlforce.py`, `wlhybrid.py`,
`wlhybrid2.py`, `saleprice.py`, `selllag.py`, `mkstreams.py`, `oracle.py`, `shep_oracle.py`,
`wlv_streams.json`, `oracle_out.json`). Orchestrator: please copy it to `moe/r3/fable_scratch_r2/`
as was done in round 1. ~12 CPU-min total, ≤2 workers at nice 10. I read `moe/r3/wlv_pull.md`
(negative: no public kernel reaches a full match; current WL kernels still diverge at step 53).

## 0. New evidence this round

**E1. Opus's WLV is my "(5,0)" family, and the record is 4-14, not 3-11.** The step-1 opening
`BUY_PRODUCT WHEAT 5, BUY_SEED WHEAT 1` (Opus `wl_games.json` "open") is exactly my fingerprint
(5 bought, 0 sold). My round-1 claim that it "matches no public agent we hold" was wrong: I ran five
candidates and none was WL-family. Running public WL (`rivals4/kaggriculture-yummers`) closed-loop in
the opponent seat against our tape on every WL-opening game (`/tmp/fable_r2/wlmarket.py`):

| opponent (R) | build | margin | first unit divergence vs public WL | first market divergence |
|---|---|---|---|---|
| ouga 2562, oycr 2552, Yin Li 2444, kwon 2441, zero waste 2435, ykhnkf 2420, Dom Bavuso 2405, ReCurSiON 2377, techtech69 2301, ShadowT_T 2283, 胜你 2281, 小娃娃 2243, Kamma 2189, HireMe 2179 | Opus's 14 | 3-11 | **53** (14/14) | **57** (14/14) |
| Maxy5illion 2048 (×2), ekkkcz 2038, M.Y.C.E.L.I.S 2036 | 4 more | 1-3 (+193, −394, −179, −37) | **53** (4/4) | **57** (4/4) |
| AcidicBlaster 2100 (×2) | public WL itself | **2-0** (+806, +1363) | 383 | 169 |

So WLV is 18 games at 4-14 (0.22), mean margin −$448, team ratings 2036-2562 (median 2282 with the
four sub-2100 teams; Opus's 2391 was over the 14). Both medians are matchmaking-selected; the
head-to-head implies ~+220 over us, which stands. The near-exact public ancestor we beat 2-0.

**E2. WLV's market layer is private, and it is a v9-family sibling, not WL's wrapper.** The
deconfounded test (`/tmp/fable_r2/wlhybrid.py`, kagsim, 14 tapes): the candidate computes its
MARKET orders closed-loop from the true observation, but its UNIT ops are replaced each tick by WLV's
recorded unit ops, so the farm state is WLV's by construction. Agreement with WLV's recorded market
stream:

| candidate market policy on WLV's exact farm | exact market-list agreement | sell-event-set agreement | sell-set agreement t≥300 | our recorded tape's margin vs it |
|---|---|---|---|---|
| public WL (yummers) | 0.792 | 0.870 | **0.787** | **+2,556** |
| shepherd | 0.820 | 0.895 | 0.831 | +814 |
| hyb2965 | 0.847 | 0.912 | **0.858** | +670 |
| (recorded WLV) | 1 | 1 | 1 | **−546** |

Public WL's market is the *furthest* of the three from WLV's, and it diverges at **step 91 at
identical state** (WLV: `SELL WHEAT 3`; WL: nothing) in 12/14 games. The v9-family markets match
WLV exactly through step 90 apart from the opening (`wlhybrid2.py`). Their differences from WLV,
in order of appearance: `SELL WHEAT 3` at t=91; empty `[]` orders stripped (our own recorded tape
carries `[]` in 69/720 steps, so the platform does not strip them — it is WLV's wrapper); market
slot order swapped (`BUY_PRODUCT WHEAT` ahead of `SELL WOOL` at 150/152/196); WOOL 2 sold at 156
where we sell at 165-166; buy quantities (WHEAT 5 vs our 3 at t=252, 7 vs 14 at 249, 24 vs 48 at
296); then **22-94 differing steps per game in d13-24 and 25-77 in d25-29** (shepherd; hyb2965
similar). That late block is where the money is (round 1 §1b) and it is opponent-conditioned.
WLV's market beats hyb2965's market on the same farm by ~$1.2k/game.

**E3. What the herd layer explains, and what it does not.** Forcing public WL's hand 0 to PASS at
53-58 and 84-91 (`wlforce.py`) moves the market divergence from 57 to 91 (12/14) or 121 (2/14): the
step-57 divergence was state-driven, so Opus's herd-layer reading of the *farm* is right. But public
WL keeps its herd (17 animals at end in 13/14 closed-loop games, `wlunits.py`); the "$2k private
delta" is the market channel, not herd survival. Public WL also over-orders (MILK sell orders ~1,200
units/game vs WLV's ~200): order quantities are not fills (HANDOFF 09-20j trap), so my
`saleprice.py` table is order-based and I use only sell-event sets above.

**E4. The PREDICT refresh has a measured ceiling against WLV.** Shepherd ships a dormant
whole-library forecaster (`_v92_predict2`, `subW_shepherd.py:3586-3720`): `path = None  # Frozen
offline build`, so it loads zero streams in production. I built WLV's premium-sale streams from the
18 tapes (`mkstreams.py`, format `[{"ep", "ev": [[tick, item, qty]]}]`), pointed the layer at them
via env var (`shep_oracle.py`, two lines changed), and replayed shepherd as the **live** agent
against each WLV tape open-loop (`oracle.py`, Python harness, 2.3 s/game). The built-in
`_V92_EP` parity holdout excludes same-parity episodes, i.e. the game's own stream.

| arm | library | mean Δ vs vanilla | losses→wins / wins→losses | record vs 18 WLV tapes | our-bank Δ | their-bank Δ | fires/game |
|---|---|---|---|---|---|---|---|
| vanilla | none (production) | — | — | 5-13 | — | — | 0 |
| oracle | 18 WLV streams incl. own game | **+$1,242** | **8 / 0** | **13-5** | +613 | −629 | 11-17 |
| holdout | 9 other-world WLV streams | **+$628** | **4 / 0** | **9-9** | +376 | −251 | 5-21 |

Vanilla reproduces the recorded margin to the dollar in all 13 shepherd-seat games (the 5
hyb2965-seat games have shepherd substituted). Telemetry (`_V92_Q_REPORT`) confirms the layer fires.
Caveat, stated: the rival is open-loop, so the their-bank half is the flattered part; the our-bank
half (+$376 holdout) is the conservative number. The holdout library is only 9 streams from other
shop worlds; the real refresh has 18 WLV + ~28 WLV games in the 09-23/24 corpus (Opus E3) + the
other families.

**E5. Mechanism check.** Sell-set agreement us-vs-WLV on the recorded tapes is 0.901 (0.842 at
t>300), the same distance as E2's shepherd-on-WLV-farm, consistent. Premium sells on a DROP/PLACE
tick: us 915, WLV 938 → not a same-tick trick. Order-based unit lag: WLV sells the k-th unit ≥5
ticks earlier on 2,979 unit-pairs vs our 1,493; ±1-2 ticks 530 vs 416. WLV sells earlier in the
window, not one tick ahead — scheduling, consistent with (unproven) forecasting of us.

## 1. Agree

- **Opus §3 / my F1:** pre-deadline rating is worth ~0; the convergence freeze is void; both slots
  are probes; ≥8 h between uploads; fixed-snapshot MLE reads with a family split; final pair = best
  measured + best from a different family; last upload ~14:00 UTC 09-30 with an 18:00 buffer.
- **Opus §2:** exact-opponent closed-loop is valid (2/2 to the dollar); ancestor-proxy fails (1/11).
  I reproduce the spirit: public WL loses to our tape on 18/18 seeds where WLV beat us (E1/E2).
- **Opus E3:** WLV is one private agent and our largest loss source; my 18-game count extends it.
  Its farm is the shared pipe16-lineage tape plus herd-idle layers (E3 confirms the step-53 idle
  is what shifts the early market divergence).
- **Claude §1:** the band is the shepherd farm plus private market overlays; "verify a layer fires"
  — I did (telemetry, E4). Claude Code's `wlv_pull.md`: Opus #1 (exact WLV) is dead.
- **All three:** the public-pool gate and open-loop replay-substitution rank nothing that touches
  market timing. Whisker layers (BRX2, delivery, koshinm cell) are below live resolution.

## 2. Dispute

**Opus — weakest claim: "WLV ≈ WL market/opening wrapper + herd layers; rebuild from yummers,
keep WL's opening and market wrapper, graft shepherd's layers" (opus.md E3, §4 note B).** E2
refutes the market half: on WLV's own farm WL's market agrees with WLV's *less* than shepherd's or
hyb2965's, and differs at identical state from step 91. The recipe reproduces the farm (which
hyb2965/shepherd already match at 0.97-1.00) and the wrong market; Opus's own gate (median
first-divergence ≥600) would fail at the first d6-12 difference. The rebuild is only alive from the
hyb2965 side, and the part that matters (50-170 differing steps/game in d13-29) is
opponent-conditioned and not recoverable from 18 tapes without the code. Smaller points: the "$2k
stronger than its ancestor" is entirely market (E3); "median 2391" is 2282 on all 18 and
matchmaking-selected either way; E1's "hyb2965 0/2 vs 2600+" games are 0%-identity private agents,
not the band.

**Claude — weakest claim: "X is plausibly one of the public market overlays we hold" (claude.md
§2.1).** Dead by Claude's own pilot (best 0.74-0.90, all diverge at step 0-1) and by E2 (the closest
public market, hyb2965's, is 0.86 sell-set agreement at identical state). With no identified
population, §2.2's closed-loop tournament has no opponents. §3's "re-upload shepherd if B is worse"
protects nothing: a re-upload is a new id starting at 600, and the pre-deadline number has no final
value. The 09-28 freeze is withdrawn by all.

**Fable (self):** "(5,0) matches no public agent we hold" — wrong (E1). "C1 confidence 0.30" was a
guess; it is now a measured open-loop ceiling with an unmeasured reaction discount (E4). The hybu
probe "now" — withdrawn (§3).

## 3. Changed my mind

1. **WLV identity.** It is the WL-opening family with a private v9-sibling market. Opus identified
   the family; I mislabelled it private end-to-end. The private part is the market only.
2. **Probe now: no.** Round 1 said upload hybu immediately because C1 was 3-5 h away and unmeasured.
   C1 now has a measured ceiling and is ~4 h from upload-ready (streams + variant exist). The
   shepherd slot should go to C1, not to a probe whose 6-h partial read is unreadable (SE ±65 needs
   ~35 band games ≈ 16 h). hybu is filler only if C1 fails its kill test.
3. **C1's remaining risk is reaction, not the library.** E4 shows pre-emption works against WLV's
   tape whether or not WLV forecasts us. The validation that matters is the price-reactive rival
   (tier-1 SCL), not more library engineering. My round-1 V2-V5 ordering is reduced to that one check
   plus the live read.
4. **hyb2965 stays a finalist candidate in its own right.** Max Fofanov's team runs exact hyb2965
   at 2234 (Opus E2) — the bronze line; replay outcome correlation with shepherd is 0.50 (HANDOFF
   09-25i). I withdraw "stop calling it a hedge".
5. **The clock.** ~124 h to the deadline, not four days.

## 4. Deciding experiment (≤3 h, ≤2 workers, no submissions)

**Disagreement:** first build = WLV rebuild (Opus #2, now necessarily from the hyb2965 side) vs
PREDICT2 refresh (C1). Run both arms in parallel, one worker each, 3-h cap.

**Arm C1-full (Fable, worker 1).** Extract premium-sale streams for every ≥2200 post-lock rival
tape: the 28 mirror tapes + the 291 ≥2200 games in `moe/opus/eps_index.json` (exact replay, ~1 s/game
≈ 6 min; format as `mkstreams.py`). Embed as a compressed blob; keep the `_V92_EP` parity holdout.
Score shepherd+PREDICT2 vs (a) the 18 WLV tapes, (b) the 28 ≥2200 mirror tapes, open-loop
(2.3 s/game); then (c) the same with a price-reactive rival: each recorded rival lot waits up to
W=12 ticks while that product's price index is below 0.9× its recorded fill index (δ=0.10), so a
pre-empted rival can decline to dump.
- **C1 is right if** on (b): mean Δ ≥ +$400/game, losses→wins ≥ 8 of 22, wins→losses ≤ 2; **and** on
  (c) the our-bank component keeps ≥ 60% of its open-loop value. Then C1 is the first upload.
- Prediction: (b) passes (already 4/13 flips with 9 streams); (c) is the risk — 55%.

**Arm R (Opus, worker 2).** hyb2965-side graft: (5,0) opening, empty-order strip, slot-order rule,
WOOL at 156, buy-quantity rule; bisect against the 18 WLV tapes with per-channel first-divergence
(`exact2.py` style, market channel separately).
- **Opus is right if** ≥10/18 tapes reach ≥600-step market match **and** shepherd-vs-R closed-loop
  loses ≥10/18 on those seeds (retrodiction). Then R is the first upload (it is exact WLV).
- Prediction: R stalls in d13-24 (opponent-conditioned block) — 20%.

Both pass → C1 first (ready sooner), R second the same evening. Both fail → hybu as filler,
finalists = hyb2965 + best live read.

## 5. Revised plan, owners, timeline

Claude Code is the only participant with credentials; every upload below is theirs, gated by
`kaggle_load_check` + official-env smoke both seats. Uploads ≥8 h apart. Times UTC.

| # | build | owner | expected | kill / read rule |
|---|---|---|---|---|
| 1 | **C1: shepherd + PREDICT2 refreshed with all ≥2200 post-lock streams** (+ WLV's 18). Optionally re-encode the P library (`_V92_P_BLOB`, 64 worlds, 2,398 streams — decoded, format known) with post-lock streams; PREDICT2 alone suffices for the first upload | Fable builds; Claude Code uploads | vs WLV 0.22→≥0.40; vs ≥2200 0.21→≥0.33; ~+60-100 if reaction halves E4 | §4 arm C1; live: W-L vs ≥2200 on a fresh LB snapshot, ≥12/24 PROMOTE, ≤7 KILL, sanity ≥0.85 vs <2000, zero errors |
| 2 | **C2: hyb2965 + the same library** (hyb2965 carries the identical dormant layer, `path = None` at `subX_hyb2965.py:3590`) | Fable/Opus build (+1 h); Claude Code uploads | same mechanism on the base whose market is closest to WLV's (E2) | same; natural second finalist, correlated with C1 (choose by family split of the read) |
| 3 | **R: hyb2965-side WLV market rebuild** | Opus | exact WLV if it passes | §4 arm R; drop at 3 h |
| — | hybu probe | Claude Code | filler only | only if C1 fails §4 |

**Pre-deadline episodes in the final fit — how sure.** `context.md:41` ("Games will continue to
run for approximately two weeks to continue to reduce uncertainty… A final Bradley-Terry tournament
will be run on those episodes"), staff `discussions.md:103`, and two unanswered forum questions
(`:128`, `:139`). I read "those episodes" as the two-week window: **55-60% post-deadline only.** It
is decision-invariant: only the final two submission ids score under either reading; a probe's games
never count; a 09-30 re-upload has only post-upload games either way; and eviction-by-recency means a
finalist uploaded early cannot be kept alive through probes (each probe evicts the older id, a
re-upload is a new id). Under the full-history reading the cost is ~800 fewer games in the fit
(CI ±40 → ±35 Elo), no bias. Not worth planning around.

**Timeline (now 09-25 19:50 UTC):**

| when | action | pair after |
|---|---|---|
| 09-25 20:00-23:00 | Fable: C1-full streams + leave-one-out + tier-1 check (§4). Opus: arm R. Claude Code: fetch fresh episodes + LB snapshot at ~23:00 | [shepherd, hyb2965] |
| 09-25 23:00-01:00 | C1 passes → Claude Code load-check, official smoke, **upload C1** (evicts shepherd; its read is complete at 89 games). Write the live prediction next to the upload | [hyb2965, C1] |
| 09-26 09:00 | read 1: C1 ~70 games / ~20 band; hyb2965 ~170 games (read complete) | |
| 09-26 17:00 | read 2: C1 ~120 / ~40 band → PROMOTE/KILL. **Upload C2** (or R if it passed §4 and C1 did not) — evicts hyb2965 | [C1, C2] |
| 09-27 09:00 / 17:00 | read C2 at +16 h; C1 at +40 h. Upload probe 3 (R or hybu) at 17:00, evicts C1 (noted, file on disk) | [C2, P3] |
| 09-28 09:00 / 17:00 | reads; probe 4 at 17:00 if a candidate with plausible ≥+100 exists; else hold | |
| 09-29 17:00 | last probe read; choose finalists by family-split mirror record, fresh snapshot | |
| 09-30 08:00 | **re-upload finalist A** (best read) after load-check + official smoke | |
| 09-30 14:00 | **re-upload finalist B** (best of a different family: hyb2965/C2 if A is C1) | final pair |
| 09-30 18:00 | freeze; crash replacement only | |

If C1 fails §4 by 23:00: upload hybu as the probe at ~01:00 and continue R; finalists default to
hyb2965 (never evicted until 09-26 17:00, then re-uploaded) + the best of {shepherd, R, hybu}.

**Stop (unchanged from round 1, plus):** stop the WL-side rebuild (E2); stop identifying band agents
against public overlays (Claude §2.1); stop reading the displayed rating; stop the 09-28 freeze.

**Not verified:** the reaction discount on E4 (arm C1 (c)); whether WLV forecasts us (E5 is
suggestive only); the medal thresholds remain the standard Kaggle rule plus forum remarks; the
`_V92_EP` holdout used 9 streams, a weaker library than the real refresh.

P(top-10): 0.5%  P(silver): 7%  P(bronze): 40%
