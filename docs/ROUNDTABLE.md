# Round table: how do we reach 3000+ on Kaggriculture?

You are one of three senior engineers (Devin, Claude, Codex-Astra) solving this. Read
`HANDOFF.md` (project state, ground rules, falsified list) and `MEMORY.md` (session log) first.
Engine source of truth: `.venv/lib/python3.14/site-packages/kaggle_environments/envs/kaggriculture/kaggriculture.py`.
Data available locally: `mine/opp/*.json.gz` (reduced live replays: teams/rewards/full action
tapes), `mine/top/`, `mine/tapes/`, `data/lb.json` (fresh 9,846-team leaderboard).

## The position

- Live pair `subV_f55rec` / `subV2_f55rec` (subs 56465704/56465708): ~2506 / ~2575, plateaued.
  Last-20 fetched episodes: 8W-12L. Overall fetched 22-22. Win rate vs 2400-2700 band ≈ 55%.
- Top-10 cutoff: **2977** (rising). Gap ≈ **+400-450 Elo**. Deadline 09-30, final BT refit Oct 1-15.
- A 9-agent round-robin (2,160 games) says this pair is already our best: f55rec mean WR 0.773,
  beats vanilla pipe16 0.83. The ONE losing cell: **koshinm beats both builds 0.58 / 0.63**
  (but loses 0.00 to melon — intransitive).

## Architecture (what we run)

A mined "tape": ~41 recorded routes (per-step farmer/hands ops + market orders), one chosen at
day ~6 by a learned signature router from the first 2 shop draws, then executed verbatim.
Overlays wrap it: premium-sell layer, f55 floors, clamp, 3 rival-sale estimators (reconciled),
animal-tile dead-op reclaim. ~1MB single file, no deps.

## Hard evidence (measured, do not re-litigate)

- **Opponents 2700+ run the SAME tape lineage** (identical op counts ±10, identical buy
  schedules COW6+SHEEP11) — and beat us on execution quality, not strategy.
- **The blowout mechanism**: tape burns cash to ~0 by design days 6-9 (7 pasture builds +
  8-9 hires + seeds). Opponent revenue compression pushed our trough below animal-buy costs →
  3 buys silently failed → 14 vs 17 animals placed → −21k. Same-seed mirror shows our cash is
  fine uncontested — the trough is opponent-induced. Buy→place gap is buy+2..+9 steps,
  single-shot; deferred buys strand in shed (cap pressure).
- **Whisker losses** dominate: −100..−1500, identical production, last-week liquidation bleed.
- **Top-10 agents emit a different buy signature EVERY game** (6/6 distinct) — they replan
  production against each new shop draw (8 shops unlock over ~21 days). We commit at day 6.

## Falsified this week (full list in HANDOFF §5, entries 21-29)

Sell phasing to post-drain peaks (subsidizes opponent, 0/10 ×2); market bracket/float trades
(−24.6k, −4.6k); animal-buy rescue ×3 incl. dedicated shepherd hand (uniform −255..−1516);
mid-game route switching (routes diverge physically step 144); hire suppression; buy/sell arb
(net-zero by design); staple spike-selling (shed is always ~0); land-buy failsafe; plant-tile
reclaim (weed-RNG re-rolls shared shop draws).

## Constraints

- 720 steps, market cap 10 orders/turn, crashes = auto-loss, everything ships in one .py file.
- Overlay edits fight the tape's zero-slack choreography: measured friction $300-1500/game.
- A replacement must beat the live pair by >±200 Elo locally (paired seeds, both seats) before
  it is worth a submission slot.

## The question

Design the path from ~2575 to **3000+**. Concrete options on the table:

1. **Reactive replanner**: replace tape-commitment with per-day replanning against observed
   shop draws. Biggest possible win but a real build — the tape's execution choreography
   (per-tile op schedules) is the hard part to reproduce reactively.
2. **Koshinm cell**: reverse-engineer what koshinm does (replays in mine/) that beats our pair
   0.58-0.63; port the mechanism as a targeted fix.
3. **Late-signature re-routing**: keep field choreography; swap only the *market-order tail*
   when day 9-18 shop draws reveal a different demand profile than the day-6 route assumed.
