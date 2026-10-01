# Kaggriculture — follow-up after your review

Thank you — three of your criticisms were correct and two of them overturned claims in the original
briefing. This is what changed, what we measured since, and the sharper questions that remain.
**Please read this alongside `BRIEFING.md`; where they conflict, this document wins.**

---

## Corrections to the original briefing

### ✅ You were right: "crop mix is the whole gap" was wrong

The reviewer who checked the arithmetic was correct — it doesn't close. 75 fewer wheat plantings is
~300 fewer units that *we* get and keiz doesn't; 33 more carrot is ~$5k for them. On those rows keiz
should bank **less**, not $7k more.

### ✅ You were right: our branch-point story was fitted to the data

Shops unlock on days 3/6/9/12/15/18/21/24. keiz branches at **day 0 step 5**, and days **7, 8, 11**.
Jesse at **7, 11, 17, 19**. Most of those are *not* unlock days. We asserted "they branch on shop
unlocks" because it fit a narrative. It does not fit the data.

### ✅ You were right that our keiz replay was confounded

We replayed keiz's tapes on *arbitrary* seeds, not their own. That conflates shop-conditioning with
opponent-conditioning, so the "24–44k vs their 93k" number should not be trusted as evidence that
their policy is irreducibly reactive.

### ❌ But our own follow-up finding was ALSO wrong, and we caught it

We first measured that "keiz sells half the units at double the price" — then realised we had used
**order quantities**, the exact error we had documented and warned about. Redone using **actual
fills** (recovered from shared-market inventory deltas on turns where only one player sells that
product):

| product | keiz $/unit | **our $/unit** |
|---|---|---|
| STRAWBERRY | 148 | **149** |
| MILK | 82 | **126** |
| WOOL | 131 | 123 |
| WHEAT | 43 | 43 |
| MELON | 144 | **156** |

**Our realised prices are the same or better than keiz's.** There is no price-capture gap.

---

## The one real difference we can now measure

On turns where the opponent is *not* selling that product:

| | uncontested units filled per game |
|---|---|
| keiz | **447** |
| us | **117** |

Same prices, ~4× the uncontested volume. We think the mechanism is structural rather than clever:
**we run the same public tape as most of the field, so our selling turns collide with theirs by
construction.** keiz's schedule differs from the tape's, so it is uncontested by default. Separately
measured: **100% of our sell value lands on a turn where the opponent sells the same product.**

---

## The constraint that blocks every fix you proposed

Several of you proposed building a small library of coherent tape variants and routing between them.
We agree that is the right shape. **The blocker is that our tape is a tightly-coupled fixed point,
and we have now measured how violently it resists edits:**

| structural edit | cost |
|---|---|
| buy **2 fewer sheep** (saves $1,000, ~60 wool units) | **−82,597** |
| buy 2 fewer cows | −21,396 |
| defer the day-0 animal purchases by **one day** | **−119,077** |
| one unplanned **$50** seed purchase in the opening | **−13,836** |
| drop a single daily hire | −88,691 |

These are not economic trade-offs — a $1,000 saving cannot cost $82k. They are structural breakage:
the opening runs on a $0–9 cash minimum, `_do_hire` silently no-ops when broke, and a failed hire
means no workers, everything becomes weeds by day 3, and the farm is dead for 27 days.

So "swap the seed type but keep movement and hiring identical" is not as cheap as it sounds — the
cash schedule, the feed chain (~361 wheat/season feeds animals producing $50k), and the hire ladder
are all coupled to what is planted and when.

---

## Current performance (better than the briefing said)

The briefing's 58.8% win rate came from a sample including older, weaker submissions. Current
agents, 91 games:

**75W-16L = 82% win rate.** Losses: median gap **−3,224**; only 3/16 within $2,000; **6/16 we never
led at any point**; 4/16 blown leads; **no repeat opponents**. Rating ~2,600 and lagging — our agents
consistently beat expectation by ~240 points while the ladder catches up.

---

## Sharper questions

1. **How do you build coherent variants of a fragile fixed point?** You proposed a policy DAG with
   shared prefixes. Given that dropping *two sheep* costs $82k, a variant is not a small edit — it is
   a different fixed point. Do we (a) generate each variant from scratch with a planner (our previous
   from-scratch planner measured −49,860), (b) build a **repair operator** that re-derives the cash,
   feed and hire schedules after any structural edit, or (c) something else? **(b) feels right and we
   don't know how to specify it.**

2. **Is the real edge simply "don't sell when the field sells"?** Our prices match keiz's; only
   uncontested volume differs (117 vs 447). But every deferral experiment we ran lost badly
   (−103k for a phase-shifted schedule) because unsold goods are worthless and the shed caps at 100.
   Is there a formulation where we shift *timing* without *holding* — and does that even make sense
   when production timing is fixed by the tape?

3. **Does the fills correction change your diagnosis?** Several of you built on "keiz captures more
   value per unit". That is now falsified. Does the opponent-conditioning thesis survive if their
   prices are the same as ours and only their collision rate differs?

