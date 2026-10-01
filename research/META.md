# Kaggriculture — community strategy meta report

Compiled from 16 Kaggle notebooks pulled into `./research/<slug>/`, cross-checked against the
installed engine (`kaggle-environments 1.32.7`,
`.venv/lib/python3.14/site-packages/kaggle_environments/envs/kaggriculture/kaggriculture.py`).

Every engine claim in §5 is **empirically verified** by `research/verify_engine.py` (12/12 pass).
Every market/town number is recomputed from the installed engine, not copied from a notebook.
Where a notebook's number disagrees with the installed engine, the engine wins and I say so.

**Legend for sources** — `[LIVEMETA]` cjlcjlcjl/what-the-top-farms-do · `[DAILY]` georgymamarin/daily-replays ·
`[VIZ]` georgymamarin/visualized-what-every-crop-pays · `[DIARY]` raykkretzschmar/findings-from-zero-to-top-meta ·
`[RANK]` raykkretzschmar/rank-your-agent · `[59U]` busyaprime/the-best-thing-to-farm-has-a-market-of-59-units ·
`[YARN]` busyaprime/one-town-in-three-has-no-yarn-store · `[LADDER]` busyaprime/what-actually-wins-on-the-ladder ·
`[MEAS]` destbreso/measure-twice-submit-once · `[XR]` destbreso/x-ray-your-agent ·
`[NOISE]` destbreso/know-your-noise · `[WKOG]` destbreso/what-kind-of-game-is-this ·
`[EPSO]` destbreso/everyone-is-playing-the-same-opening · `[4000x]` nikital7/4000x-environment-speedup ·
`[ASG]` reyhanksatria/adaptive-shop-guard (decoded from its base85 blob) ·
`[TIE]` andrewsokolovsky/breaking-the-tie (contains no tie analysis — it is an imitation-learning notebook, ignore).

---

## 0. READ THIS FIRST: the engine changed on 16 August and most published strategy predates it

The installed engine is **1.32.7**. On **16 Aug 2026** a balance patch changed the *scarcity* (below-`I0`)
side of the price curve for exactly three goods to a new `hinge` shape (`[DAILY]` cell 20 names the patch
and the date; the constants confirm it):

| product | below-curve in ≤1.32.6 | below-curve in **1.32.7** |
|---|---|---|
| CARROT | `log`, target 0.20 | **`hinge`, target 1.00** |
| TOMATO | `linear`, target 0.40 | **`hinge`, target 0.40** |
| EGG | `linear`, target 0.40 | **`hinge`, target 0.40** |

`hinge(u) = u + 8·max(0, u−1)²` where `u = x/T`. Below the knee it is linear; above it, quadratic.
The **glut** (above-`I0`) side was **not** touched — every "units to the $1 floor" number the community
published is still correct. What changed is that holding CARROT/TOMATO/EGG *back* now pays superlinearly.

Prices at N units **below** `I0` (recomputed from the installed engine):

| units below I0 | 0 | 100 | 200 | 300 | 400 | 500 | 600 | 800 |
|---|---|---|---|---|---|---|---|---|
| **TOMATO** (T=200) | 60 | 72 | 84 | **144** | **300** | **552** | **900** | **1884** |
| **EGG** (T=332) | 50 | 56 | 62 | 68 | 81 | **121** | **190** | **416** |
| **CARROT** (T=450) | 35 | 43 | 51 | 58 | 66 | 77 | **113** | **267** |
| MILK (sqrt) | 160 | 247 | 283 | 311 | 334 | 354 | 373 | 406 |
| STRAWBERRY (sqrt) | 120 | 204 | 239 | 265 | 288 | 308 | 326 | 358 |
| WOOL (log) | 200 | 240 | 245 | 249 | 251 | 253 | 255 | 257 |
| MELON (log) | 250 | 290 | 296 | 300 | 303 | 304 | 306 | 309 |

Several widely-read notebooks **embed the old 1.32.2 constants on purpose** and will mislead you:
`[LIVEMETA]` §1 hardcodes `CARROT below_func:"log"`, `TOMATO:"linear"`, `EGG:"linear"` and asserts they are
correct "everywhere in 1.32.x". They are not correct on 1.32.7. `[RANK]`'s goose/crop rankings and
`[59U]`'s season-ceiling table are also pre-hinge.

**Other version traps**
- `[4000x]`: the `kaggle_environments` preinstalled in Kaggle notebook images is **not** the competition
  version and has defaulted to `startingMoney = 2000` while every downloaded replay says 3000.
- `[DIARY]` §0: **1.32.4** made `BUY_PRODUCT`/`BUY_ANIMAL` fail when the shed is full — a full shed can now
  silently block feed and starve the herd. (Verified: `BUY_SEED` is *not* blocked.)
- `[VIZ]` §7: **1.32.3** made units able to walk across land they do not own. Before that, hands spawning on
  a locked shed tile were stranded all day. Ladder has run the fixed engine since 3 Aug.
- `[VIZ]` §10: **1.32.6** removed the town-centre ramp (it used to buy twice a day, ×2 from day 10 and ×4
  from day 20) and made shops a with-replacement draw. Any writeup describing that ramp is stale.
- `[MEAS]`: `importlib.metadata.version()` can read newly-written metadata while `import
  kaggle_environments` still resolves an older copy earlier on `sys.path`. Pin *behaviourally*: replay a
  recorded game and assert the bank to the coin.

---

## 1. What the top-ranked ladder agents actually do

### 1.1 The modal farm, day by day (`[LIVEMETA]` §8.5, Elo band ≥3100, 148 episodes / 296 seats)

| match-day | min-Elo | median Elo | median final bank | modal share | modal farm |
|---|---|---|---|---|---|
| 2026-08-07 | 3000 | 3029 | **109,071** | 25% | 8 cow + 6 sheep · 9 wheat · 10 hands · NE+NW+SW |
| 2026-08-08 | 3100 | 3121 | 78,020 | **54%** | 8 cow + 6 sheep · 4 wheat · 11 hands · NE+NW+SW |
| 2026-08-09 | 3100 | 3131 | 77,737 | 26% | 8 cow + 6 sheep · 4 wheat · 11 hands · NE+NW+SW |
| 2026-08-10 | 3100 | 3128 | 82,237 | 29% | 9 cow + 4 sheep · 1 wheat · 10 hands · NE+NW+SW |
| 2026-08-11 | 3100 | 3137 | **84,151** (max 154,941) | 30% | 9 cow + 4 sheep · 1 wheat · 10 hands · NE+NW+SW |

Top-5 compositions on 08-11:
1. 1 wheat + **9 cow + 4 sheep** + 10 hands, NE+NW+SW — ×89
2. 2 wheat + **9 cow + 5 sheep** + 9 hands — ×73
3. 9 cow + 1 sheep + 9 hands — ×17
4. 7 wheat + 9 cow + 4 sheep + 10 hands — ×16
5. 2 wheat + 7 cow + 4 sheep + 9 hands — ×10

### 1.2 "8C/4S" — confirmed, but it is one point on a moving axis

The shorthand is real and it is a **cow/sheep ratio dial, not a fixed recipe**. Observed variants, all with
~13–16 animals total on 3 quadrants:

| source | date | composition |
|---|---|---|
| `[DIARY]` top-5 leaderboard snapshot | 3 Aug | **8 cow / 5 sheep**, 5 strawberry, 12 hands (all five teams) |
| `[DIARY]` ten-team refresh | ~6 Aug | **8 cow / 6 sheep**, 3 quadrants, 12 hands, 21 melon + 44 strawberry seeds |
| `[DIARY]` 11 of top 12 | 8 Aug | 8 cow / 6 sheep, **23 strawberry, 31 wheat tiles**, 3 quadrants |
| `[LIVEMETA]` modal | 8–9 Aug | 8 cow / 6 sheep, 4 wheat, 11 hands |
| `[LIVEMETA]` modal | 10–11 Aug | **9 cow / 4 sheep**, 1 wheat, 10 hands |
| `[LIVEMETA]` code-area watch | 12 Aug | boatlee ships an explicit **"8c-4s"** route family |
| `[59U]` reference-agent manifest | — | **8 cow, 5 sheep, 6 strawberry**, three quadrants (the shared tier-6..9 plan) |
| `[ASG]` decoded live submission | ~late Aug | **11 cow + 4 sheep** default; **6 cow + 10 sheep** if YARN_STORE is the 1st or 2nd shop |
| `[XR]` leader reference, 245 episodes | 30 Aug | **7 COW**, ~280 CARE actions |
| `[DIARY]` Seb (rank-1-adjacent, 4-quadrant outlier) | — | 9–10 cow, **11–13 sheep**, four quadrants, 12 hands |

So: **8C/4S is confirmed as a real, named route**, and the family spans roughly 7–11 cows and 4–6 sheep.
`[ASG]` shows the ratio is now *conditioned on the shop draw* (see §1.6).

