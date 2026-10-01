# Kaggriculture — full briefing for an outside perspective

**Purpose:** we are stuck at a rating ceiling of roughly 2,600 and want to reach 3,000+ (rank #1).
This document is self-contained: engine rules, economics, what our agent is, everything we have
tried with measured numbers, and precisely where we are stuck. If you are reading this cold, you
have everything you need to reason about it.

**Ask at the end.** Please challenge the assumptions, not just the tactics — we suspect the
limitation is structural, and would rather be told the framing is wrong than get another parameter
to sweep.

---

## 1. The competition

Kaggle "Kaggriculture". Two players, one shared market, **720 turns** (30 days × 24 hours).
Each turn you submit one action dict:

```python
{ "farmer": ["WATER"],                        # your 1 farmer
  "hands":  [["MOVE_N"], ["HARVEST"], ...],   # one action per hired hand (up to ~12)
  "market": [["SELL","MILK",3], ["HIRE"], ...] }   # max 10 orders/turn
```

Whoever has more money at turn 720 wins. **Scoring is win/loss only** — we measured this directly
over 18 live episodes: a **$596 loss cost −5.80 rating** while a **$16,891 loss cost only −4.70**;
a **$416 win paid +4.30** while a **$15,435 win paid only +3.90**. Correlation between margin and
rating change is **−0.43**. Margin is irrelevant except as a proxy for win probability.

Ladder: TrueSkill-like. Every submission **starts at 600** and moves ~±4-5 points per game, so it
takes 100+ games to approach true skill. **Only your latest 2 submissions are matched**; older ones
freeze and stop counting for rank. 5 submissions/day, quota resets ~22:00 UTC.

---

## 2. Engine mechanics that matter

**Board:** 10×10, four quadrants of 25. You start with one quadrant (25 tiles), **$3,000**, 1 farmer.
Extra land costs $1,000 / $2,000 / $4,000 in fixed order. Everyone ends up with ~75 tiles.

**Hiring:** cost is Fibonacci *within a day* (1,1,2,3,5,8,13,21,34,55,89…). Critically,
`_do_hire` **silently no-ops if you cannot afford it** — no error. Being broke in the morning means
zero workers, nothing watered or fed, every crop a weed by day 3, and a dead farm for 27 days.

**Crops:**

| crop | seed | first yield | max-yield day | max yield | ongoing? |
|---|---|---|---|---|---|
| WHEAT | $10 | d2 | 4 | 6 | no |
| CARROT | $20 | d2 | 3 | 4 | no |
| TOMATO | $50 | d8 | 8 | 4 | **yes** (every 1d) |
| STRAWBERRY | $100 | d10 | 10 | 4 | **yes** (every 2d) |
| MELON | $80 | d10 | 12 | 6 | no |

**Animals:** GOOSE $300 (COOP, EGG, every 1d), COW $400 (PASTURE, MILK, every 2d),
SHEEP $500 (PASTURE, WOOL, every 3d). Must be FED daily (costs wheat).

**Two engine gates we found the hard way:**
- Watering adds yield only when `(max_yield_day+1)//2 <= age <= max_yield_day`, **and only if the
  crop is not `ongoing`**. So watering strawberry/tomato adds *nothing* — it only prevents weeds.
- Unit actions resolve **before** market orders in the same turn, so a seed bought this turn cannot
  be planted until next turn.

---

## 3. The economics (this is the important part)

One shared market, inventory starts at **10,000** per product.
`price = base ± amplitude × f(|inventory − 10,000|)`, floored at $1.
**You sell → inventory up → price down, for both players. The town eats → inventory down → price up.**

**The market is extremely thin.** Surplus units needed to *halve* the price:

| product | base | units to halve | at +100 | if 400 under-supplied |
|---|---|---|---|---|
| STRAWBERRY | 120 | **31** | **$1** | $288 |
| MILK | 160 | **38** | **$1** | $334 |
| WOOL | 200 | **42** | **$1** | $251 |
| MELON | 250 | 112 | $150 | $303 |
| TOMATO | 60 | 135 | $35 | $300 |
| CARROT | 35 | 230 | $23 | $66 |
| WHEAT | 25 | >4000 | $21 | $45 |
| EGG | 50 | >4000 | $42 | $81 |
| FERTILIZER | 100 | 248 | $80 | $180 |

**All demand comes from the town.** Town centre eats 1 of each of 8 products every 24 turns
(30×/game). A **shop** eats 1 of each product it carries every 4 turns (up to 180×/game), doubled if
it is a single-product shop. Up to **8 shops unlock, one every 3 days, drawn with replacement**:

| shop | consumes |
|---|---|
| BAKERY | EGG, WHEAT |
| PIZZA_SHOP | MILK, TOMATO, WHEAT |
| BRUNCH_SPOT | EGG, WHEAT, STRAWBERRY |
| **YARN_STORE** | WOOL only (**2×**) |
| ICE_CREAM_SHOP | STRAWBERRY, MILK, WHEAT |
| **PET_CAFE** | CARROT only (**2×**) |
| SMOOTHIE_SHOP | STRAWBERRY, MILK |
| FARMERS_MARKET | WHEAT, CARROT, TOMATO, STRAWBERRY |

**FERTILIZER has no consumer at all** — no shop, not in the town-centre list. Its inventory only
rises; price goes $100 → $1 and never recovers. (It is still useful as an *input*: FERTILIZE doubles
the watering yield bonus.) **MELON is in no shop** — 30 units of season demand, total.

Total earned in a measured game: **$180,484 across both players**, from ~5,044 units consumed.

**The structural consequence — a prisoner's dilemma.** Because the top products halve after ~31–42
surplus units, both players would earn far more if both sold slowly. But whoever sells first takes
the high prices and leaves the other the crash, so unilateral restraint is punished brutally (we
measured **−$103,111** for a polite selling schedule). Dumping first is dominant.

**The governing law we keep rediscovering:** *demand is fixed and shared. Producing more of a
valuable product destroys its price, and the high price of a product you don't make is unreachable.*

---

## 4. What our agent is

The strong agents in this competition are **fixed 719-turn action tapes** — offline-optimised
scripts, replayed blind. Public notebooks publish them. Ours is:

1. **Base tape:** a pure-Python port of yhay81's published tape (verified action-identical). It has
   2 routes and picks between them once, at step 360, via a hand-written rule.
2. **Sell-timing overlay** (ours): decides *when* to sell rather than following the tape's schedule,
   using a model of town drain and price curves. **+$3,361/game.**
3. **Survival override** (ours): if the morning hires fail and we have 0 workers, abandon the script
   and save the livestock. On real ladder replays it fires in exactly the games that ended at $0 and
   in **zero** healthy games.
4. **Mirror-tuned parameters:** `mode=model, fert_keep=5, guard_protect=0, wheat_start=450`.
   **+$2,616** on holdout seeds.
5. **Price-impact slot ordering** (ours, the best idea we had): market orders settle **slot by slot**
   — our order #1 against their order #1 — and each unit committed moves the shared price. So the
   cost of conceding the earliest slot is `qty × (price_now − price_after_their_burst)`, which
   depends on the curve. Ranking sells by that beats ranking by raw value. **+729 on holdout.**

**Our benchmark:** candidate vs the exact current build, same seeds, both seats, scored by **mean
margin**. The null control returns *exactly* 0.0, so any signal is real. We learned the hard way not
to use win-rate here: identical agents tie exactly, so any perturbation "wins" ~96% of tie-breaks by
$3-6 — a pure artifact.

---

## 5. Where we are

- Rank ~**80/1200**, best rating **2,613**. Top-10 cutoff **~2,830**. #1 (keiz) **3,047**.
- Our live agents are consistently **under-rated by ~240-250 points** at 100-130 games, because the
  ladder moves ~3 points/game at our win rate. True level is around **2,530-2,650**.

**The top 3 are adaptive; we are not.** We mined their episodes:

| | branches between games at |
|---|---|
| Andrey Tikhomirov (#3) | day 3 (64 of 66 game pairs) |
| Jesse Bullard (#2) | days 3, 6, 7, 9, 11, 12, 17, 18, 19 |
| keiz (#1) | day 0 (step 5), 6, 7, 8, 11 |

They are **tape libraries with routers keyed to shop unlocks** — our architecture, but with many
branch points where ours has one.

**And the behavioural gap is entirely crop mix:**

| metric | us | keiz (#1) | Jesse (#2) | Crop Dusta |
|---|---|---|---|---|
| plant WHEAT | **194** | **119** | 174 | 131 |
| plant CARROT | **9** | **42** | 23 | 34 |
| plant TOMATO | 0 | 9 | 0 | 3 |
| PASS (idle) | 560 | 244 | 574 | 341 |
| WATER | 1,119 | 981 | 1,151 | 1,062 |
| HARVEST | 466 | 405 | 470 | 412 |
| land buy days | 6/11 | 6/11 | 6/11 | 5/8 |

**keiz does fewer productive actions than us and banks more** (95,923 vs our 88,606). Land timing is
identical across everyone. The entire difference is what they plant.

---

## 6. Everything we tried (all measured in the mirror, margin per game)

**Worked and shipped:**

| change | value |
|---|---|
| Port yhay81's *newer* published tape | 100W-0L vs our previous build |
| Sell-timing overlay | +3,361 |
| Mirror-tuned parameters | +2,616 |
| Price-impact slot ordering | +729 |
| Survival override | removes the ~4-7% of games that ended at $0 |

**Measured and dead — the interesting failures:**

| idea | result | mechanism |
|---|---|---|
| Match the top's crop mix (+14 carrot) | **−5,876** | wheat is **feed**: we consume ~361 wheat feeding animals worth $50k of milk/wool |
| Same + buying feed wheat to compensate | **−2,921** | recovers half the loss, confirming the mechanism, still negative |
| Only swap wheat cycles harvested ≤3 days (carrot's full-yield point) | −3,260 | same |
| Strawberry → tomato | −34,034 (−100 after fixing a confound) | tomato's high price exists *because* nobody supplies it |
| All-cow / all-sheep | −90,638 / −69,822 | concentrating crashes the price of what you make |
| Demand-aware cow/sheep swap | −6,755 | animals are bought d0-11, decisive shops unlock d12-24 — no signal at decision time |
| Buy land earlier (Crop Dusta's d5/8) | −509 → −15 after cash fix | neutral |
| Cut the expensive tail of daily hiring | −88,691 | a hand is worth far more than its fib cost |
| Sell only on the best price phase (phase 1 is genuinely 1.7-2.9% better) | −103,111 | deferring costs more than the better price |
| Reclaim the tape's ~672 idle turns | ±0 | watering/caring are per-day booleans already satisfied |
| Water in-window unwatered tiles (143/game!) | **±0** | **engine gate: watering adds no yield to `ongoing` crops**, and 104 of the 143 are strawberry |
| Withhold stock for a big final-turn dump | −103 to −2,059 | crashes a thin market |
| Unmetered fertilizer liquidation | −2,092 | fertilizer is an input (FERTILIZE doubles the water bonus) |
| Defer the day-0 animal purchases by 1 day | **−119,077** | the opening is a tuned cash schedule |
| Clone the #1 by replaying their tapes | **0/70 and 0/12** | their policies are reactive; tapes don't transfer (keiz's own tapes score 24-44k vs their 93k) |
| Single-edit hill-climbing on the tape | 1,800+ mutations, best confirm **+45** | single edits can't express a coordinated change |

**A trap worth knowing:** one unplanned **$50** seed purchase during the opening costs **−13,836**,
because the tape commits $2,830 of its $3,000 on day 0 and runs on a $0-9 minimum — so the spend
starves a later HIRE, and a failed hire is the death spiral. This confounded several earlier verdicts
by ~70×. Gating purchases on `day>=12 and money>=5000` takes the same buy to −50.

---

## 7. Why we think we are capped — quantified

Over 102 real ladder games:

| | |
|---|---|
| mean margin | **+342** |
| game-to-game spread σ | **$4,295** |
| μ/σ | **0.08** |
| win rate | 58.8% |

Against a *fixed* opponent (the bare tape) our margin is +2,685 with σ of only **1,576**. So most
ladder variance is **which opponent we drew**, not the shop draw (shop effects are real but modest:
YARN_STORE +659, BRUNCH_SPOT +377, PET_CAFE +236).

**So the ceiling is not noise we can engineer away.** We beat the mid-field (60-75%) and lose to the
top, and Elo settles us exactly in between, around 2,550-2,650. Every overlay improvement we can find
is worth $700-3,400 against a $4,295 spread — enough to win a few more coin-flips, not enough to beat
the players above us.

---

## 8. Where we are stuck, precisely

The only thing separating us from #1 is **crop mix** (119 wheat / 42 carrot / 9 tomato vs our
194/9/0). We cannot graft it on, and we now know exactly why — three independent reasons, each
measured:

1. **Wheat is feed, not a crop.** ~361 wheat/game feeds animals producing $50k of milk and wool.
2. **The tape's tending schedule is co-tuned to what it planted.** Watering turns and harvest turns
   are positioned for wheat's 4-day cycle; a substituted crop is watered and harvested wrongly.
   Adding tile-local repair changes nothing, because the tape moves units away after planting — no
   one is standing there when the crop ripens. Fixing that needs *routing*, i.e. a planner.
3. **Carrot yields less per planting** (4 vs wheat's 6) and only pays if the tile is also recycled
   faster — a schedule change, not a crop change.

So capturing keiz's edge requires a tape built *around* that crop mix, not ours edited toward it.
We have a validated forward model (`plan/fastsim.py`, money error median $0) and ~35,000
episodes/hour of search throughput, but a previous from-scratch planner measured **−49,860 margin,
0% win rate**, and single-edit hill-climbing on the existing tape has found nothing in 1,800+ trials.

---

## 9. Questions we would genuinely like challenged

1. **Is the fixed-tape architecture itself the ceiling?** Every top-3 player branches on shop
   unlocks; we branch once. Is there a way to get branch-point adaptivity without rebuilding the
   whole plan — e.g. generating internally-consistent variants offline that share a prefix?
2. **Is there an angle on the shared market we have missed?** We know the opponent's exact policy
   (most of the field runs our tape) and can reconstruct their trades from public data at **97.9%
   accuracy**. We exploited that once (slot ordering). Is there more there — and is there any way to
   profit from *predicting* their sells rather than merely out-ordering them?
3. **Is our objective wrong?** We optimise mean margin in a mirror as a proxy for win probability.
   Given scoring is win/loss and σ is $4,295, should we instead be maximising something like
   `P(margin > 0)` directly — e.g. deliberately *reducing variance*, or taking high-variance lines
   only when behind? Nobody in this game seems to play conditionally on the score.
4. **Is there a better search formulation?** Single-edit hill-climbing fails because the useful
   changes are coordinated. What would you search over instead, given a fast exact forward model and
   ~35k episodes/hour?
5. **Are we wrong that crop mix is the whole gap?** It is the only large behavioural difference we
   can measure, but we only observe actions, not intent.
