# Kaggriculture — round 4. Two open questions, and a long list of what is already dead.

Please read the "already falsified" section before answering. Fourteen plausible ideas have been
measured and killed on this problem, several of them suggested by earlier reviewers, and the most
useful thing you can do is propose something outside that set — or tell us the target is not
reachable and why.

---

## The game, in one paragraph

Two players, 720 turns (30 days x 24 hours), shared market. You buy land/seeds/animals, hire hands
(cost = fibonacci of hires-that-day, resets daily), grow crops, keep animals, and sell into a market
whose price falls as inventory rises: `price = base ± amp·f(|inventory − 10,000|)`, floor $1. The
only demand is a town of 8 shops, drawn **with replacement** from 8 types, one unlocking every 3
days; each shop consumes its products every 4 turns, doubled if it sells only one product. Higher
bank at turn 720 wins. Ladder is TrueSkill-like; the final prize is decided by a **Bradley-Terry
tournament** refitted on post-deadline games, and 1st-10th all pay the same.

## Where we are

Our agent is the strongest published notebook (a "public-state router": four recorded 720-turn
action tapes with byte-identical prefixes, switching between them at t=226/360/433 on public
observations) plus our own overlays. It converged at **~2600**. The top-10 cutoff is **~2800** and
rising ~25/day. We are ~200 short with 23 days left.

**The core difficulty:** per-game margin against a fixed opponent has σ ≈ 6,000. Every overlay we
have successfully built and validated is worth **+68 to +466** mean margin. Stacked, that is maybe
30-50 rating points. Meanwhile the single act of adopting a better published base was worth **+190**.

## Already falsified — please do not re-propose these

Each was measured, most on 300+ games with a held-out seed set.

| idea | result |
|---|---|
| crop-mix grafting from top players | −5,876 to −49,860 |
| animal mix/count changes | 2 fewer sheep = **−82,597** |
| deferring day-0 purchases by one day | −119,077 |
| any extra $50 purchase in the opening | −13,836 (starves a hire; farm dies) |
| cutting a daily hire | −88,691 |
| sale-timing / anti-collision scheduling | contested selling costs $1/unit once time-controlled |
| holding stock for better prices | −103 to −103,111 |
| endgame liquidation | flat |
| score-aware variance (play the scoreboard) | flat |
| cloning the #1 agent's tapes | their tapes score 24-44k vs their own 93k |
| labour-cost / fibonacci-tail optimisation | the #1 player spends **$1,721 MORE** than us |
| "the top player has a $4,708 farm advantage" | invalid comparison; they beat #2 by only +1,180, σ 4,320 |
| retuning the router's 3 switch thresholds | oracle over its 4 tails is only +932 above the shipped rule |
| **matching the herd to the shop draw** (see below) | **−7,758 in exactly the games it targets** |

Things that DID work, for calibration: price-impact ordering of sell slots (+68), retiring one of
the router's four tails (+117), venting the shed near its cap (+277).

---

## Open question 1: the shed cap appears to be the binding constraint. What is the right policy?

This is our newest and best-evidenced finding, from tracing all 69 lost episodes with full per-turn
state.

- The shed holds **100 items**. The engine's end-of-day routine moves inventories into it with
  `room = capacity − current` — **everything above the cap is silently discarded.**
- Our route runs at **76-100 of that cap through days 18-25**. It is destroying production.
- Yet it places market orders on only **89 of 719 turns**, and rarely uses more than a few of the
  **10 order slots** a turn allows. The capacity to sell exists; the tape has no order scheduled.
- Appending sell orders for whatever is crowding the shed, only above 80/100 occupancy, into slots
  the tape left empty: **+277 on held-out seeds** (win rate 0.889 → 0.894). Doing the same at 70/100
  is **−520 to −1,342** — it competes with the tape's own schedule.

So there is a real, sharp optimum around "sell only what would otherwise overflow". That smells like
the visible face of a proper joint problem we are not solving:

> Production is set by decisions made on days 0-11. Demand is revealed gradually (one shop every 3
> days, to day 24). Storage is capped at 100 with discard-on-overflow. Selling n units depresses the
> price for everyone, permanently within a game, and the opponent sells into the same book.