### 1.3 Hands per day, and the actual curve

Field consensus measured over **490 seat-seasons** (`[XR]` MD 29):

> **4 hands to day 4 · 8 by day 6 · 11 by day 10 · 12 from day 13 to the bell; IQR 0–2 hands all season.**

`[ASG]`'s decoded `default` route hires per day:
`[2,3,3,3,3,6,6,6,7,8,12,13,10,11,11,11,11,11,12,12,12,13,12,11,13,11,15,13,12,9]` (282 HIRE orders total).
`[LIVEMETA]` reports **first HIRE on day 0** as the median, and peak crews of 9–11.

The cost curve is why nobody goes past ~12 (recomputed; hire *n*-th of the day costs `fib(n)`, counter
resets every morning):

| hands | cost for one day | cost for 30 days | **marginal season cost of that Nth hand** |
|---|---|---|---|
| 8 | 54 | 1,620 | +630 |
| 10 | 143 | 4,290 | +1,650 |
| 11 | 232 | 6,960 | **+2,670** |
| 12 | 376 | 11,280 | **+4,320** |
| 13 | 609 | 18,270 | **+6,990** |
| 14 | 986 | **29,580** | **+11,310** |
| 15 | 1,596 | 47,880 | +18,300 |

Going 12 → 14 hands every day costs **$18,300 over the season** — ~22% of a median 84k bank.
`[RANK]`'s checklist calls under-hiring "the single most expensive mistake available" but its example is
**four hands for 7 coins**, taking you from 24 to 120 actions/day — the cheap region, not the top.

### 1.4 Land: which quadrants, and on which day

**Universal consensus: buy NE and SW, do NOT buy SE.** Land order is fixed in the engine
(`LAND_ORDER = ["NE","SW","SE"]`, prices 1000/2000/4000), so the only decision is *when*.

- `[LIVEMETA]`: every one of the top-5 compositions is `land NE+NW+SW`. Median first `BUY_LAND` order = **day 6**.
- `[XR]` leader reference over **245 episodes**: 2nd quadrant on **day 5 in 245/245 episodes** (zero variance);
  3rd quadrant **day 8 in 196/245 (80.0%)**, day 9 in 43, day 10 in 6.
- `[ASG]` decoded routes: land at steps **160 and 252** (days 6 and 10) — the author notes this is
  a day late on the 2nd and 2–3 days late on the 3rd versus the leader reference.
- `[DAILY]` §5: across all replayed seats, `first_land_day` has a **rank correlation with final bank of
  ≈ 0.00** — near zero, "even though land is the thing everyone talks about". Labour leads instead.

**The SE quadrant is a well-tested negative result** (`[DIARY]` §13). Three implementation families
(paid-slack, dedicated crew, seasonal setup crew) × four score gates, **5 seeds, both seats, 450 games**:
*every* four-quadrant variant lost **10–0** to the three-quadrant incumbent C92. Bradley-Terry: C92 2039 vs
best four-quadrant variant 1724 (mean margin **−3,687**). Three fully-productive four-quadrant *Seb*
trajectories also lost 10–0, by mean margins of **14,608 / 29,016 / 36,980**. The frozen candidate C93 went
**0–40** vs C92 on fresh paired seeds. Stated reasons: hands reach SE too late to plant *and* water before
the day reset; extra crew disrupts feed finance (one diagnostic cow starved at step 408); SE exposes **25
more empty tiles to weed spawns**; more strawberry/wool deepens the shared glut; and the 4,000-coin spend
reads as "falling behind" to a score-conditioned router.

### 1.5 Crop mix and the money curve

- Early seeds bought days 0–4, average per player (`[LIVEMETA]`): **wheat 11.4, melon 6.3, strawberry 2.8,
  carrot 0.0, tomato 0.0**.
- `[ASG]` full-season seed buys: WHEAT 140, STRAWBERRY 41, CARROT 20, MELON 11 (+105–126 wheat bought as
  `BUY_PRODUCT` feed). Yarn routes shift to WHEAT 129–132 / STRAWBERRY 32–36 / CARROT 12 / MELON 11.
- **Median on-hand cash** (`[LIVEMETA]`): d5 = **545** · d10 = **2,172** · d15 = **11,782** · d20 = **36,414**.
  `[DAILY]` §3: top farms cross a tenth of their final bank late — "reinvest almost everything, then
  compound"; the elbow, not the last-day sprint, is where the game is decided.
- Verb mix of a real strong route (`[ASG]` `default`, 7,148 unit-turns): movement **48.9%**, WATER 13.8%,
  HARVEST 5.9%, PASS 5.3%, FEED 4.9%, CARE 4.8%, COLLECT_FERTILIZER 4.7%, PICKUP 4.2%, PLANT 2.9%,
  DROP 1.9%, FERTILIZE 1.1%, DIG 0.7%, PLACE 0.6%, BUILD_PASTURE 15 total. **BUILD_COOP = 0, GOOSE = 0.**

### 1.6 Typical final bank in a real head-to-head — and how close it is

| statistic | value | source |
|---|---|---|
| median winning bank, Elo ≥3100 | **84,151** | `[LIVEMETA]` 08-11 |
| best single game that band | 154,941 | `[LIVEMETA]` |
| **winners vs losers, same band** | **85,501 vs 81,412** — a 4,089 gap (**4.8%**) | `[LIVEMETA]` |
| median margin at the top of the ladder | **< $2,738** decides half of games | `[NOISE]` |
| median margin at the bottom (400–800 Elo) | $23,148 | `[NOISE]` |
| σ of the margin, 22,702 episodes | **$27,300** | `[NOISE]` |
| donor-field medians, 20 strong public agents × 128 games | best **82,161** (range 42k–141k); strong band **65k–79k** | `[MEAS]` |
| reference tiers | tier 5 ≈ **46k**; meta band (tiers 6–9) ≈ **149k–165k** vs weak opposition | `[RANK]` |

**The single most important framing number:** at the top of the ladder the two banks differ by ~5%, while
the season-to-season spread of one agent's bank is ~$27k. You are not optimising bank; you are optimising
the sign of a small difference inside a large common-mode swing.

---

## 2. Best products — the consensus, and where it is now wrong

### 2.1 The town is the only real buyer, and its season demand is a hard cap

Recomputed exactly. Shops unlock at the end of days 2,5,8,…,23 (visible from days 3,6,…,24), capped at 8
instances drawn **uniformly with replacement**; each instance eats its whole menu every 4 turns (**6 ticks
a day**), and **single-product shops eat double**. Town centre eats 1 of every non-fertilizer product once
a day. Summing `min(8, floor(d/3))` over the 30 days gives **132 shop-days** out of a possible 240.

| product | shops on menu | mean shop demand/day (all 8 open) | **season units the town will buy** | @ base price | price if **nobody** sells | P(no shop buyer at all) |
|---|---|---|---|---|---|---|
| WHEAT | **5** | 30 | 525 | 13,125 | 48 | **0.04%** |
| STRAWBERRY | 4 | 24 | 426 | **51,120** | 293 | 0.39% |
| MILK | 3 | 18 | 327 | **52,320** | 317 | 2.33% |
| CARROT | 2 (PET_CAFE doubles) | **18** | 327 | 11,445 | 60 | **10.01%** |
| EGG | 2 | 12 | 228 | 11,400 | 64 | **10.01%** |
| TOMATO | 2 | 12 | 228 | 13,680 | 91 | **10.01%** |
| WOOL | 1 (YARN_STORE doubles) | 12 | 228 | 45,600 | 247 | **34.36%** |
| MELON | **0** | 0 | **30** (town centre only) | 7,500 | 280 | n/a |
| FERTILIZER | **0** — and no town centre either | 0 | **0** | — | — | n/a |
| | | | | **$206,190 total** | | |

My enumeration of all **C(15,7) = 6435** possible towns reproduces `[YARN]`'s headline numbers exactly
(34.36% wool, 10.01% carrot), so both are trustworthy.

**The $206k pot is shared by both players.** An even split at base price is **$103,095 each** — and the
observed median bank is **$84,151**. The field is capturing ~82% of the theoretical even split, which means
the remaining edge is (a) buying more than half the pot, (b) selling above base by holding, and (c) money
that is *not* in the pot at all (fertilizer, see §2.5).

### 2.2 Is TOMATO underused? **Yes — dramatically, and it is the clearest open lane.**

- In the 08-11 top-band census of **296 players**, the products with recorded SELL orders were: Carrot
  (12 players), Fertilizer, Melon, Milk, Strawberry, Wheat, Wool (296 each). **TOMATO appears zero times.**