4. **Trough insurance**: make the days 6-9 cash position robust to opponent compression
   without adding animals/hands the schedule can't absorb (3 rescue variants all failed).
5. Your own mechanism — but it must survive contact with the falsified list.

Deliver: a concrete design with the causal mechanism, why it survives the falsified evidence,
what to measure to falsify it cheaply BEFORE a full build, and the honest expected Elo delta.
Be rigorous — margin is noise, only win rate vs 2400+ opponents matters.

---

# ROUND 2 UPDATE — SIR measured (2026-09-23 ~02:45 IST)

Since the brief was written, the koshinm `sell_impact_reorder` operator was ported
verbatim onto both live files (`subV_sir.py`, `subV2_sir.py`) and measured on
fresh seeds 224–247, both seats, real engine:

| matchup | base result | +SIR result | Δ |
|---|---|---|---|
| vs own twin (subV_f55rec) | — | **48-0, +1054..+1456** | huge |
| vs subV2_f55rec | — | **16-0, +1599** | huge |
| vs subK_pipe16 (our best ever, 2787) | rec pair won ~80% | **16-0, +1381** / 14-2 +1187 | +800-900 margin |
| vs subOb_pipe16prem | — | **16-0, +1302** | — |
| vs koshinm local-best | 8-8, **−168** | **10-6, +178** / 9-7 +201 | +350, matchup flips |
| vs melon-squeeze-2749 | 7-9, +314 | **8-8, +633** | +319 |

- Mechanism: per-item market inventories are independent; reordering sells only
  changes WHICH index our same-item dump lands relative to the opponent's — we
  capture pre-dump prices, they eat our glut. Zero-sum positional theft,
  ~$2/turn compounding over 700 turns.
- SIR permutes ONLY SELL slots (BUY order preserved → seed-first ordering safe).
- Extension tested and REJECTED: moving BUY_PRODUCT to last index → catastrophic
  (−27k to −43k; likely cap-truncation dropping feed buys when prem overlay
  fills the queue). Plain SIR only.
- Official env: DONE both seats, ~91k banks.
- Per claude's whisker model ($300 margin ≈ 100 Elo), +1000-1500 vs the clone
  band ≈ +300-500 Elo → plausible 2800-3000 territory.

## Questions for round 2

1. What is the NEXT lever to stack on SIR? Specifically: is there a second
   microstructure edge in `_process_market` we haven't exploited (e.g., sell
   timing relative to shop consumption ticks every 4 turns)?
2. Given SIR exists, does the marginal value of the bounded replanner change?
3. Should slot B be a SIR variant of a DIFFERENT chassis (metav4 base) for
   diversity, or subV2_sir?
4. Anything in the koshinm operator file (/tmp/koshinm_operator.py) beyond
   sell_impact_reorder worth porting — e.g. sale_advance_pressure,
   opponent_front_run detector?

---

# ROUND 3 — why aren't we at 3k? (2026-09-23 ~13:00 IST)

SIR pair submitted 00:02 UTC, ~7h ago. 174 scored episodes: **131-42 (76% WR),
mean margin +7612, last-30 23-7 +2386**. Scores still converging: subV2_sir 2302,
subV_sir 1883 (was mid-convergence snapshot). No blowouts > −3.6k.

## Decoded losses (replays /tmp/sirloss/episode-*-replay.json)

| ep | opp | margin | signature |
|---|---|---|---|
| 112294003 | fufufukakaka | −3598 | DIFFERENT MIX: they grew TOMATO×98 + more EGG/CARROT/MELON; we sold WHEAT×838. AND we led +6.1k at step 600 then lost 9.5k in the last 120 steps. |
| 112270783 | Quickpanda | −3144 | clone; identical animals; dead-even to step 600 (100478 vs 100850), lost −4.1k in the final 120 |
| 112329844 | Utkarsh #2 | −2801 | clone; we sold FERTILIZER 2334@$9.9 vs their 332@$39.3; their premium qty higher |
| 112352099 | ominteam | −2580 | clone; FERTILIZER 1391@$9.9 vs 444@$29; their premium qty higher |

## Two candidate loss modes

A) **Endgame liquidation bleed** — in 2/4 losses we were even/ahead at step 600
   and lost 3-9k in days 25-29. Koshinm's residual edge is the same signature.
   Hypothesis: our route-2 terminal sells hit worse price windows than theirs.