**Question:** how would you formulate and solve the sell-rate policy here? We currently have a
hand-built model (estimate each product's town drain rate from unlocked shops, project future
unlocks, forecast the price after drain, meter sales against a shed target). Is there a better
formulation — and is the right answer to sell *more* earlier so the shed never binds, even at worse
prices? Our instinct says yes but every "sell earlier" experiment we ran historically lost badly,
and we cannot tell whether that is because the idea is wrong or because we always tested it as a
schedule shift rather than as a feedback policy on shed occupancy.

## Open question 2: we can see the mismatch, we cannot act on it. Is there a way?

The shops are drawn with replacement, so the demand mix varies enormously between games. Measured
across our losses, by how many YARN_STOREs (the only shop that consumes WOOL, and it consumes
double) the game ends with:

| # YARN_STOREs | share of games | our SHEEP | their SHEEP | our COW | their COW | our wool sold | theirs | our median margin |
|---|---|---|---|---|---|---|---|---|
| 0 | 34% | 5 | 5 | 9 | 9 | 131 | 131 | −1,412 |
| 1 | 40% | 8 | 8 | 9 | 9 | 195 | 196 | −2,053 |
| 2 | 19% | 8 | 9 | 9 | 8 | 196 | 270 | −2,764 |
| 3 | 6% | **8** | **12** | **9** | **6** | 196 | 301 | **−16,062** |
| 4 | 1% | **8** | **11** | **9** | **6** | 196 | 278 | **−19,652** |

Our herd is **frozen** at 8 sheep / 9 cows in every draw; opponents shift toward sheep. Independently
confirmed offline: on seeds that finish with 3+ YARN_STOREs our agent wins **50%** against a strong
pool versus **79%** on random seeds. About 7% of our games are coin flips.

The obvious fix fails. COW and SHEEP share the same PASTURE, so swapping is structurally free, and
we built it: it fires correctly (herd goes to 5 cows/12 sheep, matching the opponents exactly) and
it measures **−7,758 on precisely the high-yarn seeds it was designed for**, −2,564 on random seeds.
The mechanism is question 1: the extra wool overflows the same 100-item shed and is discarded — wool
actually *sold* went DOWN (196 → 191) while milk collapsed (261 → 157).

The deeper problem is timing. **All nine cows are bought on days 0-8, when at most one YARN_STORE is
visible.** Shops are iid uniform over 8 types, so seeing k stores in the first m unlocks implies a
final count of k + Binomial(8−m, 1/8): seeing 2 by day 8 gives only a ~49% chance of finishing at 3+,
and seeing 1 gives ~9%. Sheep bought later still pay (first yield 6 days after purchase, then every
3 days, 6 units each), but need pasture, feed and — per question 1 — somewhere to put the output.

**Question:** is this regime worth attacking at all, given it is ~7% of games and the information
arrives after the commitment? If yes, what is the right shape: a hedged herd that is never optimal
but never catastrophic, a late-game capacity addition, or something on the sell side only?

## Open question 3 (strategic): is copying the best public agent self-defeating?

Our base is a public notebook, one day old when we adopted it, now widely used. Measured: **2 of our
last 38 ladder games were against opponents with 99.9-100% identical actions, and both ended in
exact ties** (e.g. 84,557 vs 84,557). Zero such games in the previous 287. In the final Bradley-Terry
fit an identical-agent cluster shares a single θ, so we cannot rise above the cluster without beating
it. We have one small answer — ordering our sell slots by price impact wins 93% of mirror matches,
because in a mirror both sides submit the same orders on the same turns — but is there a better
general answer? Is there an argument for deliberately running a *different, slightly weaker* base to
avoid the cluster?

---

## What we can measure, if you want a specific experiment run

Exact forward model (the real engine, ~1 episode/0.7s, 7 workers), full replay access to any
player's episodes including both action tapes and per-turn state, ~600 of our own games and 2,200
top-player games cached locally, and the ability to index seeds by their shop draw. We would rather
run one decisive experiment than another sweep. Name it precisely and we will run it.


---

# ROUND 4 RESULTS — the shared premise was wrong, and one measurement ended it

Thank you: three of you converged on "the swap failed because the sell schedule cannot absorb the
surplus", which was a better hypothesis than mine ("the shed discarded it"). Both are wrong, and the
reason is embarrassing.

## The herd swap: nobody counted the animals

Animals alive in the pasture at game end:

| | sheep alive | cows alive |
|---|---|---|
| base | 8 | 9 |
| swap variant | **8** | **5** |

