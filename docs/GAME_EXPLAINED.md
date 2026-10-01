# Kaggriculture, explained

Everything about the game, the economy, how we're scored, and how our agent is built.
Written for you to read and push back on — the open questions are at the bottom.

---

## TLDR

- **The game.** Two farms, 30 days × 24 turns = 720 turns. You grow crops, keep animals, and sell
  into **one shared market**. Whoever has more money at the end wins.
- **The economy is contested, not fixed.** The only demand is the town eating a set amount per turn
  (~5,044 units/game). Selling pushes the price down for *both* of us, so the pot is
  `town demand × whatever price you have left intact` — measured at **$180,484 earned** in one game,
  but it shrinks the harder both sides dump. It is NOT a fixed $200k.
- **Scoring is a skill rating (TrueSkill-style μ/σ), updated per episode.** The size of each ±move
  varies a lot, but it varies with *who you played* and *how certain the system is about you* — not
  with how much you won by. Beating someone far above you gains a lot; losing to someone below you
  costs a lot; a brand-new agent swings hard until its σ shrinks. (Being measured — see below.)
- **Everyone runs the same bot.** The strong agents are a *published* fixed action script ("tape").
  At our level, every opponent has the identical 75-tile farm we do. Games are decided by 1–2%.
- **We're rank ~480/1200 at ~2240**, but that's a lagging number — measured, we're beating
  2,300-rated opponents 74% of the time, so our real level is ~2,500 and still climbing.

---

## 1. The board and your farm

| | |
|---|---|
| Board | 10×10 = 100 tiles, split into 4 quadrants of 25 |
| You start with | 1 quadrant (NW, 25 tiles), **$3,000**, 1 farmer |
| Extra land | Buy in fixed order NE → SW → SE for **$1,000 / $2,000 / $4,000** |
| Workers | Hire "hands". Cost is Fibonacci **within a day**: 1st hire $1, 2nd $1, 3rd $2, 4th $3, 5th $5… |
| Shed | Central storage, **cap 100 items total** |
| Weeds | Any tile can spontaneously become a weed (0.5%/day). Unwatered crops become weeds. |

**The hire rule bites.** `_do_hire` **silently does nothing if you can't afford it** — no error. If
you're broke in the morning you get zero workers, nothing is watered or fed, every crop is a weed
within two days, the animals starve, and the game is over on day 3 while 27 days still run. This is
what killed several of our games; we now have a survival layer for it.

---

## 2. What you can grow and raise

**Crops** (a tile is occupied until harvested):

| crop | seed cost | first yield | max-yield day | max yield | keeps producing? |
|---|---|---|---|---|---|
| WHEAT | $10 | day 2 | 4 | 6 | no |
| CARROT | $20 | day 2 | 3 | 4 | no |
| TOMATO | $50 | day 8 | 8 | 4 | **yes**, every 1 day |
| STRAWBERRY | $100 | day 10 | 10 | 4 | **yes**, every 2 days |
| MELON | $80 | day 10 | 12 | 6 | no |

**Animals** (need a built structure on the tile):

| animal | cost | structure | first yield | every | max held | product |
|---|---|---|---|---|---|---|
| GOOSE | $300 | COOP | day 4 | 1 day | 4 | EGG |
| COW | $400 | PASTURE | day 8 | 2 days | 6 | MILK |
| SHEEP | $500 | PASTURE | day 6 | 3 days | 6 | WOOL |

**How yield actually works — this is the subtle part.** Watering only adds yield inside a window
that depends on the crop: roughly from `(max_yield_day+1)//2` up to `max_yield_day`. Fertilizer
doubles the bonus. Animals must be **FED** (costs wheat) every day, and **CARE** banks a bonus paid
on the next production — but only if the animal was also fed.

This per-crop yield window is why you can't just swap one crop for another in a fixed script: the
watering turns are tuned to the crop that was planted. We tested it — swapping wheat for carrot
cost us $28k a game even though carrot earns 3× more per tile.

---

## 3. Demand and supply — the bit that decides everything

**There is one shared market.** Both farms sell into the same inventory, which starts at **10,000**
per product.

```
price(item) = base ± amplitude × f( |inventory − 10,000| )      floor $1
```

- **You sell → inventory UP → price DOWN** (for both of you).
- **The town eats → inventory DOWN → price UP.**

### The market is far thinner than it looks

This is the single most important table in the game. "Units to halve" = how much *surplus* over
10,000 it takes to cut the price in half:

