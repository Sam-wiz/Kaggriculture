# Idea backlog — every direction, with status

Goal: **rank #1** (Crop Dusta, 3023.9). Nothing else counts.
Governing law, from repeated measurement: **demand is fixed and shared — you cannot out-produce it.
Producing more of a valuable product destroys its price. The only wins are (i) capturing more of the
fixed pool than the opponent, and (ii) not wasting resources.**

Status key: **SHIPPED** · **TESTING** · **OPEN** · **CLOSED** (measured dead, do not retry)

---

## 1. Market contention / "sabotage" — **SHIPPED** ✅ *(user's idea d)*
Sell from earlier market slots than the opponent. Orders settle slot-by-slot, each committed unit
raises shared inventory, so earlier slots get better prices — and 100% of our sell value collides
with theirs on the same turn/product.

- Slot hoisting: **+3,474, 96W-0L** on fresh mirror seeds. Falsification control (SELLs last): −65,942.
- Sort key upgraded from static steepness to **live value-at-risk** (qty × price): **+1,565 more**.
- Verified: atomic orders (HIRE/BUY_LAND) are never truncated by the 10-order cap.

## 2. Track opponent crops, keep demand up for price — **CLOSED** *(user's idea a)*
Principle is correct and is *why the tape hedges*, but every implementation loses.
Phase-timing (phase 1 prices genuinely 1.7–2.9% higher): **−103,111**; hot items only: −58,654.
Deferring costs more than the better price is worth (shed cap 100; a delayed sale becomes a lost one).

## 3. Grow what the open shops want — **CLOSED (supply side)** *(user's idea b)*
Shops *are* the demand: one shop = 108–216 units vs the town centre's 30 (**4–7×**); 8 shops fire
936×/game. CARROT (PET_CAFE) and WOOL (YARN_STORE) get **2×** from single-product shops.
But supply-side adaptation fails: crop substitution **−28,275** (per-crop yield windows), all-cow
**−90,638** (milk crashes $160→$67), all-sheep **−69,822**, demand-aware swap −6,755.

## 4. Manage hiring like HR — **CLOSED** *(user's idea c)*
Dropping a single daily hire: **−88,691**. Labour massively outvalues the fib cost (~$232/day).

## 5. Opponent modelling — **OPEN** *(user's idea 1)*
**Capability proven:** we can reconstruct the opponent's trades from public data at **97.9% exact**
(`their_trades = Δinventory + town_drain − our_trades`; 6,329/6,462 item-turns). Available from turn 1.
**Unresolved: what decision does it change?** We already hoist *all* sells to the front. The genuinely
different case is a **dying or off-tape opponent** — the market is then uncrowded and we could sell
far more aggressively. Needs a decision rule before it's worth building.

## 6. Race the zero-demand goods — **CLOSED**
**FERTILIZER has no consumer at all** (no shop, not in the town-centre list): inventory only rises,
price goes $100 → **$1** and never recovers. MELON is in no shop either (30 units of town demand all
season). For these the pool belongs to whoever sells first and waiting is strictly negative.
Tested: forcing them into the earliest slot is **−5,829**, selling them unmetered is **+0**.
Reason: the value-at-risk sort already races them *dynamically* — early on, when fertilizer is $100,
it ranks high on its own; forcing it first once it has fallen to $1 wastes the best slot and pushes
milk/wool later. The theory was right and the shipped ordering already captures it.

## 7. Late-only animal adaptation — **CLOSED**
Milk vs wool value swings enormously by seed (seed 2100: milk $166 / wool $87; seed 9500: milk $37 /
wool $217 — a ~$48k revenue swing) and the tape buys 9 cows + 9 sheep regardless.
Blanket swap failed (−6,755); diagnosis is that **animals are bought days 0–11 but the decisive shops
unlock days 12–24**, so early swaps are blind. Restricting to later purchases confirms the diagnosis
but never turns positive: day 1 **−9,768** → day 8 **−3,750** → day 10 **−1,754**. It converges toward
zero *from below*, so the optimal amount of animal swapping is **none**.

## 8. Endgame liquidation — **CLOSED**
Only **$219** stranded at step 718 (9 fertilizer worth $9 because it's at the $1 floor, 6 wheat,
1 sheep yield). 0.2% of bank — not worth engineering.

## 9. Submission cadence — **SHIPPED**
Quota resets **00:00 UTC**. Episodes take ~200s; a submission plays **11–19/hour** and needs ~110
games (6–11 h) to converge — and at 133 games ours was still under-rated by ~250, so true convergence
may need 200–300 games.
Only the **latest 2** submissions are matched, and the leaderboard shows the best **active** one, so
churn is expensive. **Max 4/day at 00:01 and 12:00 UTC** — *not* 22:00, which leaves the second pair
only 2 hours. Near the deadline: freeze and let one pair run for days.

## 10. Clone the #1 agent from replays — **CLOSED**
The standard winning move in Kaggle sim comps (Lux AI S1, Hungry Geese). Tested: replaying Crop
Dusta's own 70 recorded tapes goes **0/70, mean margin −113,523** — they're adaptive, so a tape from
another game doesn't transfer. Would need a real state→action model (the from-scratch planner that
measured −49,860).