**The swapped purchases never became living sheep.** The variant destroyed four cows and created
nothing; that is the entire -7,758. Every downstream number we all reasoned from was a consequence
of having fewer animals: wool sold fell 196 -> 191, the shed pinned at 100 for six days, discards
rose 4.5 -> 7.5. All true, none causal.

The tape is a positional program -- it PLACEs, FEEDs and CAREs for specific animals on specific
tiles on specific turns. An extra purchase has nowhere to go and nobody to tend it. This is the same
fact behind "2 fewer sheep = -82,597" in the falsified table, which we had filed as fragility rather
than understood.

**So Q2 is closed, and not for the reason any of us argued.** Late additive sheep have the same
problem as swapped sheep: the husbandry schedule does not cover them.

## Q1: the storage thesis is bounded at ~$300, measured directly

No oracle needed. Instrumenting the engine's discard path over 360 games (both farms):

| item | discarded/game | stored/game | rate |
|---|---|---|---|
| STRAWBERRY | 3.1 | 178.3 | 1.7% |
| WHEAT | 2.3 | 1,075.6 | 0.2% |
| MILK | 0.5 | 257.0 | 0.2% |
| WOOL | 0.2 | 106.4 | 0.2% |

**~2 thin units per player per game.** That is Case A: the shed hypothesis is real but small, and
the vent's +374 is consistent with saving ~2 units at $150-250, not with rescuing a flood. My
earlier write-up saying the vent "rescues overflow at scale" was wrong.

### The warehouse observation was right; the fix is not

At the daily peak (days 18-25) the shed is **42.9% WHEAT, 25.0% FERTILIZER**; at >=95/100 occupancy
**78.3%** is deep-market items. But making sell quantities follow stock -- the proposed minimal
harness change, predicted to be "~neutral on the unmodified herd" -- is:

| | margin | units sold | sell turns |
|---|---|---|---|
| router | **+7,652** | 1547 | 186 |
| sell-to-stock (cap 2x) | **-4,151** | 1448 | 157 |
| sell-to-stock (uncapped) | **-19,617** | 1351 | 147 |

It sells *fewer* units: dumping early crashes the price and empties the shed, so later scheduled
sells find nothing and are clamped. **The tape's fixed quantities are a rate-limiter matched to the
town's drain**, not an oversight. That also explains the 80-vs-70 vent threshold without appealing
to a shadow price: at 70 it is overriding a schedule that is already correct.

### Market-making is not available

`BUY_PRODUCT` is honoured by the engine for exactly `("WHEAT", "FERTILIZER")`; every other item is
rejected and the order slot voided. Wool, milk, strawberry and melon cannot be bought back at any
price, so the buy-the-dip / sell-the-recovery cycle cannot be executed. The cycle-recovery audit
would measure a real quantity that no legal action can capture.

## Q3: the ties were third parties

Checked: the two 99.9-100% action-identical opponents were Igor V and SUBHASH B, not our own second
submission. The cluster is real. We agree with the conclusion -- stay in it, keep a private edge --
and the sell-slot ordering already wins 93% of mirrors.

## A correction to our own numbers that changes the outlook

We had been saying "+277 is undetectable against sigma ~6,000". Measured on 360 paired cells:

| | mean | sd |
|---|---|---|
| unpaired margin | +4,213 | 8,094 |
| **paired difference** (same seed, opponent, seat) | **+279** | **373** |

Pairing removes **99.8%** of the variance. A +277 effect needs ~14 paired cells, not thousands. The
sigma-6,000 figure describes the ladder, where the same shift is worth ~1.4% win rate. We had been
quoting the ladder number to dismiss offline results.

## Where that leaves the question

Storage is worth ~$300. The herd is blocked by positional husbandry, not by storage or sell rates.
The sell schedule is already rate-matched. **The remaining candidates are not overlays on this tape
at all** -- they are (a) a different base, which is the only thing that has ever moved us, or (b)
rewriting the husbandry schedule so the farm's composition becomes a free variable, which is the
"production -> storage -> sales as one controller" idea, but starting from production rather than
storage.

**The question we would now put to you:** given that the tape is a positional program whose
movement, feeding and care actions are bound to specific tiles and turns, is there a tractable way
to make herd composition adjustable at all -- or is the honest conclusion that any farm-composition
change requires generating a new tape from scratch, which our own from-scratch planner measured at
-49,860?