- `[ASG]`'s decoded live routes buy **0 tomato seeds** across all five branches. `[DIARY]` never mentions
  tomato. `[RANK]`, `[59U]`, `[VIZ]` all rank it near the bottom ("tied with wheat for the worst
  coins/tile/day at 20.0").
- The pre-hinge dismissal was correct: at `below_func = linear, target 0.40`, tomato scarcity was worth
  almost nothing. **Post-hinge it is the steepest scarcity curve in the game.**
- Because nobody sells it, tomato inventory drifts monotonically down all season. At the expected
  season-end deficit of **228 units** the marginal price is **$91** (1.5× base). At the p90 town draw
  (24/day tomato demand → 426 deficit) it is **$356** (5.9× base). For comparison at the same deficits,
  CARROT goes $53 → $68 and EGG $64 → $88 — **tomato is where the convexity actually bites.**
- Tile economics: seed $50, `first_yield_day 8`, `interval 1`, `max_yield 4` → 4 units over ~12 tile-days,
  or **8 units if fertilized and harvested every production day** (fertilizer gives +2 on watered days and
  the 4-unit cap only binds if you let it accumulate).

Caveats before you bet the farm on it: (i) 10.01% of towns have no tomato shop at all; (ii) the hinge is
convex, so the first 200 units of deficit are worth barely more than base — **the payoff is in the tail,
not the mean**; (iii) if the field notices, two suppliers will flatten the deficit fast.

The same argument applies with less force to **CARROT** (only 12/296 players sold it, at day 25 in batches
of 5.3) and **EGG** (zero sellers; but see §2.4 — the *volume* is the problem, not the price).

### 2.3 MELON — the community has flip-flopped twice and the current answer is nuanced

- `[VIZ]` §15 item 2 is the cleanest measurement anyone published, and the author explicitly retracted his
  earlier warning: switching a six-tile bot's crop constant from carrot to melon gained **+11,665 coins,
  se 558, ahead on 8/8 seeds**. It survived two rebalances: **+13,610 on 1.32.4 → +12,117 on 1.32.6 →
  +11,665 on 1.32.7**.
- Why it works at low volume: melon's *glut* curve is quadratic (`sq`, target 3.60), so the floor is at 158
  units — but the bot only sold **72 melons all season** and melon closed at **232 against a base of 250**.
- Why it fails at high volume: **no shop ever buys melon.** Its only buyer is the town centre's 1/day = **30
  units for the entire season**. Everything above that sits in inventory forever, and two players both
  dumping is exactly the "$1 floor" story. `[59U]`'s natural experiment: in five recorded seasons where
  nobody sold melons the price walked 256 → 280 *identically to the coin in all five*; in the sixth it
  ended at **7**.
- Melon is also the most **price-inelastic** good per batch (recomputed): 100 units in one order still
  averages **$217/unit**, vs $80 for wool. So melon rewards a *lump* sale in a way nothing else does.
- `[DIARY]` §2's marginal-tile analysis: "public leaders often use ~6–16 melons, not a full 25-tile dump",
  and `[LIVEMETA]` shows exactly **6.3 melon seeds bought days 0–4** and a first melon sale on day 10 in
  batches of 7.7. `[ASG]` buys **11 melon seeds** in every branch.

**Verdict:** melon is a *capital event*, not a crop line. ~6–16 tiles, harvested around day 10–12, sold as
one or two lumps to fund the herd and the land. Scaling it past that is the classic trap.

### 2.4 MELON / STRAWBERRY / MILK / WOOL gluts and the $1 floor

Units you must sell (from `I0`) before the price hits the $1 floor — recomputed, identical to `[LIVEMETA]`'s
1.32.x reference because the glut side was never patched:

| product | units to the $1 floor | curve shape |
|---|---|---|
| **WOOL** | **59** | `sq`, target 3.20 |
| **STRAWBERRY** | **62** | `linear`, target 1.60 |
| **MILK** | **76** | `linear`, target 1.60 |
| MELON | 158 | `sq`, target 3.60 |
| FERTILIZER | 493 | `linear`, target 0.40 |
| TOMATO | 529 | `sqrt`, target 0.60 |
| CARROT | 842 | `sqrt`, target 0.70 |
| WHEAT / EGG | >5,000 | `log`, target 0.20 — effectively never crash |

`[59U]`'s title comes from this: **sheep top the published rate table at 266.7 coins/tile/day and the wool
market absorbs 59 units.** But `[59U]` itself publishes the refutation in MD 14, and it is important:

> "milk has a 76 unit ceiling … and it sells **above** its 160 base price for an entire season, because
> three shops drain it faster than sixteen cows can fill it. The ceiling never binds."

**So `units_until_price_floor` is the wrong column to optimise.** `[RANK]`'s formulation, which `[59U]`
verified against the engine and I re-verified: **base price × shop demand** is what you can actually bank.
The depth column only misleads where shop demand is real; where it is absent (melon: 0 shops; wool: 1 shop
and 34.4% of towns have none) the two measures agree and the collapse is real.

`[RANK]`'s measured end-of-season market state makes the point concrete:

| farm | MILK inventory | MILK price | EGG inventory | EGG price |
|---|---|---|---|---|
| 16 cows | −148 (scarce) | **266** | −302 | 68 |
| 16 geese | −464 | 347 | **+104 (glutted)** | **42** |

**The $1 floor is a one-way door.** Verified: a `SELL` that clears at $1 does **not** add to market
inventory (`if price > 1: market["inventory"][item] += 1`). You get $1 and the price does not recover any
faster. `[XR]`'s leader reference for `floor_sells` is **0** — the best agent on the board never does it.

### 2.5 The one product outside the pot: FERTILIZER

- **No shop and no town centre ever buys fertilizer.** It is not in `TOWN_CENTER_PRODUCTS` and not on any
  shop menu. So its inventory only ever goes *up* — but it starts at base $100 with a shallow linear curve.
- Every animal produces **1 collectible fertilizer per day, fed or hungry** (only escaping stops it), and
  `COLLECT_FERTILIZER` costs one action. Verified: 21 separate days of fertilizer revenue from **one** cow.
- Recomputed: selling fertilizer from `I0` to the $1 floor is **493 units for $25,045** (avg $51/unit).
  The realistic haul — 13 animals × ~25 days ≈ **325 units — is worth $21,970** at an average of **$68/unit**.
- `[ASG]`'s decoded route sells **400 fertilizer units = 22.2% of all its sell volume**, spread over 165 of
  580 SELL orders, and fertilizer is its **only** income on days 1–3.
- `[LIVEMETA]`: **296 of 296 players** sell fertilizer, first sale day **4**, average batch **4.9**.
- `[DIARY]` §2.3 flags it as "a real sidecar income stream"; `[VIZ]` §5 calls the animal↔fertilizer loop
  "designed to feed each other" (fertilizer is the *only* way wheat reaches its 6-unit cap).

**This is the single biggest non-zero-sum pot in the game** and it is already fully exploited by the field.
Match it, don't expect an edge from it.

### 2.6 Animal economics, simulated through the real end-of-day routine

`CARE` is the biggest single multiplier in the game and it is under-documented. The rules say CARE banks
+2/day; **the engine adds +1** (`[RANK]`, confirmed in source at `_daily_refresh_animals`). The counter
accumulates on every day the animal is *both fed and cared for*, and dumps into yield on the next
production day *if fed that day too* — capped by `max_held`.

Simulated over 30 days, placed on day 0, harvested on every production day:

| animal | cost | no CARE | **with CARE** | multiplier | gross @ base with CARE | first pickups (with CARE) |
|---|---|---|---|---|---|---|
| GOOSE | $300 | 27 EGG | **56 EGG** | 2.1× | $2,800 | day 4: 4, then 2/day |
| COW | $400 | 12 MILK | **39 MILK** | 3.25× | **$6,240** | day 8: 6, then 3 every 2 days |
| SHEEP | $500 | 9 WOOL | **38 WOOL** | **4.2×** | **$7,600** | day 6: 6, then 4 every 3 days |

`[VIZ]` §6 states the rule cleanly: a cared animal produces `1 + interval` instead of 1 — **double for a
goose, triple for a cow, quadruple for a sheep**. *"The slower the animal, the larger the multiplier, and
that is backwards from what the schedule alone suggests."* An **uncollected** cared goose is already at its
4-unit cap on its first production day and earns nothing after that — you must harvest every production day.

Cost of a cared animal: **4 actions/day** (FEED, CARE, HARVEST-on-production-days, COLLECT_FERTILIZER) plus
1 wheat/day of feed. That is the real reason hands matter.

### 2.7 The measured animal-mix experiment (`[RANK]` §5)

Same 16 animals, 16 structures, same land, same feed load:

| cows | sheep | geese | bank | vs the 10c/6s baseline |
|---|---|---|---|---|
| 10 | 6 | 0 | 52,957 | — |
| 12 | 4 | 0 | 54,512 | +1,555 |
| **16** | **0** | 0 | **57,407** | **+4,450** |
| 10 | 0 | 6 | 38,845 | −14,112 |
| 8 | 0 | 8 | 36,638 | −16,319 |
| 0 | 0 | 16 | **10,602** | **−42,356** |

Also: **32 goose configurations, all 32 lost, best −7,569.** Geese are measurably bad — but note the
mechanism is *volume*, not price: 16 geese produce 896 eggs against 228 units of season demand.

**Critical caveat the author himself supplies:** the +4,450 for all-cows **evaporated on held-out seeds** —
on seeds 8000–8005, both seats, it lost **3–9 with a −3,627 margin** while beating every other tier 12–0.
This is the single best cautionary tale in the corpus about tuning-set overfit.

---

## 3. Selling policy

### 3.1 The consensus is metered, not dumped — but the size of the effect is small at low volume

Revenue for one batch of *q* units from equilibrium (recomputed; $/unit in parentheses):

| item | q=5 | q=10 | q=25 | q=50 | q=100 |
|---|---|---|---|---|---|
| WOOL | 998 ($200) | 1,983 ($198) | 4,715 ($189) | 7,655 ($153) | 7,969 (**$80**) |
| MILK | 780 ($156) | 1,506 ($151) | 3,372 ($135) | 5,430 ($109) | 6,205 ($62) |
| STRAWBERRY | 580 ($116) | 1,113 ($111) | 2,424 ($97) | 3,648 ($73) | 3,847 ($38) |
| **MELON** | 1,250 ($250) | 2,498 ($250) | 6,202 ($248) | 12,098 ($242) | 21,721 (**$217**) |
| FERTILIZER | 498 ($100) | 991 ($99) | 2,440 ($98) | 4,755 ($95) | 9,010 ($90) |
| TOMATO | 284 ($57) | 550 ($55) | 1,295 ($52) | 2,411 ($48) | 4,318 ($43) |
| EGG | 242 ($48) | 474 ($47) | 1,151 ($46) | 2,244 ($45) | 4,371 ($44) |

Same total volume, one 50-unit dump vs ten batches of 5 with the town clearing between:

| item | dump 50 | metered 10×5 | metered gain |
|---|---|---|---|
| STRAWBERRY | $3,648 | $5,800 | **1.59×** |
| MILK | $5,430 | $7,800 | 1.44× |
| WOOL | $7,655 | $9,980 | 1.30× |
| MELON | $12,098 | $12,500 | **1.03×** |

**But `[VIZ]` §15 item 5 put an absolute meter on it and the number is humbling:** a six-tile carrot bot
makes 24 sales a season, 22 of them exactly 6 units, and its **whole-season slippage is 104 coins** (48–146
across eight seeds). Switched to melon, it sells 3 times, and the 36-melon lump on day 12 gives back **645
coins in one order — still keeping 93.4% of its first-unit quote**; whole-season slippage **827 coins**.
It still wins by eleven thousand.

**Conclusion:** metering is real and free, so do it — but at realistic volumes it is worth hundreds to low
thousands, not tens of thousands. Do not trade production or logistics for it.

### 3.2 What good agents actually do

Observed sell rhythm, top band, 296 players (`[LIVEMETA]` 08-11, first sell day · avg batch):

| product | first sell day | avg batch | players |
|---|---|---|---|
| Fertilizer | **4** | 4.9 | 296 |
| Wool | 6 | 9.8 | 296 |
| Wheat | 8 | 11.6 | 296 |
| Melon | 10 | 7.7 | 296 |
| Milk | 11 | 7.7 | 296 |
| Strawberry | **15** | **15.4** | 296 |
| Carrot | 25 | 5.3 | **12** |
| Tomato | — | — | **0** |

Strawberry batch size has been growing fast (9.9 → 14.1 → **15.4** over three days) and **winners sell it
on day 14, losers on day 16** — the win/loss split widened from 1 day to 2 days over the same window.

`[ASG]`'s decoded route is far more granular: SELL quantity histogram is `q=1` in **224 orders**, q=2 in 90,
q=3 in 110, q=6 in 51, and **only 8 orders in the whole season exceed 16 units**. 37.4% of turns carry at
least one SELL. Volume ramps hard into the bell: **day 29 alone is 260 units = 14.4% of the season's 1,801.**

### 3.3 Reading `market["inventory"]` to detect the opponent — yes, this is the current frontier

This is where the top of the ladder is actually competing. Three independent implementations:

**(a) `[DIARY]` C68's horizon inference.** The controller "observes premium-product market inventory
changes, **removes its own sale and the deterministic town drain**, fits the opponent's extra batches to
horizons 1–6, and races one turn ahead." Defaults to horizon 4 until enough evidence arrives; gated by
public-farm similarity so unrelated families keep the base schedule. In diagnostics it correctly identified
horizons 2, 3, 4 and 5.

**(b) `[ASG]`'s `_phase_evidence`** — the cleanest formulation, straight from the decoded source:

```
excess = Δ market.inventory[item] − own_net(our last emitted orders) − normal(route's own previous-turn SELL)
```
> "Town/shop demand and an opponent BUY can only *reduce* this value. A positive remainder is therefore
> conservative evidence that a near-clone supplied more than its ordinary previous-turn slot."

Live parameters: detection window **steps 144–159** only, `minimum_excess_units=2`, `maximum_excess_units=4`,
`future_window=2`, watching exactly `(STRAWBERRY, MELON, MILK, WOOL)` — the four steep-curve goods.
Clone identification is an L1 distance ≤ 2.0 over the opponent's *public* signature (hand count, quadrants,
per-tile counts of every crop/animal/structure), needing a **24-consecutive-turn streak** from step 48 to
latch, active from step 160.

