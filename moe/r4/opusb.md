# MoE r4 — opusb (Opus 5.5 #2, BUILD lane), round 1

Clock: started 05:16 UTC 09-26 (`date -u`); written 06:00-07:05 UTC (§6 appended later). ≤2 workers, nice 10, kagsim (bit-exact).
No submissions. Everything I ran is in `moe/r4/build/opusb/` (scripts + jsonl). One decode output landed in the repo
root by accident at 05:20 and was moved into my dir within a minute; one scratch file was written to and deleted
from /tmp. Items still running when this was written are marked PENDING and will be appended below §6.

## 0. Bottom line

1. **The top teams' edge over our chassis is shop-world-conditioned planning, and it is huge.** I played recorded
   top-team seat streams ("tapes") as *our* agent against C1 closed-loop (C1 reacts; the tape is the candidate, so this
   is not the C18 trap). With the shop sequence **pinned to the tape's own recorded world**, the four robust teams'
   tapes (Boey, 吃白饭的大肥鱼, THIRD FARM CLUB, Majkel1337) **beat C1 in 25 of 28 worlds, median +$15.1k**. The *same
   tapes* in natural (re-rolled) shop worlds win **5/56, median −$36.8k**. C1 banks ~$113k in both conditions; the tape
   banks $117k in its world and $77k out of it. Nothing else we have measured moves money like this.
2. **So "build a submission from the top-10 tapes" fails, for a measured reason.** Raw tapes on fresh seeds: **8/125
   (6.4%)**. A V45-style router over THIRD FARM CLUB's routes (shared day 0-5 prefix, switch at dawn 6 on the first two
   shops): **16/66 (0.24), −$14k/g**. The world re-rolls because the engine's daily RNG draws once per empty tile on
   *both* farms before choosing the shop, so a different opponent re-rolls shops from day 3 on, and only 2 of 8 shops
   are known at the router's switch. Five of eight teams' tapes additionally collapse because their plans are
   cash-lean (dawn cash $4-$800 through day 8): a $4 price change from C1's opening buy makes HIREs/BUYs fail and
   cascades into ~2,400 dead actions (DSM trace, §2).