---

## 11. Sell-volume aggressiveness — **CLOSED**
Re-opened because slot ordering changed the payoff to pushing more volume through early slots.
All flat: greedy −4, window_cap 48/72 +0, smaller feed reserve −533. Volume is bounded by the tape's
own schedule (`_sched_window`), not by the tranche cap, and widening it buys nothing.

## 12. `drain_gate` — **CLOSED (was a measurement artifact)**
Looked like a 94.5% win rate. It was a tie-break artifact: in the mirror an unchanged candidate ties
*exactly*, so any perturbation wins those ties by $3–6 — values 1, 3 and 5 all scored identically in
opposite directions. Against a genuinely different opponent the change is worth **−$2 ± $2** against
a margin of +$2,766 (stdev $914). See MISTAKES.md §C9: **score the mirror by margin, never win-rate.**

## 13. Route selection — **CLOSED (too small / inconsistent)**
The tape carries two complete routes and picks at step 360 with the author's rule. This is the one
adaptation that *cannot* hit the yield-window trap, because each route is a whole internally
consistent plan. Measured:
- always route 1 **+2,745** vs the author's selector **+2,560**, and the per-seed oracle is only
  **+2,771** — i.e. total headroom from perfect route choice is just **+212**.
- But in the MIRROR, forcing route 1 is **−12 / −43** (no gain), while vs a different opponent it
  showed +200. Inconsistent, so not shippable under MISTAKES §C9.
- **Differentiation hypothesis tested and dead.** 2x2 of (our route x their route): matching +0,
  differentiating **+0**. Route 1 simply beats route 0 by ~$68 head-to-head; there is no
  game-theoretic niche effect. Worth revisiting only if a cheap oracle-selector appears.

## 14. The $50 cash trap — **FOUND, and it confounded earlier work**
One unplanned $50 seed purchase in the opening costs **-13,836**, because the tape runs the opening
on a $0-9 minimum and a starved HIRE is the death spiral. Gating on `day>=12 and money>=5000` takes
it to -50. Every earlier crop experiment bought seed early, so their magnitudes were inflated
~70x. Conclusions unchanged after re-testing, but see NOTES.md.

## 15. Match the top players' crop mix — **CLOSED (re-tested clean)**
Everyone above us plants 2-4x more carrot and less wheat (Jesse #2: 23 carrot / 171 wheat;
Giulio #5: 19/175; Crop Dusta 34/131; **us 9/195**). Grafting it on, with the cash trap fixed:
+5 carrot **-399**, +10 **-795**, +14 (matching the top) **-5,876**. Their advantage is a coherent
tape built around that mix, not a mix we can bolt on.

## 16. Retest of everything the cash trap confounded — **ALL STILL CLOSED**
| idea | original | retested clean |
|---|---|---|
| land hoist (days 5/8) | -509 | **-15 / -162** (neutral, not a win) |
| wheat -> carrot | -28,275 | -399 |
| strawberry -> tomato | -34,034 | -100 |
| animal swap | -6,755 | -89,164 (cash-positive direction is *worse*) |
| **defer day-0 animal buys** (the inverse experiment) | new | **-119,077** |

Conclusion: the opening is a tuned cash schedule, load-bearing in BOTH directions. Adding spend
costs $14k; removing it costs $119k. Nothing here is exploitable.

## 17. Price-impact slot ordering — **SHIPPED** ✅
Rank sells not by raw value (qty x price) but by **the dollars lost from going second**:
`qty x (price_now - price_after_their_burst)`. That gap depends on the curve — MILK/WOOL/STRAWBERRY
halve after 31-42 surplus units while WHEAT/EGG barely move — so a thin product deserves the earliest
slot even at a lower headline value. Burst estimate 30 units (10/30/60 all positive, 30 best).
**+729 on holdout (44W-4L); 71W-9L (+772) vs the previous shipped build; 48W-0L (+3,377) vs sub_tuned.**

## 18. Learning from 102 mined episodes — **our play is invariant**
Mined 102 of our own games with both players' full behavioural profiles (`scratchpad/learn.py`,
opponent tapes kept in `mine/opp/`). **Our behaviour is identical in wins and losses** — WATER
1,117 vs 1,117, MOVE 3,284 vs 3,284, hires 286 vs 286, every metric ~0 difference. We run a fixed
script, so outcomes are decided by the matchup and seed, not by anything we do differently.
*There is no situational error to fix* — which is why every situational fix has come back flat.
The only behavioural gap that survives: in losses, winners plant **17 carrot vs our 9** and
**182 wheat vs our 195**.

## 19. Fixed-tape detection — **tool built, needs top-player data**
Hashing an opponent's action sequence across games identifies who runs a portable fixed tape.
Of 8 opponents seen twice, 3 are deterministic (AkiraIshikawa, VAP RF5, Jince) — but we already beat
all three 2-0. **The method is ready; it needs a top-10 player's episodes as input, which requires
their submissionId (visible only in the leaderboard URL in a browser).**