**(c) The front-run itself, and the conservation rule that makes it safe.** `[DIARY]` §15.2 found **11
losses sharing the same field-tape hash**: nearly identical routes won when their market timing was
ordinary and lost when the opponent sold fertilizer or wheat **exactly one turn before** their batch.
Production was unchanged; **order alone reversed the matchup by ~5,300–5,700 coins.**

The fix that survived is deliberately conservative: **move part of an already-planned sale forward, then
subtract exactly the moved quantity from the following turn.** No new liquidation, no field change.
`[ASG]` implements the same idea as explicit quantity debt booked at `step + horizon`
(normal horizon 2 / max batch 10; escalated to horizon 3 / max batch 20 when the phase detector fires).

Held-out validation of the variants (`[DIARY]` §16, **900 games over six new seeds**):

| variant | record | win rate |
|---|---|---|
| five wheat first only | 173–7 | 96.1% |
| aggressive wheat + fertilizer split | 168–12 | 93.3% |
| wheat 10 + fertilizer 5 caps | 174–6 | 96.7% |
| **fertilizer only, cap 10** | **174–6** | **96.7%** |
| split only after turn 480 | 173–7 | 96.1% |

The two tied finalists then played each other: **fertilizer-only beat wheat+fertilizer 6–0 despite a mean
margin of only 27.** In the 18-agent final (918 games, zero failures) it ranked **1st, 88–14, BT 1837**.