| product | base | **surplus to HALVE** | at +100 | if 400 units UNDER-supplied |
|---|---|---|---|---|
| STRAWBERRY | 120 | **31** | **$1** | $288 |
| MILK | 160 | **38** | **$1** | $334 |
| WOOL | 200 | **42** | **$1** | $251 |
| MELON | 250 | 112 | $150 | $303 |
| TOMATO | 60 | 135 | $35 | $300 |
| CARROT | 35 | 230 | $23 | $66 |
| FERTILIZER | 100 | 248 | $80 | $180 |
| WHEAT | 25 | >4000 | $21 | $45 |
| EGG | 50 | >4000 | $42 | $81 |

**31 surplus units and strawberry is worth half. 100 units and it is worth $1.** But keep it
*under*-supplied and it pays 2–5× base. Wheat and egg are the opposite — you can dump them forever
and the price barely moves, but they are worth little.

### So how big is the pot?

**It is not a fixed $200k** (an earlier note in this file said that — it was wrong). Measured over a
real game: both players banked $93,242 each, **$180,484 earned in total**. The pot is
`town consumption × whatever price you have left intact`. Both players dumping is what destroys it.

The town consumed ~**5,044 units** across all products that game. That is the whole demand side.

| sink | fires | eats |
|---|---|---|
| Town centre | every 24 turns → 30×/game | 1 of each of the **8 main products** |
| A single shop | every 4 turns → up to 180×/game | 1 per product it carries (**2** if single-product) |

The **8 main products** the town centre eats are: WHEAT, CARROT, TOMATO, STRAWBERRY, MELON, EGG,
MILK, WOOL. The 9th product, **FERTILIZER, has NO consumer at all** — no shop uses it and the town
centre skips it. Its inventory only ever rises and its price ends at the $1 floor.

Eight shops fire **936 times a game** against the town centre's 30, so **shops are essentially all
of the demand** — 4–7× the town centre for any product they carry:

| shop | consumes |
|---|---|
| BAKERY | EGG, WHEAT |
| PIZZA_SHOP | MILK, TOMATO, WHEAT |
| BRUNCH_SPOT | EGG, WHEAT, STRAWBERRY |
| **YARN_STORE** | **WOOL only → eats 2 at a time** |
| ICE_CREAM_SHOP | STRAWBERRY, MILK, WHEAT |
| **PET_CAFE** | **CARROT only → eats 2 at a time** |
| SMOOTHIE_SHOP | STRAWBERRY, MILK |
| FARMERS_MARKET | WHEAT, CARROT, TOMATO, STRAWBERRY |

Which shops unlock is the biggest random factor in the game. It swings product values enormously —
in one seed milk was $166/unit and wool $87; in another wool was $217 and milk $37.

### Why "just grow the thing nobody supplies" does not work

In a measured game the town ate **462 tomato and 210 egg, and neither player supplied a single
unit**. Tomato at that depth prices around $300, which looks like free money. It is not:

- Tomato's price is high **because** it is unserved. Supplying the 462 units the town wants brings
  inventory back to 10,000 and the price back to its $60 base.
- At a realistic depth (−200) tomato is **$84** while strawberry is **$239**.
- Tested directly: substituting strawberry→tomato costs **−$34,034** at just 25% substitution.

**The governing law, which every experiment has confirmed:** *demand is fixed and shared; producing
more of a valuable product destroys its price, and the high price of a product you don't make is
unreachable.* The tape's crop mix is economically correct.

### The prisoner's dilemma at the heart of the game

Because the top products halve after ~31–42 surplus units, **both players would earn far more if
both sold slowly**. But whoever sells first captures the high prices and leaves the other the
crash — so selling slowly while your opponent dumps is punished brutally (we measured −$103k for a
polite selling schedule). Dumping first is the dominant strategy, and that is exactly why the
market-slot ordering matters.

### Two engine quirks

- Buying is quoted at post-buy inventory and selling at pre-sell, so an instant buy→sell round trip
  nets **exactly $0**. There is no arbitrage.
- Orders settle **slot by slot in lockstep** — your order #1 against their order #1 — and each unit
  committed moves the price. So an earlier slot sells into a less-flooded market.

## 4. How it's judged

- You submit an agent. It plays episodes against other people's agents.
- **The rating is TrueSkill-like: a skill estimate μ with an uncertainty σ.** Each episode updates it
  based on the *result* plus how surprising that result was. So the ± is genuinely variable:
  - beating a much stronger opponent → large gain; beating a weaker one → small gain
  - losing to a weaker opponent → large loss
  - a new submission (high σ) swings hard, then settles as σ shrinks
  - **what does NOT change it is the margin.** Measured over 18 live episodes: a **$596 loss cost
    −5.80** rating while a **$16,891 loss cost only −4.70**; a **$416 win paid +4.30** while a
    **$15,435 win paid only +3.90**. Correlation between margin and rating change is **−0.43** —
    slightly *inverse*, because large margins come from weak opponents and those results are worth
    less. This is why our local benchmark treats margin only as a *proxy* for win probability.