B) **Fertilizer glut** — heavy fert dumps at $9.9 vs opponents' $29-39 avg.
   Unclear cause/effect: tape may switch hands to fert collection when premium
   prices crash (symptom) — or fert ops displace premium work (cause).

## The question for round 3

Top-10 needs ~2977. SIR lifts us to ~2700-2850 est. What closes the last ~200-400?
1. Is the endgame bleed fixable inside tape+overlays (sell-timing in days 25-29),
   or does it require the replanner?
2. Should we suppress COLLECT_FERTILIZER when fert price < threshold? Estimate
   the opportunity cost from the replays.
3. The production-mix gap (fufufukakaka grew tomatoes+eggs we never planted):
   which tape-side decision controls this, and is it adaptively choosable
   post-day-6 without breaking worker tours?
4. Anything else in the decoded losses the brief missed?

---

# ROUND 4 — 2026-09-23: the 3k+ plan (claude + codex + replay forensics)

## New evidence: realized ledger vs tetsuya (lb ~2953, ep 112111361)

Full action-stream replay through the instrumented engine (archive `actions[t]`
answers obs step t−1; replayed rewards match recorded exactly). Realized fills:

| line | us (74608) | tetsuya (88869) |
|---|---|---|
| revenue | $114.2k | $113.7k |
| spend | **$28.3k** | **$19.6k** |
| feed-wheat buys | 239u $8.65k | 96u $3.25k |
| fert buys | 79u $2.4k | **0** |
| animals placed | 23 / $10.5k | 19 / $8.9k |
| carrot seeds | 52 | **102** |
| strawberry sold | 251u @ $40 (glutted) | 200u @ $87 |
| carrot sold | 162u @ $45 | 324u @ $49 |
| FERTILIZE / FEED ops | 112 / 429 | 186 / 313 |

Same revenue, −$8.7k spend. Their edge: (a) demand-matched mix — 2× carrots when
the draw pays $49/carrot, strawberry kept under the glut point; (b) lean inputs —
grow-own feed wheat, zero fert buys (186 FERTILIZE on collected stock alone);
(c) fewer mouths (19 vs 23 animals → 116 fewer FEED ops).
The "aspiration spam" (BUY_ANIMAL GOOSE×66, BUY_LAND×14) is NOT a mechanism —
engine fills unit-by-unit until cash fails; it's a reactive replanner talking
through a dumb order interface. Both advisors + decode agree.

## Advisor verdicts (round 4)

**codex**: purchase ledger first; trim only proven surplus (+100-500); one bounded
optional-package oracle; bounded market_queue_lockstep port (+0-300); hold sirxP;
no reactive replanner inside the freeze window.
**claude**: spam orders dead on arrival; cost gap = mix not waste (fert buys the
only candidate, ~$2.4k); new risk — SIR is public post-lock, positional edge
decays, TIMING is the remaining edge; ranked: sell-earlier sweep ≥576 (+50-150
Elo), koshinm operator isolation (+30-80), fert-trim gate, slot-B rotation.
**decode (me)**: fert audit on our own games shows ~$0 removable waste (bought
units consumed or resold at gain) — BUT vs tetsuya the real gap is feed-wheat
($5.4k) + fert ($2.4k) + 2 extra animals ($1.6k).

## Execution status

- [x] Fert-waste audit: bought fert fully consumed/resold → trim lever DEAD for
  our own economy; the tetsuya Δ is mix-level, not waste.
- [~] Sell-lead sweep (endgame horizon at step≥576, mechanism = r36 reserve +
  V9 per-item horizons 40-48 today): seeds 900-983 both seats vs sirxP —
  L8 −124 (9-39) | L24 −2 | L96 **+42/+109** | L144 = L96 (caps at 695).
  Direction: longer lead wins; L96 saturates. vs koshinm regression check running.
- [ ] If L96 holds vs koshinm/melon: patch into subV2_sirxP too, gate 120 seeds,
  candidate for next submission slot.
- [ ] Deferred: market_queue_lockstep port; demand-matched crop controller
  (the real top-10 edge — multi-day, high risk); full replanner (not by 09-30).