**Why fertilizer and not wheat:** `[DIARY]` C71 sorts premium SELLs by estimated self-induced price impact
and lets MELON/STRAWBERRY/MILK/WOOL jump the queue, but keeps **WHEAT and FERTILIZER on safer timing
"because opponents can buy them"** — `BUY_PRODUCT` covers exactly those two, so dumping them hands your
rival cheap feed. C95 later relaxed this to pulling forward at most **10 wheat and 5 fertilizer**
(112–8 vs refreshed top-20 medoids, 93.3%, vs C94's 111–9).

### 3.4 The market **order slot index** is a contested priority queue — verified

This is the least-documented high-leverage mechanic in the game, and two of my sources disagreed about it
until I tested it.

The resolver walks order slot `i` across **both players**, quotes both against the same pre-commit
inventory, commits both, then repeats for the next unit; `_refresh_prices` runs **after each slot**.
Consequences, both verified in `research/verify_engine.py`:

- **Seat is worth nothing.** Two players selling 30 MELON *at the same slot index* bank **$7,158 each**.
  Confirmed independently at n > 30,000 ladder games (`[WKOG]`: seat 0 wins ≈50%, 95% CI inside ±1.5pp) and
  on 270 reference games (`[59U]`: seat 0 wins 135 of 270).
- **Slot index is worth a lot.** The same 30 MELON at slot 0 banks **$7,416**; at slot 3 it banks **$6,885**
  — a **$531 (7%) advantage** for the earlier slot, purely from list position.

`[RANK]`'s checklist item 2 is the practical form: *"Sell before you buy in the same turn — the market
queue is processed in list order, so a SELL ahead of a BUY funds it immediately."*

`[DIARY]` §15.1 is the cautionary form. Four large losses (**averaging −13,606**) shared one mechanism:
**the opponent bought 14–19 wheat before C92's slot-eight order to buy five wheat.** The raised shared price
left cash for only four units, one sheep went unfed and disappeared on day 2. The fix that worked was
simply **moving the existing five-unit order to slot zero on turn zero.** Buying *six* instead of five
regressed to 0–4 against several established agents; buying 14–19 and reselling the surplus was "a
profitable-looking exploit … sharply vulnerable to another public route family."

`[4000x]` lists this as one of its three "cost me days" porting bugs: *"Market orders resolve by slot index,
across both players … Resolving player-by-player instead produces perfectly plausible, wrong numbers."*

### 3.5 Endgame liquidation

`[ASG]` at step 718 **discards the entire scheduled market list** and rebuilds it as up to 10 SELLs ranked
by `(1 + opponent_exposure) × GLUT_WEIGHT × price × log1p(qty)`, with
`GLUT_WEIGHT = {MELON 3.6, WOOL 3.2, STRAWBERRY 2.0, MILK 2.0, EGG 1.5, TOMATO 1.3, rest 1.0}`.
At steps 717–718 it also overrides *unit* actions: carrying anything on a shed tile → `DROP`; one step away
at 717 → step toward the shed; empty-handed on a shed tile with ready yield → `HARVEST`.

> "Final-turn purchases and hires cannot improve bank reward."

`[DIARY]` §4.6: c17's terminal field controller took over at step 712; **delaying it to 717** preserved five
more turns of the stronger base tape and still left 717–718 for cleanup. That one-line change became c27,
which then went **90–10** on ten untouched seeds, both seats.

---

## 4. The ladder and matchmaking itself

### 4.1 Rating mechanics

- **Only W/L/T moves rating; coin margin is irrelevant.** `[DIARY]` §2.4 and the C70 audit are the proof:
  C70 went **83–5 with a +14,196 mean margin over 88 real live episodes** and still plateaued below 3000,
  because "increasing margins against agents it already beat could not reliably move a sub-3000 rating."
- **Matchmaking pairs by rating**, so `[MEAS]`'s hard rule applies: *"The rating delta is an upper bound by
  construction"* — rate higher and the ladder hands you harder opponents, returning part of the gain.
- **5 submissions a day; only the latest 2 are tracked** for matchmaking and the final leaderboard
  (`[VIZ]` §17). *"A submission is not a save slot; it is a lineup decision."* `[DIARY]` §4.4 adds:
  diversify the second slot — two near-identical active submissions die together in a meta shift.
- **Every submission plays exactly one unrated self-play validation game** before it is allowed on the
  board (`[WKOG]`: `distinct submissions == number of validation episodes`). This is a free diagnostic:
  if the two seats' action streams hash-identical, your agent is a fixed script; **~40% of submissions are
  still identical to themselves at turn 719, so ~60% react to something.**

### 4.2 Convergence and how many episodes

- New entrants seed at roughly **600** (`[EPSO]`).
- The matchmaker "feeds uncertainty" — episode rate starts hot and decays as placement settles (`[MEAS]`,
  four concurrent submissions): **17.0 eps/h** at 2h old · 5.5/h · 4.9/h · **0.9/h** once settled over 3 days.
  Prose figure: 35 games in a newcomer's first hours to 118 in a single day.
- Real submissions accumulate **dozens to hundreds** of games (`[WKOG]` API checks: submission 55287214 →
  389 episodes; 55323653 → 77 episodes in one day).
- **Identical bytes can land on wildly different ratings.** `[DIARY]` §4.4: two uploads with the same
  SHA-256 `569cf2d0…` scored **2182.2** and **1210.1**; the second moved to **1865.6 with no code change**
  while being watched. The first had 89 games, the second 26. Treat any rating with < ~80 games as noise.
- **Rating inflation is real:** over 2026-08-05 → 08-10 the median rating of sampled seats rose **+531**,
  but for the **323 teams present on both days it rose +323** — so ~60% of the drift is real inflation and
  ~40% is the crawler changing who it watches (`[EPSO]`). **A rating is only comparable within a date.**

### 4.3 What rating is top-10

No source publishes a clean "top-10 = X Elo" table. The best available anchors, all dated:

| date | anchor | value | source |
|---|---|---|---|
| 3 Aug | ranks 1–5 | **2858.3 / 2778.8 / 2735.3 / 2717.9 / 2700.9** | `[DIARY]` |
| ~6 Aug | rank 1 / rank 2 | 2847.0 / 2821.9 | `[DIARY]` |
| 8 Aug | **rank 9** | **3085.4** | `[DIARY]` (C45) |
| 9 Aug | ladder top `avg_score` peak | **3218** | `[59U]` |
| 12 Aug | LB #1 / #2 / #3 | **3179.7 / 3174.3 / 3133.9** | `[LIVEMETA]` |
| ~29 Aug | ladder top `avg_score` | **3026** (192 below the peak) | `[59U]` |
| mid-Aug | field median rating | ≈ 2,030–2,050 | `[EPSO]` |

Working answer: **top-10 has meant ~3050–3200 since 8 August**, and the ceiling has been drifting *down*
since 9 August. `[59U]`: the top lost 192 points in 20 days with 11 of 20 days closing lower; the median
lost 271; the top-minus-median gap narrowed **483 → 229**. Episodes/day also fell **928 → 667 (−28%)**, so
part of that is a thinner sample. `[LADDER]` reaches the same conclusion and draws the strategic inference:
*"copying the current meta buys much less than it did, and the remaining edge has to come from somewhere the
field is not already looking."*

### 4.4 Ties, mirrors, and "play it safe vs a mirror"

- **Exact dollar ties are common and they are structural.** `[NOISE]`: **~1 game in 40 (2.5%)** of all ladder
  games ends with both banks equal to the dollar, and *"every single one is a pairing of two agents that
  opened identically."* `[WKOG]`: full-stream mirrors **tie to the dollar in 99%** of cases;
  self-play validation games tie ≈50%.
- **How Kaggle scores a tie is not documented in any source I read.** The community's own harnesses
  disagree: `[RANK]`'s Bradley-Terry counts **a tie as half a win each**; `[MEAS]`'s paired verdict scores
  strictly so **a tie is a loss for both**. Resolve this before you build a tie-seeking or tie-avoiding rule.
- **A mirror is not a coin flip — it is a dead heat.** The only thing that can separate two identical routes
  is the random weed spawn, worth **a few hundred dollars** (`[WKOG]`'s ablation: with
  `weedSpawnChance = 0.0`, **300 of 300** paired games tie to the dollar). So there is essentially nothing
  to "play safe" *for* against a true mirror — the game is decided by whether you differ at all.
- `[EPSO]` states the strategic consequence bluntly: *"the more of the field plays your route, the larger the
  share of your own schedule that is guaranteed to return nothing. Your edge becomes the field, and the
  decay shows up as **draws rather than as losses**. That is a hard cap no amount of tuning removes."*
- **The real "vs a mirror" tactic is the one-turn front-run, not safety.** See §3.3. Hamburger's original
  Clone Quad H1 reported **6–0 against its own anchor, mean margin +1,865.7**; `[DIARY]`'s c15 went **14–2**
  against the same base tape it was built on, purely from the wrapper.
- `[NOISE]`'s methodological trap: run a seat-symmetry control **without excluding exact ties** and it fails
  at **win rate 0.489, p < 0.001**, sending you after a seat bug that does not exist. **Always exclude ties
  from a sign test.**

### 4.5 How much of a result is real — the numbers that should govern your harness

- **σ(margin) = $27,300** across 22,702 episodes; the two banks of one episode correlate at **+0.73**
  (and still +0.73 after subtracting each submission's own mean, so it is the shared world, not skill).
  *"Roughly half the variance in a bank is the episode's own difficulty."* Use **within-episode margin**,
  never cross-episode bank.
- **The margin is heavy-tailed** (excess kurtosis ≈ +10 to +12, best fit Student-t with ~1.5 df). Use
  **median + paired sign test**, not mean + t-test. `[MEAS]` rejects normality at the 1e-50 level.
- **Games needed for a paired effect** (exact sign test, α=0.05, 80% power) — `[MEAS]`:

  | true paired win rate | **discordant** games needed |
  |---|---|
  | 65% | 97 |
  | 60% | 203 |
  | 57.5% | 352 |
  | 55% | 820 |

  **"The discordant count is the sample size."** 535 games produced only **173** usable discordant pairs.
  A 40-game cap has **13.1% power** against a real 57.5% effect.
- **Seed panels: 12 is the measured floor.** One fixed tape's win rate against one fixed opponent set moves
  **up to 59 percentage points across seeds**. `[MEAS]` picks **one seed per "world"** (the ordered pair of
  the first two shop draws = 8×8 = **64 worlds**), because random seeds cover only 28 of 64 worlds at n=40
  and do not cover all 64 until seed index 250.
- **Consecutive ladder games are serially correlated** (matchmaking chains opponents), so Wilson/binomial
  intervals on a ladder win rate are **too narrow**. `[EPSO]` measures ICC = 0.27 on one indicator
  → design effect 1.27.
- **Environment luck is small; matchup is everything.** The weed ablation moves a bank by *a few hundred*
  coins against margin spreads in the tens of thousands.
- **Tune on one seed set, decide on another.** `[RANK]`'s worked failure: a candidate measured **+4,450** on
  tuning seeds and lost **3–9 (−3,627)** on held-out seeds 8000–8005.
- **The right σ matters.** `Φ(μ/σ)` predicts realised win rate to **MAE ≈ 0.068**, but only when σ is the
  margin against *one* opponent across seeds. Feeding it a pooled spread across different opponents
  **inflates σ by a measured factor of 2.89**.
- Speed, if you want the sample size: `[4000x]`'s C++ port runs **0.18–0.30 ms/game single-core vs 815 ms**
  for the Python env (**~2,700–4,500×**), verified bit-exact on 15/15 traces (money + market inventory at
  every step). `[MEAS]` verified **286 of 287** recorded ladder episodes reproduce both final banks **to the
  dollar**, and all **360,009** price-domain points across 9 products × inventory −10,000…30,000.

---

## 5. Engine quirks and exploits — all verified against 1.32.7

Run `./.venv/bin/python research/verify_engine.py` — **12/12 pass**. Output quoted inline below.

| # | Quirk | Status | Evidence |
|---|---|---|---|
| 1 | **`BUILD_COOP` / `BUILD_PASTURE` are free** — no coin cost, only one action | **CONFIRMED** | Source has no cost check at all; test shows `tile → {'kind':'PASTURE'}` with no money delta beyond the same-turn animal/wheat buys |
| 2 | **`COLLECT_FERTILIZER` is real income** — 1/animal/day, fed or hungry, sellable, and **nobody in the town ever buys fertilizer** | **CONFIRMED** | 21 separate days banked revenue from *one* cow; 493 units to the floor for **$25,045** |
| 3 | **End-of-day auto-drop to shed**, overflow **destroyed** | **CONFIRMED** | 95 wheat + 30 carried melon → shed 100 (5 melon kept), **25 melon silently discarded** |
| 4 | **Last executable step is 718** | **CONFIRMED** | max `obs.step` seen = **718**, `(day,hour) = (29,22)`. Step 719 (day 29 h23) never runs |
| 5 | **CARE-bonus banking** | **CONFIRMED** | cow on day 3 carries `pending_care_bonus: 3`; first pickup is 6 milk, then 3 every 2 days. **Engine adds +1/day, not the +2 the rules text says** |
| 6 | **DROP + SELL in the same turn** | **CONFIRMED** | Units act before `_process_market`. Day 1: money 1996 → 2096 on a turn whose shed held **0** fertilizer before the DROP |
| 7 | **Shed cap 100 overflow loss** | **CONFIRMED** | see #3. Cap is **total across all item types**, not per item |
| 8 | **PLANT atomicity** | **CONFIRMED** | 3 PLANT CARROT requests with 2 seeds → **0 tiles planted, 0 seeds spent** (2→2) |

### 5.1 Additional quirks worth exploiting

**Day 29 has no end-of-day at all.** `_end_of_day` fires when `(step+1) % 24 == 0`; the last one is at
step 695 (end of day 28). So on day 29 there is **no auto-drop, no plant/animal production, no weed spawn,
no shop unlock**. Anything a unit is carrying at step 718 is simply **lost**. You must `DROP` by hand and
`SELL` in the same turn (see #6).

**Shed operations resolve BEFORE the LOCKED-tile guard.** All four shed-access tiles
`{(4,4),(5,4),(4,5),(5,5)}` accept `DROP`/`PICKUP`/`PLACE` from turn 0, even though three of them start
`LOCKED`. Every *other* tile op (`FEED`, `PLANT`, `BUILD_*`, `WATER`…) still no-ops on a locked tile.
**Two of my sources contradicted each other here** — `[RANK]` MD 36 claims "(4,4) is the only usable shed
tile"; `[4000x]` and `[ASG]` say shed ops bypass the guard. **I tested it: `[4000x]`/`[ASG]` are right and
`[RANK]` is wrong on 1.32.7.** Verified output: `DROP` from locked (5,5) → `shed = {'MELON': 3}`;
`PICKUP` from (5,5) works; `BUILD_PASTURE` on (5,5) correctly stays `LOCKED`.
This matters on day 0, when all three hires spawn on tiles you have not bought.

**A full shed blocks `BUY_PRODUCT` and `BUY_ANIMAL` but not `BUY_SEED`.** Verified. This is the
starve-your-own-herd failure mode `[DIARY]` flags from 1.32.4.

**`SELL` at the $1 floor does not add to market inventory.** Verified: WOOL inventory 15,000 → 15,000,
money +1. Pure value destruction with zero further price impact.

**`BUY_PRODUCT` is quoted at post-buy inventory** so a buy/sell round trip against an unchanged market nets
zero — and it covers **WHEAT and FERTILIZER only**.

**The shop draw is not independent of the players** (`[YARN]` §5, `[VIZ]` §10, `[WKOG]` §3.1). One
`random.Random((seed*1_000_003) ^ day)` per day is consumed in a fixed order: player 0's weed rolls, then
player 1's, then `rng.choice(sorted(SHOPS))`. `spawn_weeds` only calls the RNG on **empty** tiles — so how
much bare ground each farm leaves changes how many words are consumed and therefore **which shop opens**.
Consequences: (i) **you cannot precompute your shop draw from the seed**; (ii) it does not bias the draw
(each shop still comes up within a couple of points of 1/8); (iii) `[VIZ]` ran the control both ways —
the *same* bot with one constant changed drew the **identical town on 12/12 seeds**, but two *different*
bots drew different towns on **12/12**. So the town is a valid control for your own A/B, and is silently
lost the moment you benchmark against someone else's agent.

**Python dict insertion order is load-bearing** (`[4000x]`'s "this one cost me a day"). Per-unit inventories
are dicts and `DROP`/end-of-day walk them via `list(inv.items())`. When the 100-item cap binds, **insertion
order decides which items win the last slots and which are destroyed.**

**PLANT atomicity counts phantom hands.** `[4000x]`: demand is summed over *every submitted unit action,
including ones addressed to hands that do not exist*, because the blocked set is computed before the
position lookup no-ops. Submitting plant orders for hands you did not hire silently kills your real plants.

**Trace indexing off-by-one:** the action that drives `steps[t] → steps[t+1]` is recorded on the
**resulting** state, i.e. `env.steps[t+1][seat].action`. Get this wrong and every replay analysis shifts a
turn (`[4000x]`, `[XR]`).

**Nothing observable differs before turn 48** (`[WKOG]` §3, measured over 6 seeds × 5 opponents):

| what first becomes visible | earliest turn | median turn | channel |
|---|---|---|---|
| anything at all | **48** | 72 | a weed on the opponent's land |
| your own farm | 72 | 168 | your weeds, then the shop draw |
| **anything about your opponent** | **136** | **175** | market inventory moving under their sales |

So adaptivity is worth **exactly zero before turn 48** and nothing about the opponent before turn 136 —
the first fifth of the episode is committed blind. Turn-24 opening agreement between two agents is engine
determinism, not evidence of copying.

**Other constants worth having in one place:** hire spawn is the first free shed-access tile in NW→NE→SW→SE
order, ties broken by lowest occupancy. Plants start at `consecutive_unwatered = 1` (the planting day counts
as dry) and become a WEED at 2 — **water on the day you plant**. Animals escape at 2 unfed days and the
structure remains. Wheat cannot reach its 6-unit cap without fertilizer (1 base + 3 watered window days = 4);
melon hits its 6 cap on water alone by age 10. Watering window for one-shot crops is
`ceil(max_yield_day/2) ≤ age ≤ max_yield_day`. 10 market orders max per turn. 1 s per turn, 60 s overage.
Invalid actions are **silent no-ops** — the engine never errors at you.

---

## 6. Failure modes

### 6.1 What the field's own instrumentation counts (`[XR]`, 245 leader episodes)

These are the **leader's own** numbers — "not targets, but what the strongest agent happens to tolerate":

| indicator | leader reference | distribution I recomputed from the embedded dataset |
|---|---|---|
| `stranded` — shed + hand inventories × last price at the bell | **$442** median | mean $545, p90 $1,184, max $1,878. **41/245 (16.7%) end at exactly $0; 113/245 (46.1%) strand >$500; 51/245 (20.8%) strand >$1,000** |
| `pass_work` — idle unit-turns *with work available* | ~330 | median 330, p10 319, p90 341, range 313–361 → **≈3.5% of all unit-turns wasted by the best agent on the board** |
| `fallow_late` — mean empty tiles days 25–29 while still holding seeds | **13 tiles** | median 13.0, p90 17.2, max 30.8; only **2/245** episodes end at 0 |
| `shed_cap_turns` — turns at shed ≥ 100 | **0** | — |
| `floor_sells` — SELLs issued at price ≤ 2 | **0** | — |
| `care` | ~280 CARE actions | `[ASG]`'s route: 343 |

**Movement is not waste.** Measured on 40 episodes of a leader vs 40 of a mid-table agent: the leader spent
**53.8% of unit-turns walking and 3.8% standing still**, against **42.9% and 11.8%**. *"The ten points of
movement the weaker agent did not spend came back as idling in place."*

### 6.2 The high-frequency bug list (`[DIARY]` §7, from real replay audits)

| bug | symptom | fix |
|---|---|---|
| CARE priority ranked above melon WATER | day-9 watering covers only part of the field; **yield ~70 instead of ~96** | water first during ages 6–12 |
| No `DROP` after `HARVEST` | produce stuck in unit inventory; the melon IPO is underfunded; `SELL` only ever sees the **shed** | DROP whenever carrying a melon/milk stack |
| DIG melon tiles for pastures too early | destroys fruit before harvest | protect valuable melons until sold |
| Buy many cows on day 0 with no feed reserve | **animals escape by day 2** | reserve wheat cash before animal spam |
| Fixed 10 cows forever | mirror banks collapse toward **~40k** | add sheep/strawberry/opponent routing |
| Optimise only mean bank vs `starter` | high local bank, mediocre Elo | H2H vs strong bots, both seats |
| Two near-identical active submissions | a meta shift kills both | diversify the second slot |

### 6.3 Animals starving — the specific mechanism that costs whole games

`[DIARY]` §15.1 is the best-documented single failure in the corpus: the opponent bought **14–19 wheat**
before C92's slot-eight five-wheat order; the raised shared price left cash for only four; **one sheep went
unfed and disappeared on day 2**; those four losses averaged **−13,606**. Two compounding causes: the market
slot queue (§3.4) and the 1.32.4 rule that a full shed blocks `BUY_PRODUCT` entirely.

`[RANK]`'s checklist item 3 — *"Feed before you expand. Animals die permanently after two unfed days; buy
wheat before land or livestock"* — and item 8 — *"Count what your hands carry, otherwise you sell your feed
each morning and rebuy at double"* — are the two guards worth writing first.

### 6.4 Weeds

`weedSpawnChance = 0.005` per empty unlocked tile per night. `[DIARY]` §12 is the definitive study, and the
conclusion is narrower than "clear every weed":

- **C90** (dig only with truly idle labour): **16–14–30** vs its parent over 30 untouched paired seeds,
  mean margin +234. Marginal.
- **C91** (add a future-use guard): economically **neutral** — 17–17–66 over 100 paired games, −35.2 mean
  coins. "The guard improves causal discipline, not measured strength."
- **C92** (substitute `DIG` when a weed *blocks a productive action right now*, delay only that actor by one
  turn, absorb the delay at the next scheduled `PASS`): **22–6–72 vs C91** (+446.6) and **22–6–72 vs C90**
  (+388.1). In one concrete episode a weed at (5,3) blocked `BUILD_PASTURE` + `PLACE COW` at step 176;
  repairing it turned a **−7,288 loss into a +3,455 win**. With weeds disabled C91 and C92 tie exactly,
  confirming the overlay is dormant when nothing is blocked.

`[ASG]` implements the same idea with an 8-turn route replay after the DIG, and its telemetry shows DIG
firing **29–49 times per season** depending on the branch.

`[59U]` adds the counter-intuitive note: **the reference agent with the most weeds is the third best.**
"Weeds are a symptom of an action budget, not of a bad plan. Planting more than you can tend still beat
planting less."

### 6.5 Unsold inventory at the end

`[RANK]` checklist item 7: *"Stop investing near the end — coins spent on day 28 never come back, and shed
contents at the final bell score exactly nothing."* The leader still strands a median **$442** and >$1,000
in one game in five (§6.1), so a clean terminal liquidation (§3.5) is worth roughly a thousand coins — real,
but smaller than a single market-timing swing.

Also note `[XR]`'s inverse finding: its author's own agent stranded **~$7** at the bell — *sixty times less
than the leader tolerates* — and flagged this as **over**-liquidating, i.e. selling into a depressed price
rather than leaving goods unsold. The optimum is not zero.

### 6.6 Shed overflow

`shed_cap_turns` reference is **0** — top agents simply never let the shed reach 100. Given that a full shed
also blocks `BUY_PRODUCT WHEAT` (and therefore feed), treat 100 as a hard invariant, not a soft target.
`[ASG]` reserves `shed_headroom = 15` before entering any market-maker position.

---

## 7. Where the field is demonstrably *not* looking

Ranked by (my estimate of) expected value, with the evidence:

1. **TOMATO.** Zero of 296 top-band players sell it. Post-16-Aug it has the steepest scarcity curve in the
   game. Season pot **$13,680** at base, and the price is **$91 at the expected end-of-season deficit** and
   **$356 at the p90 town draw**, because nothing ever pushes its inventory back up. (§2.2)
2. **The whole hinge trio.** TOMATO + CARROT + EGG = **$36,525** of season pot that essentially nobody
   contests, on curves that were re-tuned two weeks ago in exactly that direction. `[DAILY]` cell 20 asks
   the open question outright: *"whether the field has learned to farm the spikes."*
3. **Shop-conditioned herd selection.** `[ASG]` is the only public agent I found that branches on the shop
   draw, and it swings **+6 sheep / −5 cows** when YARN_STORE opens first (+51% wool units, −52% milk units).
   Its `yarn_third` branch is *allow-listed to two openings only* and its author explicitly calls a third
   branch "an open question, not a settled no". Meanwhile **34.4% of towns never open a yarn store at all**,
   and the modal meta plants 4–6 sheep regardless. `[XR]` cites a top router pricing its second shop branch
   at **+0.136 rating points per game over a 24,000-game census**.
4. **Market slot-zero discipline.** A 7% price advantage for free (§3.4), and a documented **−13,606 mean
   loss** when you get it wrong on the wheat opening.
5. **Selling the wheat you grow.** Wheat is on **5 of 8 shop menus** (P(no buyer) = 0.04%), has the deepest
   market in the game, and a **525-unit season pot**. `[YARN]`'s closing line: *"Wheat is the boring answer
   and the arithmetic keeps agreeing with it. It is the only good whose worst-case town still supports a
   real farm."* The field grows wheat purely as feed.

Two structural facts that bound all of the above: the **$206k town pot is shared**, so anything you take
mostly comes out of the opponent's half; and **fertilizer's $25k is outside the pot entirely** but already
fully exploited by 296/296 players.

---

## 8. Where the evidence contradicts your working assumptions

### (a) "Buy all four quadrants as early as cash allows" — **CONTRADICTED, strongly**

The SE quadrant is the single most thoroughly falsified idea in the corpus. `[DIARY]` §13: **450 games,
5 seeds, both seats, three implementation families × four gating policies — every four-quadrant variant lost
10–0** to the three-quadrant incumbent (BT 2039 vs 1724, mean margin −3,687). Three *fully productive*
four-quadrant Seb routes also lost 10–0, by mean margins of **14,608 / 29,016 / 36,980**. The frozen
candidate went **0–40** on fresh paired seeds. `[LIVEMETA]`: **≈0% of top players buy SE**; every one of the
top-5 compositions is `NE+NW+SW`.

"As early as cash allows" is also wrong for the first three. The consensus is **NE on day 5–6** and
**SW on day 8** — not day 1 — because the median on-hand cash at day 5 is only **$545** and the opening
money is contested by seed, animal and feed purchases. `[DAILY]` §5 measures `first_land_day`'s rank
correlation with final bank at **≈ 0.00** across every replayed seat.

**However**, note the one dissent: `[DAILY]` §4's record-holder fingerprint attributes the leader's edge to
"labor and land". And the SE result was measured *before* the 16-Aug hinge patch — if you build a
tomato/carrot line you need tiles for it, and 25 more tiles is the only place they come from. Re-test SE
specifically as *hinge-crop land*, which is not what any of the 450 games tested.

### (b) "Hire 11–14 hands/day" — **PARTLY CONTRADICTED at the top of the range**

The measured field consensus is **4 by day 4, 8 by day 6, 11 by day 10, 12 from day 13 to the bell, with an
IQR of 0–2 hands all season** over 490 seat-seasons. So 11–12 is right; **13–14 is off the observed
distribution** and expensive: the 13th hand costs **$6,990** over a season and the 14th **$11,310**, against
a median bank of $84k and a winner-vs-loser gap of $4,089. You would need each of those hands to generate
more than 8–13% of a whole bank.

Also relevant: `[VIZ]` §15 item 1 **measured hands as a loss** when there is no work for them —
idle hands cost exactly the hire fee (−4 coins on 10/10 seeds), and hands wired to run the farmer's job list
did *worse* (−58 on seed 0). *"Extra hands are extra actions, not extra judgement."* Hire to your work
queue, not to a constant.

### (c) "Melon is the best early crop" — **SUPPORTED at small scale, CONTRADICTED as a strategy**

`[VIZ]`'s +11,665 (se 558, 8/8 seeds, re-measured across three engine versions) is the strongest single
crop measurement anyone has published, so melon is genuinely excellent — **at 6–16 tiles**. The field
agrees: **6.3 melon seeds bought days 0–4**, `[ASG]` buys exactly 11, `[DIARY]` says "~6–16, not a full
25-tile dump".

What breaks is scaling. **No shop ever buys melon**; the town centre's 1/day is **30 units for the whole
season**, against a $1 floor at 158 units. `[59U]`'s five-season natural experiment shows the price walking
256 → 280 identically to the coin when nobody sells, and crashing to **7** when one agent does. A second
melon dumper hits the floor. Treat it as a one-off capital event around day 10–12, not an early crop line.

### (d) "Cows are the best animal" — **CONTRADICTED on rate, SUPPORTED on risk. It is a portfolio call.**

Per-animal season gross at base price, with CARE (my simulation through the real end-of-day routine):

| | cost | units/season | gross @ base | gross per $ invested | P(dead market) | season town demand |
|---|---|---|---|---|---|---|
| **SHEEP** | 500 | 38 WOOL | **$7,600** | **15.2×** | **34.36%** | 228 |
| **COW** | 400 | 39 MILK | $6,240 | 15.6× | 2.33% | 327 |
| **GOOSE** | 300 | 56 EGG | $2,800 | 9.3× | 10.01% | 228 |

So sheep out-gross cows per animal (`[59U]`: sheep top the published rate table at **266.7 coins/tile/day**,
the best figure in the game) and cows edge them per dollar. Cows win on **risk**, not on rate:
34.4% of towns have no wool buyer at all, and wool floors after only **59 units**.

Two things sharpen this. First, `[RANK]`'s **measured** experiment says pure cows beat mixes (16c = 57,407
vs 10c/6s = 52,957) — **but that +4,450 evaporated on held-out seeds, losing 3–9 with a −3,627 margin.**
Treat it as unreplicated. Second, and more importantly: **at the meta's own herd sizes both milk and wool
are over-supplied.** Simulated with a realistic ramp (4 sheep on day 0, cows arriving days 4–10 as in
`[ASG]`'s decoded route), one player produces **237 milk and 136 wool**; two players produce **474 milk
against 327 units of season town demand (+45%)** and **272 wool against 228 (+19%)**. Everything past the
drain goes down a linear curve that floors at 76 units for milk and a quadratic one that floors at 59 for
wool. That surplus is a large part of why the median bank ($84,151) sits well below the even-split-at-base
figure ($103,095).

The actionable form: **animal counts should be sized to the town's demand for their product, and the
cow/sheep dial should be conditioned on the shop draw** — which is exactly what `[ASG]` does and almost
nobody else. Geese are the one clear negative (32/32 configurations lost), but the mechanism is volume
(896 eggs vs 228 demand), so **2–4 geese sized to the egg pot may now be positive under the hinge** — that
is untested by anyone.

### (e) "Sell continuously at roughly the town drain rate" — **DIRECTIONALLY RIGHT, but it leaves the two biggest levers on the table**

The rate is right: matching the drain keeps inventory near `I0` and price near base, and metering beats
dumping by **1.30×–1.59×** on wool/milk/strawberry. The field does exactly this (batches of 5–15).

Three corrections:

1. **Melon is the exception — it is nearly price-inelastic.** 100 melons in one order still average
   **$217/unit** (vs $80 for wool). Metering melon is worth **1.03×**. Sell it in lumps and spend the
   logistics elsewhere. `[VIZ]`'s meter: the whole-season slippage of a *deliberately naive* seller is
   **104 coins** on carrot and **827** on melon — real, but two orders of magnitude below a market-timing swing.
2. **Selling *below* the drain rate is strictly better for the hinge goods.** Because CARROT/TOMATO/EGG now
   spike superlinearly below `I0`, under-supplying them and selling late into a deepened deficit beats
   matching the drain. This is the opposite of the right policy for wool/milk/strawberry.
3. **When you sell matters more than how much.** This is the corpus's loudest single finding.
   `[DIARY]` c18 changed **20 field turns and 112 market turns** and swept its gate — *"the current edge
   comes from inventory-sale timing rather than another change in herd composition."*
   `[59U]`: the four top reference agents **share one field plan and differ only in the order they sell in,
   and that order alone is worth 15,994 coins — 35% of everything the best individually designed farm earns
   in a whole season.** `[DIARY]` §15.2: identical routes, and selling **one turn** earlier or later
   reversed the matchup by **5,300–5,700 coins**. Continuous drain-rate selling with no opponent model
   forfeits all of that.

---

## 9. Unresolved / conflicting, flagged rather than smoothed over

- **How Kaggle scores a tie.** `[RANK]` treats a tie as half a win; `[MEAS]` treats it as a loss for both.
  Nobody quotes the actual rule. Given ~2.5% of ladder games and ~99% of true mirrors tie, this is worth
  resolving from the competition rules before building any tie-related logic.
- **`[RANK]` vs `[4000x]`/`[ASG]` on shed-access tiles.** Resolved in favour of the latter by direct test
  (§5.1), but it means `[RANK]`'s day-0 logistics advice is wrong on 1.32.7.
- **`[LIVEMETA]`'s embedded market model is pre-hinge** and is presented as authoritative. Do not import its
  §1 constants.
- **`[RANK]`'s pure-cow result is unreplicated** and its author says so.
- **`[59U]`'s "sheep are best" headline is refuted inside `[59U]` itself** (MD 14). Read the whole notebook,
  not the title.
- **`[TIE]` (andrewsokolovsky/kaggriculture-breaking-the-tie) contains no tie analysis** — the slug was
  reused for a DAgger imitation-learning pipeline whose payload is a base64 blob. Nothing to extract.
- **Nobody has published a turn-by-turn decode of the dominant opening.** `[EPSO]` measures that hundreds of
  teams are byte-identical to turn 100 but only decodes the trivial all-`PASS` stream. `[ASG]`'s five
  routes are the closest thing to a readable strong tape in the corpus, and they are in
  `research/kaggriculture-adaptive-shop-guard/`.
- **Rating numbers are only comparable within a date** (~60% of five-day drift was real inflation).
  Every rating in §4.3 carries its date for that reason.

---

## Appendix: what was pulled

All under `./research/<slug>/`. Text renderings (markdown + code + outputs) are reproducible with the
extractor logic; `research/verify_engine.py` is the only executable artifact and touches nothing outside
`kaggle_environments`.

| slug | author | what it is worth reading for |
|---|---|---|
| `kaggriculture-findings-from-zero-to-top-meta` | raykkretzschmar | **The single best source.** A real agent-development diary c14→C95 with per-candidate gate records, the SE negative result, the feed-denial and fertilizer-preemption loss audits |
| `kaggriculture-what-the-top-farms-do-a-live-meta` | cjlcjlcjl | Daily modal-farm census by Elo band; sell rhythm and build-order tables. **Pre-hinge market constants** |
| `kaggriculture-daily-replays-the-live-meta-report` | georgymamarin | Ladder-wide statistics, the +0.73 seat correlation, and the only mention of the 16-Aug patch |
| `kaggriculture-visualized-what-every-crop-pays` | georgymamarin | The best mechanics reference; measured melon/hands/slippage experiments with standard errors |
| `kaggriculture-rank-your-agent` | raykkretzschmar | Local BT harness; the shop-demand argument; the animal-mix experiment and its held-out failure |
| `the-best-thing-to-farm-has-a-market-of-59-units` | busyaprime | Price-depth vs season-ceiling; the melon natural experiment; the "selling order is worth 15,994" finding |
| `one-town-in-three-has-no-yarn-store-at-all` | busyaprime | Exact enumeration of all 6435 towns; joint dead-market probabilities; the player-coupled shop draw |
| `what-actually-wins-on-the-kaggriculture-ladder` | busyaprime | Replay-parsing methodology; the "ladder stopped climbing" thesis (unexecuted — no outputs) |
| `measure-twice-submit-once-know-your-error` | destbreso | **Best evaluation methodology.** Sample-size tables, the 64-world seed panel, engine-exactness validation |
| `x-ray-your-agent` | destbreso | Agent-diagnostic instrument + the 245-episode leader reference distributions |
| `kaggriculture-know-your-noise` | destbreso | σ(margin) = $27,300, rating-band gradient, the tie trap, bank is normal not lognormal |
| `kaggriculture-what-kind-of-game-is-this` | destbreso | Game-theoretic framing, seat-advantage disproof, the weed ablation, observability horizons |
| `everyone-is-playing-the-same-opening` | destbreso | Opening-stream census, mirror/tie dynamics, "your edge becomes the field" |
| `4000x-environment-speedup-kaggriculture` | nikital7 | Bit-exact C++ port; the three porting gotchas (RNG, dict order, market slot index) |
| `kaggriculture-adaptive-shop-guard` | reyhanksatria | **A real strong agent, decodable.** Shop-conditioned routing, clone detection, terminal liquidation |
| `kaggriculture-breaking-the-tie` | andrewsokolovsky | Nothing usable (see §9) |