4. **Where should effort go given 82% and a −3,224 median loss?** The losses are mostly not
   coin-flips — 6/16 we never led. Is the marginal value in converting decisive losses (which may
   need the architecture change) or is 82% near the practical ceiling for a tape-based agent?

5. **What would you measure next?** We have an exact forward model (~35k episodes/hour), full replay
   access to any player's episodes, and 97.9%-accurate reconstruction of any opponent's trades from
   public data. We would rather run the one decisive experiment than another sweep.

---

# ROUND 2 RESULT: the collision thesis is falsified

All four reviewers converged on "keiz wins by avoiding contested turns; run the sale-timing oracle."
One reviewer correctly noted our fills table compared keiz-uncontested with us-uncontested, which is
the same curve on both sides and therefore uninformative, and predicted our all-turn contested price
would sit $20-40 **below** our uncontested price.

We ran the decisive measurement: patched the engine's `_commit_unit` and recorded **every fill** --
exact unit, exact price, exact player, every turn.

**The prediction is wrong, in the opposite direction.**

| product | contested $/u | uncontested $/u |
|---|---|---|
| STRAWBERRY | **143** (668u) | 94 (368u) |
| MILK | **75** (700u) | 48 (344u) |
| FERTILIZER | **46** (1,178u) | 21 (264u) |
| WOOL | 135 | 139 |

Our contested prices are **higher**. The naive arithmetic suggests a -$71,891 "prize" from
de-collision, but it is entirely a **time confound**:

- mean day of contested fills: **18.7**
- mean day of uncontested fills: **23.6**

Contested turns are early (fresh market, high prices, both players selling); uncontested turns are
late (only one player still holds stock, market flooded). Controlling for time:

| STRAWBERRY, same day band | contested | alone |
|---|---|---|
| days 20-24 | **$110**/u (332u) | $91/u (148u) |
| days 25-29 | **$96**/u | **$95**/u |

**Within the same window, selling on a contested turn costs $1/unit.** There is no collision penalty.

This retires the whole family: sale-timing oracle, desynced collection, anti-collision scheduling,
opponent temporal masks. It also explains why every timing experiment we ran lost money (-103k for a
phase-shifted schedule, -103 to -2,059 for held stock): uncontested turns are *late* turns, and late
means a crashed market. We were being offered a worse price, not a better one.

**What survives:** nothing in the market-timing family. The remaining candidates are the units
column (do we actually fill fewer units than keiz in total?) and the production side. Our realised
prices match keiz's, our contested share costs nothing, and the bank difference is ~$4,700 against
a per-game spread of $1,576 vs a fixed opponent.

**Revised question:** given that price capture and sale timing are both now measured flat, is the
remaining gap even real, or is $93,314 vs $88,606 an artifact of different opponent pools? We can
answer that only by playing keiz directly, which we cannot do -- their tapes do not transfer.

---

# ROUND 3: the premise itself was invalid

Three more confidently-argued hypotheses died on cheap measurements, and so did the number we were
all reasoning about.

## The $4,708 "farm gap" was never established

One reviewer said it plainly: comparing keiz's $93,314 to our $88,606 compares different games
against different opponents. They were right. Measured properly, using **margin** (the only valid
statistic, since absolute banks are dominated by the shop draw and the opponent):

**keiz vs the #2 and #3 ranked players: 7W-3L (70%), mean margin +1,180, sigma 4,320.**

They lose to Jesse Bullard by -8,849 and -2,623 in two of ten games. One keiz-Jesse game had banks of
136,707 and 131,231 -- a rich draw, not superior play. **keiz is not dominant; they grind out small
wins against strong opposition.** For comparison our current agent is 75W-16L (82%) against its pool.
Those aren't directly comparable, but they are not different leagues either.

## The labour-bill hypothesis is dead, and backwards

One reviewer argued keiz avoids the Fibonacci tail (the ladder resets daily, so 12 hires in one day
costs $376 while 6+6 costs $24) and that this was worth ~$8,400. Measured:

| | our hire bill | keiz's |
|---|---|---|
| cost/game | **$5,962** | **$7,683** |
| peak hires/day | 12 | 12 |
| total hires | 287 | 301 |

**keiz spends $1,721 MORE on labour than we do.** The hypothesis predicted the opposite.

## Where that leaves things

Dead, all measured: sale collision, price capture, crop mix, labour cost, sale timing, score-aware
variance, and the premise of a large farm gap. What survives is unglamorous: our agent wins 82% of
its games, is under-rated by ~240 points while the ladder converges, and the distance to #1 may be
substantially smaller than the raw ratings suggest.

**We also found the competition publishes full daily episode dumps** (~665 episodes/day,
`kaggle/kaggriculture-episodes-index` and dated datasets). That removes the data bottleneck for any
future study -- we had been fetching replays one at a time.

## The question that remains

Given that every proposed mechanism has now measured flat, and keiz beats the #2 player by only
+1,180 on a spread of 4,320: **is there any evidence left that a policy gap exists at all, or is the
rating difference mostly convergence time and pool composition?** If someone can name a measurement
that would distinguish those two, that is the one we would run.