## 20. Crop substitution with tile-schedule repair — **CLOSED**
The mechanism behind every failed substitution is that the tape keeps tending on the OLD crop's
timetable. Adding repair (harvest/water the substituted tile when a unit stands on it) changes
**nothing** (-176 with repair, -176 without) — the tape moves units away after planting, so nobody is
ever standing there when it ripens. Proper repair needs routing, i.e. the planner.

## 21. The top 3 decoded — **they are reactive tape libraries, and the gap is CROP MIX**
Mined keiz (#1), Jesse Bullard (#2), Andrey Tikhomirov (#3) from their submission ids.

**Structure:** none runs a fixed tape. They branch on **shop-unlock days**:
Andrey diverges at day 3 in 64/66 game pairs; Jesse at days 3/6/7/9/11/12/17/18/19; keiz at day 0
(step 5) and days 6/7/8/11. They are tape libraries with routers — our architecture, but with many
branch points where ours has **one, at day 15**.

**Cloning them does not work.** Replaying keiz's own tapes scores 24-44k against their original 93k
median (0/12 beat us, mean margin -67,063). Their actions depend on state that does not survive
transplanting — so retrieval/imitation by tape is dead, and cloning would need a learned
state->action model.

**The gap is entirely crop mix, not effort:**

| metric | us | keiz | Jesse | Andrey |
|---|---|---|---|---|
| plant WHEAT | 194 | **119** | 174 | 172 |
| plant CARROT | 9 | **42** | 23 | 20 |
| plant TOMATO | 0 | **9** | 0 | 0 |
| PASS (idle) | 560 | **244** | 574 | 328 |
| WATER | 1,119 | 981 | 1,151 | 1,302 |
| HARVEST | 466 | 405 | 470 | 465 |
| land buy days | 6/11 | 6/11 | 6/11 | 6/11 |

keiz does FEWER productive actions than us and banks more (mean 95,923 vs our 88,606). Land timing
is identical across everyone, confirming it is not the differentiator. **The entire edge is planting
less wheat and more carrot/tomato** — which we cannot graft on, because our tape's watering and
harvest schedule is tuned to wheat (every substitution attempt fails for that reason).

**Conclusion: capturing this needs a coherently re-planned tape, not an overlay.**

## 22. In-window watering with idle units — **CLOSED (engine gate)**
Watering gives no yield bonus to `ongoing` crops (STRAWBERRY, TOMATO) -- the engine gates it on
`if not crop_data["ongoing"]`. 104 of our 143 in-window misses are strawberry, so the apparent
$10k opportunity does not exist. Verified end-to-end: layer fires, covers 16 more tiles, tile yield
stays at exactly 632, bank identical. Weeds are also negligible (~$150/game).

## 23. Tape search — **SHIPPED** ✅ (after fixing my own threshold)
~3,400 hill-climbing mutations on the action tape, scored by mirror margin. Nothing cleared the
+150 accept bar individually, and I nearly called it dead. But several confirmed *reproducibly* at
+22 to +45, and **every hit was a late-game planting edit (steps 476-669, days 20-28)** where the
tape plants crops that can no longer pay for themselves. Stacking the 8 with mean confirm >= +15:
**+214 / +221 / +211 across three DISJOINT seed sets** (60W-4L, 60W-4L, 63W-1L).
Lesson: an arbitrary accept threshold was rejecting real wins one at a time. Small reproducible
gains should be stacked, not discarded.
Shipped in `port3/newtape_final.py`: beats the live best 76W-4L (+223).

## 24. Score-aware variance (play the scoreboard, not the bank) — **CLOSED**
Scoring is win/loss, so when behind you should raise variance and when ahead lower it. Implemented
and it works *mechanically* -- sigma rose 12x (1,075 -> 13,397) exactly as designed. But the mean
fell faster than sigma grew, so mu/sigma got **worse** (-2.34 -> -2.74) and the win rate never moved
off 0%. **There is no mean-neutral variance source in this game**: every lever is "when to sell",
and the thin market punishes lumpy selling. Sound theory, killed by the price curve.

## 25. Shop-mismatch as an edge case — **cancels against tape-runners**
YARN_STORE is the only wool consumer; if it never unlocks, our ~300 wool units meet 30 units of
demand. But measured against the bare tape the draw affects BOTH sides equally: margin stays
+2,161 to +2,794 and win rate 97-100% **regardless of the draw**. So the mismatch only costs us
against *adaptive* opponents -- i.e. the top few players specifically, not the field.

## Open questions for discussion
- **(5)** What should opponent modelling actually *change*? Is the dying/off-tape opponent case
  common enough on the ladder to be worth a branch?
- Is there any lever that increases the **total pool** rather than our share of it? So far the answer
  looks like no — town demand is fixed and exogenous.
- Predatory dumping only pays when the opponent holds **more** of a product than we do. Against a
  mirror it's symmetric. Our real asymmetry is that ladder opponents run the published tape *without*
  our overlay, so our sell timing already differs — which is exactly what (6) exploits.