- Every submission **starts at rating 600**. Matchmaking pairs you with similar-rated agents, so
  gains slow as you approach your true level.
- **Only your latest 2 submissions play.** Older ones freeze and stop counting for your rank —
  the leaderboard shows your best *active* submission.
- 5 submissions/day. **The quota resets around 22:00 UTC, not 00:00 UTC** (measured: all 5 were spent
  by 21:05 UTC and the counter had reset by 22:55 UTC).

**The trap we fell into:** each new submission resets to 600 and needs **100+ games** to converge.
We submitted 8 times in two days, so nothing ever finished climbing — that's the "stuck at 2200".
Our best-ever score (2610) happened only because that agent was left alone for 127 games.

Current cutoffs: **top-10 = 2857**, top-25 = 2788, top-50 = 2727, top-100 = 2659. #1 is 3024.

---

## 5. How an agent is actually built

Every turn your agent returns one dict:

```python
{
  "farmer": ["WATER"],                     # what your farmer does
  "hands":  [["MOVE_N"], ["HARVEST"], …],  # one action per hired hand
  "market": [["SELL","MILK",3], ["HIRE"], …]   # max 10 orders per turn
}
```

Unit actions resolve **before** market orders in the same turn — so a seed you buy this turn can't
be planted until next turn.

**The dominant approach in this competition is a "tape".** Because your own farm evolves
deterministically from your own actions, you can pre-compute a 719-turn script offline and just play
it back. The strong public notebooks are exactly this. It's not adaptive at all — it plants the same
thing whether or not carrot is worth $500 — but it's very well optimised.

**Our agent, in layers:**

1. **The tape** — a pure-Python port of the strongest published script (credit: yhay81), verified
   action-identical to the original.
2. **Sell-timing overlay** — our own work. Decides *when* to sell rather than dumping on the tape's
   schedule, using a model of town drain and price curves. Worth **+$3,361/game**.
3. **Survival override** — our own. If the morning hires fail and we have zero workers, stop
   following the script and save the animals. Fires in exactly the games that would end at $0 and in
   none of the healthy ones.
4. **Tuned parameters** — found by a "mirror" benchmark (see below). Worth **+$2,616/game**.

**How we measure.** Because every opponent runs our own tape, the only benchmark that predicts rank
is *candidate vs our exact submitted agent, same seeds, both seats, scored by average margin*. The
null control returns exactly ±0, so any signal is real. Win-rate against weak bots tells us nothing.

---

## 6. What we've tried, with numbers

**Worked:**

| change | effect |
|---|---|
| Port the *newer* published tape (it gets updated!) | 100W-0L vs our previous build |
| Sell-timing overlay | +$3,361/game |
| Mirror-tuned parameters | +$2,616/game on unseen seeds |
| Survival override | removes the games that end at $0 |

**Measured and dead — don't let me retry these:**

| idea | result |
|---|---|
| Swap wheat → carrot (more $/tile) | **−$28,275**, three attempts, all negative |
| Buy land earlier (like the #1 agent) | −$509 |
| Use the tape's ~672 idle worker-turns | ±$0 — labour isn't the bottleneck |
| Build an agent from scratch | −$49,860 margin, 0% win rate |
| Copy the #1 agent's recorded games | **0/70 tapes beat us** — they're adaptive, so their script doesn't transfer |
| Cash guard (force a sale to fund hires) | costs ~300 rating; it meddles with the market |

---

## 7. Where the remaining edge probably is

Everyone at our level plays the **same script**, which means **we know exactly what our opponent
will do on every turn of the game.** Almost nobody gets that in a competition like this. Two ideas
follow from it, neither tried yet:

1. **Sell ahead of them.** We know the exact turn they'll dump wool and melon. Selling into a market
   they're about to flood is the single most avoidable loss in a mirror match.
2. **Adapt to the shops.** The script plants the same crops regardless of which shops unlocked. When
   two PET_CAFEs appear, carrot demand quadruples and the script ignores it. Adapting *demand-side*
   (what to sell, when) is safe; adapting *supply-side* (what to plant) breaks the yield windows, as
   we measured.

---

## 8. Where I'd like your input

1. **How hard do you want to push for #1 (3000+) vs locking in a solid top-50/top-25?** Getting to
   3000 means beating the one genuinely adaptive agent; top-50 looks reachable with what we have,
   just by leaving it alone to converge.
2. **Am I right to stop resubmitting?** Each submission costs ~100 games of climbing. I think we
   should only submit when a candidate beats the live one in the mirror.
3. **Is there anything about the game you'd play differently as a human?** You may spot something in
   the demand table above that I've been ignoring — the shop-unlock randomness in particular is a
   big lever nobody in the field is using.