3. **Q1 answer:** a 3k agent re-plans production as each shop unlocks (days 3, 6, 9, 12, …). Our chassis re-plans once
   (step 144, first two shops) plus a few demand-gated annexes. E-shop2 sizes the lever by day (robust teams' tapes vs
   C1, n=56 per arm, pinning only the first k shops of the tape's world): **k=0 WR 0.09 (−$36.8k); k=2 0.50 (+$0.1k);
   k=4 0.89 (+$11.8k); k=6 0.89 (+$13.8k); k=8 0.89 (+$15.1k)**. Fitting the first four shops (known by day 12) carries
   essentially all of it. Nothing on our chassis captures it; a planner that does is a new agent. **P(3k+) 0.3%.**
4. **The one tape construction that could follow the world — a shop-prefix tree router — is also dead, measured.**
   Idea: at each dawn a new shop appears, splice onto a recorded game of the same team whose shop prefix matches and
   whose recorded farm state matches ours (dawn splices are positionally safe). THIRD FARM CLUB (241 replay-exact
   games, all 64 first-two pairs covered) is the best-covered robust team. `statecompat.py`: at dawn 6, 72% of game
   pairs are state-identical (≤2 tiles); at dawn 9, games sharing the first two shops already differ by a **median
   13.5 tiles** (19% within 2); 3-shop prefixes hold **1.3 games each** (192 prefixes / 241 games). My pre-registered
   kill (depth-3 coverage < 50%) fires. The data needed to follow the world through recorded plans does not exist.
5. **Q3 builds on the C1 chassis:** **C1-R2** (C1 + 324 WLV-proxy streams in the PREDICT P library, 5-line diff)
   **passes a pre-registered closed-loop gate**: beats C1 12-8; paired over C1 +$534 vs R2S, +$372 vs WL+S2, +$677 vs
   hyb2965, +$310 vs shepherd; 0 errors; load check OK. **Against the 18 real WLV tapes (holdout, open-loop) it adds
   +$244/g but only +$70 on our own bank (14/18 better)** — below my pre-registered +$150 our-bank bar, so the proxy
   gain was mostly circular (§6). Not handed over as a probe; best C1-family variant if one is wanted anyway.
   **C1-D** (shift our premium-sale ticks to dodge band forecasters) is **dead: 0-13 vs the shepherd mirror, −$12.3k
   paired** — in a mirror, whoever sells first wins.
6. **Instrument findings:** (a) tape proxies of top teams cannot retrodict — C1 beats frozen top tapes ~94% on natural
   shops while the live teams sit ~900 Elo above C1; any TOP-SUB-style gate is dominated by the opponent tape
   breaking (−$40k on Boey in `opus/sub1`). (b) Two harness bugs caught, one mine, one in r3 (§3): the `_V92_EP`
   parity holdout also disarms the P library on odd episodes. (c) Any open-loop check on the 18 WLV tapes run
   *without* a holdout flatters C1-family builds by ~$600/g, because C1's PREDICT2 library holds those games' own
   streams (C1 vs real WLV: +$820 without holdout, +$210 with).

## 1. The three questions, from the build lane

**Q1 — how do we move to 3k+?** Measured decomposition (E-shop, §3): our chassis is *world-robust but world-blind*;
top plans are *world-fitted*. In the tape's own shop world a top plan beats C1 by ~$15k; out of it, it loses by ~$37k.
The live top teams presumably get most of the upside and none of the downside by re-planning at each shop unlock.
That is the 900-Elo gap. Market timing is not it: our captured/held price ratio is *higher* than theirs on
MILK/STRAWBERRY/MELON (decode lane's `mskill`, 188 top seats vs 168 of ours). What their plans do differently, and
what a re-planner would have to choose per world: product mix (fewer premium units, 2-9× more EGG/TOMATO/CARROT, i.e.
supply what this world's shops demand and what the opponent is not flooding), land 2-3 days earlier (SW at ~199-225
vs our 265), and no idle cash. A from-scratch re-planning agent at tape-level execution efficiency is not buildable
and validatable by 09-30 (our v1-v31 from-scratch agents went 0/72 vs rivals). Realistic targets are bronze/silver
through the band, where the measured lever is the PREDICT library (r3 E-A +$1.3k/g; C1-R2 below).

**Q2 — decode the top-10 and build a submission from them.** Everything is recoverable except the policy off its own
trajectory — and that is exactly what a submission needs. Built and measured: raw tapes 8/125; own-seed tapes vs C1
8/40 (T1); THIRD FARM CLUB router 16/66. None is a submission. The one construction that can use recorded top plans
*and* follow the world as it unfolds is the tree router (§0.4), and it fails on coverage and state divergence. **My
Q2 deliverable is therefore a measured negative plus the decomposition that explains the top-10 (world-fitted
plans), not an upload.** Anything uploaded "from the top-10 tapes" would be a several-hundred-Elo regression.

**Q3 — a build for the private field + an instrument that retrodicts.**
- *Top private agents (2,800+)*: we rarely meet them at our rating, and no closed-loop proxy exists (tapes collapse or
  are out-reacted, and they cannot re-plan). Nothing should be gated against top-team tapes as opponents.
- *The band (2,000-2,600), which decides bronze/silver*: public chassis + private market layers with PREDICT libraries.
  The r3 proxies (R2S, WL+S2) match the band's aggregate strength vs shepherd, not per game. C1-R2 is gated against
  them and our live builds (§3). **Retrodiction rule I propose:** C1 was promoted by this same instrument class
  (closed-loop gate (d) 0.90/0.80; open-loop gate (b) +$914/g). Before C1-R2 or any other PREDICT-class change is
  promoted on offline evidence, C1's live band record must confirm the class: C1's fitted rating vs ≥2000 opponents
  ≥ shepherd's ~2160 + 50 at ≥30 such games. If it does not, the instrument over-predicts market layers and C1-R2
  inherits that failure.

## 2. Method — how I reverse-engineer a recorded game (tested on the dump)

Recoverable from a replay: both seats' action streams, seed, final banks, shop draws; exact replay then gives every
fill, price, stock, shed, seeds, cash, hires and kagsim's failure telemetry (`Game.telemetry(p)`: dead actions,
refused buys/hires/land, escapes, dry plants, discards) at every tick. Not recoverable: the policy's response to any
state it did not visit. So the method is to *move the trajectory* one factor at a time and measure what breaks:

| step | what | tool | tested on |
|---|---|---|---|
| 1 | exact replay of both recorded seats; banks must match to the dollar | `t1.py` arm `rec` | 40/40 top seats |
| 2 | swap only the opponent (C1, closed-loop) on the recorded seed | `t1.py` arm `own` | 40 seats, 8 teams |
| 3 | move the tape to other seeds | `t1.py` `xseed`, `t2.py` | 40 + 125 games |
| 4 | first-divergence trace: per-step cash, hands, refusals, shops, tile diff vs the recording | `t1trace.py` | DSM 113067521 s1 |
| 5 | pin the shop sequence (`kagsim.Game(seed, shops=[...])`, prefix pins allowed) to separate world mismatch from opponent/market effects | `eshop.py` | 36 tapes, 180 games |
| 6 | turn recordings into a candidate (router over a team's routes) and gate it closed-loop | `t3.py`, `mkspec.py` | THIRD FARM CLUB, 66 games |
| 7 | state compatibility of recorded games at each dawn, grouped by shop prefix (tree-router feasibility) | `statecompat.py` | 241 THIRD FARM CLUB games: dawn 6 72% ≤2 tiles; dawn 9 (same 2 shops) median 13.5 tiles; dawn 12 (same 3) median 22, 1.3 games/prefix |

**Worked trace (DSM, ep 113067521 seat 1, own seed, C1 instead of DECEM):** cash differs by $4 at t=1 (C1 bought 20
wheat at t=0); refused hires 7 vs 5 by t=48; the shop sequence re-rolls by t=96 (day 4); 47 tiles differ by t=240;
dead actions 2,438 vs 37 at t=672; bank ~1/3 of the recording. Units respawn every dawn, so damage is never
positional — it is inventory (a refused BUY_ANIMAL/BUY_SEED leaves PICKUP/PLACE/FEED/PLANT ops dead for the game).

**Engine facts used (checked in `kaggriculture.py` / kagsim):** `_end_of_day` builds `Random(seed*1_000_003 ^ day)`
fresh each day and draws once per empty unlocked tile, player 0 then player 1, then the shop; so the shop depends on
both farms' empty-tile counts that day. Units respawn at dawn (splices at step%24==0 are positionally safe). Market
slots are processed in lockstep by slot index, unit by unit, at a shared quote. **New:** with the shop sequence pinned,
kagsim games are effectively deterministic — weeds still vary by seed but land on tiles nobody uses, so two seeds
gave bank-identical games. *The seed matters almost only through the shop sequence.* (Consequence for the E-shop
counts: each pinned tape is one world; I count distinct tapes, not rows.)

**Per-team transfer profile (T1 own/other seed, vs C1) and E-shop (natural vs own world pinned, vs C1):**

| team | own seed: bank kept / W | other seed: bank kept / W | dead actions | natural shops W, median | own world pinned W, median |
|---|---|---|---|---|---|
| 吃白饭的大肥鱼 | — | — | 12-140 | 2/16, −$30.1k | **8/8, +$18.9k** |
| Boey | 0.86 / 3-2 | 0.79 / 3-2 | 64-146 | 2/16, −$18.9k | **6/8, +$16.1k** |
| THIRD FARM CLUB | 0.93 / 4-1 | 0.91 / 1-4 | 0-70 | 0/16, −$44.4k | **7/8, +$17.7k** |
| Majkel1337 | 0.87 / 0-5 | 0.86 / 0-5 | 95-1,579 | 1/8, −$44.4k | **4/4, +$8.5k** |
| DSM | 0.71 / 0-5 | 0.54 / 0-5 | ~1,800 | 0/8, −$108.9k | 0/4, −$89.0k (collapses) |
| Vadim Vasilenko | 0.48 / 0-5 | 0.60 / 0-5 | ~1,700 | 0/8, −$72.0k | 0/4, −$75.3k (collapses) |
| M & M & P & Q | 1.14 / 1-4 | 0.98 / 1-4 | 16-1,727 | — | — |
| Unknown Mother-Goose | 0.45 / 0-5 | 0.44 / 0-5 | ~2,200 | — | — |
| mtmr_s1 | 0.33 / 0-5 | 0.11 / 0-5 | ~1,900 | — | — |

Cash lean-ness predicts fragility: dawn cash d1-d8 (median) DSM 5/57/18/9/279/716/66/160, Vadim 4/40/18/108/336/745/60/162
vs us (live) 19/101/214/276/685/798/1,124/542; at d10 top teams hold $6-8.5k, we hold $16k.

## 3. What I built, gates, retrodiction

| candidate | what | gate (closed-loop, kagsim) | result | verdict |
|---|---|---|---|---|
| raw top tapes (`t2.py`) | 63 seat streams from the 09-25 dump, 2 fresh seeds each (one per seat); screen stopped once decisive | vs C1 | **8/125 (6.4%)**; 93 collapsed runs (≥300 dead actions) 0 wins; 32 held 8 wins, median −$24k | dead |
| TFC router (`t3.py`, `spec_tfc_*`) | modal step 1-144 prefix (129/241 games identical), switch at dawn 6 on first two shops; route = best recorded bank (or margin) | vs C1, 20 fresh seeds × 2 | bank **10-30, −$14.5k (SE 3.5k)**; margin 6-20, −$13.3k | dead |
| C1-D2 / C1-J3 (`mkdc.py`) | outermost layer on C1: defer native MILK/WOOL/STRAWBERRY sells 2 ticks (or jitter 1-3), never PREDICT dumps; `[]` holes keep slot priority; fires ~122 orders/g, 0 errors | vs shepherd, 10 seeds × 2 | **0-13, −$11.5k; paired vs C1 −$12.3k (SE 1.0k), 0/13** (our bank −$3.2k, mirror +$9.1k) | dead |
| **C1-R2** (`cand_C1R2.py`, md5 b8919bed) | C1 with shepR's P library (shepherd's f9af + 324 WLV-proxy R2 streams); 5-line diff | §3b | **beats C1 12-8; paired over C1 +$534 / +$372 / +$677 / +$310** (R2S / WL+S2 / hyb2965 / shepherd); **vs 18 real WLV tapes: no holdout +$8 (our-bank −$75); with holdout +$244 (our-bank +$70)** | passes the pre-registered gate; real-WLV holdout +$244 margin / **+$70 our-bank** (< +$150 bar) → **not handed over** |
| C1-RS (`cand_C1RS.py`, md5 ae884dde) | C1-R2 + 324 shepherd streams in the P library (W1's "WL+S" arming, aimed at the shepherd-chassis band); 6-line diff | same cells | **beats C1 12-8 (+$351, SE 165); paired over C1 +$472 / +$401 / +$632 / +$449** (R2S / WL+S2 / hyb2965 / shepherd, 14/20); 0 errors; load check OK; real-WLV holdout +$184 (our-bank +$73) | passes the §3b legs; same real-WLV shortfall → **not handed over**; the more balanced of the two variants |

Baseline reproduced: C1 vs shepherd **18-2, +$596 (SE 76)** on seeds 9400001-10 (r3 gate d: 36-4, +$813).

**Harness bugs (disclosed).** (1) Mine: the first gate run set the `_V92_EP` parity holdout on *both* modules. The
same global filters the P library, whose streams carry `ep=-1`, so on odd episode ids (6 of the 14 WLV seeds) it
silently disarmed both sides' P forecasters — including WL+S2's appended shepherd streams, the arming the proxy exists
for. It read C1 vs WL+S2 13-1 (+$1,690). Fixed in `gate.py` (holdout on the candidate only, its P forecaster
shielded), verified on an odd episode (both P layers fire, 16 / 10), contaminated rows moved to
`gate_bug_ep.jsonl`; rerun C1 vs WL+S2 **11-3, +$934** (r3: 11-3, +$824). (2) r3: `moe/r3/build/opus/c1test.py` set
`ma._V92_EP` on C1, so C1 played the 6 odd WLV games *without its P library* — r3's C1 vs R2S 10-4 / vs WL+S2 11-3
are biased against C1, not for it. Fable's gates (b)/(c) edit the PREDICT2 cache directly and are unaffected.
(3) Operational: my first chain scripts waited with `pgrep -f <pattern>`, which matches the waiting shell itself, and
spun for 35 min; killing a pool parent orphans its workers. All reaped by explicit PID; replaced by a plain sequential
script (`chain3.sh`).

### 3b. C1-R2 gate (pre-registered before results)
Pass iff all of: (i) paired vs C1 ≥ +$150/g against R2S and WL+S2, (ii) ≥ 0.50 head-to-head vs C1, (iii) no cell
(hyb2965, shepherd) more than $150/g below C1 paired, (iv) PREDICT fires/errors comparable, (v) `kaggle_load_check` OK.

| opponent | C1 (baseline) | C1-R2 | paired C1-R2 − C1 | better | our bank / their bank |
|---|---|---|---|---|---|
| R2S (WLV proxy armed with shepherd streams), WLV14 | 11-3, +$726 | **14-0, +$1,260** | **+$534 (SE 152)** | 11/14 | +168 / −366 |
| WL+S2 (public WL + ~5 shepherd streams/bucket), WLV14 | 11-3, +$934 | 12-2, +$1,307 | **+$372 (SE 135)** | 8/14 | +216 / −156 |
| hyb2965 (live), fresh 20 | 14-6, +$531 | 16-4, +$1,208 | **+$677 (SE 159)** | 18/20 | +296 / −382 |
| shepherd (public mirror), fresh 20 | 18-2, +$596 | 18-2, +$906 | +$310 (SE 168) | 10/20 | −54 / −364 |
| **C1 head-to-head**, fresh 20 | — | **12-8, +$257 (SE 187)** | — | — | — |

Telemetry: P fires 15.5/g (C1 16.0), PREDICT2 5.1/g (C1 7.4), **0 errors in 88 games**. (i)-(iv) PASS; **(v) PASS**
(`loadcheck_C1R2.log`: seeds 7/1/42 DONE both seats, real `kaggle_environments` run DONE/DONE; C1-RS likewise).
Reading: the R2 streams are hyb2965-family, so C1-R2 forecasts hyb2965-chassis opponents best (hyb2965, R2S/WLV);
against the shepherd chassis the gain is mostly their-bank and only 10/20 games improve. Caveats: (a) R2S is built
from R2, so the WLV14 cells partly measure forecasting the proxy with its own family; the check against the **real**
18 WLV tapes (open-loop, our-bank half) is PENDING (`openwlv_b.py`). (b) Same instrument class that promoted C1. (c)
Same chassis and mechanism as C1 — not a hedge for C1.

## 4. Next 12 h (UTC)

1. **Now → ~08:00:** C1-RS closed-loop gate (running, `chain5.sh`). Done this round: load checks, state test, real-WLV
   checks (with/without holdout), E-shop2.
1b. **What E-shop2 implies for our chassis (already answered by the data):** C1's own bank is flat at $107-115k in
   every arm, so our chassis neither gains in a favourable world nor loses in an unfavourable one. The lever lives
   entirely in plan choice at days 9-12, which our first-two-shop routes cannot express. No cheap build on C1 reaches it.
2. ~~Tree router prototype~~ — killed by the state test (§0.4). Revisit only if the streaming dump yields ≥5 games per
   3-shop prefix for one robust team (it will not: 512 prefixes).
3. **By 09:00:** C1-R2 passed (v) but not the real-WLV check (+$8/g). Only if the holdout rerun shows ≥ +$150/g
   our-bank over C1 vs the real WLV tapes do I hand it to Claude Code as a probe (still conditional on C1's live read,
   §1 Q3). Otherwise my lane has no upload candidate this round, and I say so. Sonnet owns the pairing decision.
4. **When C1's live games are fetched:** retrodict gate (b) (+$914/g) and gate (d) against C1's live band record.
5. Not doing: tape surgery on our chassis (−15k, 09-18d), sale-tick decorrelation (dead), top-stream PREDICT libraries
   (we rarely meet the top; unrelated streams disarm the forecaster, r3 W1 WL+O −$460/g).

## 5. Probabilities (final standing)

P(3k+): 0.3%  P(top-10): 0.5%  P(silver): 7%  P(bronze): 38%
These are unchanged from r3 because nothing I built changes the live picture yet: C1-R2 is a library increment on
C1 (closed-loop +$250-680/g over C1, i.e. at most a few tens of Elo if it transfers), and every top-10-derived
construction measured below C1.

## 6. PENDING results (appended as they land)

**06:55 UTC — C1-R2 vs the REAL WLV tapes (`openwlv_b.py`, 18 live WLV games, open-loop, no holdout):**

| arm | W-L | mean margin | vs C1 | our-bank | their-bank | games better |
|---|---|---|---|---|---|---|
| C1 | 14-4 | +$820 | — | — | — | — |
| C1-R2 | 14-4 | +$828 | **+$8** | **−$75** | −$83 | 11/18 |
| C1-RS | 15-3 | +$872 | +$52 | −$47 | −$99 | 12/18 |

**This weakens C1-R2.** Against the real WLV sale streams its P-library addition earns nothing on our own bank; the
closed-loop +$534 vs R2S was mostly the circularity flagged in §3b(a) (forecasting the proxy with the proxy's family).
One confound remains: without a holdout, C1's PREDICT2 library contains each game's own WLV stream (an oracle), which
may already capture whatever the P addition could; a holdout rerun is queued (`chain4.sh`).

**07:00 UTC — same check with the PREDICT2 parity holdout on the candidate (no oracle stream; P library shielded):**

| arm | W-L | mean margin | vs C1 | our-bank | their-bank | games better |
|---|---|---|---|---|---|---|
| C1 | 10-8 | +$210 | — | — | — | — |
| C1-R2 | 13-5 | +$453 | **+$244** | **+$70** | −$173 | 14/18 |
| C1-RS | 11-7 | +$394 | +$184 | +$73 | −$111 | 13/18 |

Two readings. (1) The oracle leak was worth ~$600/g to C1 in the no-holdout run (+$820 → +$210): any open-loop gate on
these 18 tapes without a holdout flatters C1-family builds heavily. (2) C1-R2's P addition helps against real WLV in
direction (14/18) but the conservative our-bank half is **+$70, below the +$150 bar I pre-registered in §4.3**. So
**C1-R2 is not handed over as a probe.** If, after C1's live read, the second slot is to be a C1-family variant anyway,
C1-R2 is the best-supported one I have (closed-loop gate pass, +$677 vs hyb2965, positive-direction real-WLV
holdout), with an expected gain of tens of Elo at most.

**07:30 UTC — E-shop2 (`eshop2.jsonl`): how many of the tape's shops must match.** Tape vs C1, the first k shops of
the tape's recorded sequence pinned, the rest drawn naturally; 2 fresh seeds, one per seat.

| team | k=0 (natural, E-shop U) | k=2 | k=4 | k=6 | k=8 (E-shop P, distinct worlds) |
|---|---|---|---|---|---|
| Boey | 2/16, −$18.9k | 9/16, +$6.9k | 13/16, +$15.0k | 12/16, +$13.6k | 6/8, +$16.1k |
| 吃白饭的大肥鱼 | 2/16, −$30.1k | 10/16, +$4.1k | 15/16, +$10.2k | 16/16, +$18.2k | 8/8, +$18.9k |
| THIRD FARM CLUB | 0/16, −$44.4k | 7/16, −$5.2k | 14/16, +$12.6k | 14/16, +$15.9k | 7/8, +$17.7k |
| Majkel1337 | 1/8, −$44.4k | 2/8, −$11.9k | 8/8, +$7.4k | 8/8, +$6.2k | 4/4, +$8.5k |
| **robust pooled** | **5/56 (0.09), −$36.8k** | **28/56 (0.50), +$0.1k** | **50/56 (0.89), +$11.8k** | **50/56 (0.89), +$13.8k** | **25/28 (0.89), +$15.1k** |
| DSM / Vadim (cash-lean) | 0/16 | 0/16 | 0/16 | 0/16 | 0/8 (collapse regardless) |

Tape bank by k: $77k → $101k → $109k → $115k → $117k; C1's bank stays $107-115k throughout. The value of fitting
the world is front-loaded: shops 1-2 (known by day 6) turn a −$37k loss into parity; shops 3-4 (day 9, day 12) add
~$12k more; shops 5-8 add ~$3k. Note TFC's own first-two-shop router scored 0.24 (§3), below its k=2 cell here
(7/16): selecting routes by best recorded bank picks games whose later shops were lucky, which is a selection bias
worth remembering if anyone builds a router over recorded plans.

**07:40 UTC — C1-RS closed-loop gate (`gate_rs.jsonl`, same cells and seeds as C1-R2):** vs C1 **12-8, +$351 (SE
165)**; paired over C1 **+$472 (SE 131) vs R2S, +$401 (SE 145) vs WL+S2, +$632 (SE 165) vs hyb2965, +$449 (SE 178,
14/20 better) vs shepherd**; 0 PREDICT errors in 88 games; `kaggle_load_check` OK. Adding the shepherd streams fixes
C1-R2's weak shepherd cell (+$310, 10/20 → +$449, 14/20) without costing the hyb2965-family cells. Caveat as for R2S:
the shepherd cell is partly circular (streams recorded from public shepherd, tested against public shepherd); the
live band runs private edits of that chassis. Against the real WLV tapes its own-bank gain is +$73 (holdout), below
my bar.

**Round-1 verdict for the build lane:** no upload from me. If Claude Code / Sonnet decide the second slot should be a
C1-family variant after C1's live read, **C1-RS** is the one I would field (passes every closed-loop leg, positive vs
both chassis families, real-WLV direction positive 13/18), expected gain over C1 tens of Elo, and it shares C1's
failure mode. No processes of mine are left running (all pools reaped by PID; chain scripts exited).
