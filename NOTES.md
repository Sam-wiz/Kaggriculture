# Kaggriculture — working notes

2-player farming sim, 720 turns (30 days × 24). Most coins at the end wins; the ladder is
Elo-like on **win/loss only**. Deadline **2026-09-30**, 5 submissions/day, latest 2 tracked.
Goal: **top 10**.

> Process failures and the rules that now prevent them live in **`MISTAKES.md`**. Read it before
> trusting a benchmark number or spending a submission slot — most of those errors produced
> plausible-looking results rather than crashes.

## ENGINE VERSION — check this first
The venv **must** be on `kaggle-environments==1.32.7` (see `requirements-lock.txt`). 1.32.6 differs
in exactly the curves the whole strategy turns on: CARROT/TOMATO/EGG use `hinge` scarcity curves in
.7 (carrot `below_target` 1.00) and plain `log`/`linear` in .6. A subagent silently downgraded the
venv mid-session and several hours of benchmarking ran against the wrong engine. The competition
page documents the hinge curves, so 1.32.7 is what Kaggle runs. Verify with:

    .venv/bin/python -c "from kaggle_environments.envs.kaggriculture import kaggriculture as K; print(K.MARKET_PARAMS['CARROT'])"

**Kaggle exec's `main.py` with no `__file__`.** `kaggle_environments/agent.py` does
`exec(code_object, env)` on the raw source and picks the last callable out of `env`. Nothing sets
`__file__`, so *any* path-based bootstrap (`os.path.dirname(os.path.abspath(__file__))`,
`sys.path.insert` relative to the file) raises `NameError` before the agent is ever called — and a
local harness that imports by file path will never reproduce it. Multi-file bundles must therefore
either embed their dependencies or hard-code `/kaggle_simulations/agent/`. Always pre-flight a
submission with `kaggle_load_check.py <main.py> [opponent]`, which loads it exactly the way the
platform does. This cost a submission slot.

Also: `status == ["DONE","DONE"]` does **not** mean an agent worked — the interpreter overwrites an
ERROR status with DONE on the final step. Always check `r["errors"] == [None, None]` and that the
bank differs from `startingMoney`.

## Setup
```bash
python3 -m venv .venv
.venv/bin/pip install --no-deps -U kaggle-environments && .venv/bin/pip install kaggle numpy requests jsonschema tenacity termcolor
# pygame fails to build on py3.14 -- --no-deps avoids it; kaggriculture does not need it.
```
Engine source (ground truth): `.venv/lib/python3.14/site-packages/kaggle_environments/envs/kaggriculture/kaggriculture.py`

Kaggle CLI tokens expire after a few hours. Re-auth with `kaggle auth login` (run it yourself in
the shell — it opens a browser).

## Tooling
| File | What |
|---|---|
| `harness.py` | Drives the **official** interpreter with a light wrapper. Bit-exact vs `env.run` (verified) and ~8× faster. |
| `evalpool.py` | Win rate vs 8 behaviourally-distinct rivals, both seat orders. **The metric that matters.** |
| `arena.py` | Head-to-head between any two agents. |
| `tune.py` | `--ablate` / `--grid` sweeps. Resets `P` to defaults per trial (a leak here silently corrupted early results). |
| `search.py` | Coordinate descent over the parameter grid; writes `best_params.json`. |
| `diag.py` | Day-by-day money / land / tile composition / final prices. |
| `actmix.py` | Where unit-actions go (movement vs productive). |
| `cover.py` | Per-day maintenance coverage (fed %, cared %, unwatered plants). |
| `yield2.py` | Units per planting and per animal-day — the sharpest production diagnostic. |
| `production.py` | Units actually sold, inferred from market inventory. |
| `econ.py` | Price curves, town drain, $/action per recipe. |
| `capacity.py` | Upper bound on the bank given tile-days and actions. Proves tile-days bind. |
| `tiledays.py` | Where tile-days go and what each yields — the sharpest whole-farm diagnostic. |
| `kaggle_load_check.py` | **Pre-flight every submission with this.** Loads the agent the way Kaggle does (exec, no `__file__`). |

`rivals/POOL2.md` — the exhaustive sweep: **397 public kernels** enumerated to closure, 63 runnable
agents extracted. The strongest agent in the competition is
`rivals/yhay81_the-35-0-tape-a-causal-shop-router/main.py`, which beats boatlee_v29 **60-0** over 30
seeds and takes 190/192 against the rest of the pool. It was invisible to earlier sweeps because it
is a **compiled C++ policy loaded through ctypes** — without its `agent.dylib` it throws inside
`CDLL`, banks exactly `startingMoney`, and looks like a dud. It is now compiled and in the pool.
Its edge is selling *less*: it appends extra SELL orders only when replaying its own forward tape
shows a cash shortfall (233 orders vs v29's 319). Tested on our agent, that mechanism does **not**
transfer (-$84k margin vs -$62k) — it relies on knowing your own future plan exactly.

`rivals/POOL.md` — the original 16 extracted competitor agents with benchmarks. `research/META.md` — community
strategy corpus. `rivals/RIVAL_ANALYSIS.md` — teardown of the top four.

## Agent
`agents/v21.py` is current best (`main.py` is a copy of whatever was last submitted).
Design: marginal-value task scheduler. Every unit-action is scored by the dollars it creates
divided by the turns to walk there; units hold a pie-slice zone rebalanced daily by workload.
Planting is a budget-aware greedy allocation over forecast prices, so the mix self-diversifies
into whatever the town actually demands. All behaviour is in the `P` dict for sweeping.

## Measured state
| | ours | best rival |
|---|---|---|
| bank vs `starter` | ~$116k | $132–170k |
| bank vs rival pool | ~$68k | ~$137k |
| pool win rate | 0/48 | boatlee_v29 = 0.971 |
| uncontested (vs `pass`, seed 1) | $125k | $131k |

**The open problem:** uncontested we are within 5% of the best rival, but contested we take only
~33% of the shared pot instead of ~50%. The loss is in *selling*, not production — see below.

## What is verified (do not re-litigate)
- Never buy the SE quadrant (`max_quads=3`). Four-quadrant variants lose consistently.
- Melon caps at ~12 tiles; 0, 6 and 20 all measure worse. It is a day-10 capital event.
- `fert_value=1.4` (prioritise `COLLECT_FERTILIZER`) is worth ~$11k vs a live rival.
- `sell_bias_tight=2.0` (sell faster) is worth ~$6k contested and ~$5k uncontested.
- Cap geese at 3; they are the worst animal and we default to them when cash-starved.
- Forcing a fixed opening herd hurts. Land-before-seeds hurts. Longer forecast horizons hurt.
- More hands beyond ~12 does nothing: units already run at ~4% PASS.

## The ceiling of this design (measured — see `capacity.py`, `tiledays.py`)

**Tile-days bind; actions do not.** The capacity LP uses 1,800 of 1,800 tile-days but only ~2,900
of up to 7,200 available unit-actions. That kills a whole family of ideas: more hands, better
routing, and lower movement overhead are all worth little. It also explains why every hiring and
zone-routing sweep came back flat.

Per tile-day at the margin: **animals ~$300, melon ~$110, tomato ~$100, strawberry ~$94,
carrot ~$80, wheat ~$60.** Livestock is three times better than any crop, capped only by how fast
milk/wool saturate.

Uncontested tile-day accounting vs the strongest rival (seed 1):

| | ours | rival |
|---|---|---|
| bank | $112.7k | $131.3k |
| owned tile-days | 1,700 | 1,825 |
| wasted (empty/weed/dead structure) | **24.4%** | **9.8%** |
| revenue per productive tile-day | **$87.7** | $79.7 |

**Our crop economics are better than theirs.** The entire uncontested gap is 361 productive
tile-days — 236 of waste plus 125 of land bought later. Of the waste, only ~211 tile-days (days
10-25, ≈$18k) is recoverable; the rest is end-of-season, when nothing is plantable.

So Path A's realistic ceiling is roughly **parity** with the field (~$130-140k uncontested), not
superiority.

**The contested collapse has a mechanism.** Uncontested we reach 86% of their bank; contested only
46%. Head-to-head we sell *more* units than they do (1,676 vs 1,303) at $33/unit against their
$98/unit, because our opponent-aware forecast sees them flooding strawberry and milk, prices those
markets as crashed, and reroutes us into wheat and carrot. We cede the entire high-value pot. That
is correct for absolute bank and fatal for the win. Setting `opp_weight=0` (contest anyway) costs
$25k of bank and gains $15k of margin, confirming the mechanism — but not enough to win.

## Dead ends (measured, do not retry)
Forcing 20+ strawberry tiles (−$80k), forcing an opening herd (−$19k), hoarding wheat for feed,
land-before-seeds, longer forecast horizons, value-based shed runs, raising FEED/CARE priority,
extra hands beyond ~12, herd clustering (helps bank, costs margin).

**Caveat on all tuning numbers:** results are exactly reproducible but are 8 seeds against one
opponent. Differences under ~$10k can reverse on a different seed set — confirm anything important
with `evalpool.py`, which spans 8 opponents.


## Two paths, both measured (the drop decision)

**Path A — from scratch (`agents/v22.py`).** Pool win rate **0.000 (0/72)**, bank $65k vs the
field's $134k. Ceiling is *parity*: uncontested it banks $112k against the best tape's $131k, and
its revenue per productive tile-day is already higher. Getting there needs a breakthrough, not
tuning — every remaining fix measures at $1-3k and they do not compound.

**Path B — proven tape + our market overlay (`hybrid/h1.py`).** Pool win rate **0.889 (48/54)**,
bank $91k vs $75k. Beats its own base boatlee_v29 6/6; loses only to the compiled causal-shop-router.
Independently re-verified (clean episodes, no errors).

The overlay's own contribution is small and precisely measured: **+$3.3k on a ~$100k bank (~3%)**,
and only against an opponent running the *same* tape — h1 vs h1 is an exact tie on every seed.
Strawberry supplies +$1.5k of that (T=100, glut slope 1.92/unit: both farms dump ~250 units into a
market draining ~19/day and the price falls $200 -> $5; being one turn ahead of that collapse is the
whole edge). Two structural rules fell out: **never reorder the market list** (the tape fills all ten
slots, so hoisting a SELL truncates one of its buys; appending is free) and **never pull deep**
(deep pull-forward degenerates into dumping the shed).

**So the ceiling of Path B is "whatever tape you adopt, plus $3.5-5k."** A better tape is worth
$23k; a better overlay is worth $3.3k — seven times smaller. The tape is the asset.

Practical blocker on the best tape: the causal-shop-router is a compiled C++ policy. Our macOS
`agent.dylib` will not run on Kaggle's Linux workers, so adopting *that* tape needs a Linux build.


## Submitted 2026-09-02 (all 5 slots + 1 refunded)
The two **tracked** (latest) submissions are the hedge we want:
1. `main_h1_submit.py` (= `build/main_h1.py`) — hybrid, 0.889 on the 9-rival pool.
2. `agents/v22.py` — our own from-scratch agent.

Rebuild the hybrid with the embedder in this file's history; it must stay a SINGLE file
(no `__file__`). Pre-flight everything with `kaggle_load_check.py` before spending a slot.
An errored submission refunds its slot, so a failed validation is recoverable same-day.


## The strongest tape's actual schedule (decoded — `tape_schedule.py`)

Decoded from `rivals/yhay81_the-35-0-tape-a-causal-shop-router/source/tape.inc` (two routes; it
switches to route 1 at step 216 only if shops[0:3] == ICE_CREAM, FARMERS_MARKET, FARMERS_MARKET and
the opponent has >1 goose tile). Route 0:

| | value |
|---|---|
| land | days **6 and 11** only (never SE) |
| hires/day | 5, 3, 4, 5, 4, 4, then 8-9 by d6-9, 11-12 from d10, 12 through d24, 11 at the end |
| animals | **8 cows + 9 sheep**, zero geese |
| plantings | **195 wheat**, 33 strawberry, 12 melon, 9 carrot |
| also buys | 178 wheat and **64 fertilizer** from the market |
| sells | wheat 396, fertilizer 384, milk 272, strawberry 267, wool 217, melon 72 |
| first sale | wheat d0, fertilizer d1, wool d6, milk d8, melon d10, strawberry d15 |
| action mix | WATER 1099, moves ~3154, PASS **699 (11%)**, harvest 466, collect-fert 380, care 371, feed 362 |

What this says our own agent is getting wrong: it plants **195 wheat** (we plant ~63) — wheat is the
backbone that feeds 17 animals *and* is the top sell line; it keeps **17 animals alive** all season
(we buy up to 21 and lose most); and it **buys fertilizer** to double strawberry/tomato yields rather
than only selling what the animals drop. Note it also idles 11% of its unit-actions, which confirms
the capacity model: actions are not the binding resource.


## Current best agent: `port2/h_over.py`

`port/main.py` is a pure-Python, single-file port of yhay81's causal-shop-router tape, verified
action-for-action identical to the compiled C++ original (92k steps, 0 divergences; 12 head-to-head
ties). `port2/h_over.py` adds our sell-timing overlay on top.

| | evalpool wr | vs the bare port |
|---|---|---|
| `port/main.py` | 0.917 / 0.931 (two seed sets) | — |
| `port2/h_over.py` | **0.972 / 0.993** | **64/64**, +$2,639 / +$2,746; independently re-checked on a third seed set: 24/24, +$2,922 |

**Why the overlay transfers here when the "sell less" philosophy said it shouldn't:** it adds *no*
volume. Uncontested, h_over's end-of-season market drift differs from the port's by <=5 units in
~1,200 and it banks slightly *less*. It only moves units a few turns earlier inside the tape's own
schedule and repays from the tape's later orders. Contested, that timing wins the per-slot lockstep
auction. The boatlee case was the opposite (that tape over-sells), which is why the caveat did not bite.

Two load-bearing details: honour the guard's static-consumption reserve (+$1,683 — otherwise the
overlay sells wheat/fertiliser the tape has committed to FEED/FERTILIZE), and never append past the
10-order cap (route 0 fills all ten slots on 25 steps, so a naive `market[:10]` silently drops a
tape *buy*).

**Honest caveat:** about half the win-rate gain is breaking the exact tie against the compiled
mirror. That is real and reproducible (it is the same policy), and valuable on a ladder where many
opponents run this same public tape — but against the other rivals only margin moves, not wins.

### Dead ends on this base (measured)
- **The budget guard never fires.** It changes the action zero times in a full episode, so
  `min_price`, `sales_first`, `budget_mult`, `cash_floor` and `horizon` are bit-inert. Forcing it to
  fire (`protect=0, interval=24`) collapses to 0.000 wr — it sells the feed reserve and the herd starves.
- **The route switch should never fire.** Route 1 loses to all 9 pool opponents; the narrow shipped
  condition costs nothing because route 1 is simply the worse tape. "Never switch" is correct.
- Buying fertiliser in our own agent: +$1.8k, inside the noise floor.


## Ladder replays are a data source (this is the next lever)

`kaggle competitions replay <episode_id>` returns a JSON that contains the **full 719-turn action
sequence of BOTH players**, plus the episode seed, both team names and the final banks. Our own
submissions have played ~100 episodes each against real ladder opponents, many of them stronger than
any published notebook. So the replays are a way to obtain tapes nobody has shared. The public
notebooks do exactly this openly — they cite the specific episode ids they were recorded from.

Also confirmed from a replay: `module_version` is **1.32.7**, so that is what Kaggle runs.

Mechanics that make tape replay work at all: a player's own farm evolves deterministically from
their own actions, apart from seeded weed spawns. Only the market differs with the opponent, and
market orders are quantity-based. Expect some degradation off-seed, which is what the published
tapes' "weed repair" logic exists to patch.

Practical note: replays are ~30 MB each, but the actions are a tiny fraction of that — reduce and
delete as you go.


## What the ladder meta actually is (mined from 70 of our own replays)

Decoding the opponents' recorded actions (`mine/decode.py`) shows **the top of the ladder is a
monoculture of the same public tape**. "Tiannan Zhang" is byte-identical to the champion's route 0
(8 cows / 9 sheep, 195 wheat, 33 strawberry, 12 melon, 9 carrot, sells wheat 396 / fert 384 /
wool 217 / milk 272) and our game against them was an **exact tie, 121092 vs 121092**. "NiuLAI" is
the same plan with slightly different sells. "hiros" is a variant (9 cows / 5 sheep, 167 wheat,
38 strawberry, 24 carrot, 71 carrots sold).

Our h1's ladder record across these episodes: **40-9-2**. Margin distribution: 4% exact ties, **12%
decided by <= $3,000**, 33% by <= $10,000, median |margin| $18k. Our losses were to nine different
opponents with no repeating pattern — two of them by $184 and $765.

**This is why the sell-timing overlay is the right edge**: against a mirror the bare tape ties, and
h_over converts those ties plus the sub-$3k losses into wins. It is not a general strength gain, it
is precisely aimed at the shape of this ladder.

Note our own submissions play each other (we appear as our own opponent), so keeping the two tracked
slots on two *different* strong agents is better than duplicating one.

**Mined tapes are not directly adoptable.** Replayed off their recorded seed they lose 0-8 to
h_over — different weed spawns and shop draw desynchronise them. They are useful as *schedules* to
learn from, not as agents. An opponent that emits identical actions across different seeds is
running a fixed tape and could be extracted faithfully; of the opponents seen twice so far, none did.


## Deep loss analysis (202 mined ladder games) — and why the tape line is maxed out

Split of our current agent's results:

| matchup | games | record | mean margin |
|---|---|---|---|
| exact mirror of our tape | 31 (32%) | **29W-2L** | +$2,715 |
| different plan | 66 (68%) | 42W-24L | +$10,407 |

**24 of our 26 losses are to opponents running a different plan**, not to the monoculture. The
overlay is doing its job and is at its ceiling.

Full-spectrum profile of the plans that beat us vs ours (livestock, structures, land, hiring, feed
and sale timing all compared — `mine/deep.py`):

| | beat us | we beat | ours |
|---|---|---|---|
| wheat planted | 133 | 145 | **195** |
| carrot | 18 | 10 | 9 |
| melon | 19 | 16 | 12 |
| tomato | 1.3 | 0.5 | 0 |
| wheat BOUGHT from market | **674** | 462 | 178 |
| cows / sheep | 8.4 / 6.6 | 8.2 / 7.4 | 8 / 9 |
| land days, hire curve, units/day, feed+care rates | identical | identical | identical |

The whole field shares one macro skeleton; the winners differ by **growing less wheat, buying far
more of it, and putting the freed tiles into carrot/melon/tomato**.

### Four things that do NOT work (all measured, do not retry)
1. **Patching our tape toward that profile.** Rewriting wheat plantings into carrot (they share a
   watering schedule) costs **−$21k at 15%, −$31k at 30%, −$49k at 50%**. Animals do not starve —
   the loss is elsewhere. A tape is a coherent whole and its resource flows cascade; the engine also
   drops *all* plantings of a crop in a turn when demand exceeds seeds.
2. **Adopting a mined tape.** Even "HireMe", verified to run a genuinely fixed tape (byte-identical
   actions across two different seeds) and which beat us twice on the ladder, loses **0-16, −$29k**
   when replayed off its recorded seed. Ladder winners are adaptive agents, not replayers.
3. **Harvesting on idle turns.** The tape passes 699 times, and 270 of those are standing on a plant
   with harvestable yield — but every one is a ONE-TIME crop (208 wheat, 60 melon, 2 carrot) where
   harvesting early destroys the plant and forfeits the remaining yield. Zero are strawberry/tomato.
4. **Topping up animal upkeep on idle turns.** Only ~17 actions available all season; the tape's
   feed/care/collect is already near-complete.

### Where the headroom actually is
We use **0.113 ms per turn** against a **1 s/turn** limit (plus 60 s banked overage, 20 min per
episode) — four orders of magnitude spare. Nothing we run is compute-bound, so a genuinely
searching/planning agent is affordable. That is the only remaining route past the non-mirror losses.


## The local benchmark is now saturated

`port2/h_over.py` scores **1.000 (54/54)** on the 9-rival pool on fresh seeds 500-502, including
6/6 against the causal-shop-router mirror. It beats everything we have locally.

So `evalpool.py` can no longer rank improvements — any further candidate has to be measured by
**head-to-head margin against h_over itself**, not by pool win rate. The remaining real losses only
happen on the ladder, against adaptive opponents we cannot reproduce offline (mined tapes replayed
off-seed are far weaker than the agents that produced them).

Probed and confirmed sound: **extra hands bolted past the tape's do not disturb it.** The tape drives
hands 0..N-1 and keeps its slots; idle extra hands cost exactly their wages (3 hands from day 12 =
-$14.3k = 18 days x $1,220) and SE land exactly $4k. Hire cost is `fib(hires_today)`, so our HIRE
orders must be APPENDED after the tape's or every one of its hires gets dearer. This makes a side
farm on the unused SE quadrant (25 tiles, ~375 tile-days) mechanically possible.


## THE BIG BUG: 15% of games ended with a bank of exactly 0

Spotted by eye in the ladder history, then confirmed across 223 mined replays: **19 episodes ended
with our bank at exactly $0 — 18 of them h_over's** (18/117 = 15% of its games).

Cause, from the replays (identical in every one):
- The tape commits ~$2,830 of its $3,000 on day 0, then runs the entire season on a minimum balance
  of **$0-9**. (Verified locally: min cash over a season is 0-9 on every seed.)
- `_do_hire` silently no-ops when `money < cost`. If the balance touches zero exactly when the
  morning HIRE orders are processed, we get **no hands at all**.
- One farmer cannot water 19 crops. Money 3000 -> 0 on day 1, `hands` = 0 from step 27, every plant
  a weed by day 3, livestock starved, farm dead for 27 days, final bank 0.
- **The hires that failed cost $4 in total** (fib 1+1+2 for three hands).
- The tape's own six-day budget guard cannot help: it protects the static feed reserve so strictly
  that it never fires at all.

Fix (`port3/main_safe.py`): walk the market list exactly as the engine will — orders settle in list
order, so buys ahead of the HIREs move the balance first — and only if the hires genuinely cannot be
paid, raise the shortfall from the cheapest thing in the shed and hoist that SELL to slot 0. Gated to
days 0-3, where every observed death spiral began.

**Bit-identical to h_over across 40 normal episodes and 3 stress configs**; it simply never fires
outside the failure mode. Unit-tested on a synthetic zero-cash turn: it prepends one $100 fertiliser
sale and preserves all three hires.

Two failed attempts worth remembering: a general cash floor (fires constantly, −$39k) and
pre-funding on the previous turn (fires daily, −$460k over 32 games). The tape runs at zero *by
design*; any buffer you hand it just gets spent. Only the exact-shortfall, hire-turn-only version is free.

### Packaging trap this hit
Concatenating the guard onto the agent shadowed the module's existing `ANIMAL_COST` (a tuple indexed
by int) with a dict, giving `KeyError: 1` and a silent **3000-bank no-op that still reported
`status DONE`**. `kaggle_load_check.py` caught it. Namespace every appended symbol, and never trust
DONE — check `errors == [None, None]` and that the bank is not exactly `startingMoney`.


## The SE side farm does not pay (measured, closed)

Buying the unused SE quadrant and working it with extra hands loses **$4,200-4,450/game** against
h_over, on two disjoint seed sets (2-22 and 0-24). The decomposition is exact, because two h_over
seats play byte-identically:

| config | margin |
|---|---|
| side farm off | +0 (bit-identical) |
| buy SE, farm nothing | **-$4,000** |
| full side farm | -$4,446 / -$4,244 |

**The farm's own contribution is zero within noise** — 25 tiles worked by an extra hand earn back
exactly that hand's wages, and the $4,000 of land is dead loss. Scaling is strictly worse:
2 hands -$9,143, 3 hands -$17,856; geese -$6,241 to -$12,524.

Cause is **market saturation, not the planner**: by day 12 the town absorbs ~120 units/day across all
nine products and two 75-tile farms already exceed that. Marginal output sells at $15-30 per
hand-action while the 13th hand costs $233/day for ~11 useful actions. This closes the whole family
of "produce more" ideas — more tiles, more hands, more livestock.

Three real integration traps were found and fixed on the way (see `side/check_tape.py`, which proves
0 tape divergence over 720 steps on 8 seeds): the hand-slot boundary is the number of HIRE orders the
tape issued *today*, not its `n_units`; `PLANT` validation is atomic per crop, so over-requesting
drops the tape's plantings too; and the shed is shared, so selling from it steals the tape's feed and
fertiliser.


## Packaging trap #2: Kaggle ignores the NAME `agent`

`kaggle_environments.agent.get_last_callable` returns
`[v for v in env.values() if callable(v)][-1]` — the **last callable by dict INSERTION order**, with
no preference for the name `agent`. Redefining `agent` keeps its *original* insertion position, so
**any helper function defined after the first `def agent` silently becomes the submitted agent**.

That is what killed the first cash-guard submission: our helper `_gfib` was chosen and the episode
died with `TypeError: 'Struct' object cannot be interpreted as an integer`. `kaggle_load_check.py`
gave a FALSE PASS because it preferred the name `agent`.

Both are fixed. The checker now mirrors `get_last_callable` exactly, errors loudly if the chosen
callable is not the one named `agent`, and finally **runs the file through real
`kaggle_environments.make(...).run(...)`** — the only definitive test. When appending to an existing
agent file, end it with:

    del agent
    agent = _my_guarded_agent

so `agent` is genuinely re-inserted last.


## The cash bug is worse than first measured — and it is the whole ballgame

Auditing 10 of the most recent h_over ladder replays (`mine/hireaudit.py`, comparing HIRE orders
issued to hands actually held):

| | |
|---|---|
| games ending at bank 0 | **5 of 10** |
| pattern | day 1: 3 hired / 0 held, day 2: 4/0, never recovers |
| hands lost over the season | ~250 per failed game |

The rate has RISEN as we climbed (15% over 117 games, ~50% in the newest 10) — stronger opponents
drain the shared market harder, so our razor-thin opening cash tips over more often. The later
shortfalls (day 5: 4/3, day 6: 8/2) are *consequences* of the day-1 collapse, not separate faults,
which is why gating the guard to days 0-3 is the right call.

Tuning of the guard, all measured against h_over over 32 episodes:

| variant | cost in normal play |
|---|---|
| reactive, days 0-3 | **$0 — bit-identical** |
| reactive, all season | -$4,397 (fires twice needlessly) |
| + $20 opening cushion | -$5 (essentially free) |
| + $40 opening cushion | **-$214,228** (fires constantly) |

Submitted two insurance levels to A/B on the ladder: `sub_cushion.py` (reactive days 0-3 + $20
cushion) and `sub_maxins.py` (same cushion, reactive all season). Compare their rate of bank-0 games
once they have episodes.


## Any team's episodes are downloadable — the leaderboard is fully observable

`kaggle competitions episodes <THEIR_submission_id>` and `kaggle competitions replay <episode_id>`
both work for **other teams**. A replay carries the full 719-turn action list for BOTH seats, the
seed and the banks. `mine/fetch_any.py` mines them; `mine/study_top.py` and `mine/blueprint.py`
analyse them. Submission ids come from the leaderboard URL (`?submissionId=...`).

### Blueprint of "Crop Dusta" (top-5), from 70 of their games
Mean bank 94,672, record 50W-20L, **zero blow-ups**. Genuinely adaptive: 70 distinct action
sequences across 70 seeds, first divergence at day 1.

| always fixed | adapts (min-max) |
|---|---|
| land on days **5 and 8**, 2 quadrants (never SE) | cows **3-16**, sheep **2-21**, geese **0-11** |
| 13 units/day (12 hands) | wheat **51-210**, carrot **0-95**, strawberry **9-53**, tomato **0-26** |
| **never FERTILIZE** (0 in all 70 games) | wheat bought **746-2415** |
| ~1062 WATER, ~357 COLLECT, ~407 HARVEST | melon stable ~12 |

They win with more carrot (37 vs 25) and more wheat (135 vs 120), lose with more strawberry. The
adaptation is the whole point: our fixed tape plants 9 carrots whether or not pet cafes have pushed
carrot to $514.

Caveat learned the hard way: the huge `buy:WHEAT` (~1800) and `SELL WHEAT` (~1745) numbers are
**order quantities, not fills**. An agent can order `SELL WHEAT 200` holding 50. Do not read a wheat
arbitrage into them; an immediate buy/sell round trip is exactly zero by construction.

## Ladder-measurement trap: frozen submissions

Only the latest 2 submissions are matched. Everything older **freezes at its last rating**, so
comparing a live agent (still climbing from 600) against a frozen one is meaningless — I briefly
concluded the cash guard was harmful on exactly that mistake. To compare two agents, submit BOTH so
they are the latest 2 and play the same pool at the same time. Check episode counts: a count that
stops growing means the agent is frozen.


## A/B verdict: the cash guard is REJECTED (I got this backwards once — see below)

Both arms submitted within one second of each other on 2026-09-04 so they climbed together
(`mine/ab.py`, ~26 ladder games each):

| arm | games | record | bank-0 | our mean bank | *their* mean bank | Elo |
|---|---|---|---|---|---|---|
| control (no guard) | 26 | 21W-5L | 1 (4%) | 97,116 | 80,558 | 2173.5 |
| guard + cushion | 25 | 21W-4L | **0** | **100,654** | 71,029 | 1962.6 |

My first read was that the Elo gap was a matchmaking artifact and the guard was the better agent,
because it had fewer losses and no bank-0 games. **That was wrong, and the error is instructive:
the win counts are confounded by opponent strength in the direction that flatters the guard.** It
went 21W-4L against opponents banking 71,029 on average; the control went 21W-5L against opponents
banking 80,558. Beating weaker opposition by a similar margin is the *worse* result, not the better
one. Once you condition on who each arm actually played, the A/B favours the control.

The frozen submissions agree, at comparable game counts and with no cherry-picking — every
unguarded agent outranks every guarded one:

| submission | games | rating | guard? |
|---|---|---|---|
| h_over | 127 | **2609.9** | no |
| port | 139 | 2513.5 | no |
| cushion | 142 | 2314.0 | yes |
| maxins | 142 | 2271.2 | yes |

**Why a "free" layer can still cost 300 rating.** The guard is bit-identical to the base on 32/32
local seeds — but that is precisely because it *never fires locally*. Self-play produces no cash
shortfalls, so the local test proves only that it is inert when idle, never what it does when it
acts. On the ladder it does fire, and when it fires it hoists a SELL into market slot 0, disturbing
the tape's carefully ordered market list at the worst moment. It buys back ~4% of games that ended
at zero and apparently pays for them elsewhere.

**The general lesson:** proving a layer is neutral where it doesn't trigger is not evidence about a
layer that triggers somewhere else. A local test that never exercises the code path is not a test
of it. This applies equally to the survival override, which is also inert locally (0 deaths in 160
self-play games) — its ladder behaviour is likewise unmeasured, and it should be trusted only as
far as that.

## THE CENTRAL FACT: the ladder is a mirror-match monoculture, so only MARGIN matters

Audit of 30 real ladder games for `sub_newtape` (rank 482/1200, rating 2224.5, 101 games):

- record **21W-9L**, our mean bank 88,961 vs 71,199, **0 bank-0 for us, 3 for them**
- **our tiles at day 25: median 75. Our opponents': median 75.** Every single one.

Everyone at our level runs the same tape we do, so nearly every game is a near-mirror decided by
1-2% of bank:

| | us | them | gap |
|---|---|---|---|
| loss | 101,056 | 103,134 | 2.0% |
| loss | 77,105 | 77,860 | 1.0% |
| win | 46,130 | 45,994 | 0.3% |
| win | 140,856 | 139,552 | 0.9% |

**Consequences, and they invalidate most of how I have been measuring:**

1. **Adopting a stronger tape buys parity, not rank.** Beating the *old* tape 100-0 locally moved us
   from 2610-class to... 2224, because the field had already moved to the new tape. A local pool of
   stale agents (h_over, port, salem2900, pilkwang) measures nothing about the ladder.
2. **The benchmark must be the mirror**, candidate vs the exact submitted build, scored by **mean
   margin** over many seeds — not win rate against weaker agents, which saturates instantly.
3. **Small edges are the whole game.** A $3k overlay edge is ~3% of a typical bank and decides most
   of these games. This is the regime where overlay work pays, and where strategy swaps do not.
4. The safety layers are doing their job and are not the bottleneck: 0 bank-0 for us in 30 games,
   3 for opponents.

## THE $50 CASH TRAP — one early purchase costs ~$14,000

Found 2026-09-05 while isolating why a single tomato tile cost -19,446 when dropping a whole
strawberry tile costs only -1,220. A one-tile change cannot be worth $19k, so the crop was not the
cause. Isolating each part:

| change | margin |
|---|---|
| buy ONE tomato seed ($50), plant nothing | **-13,836** |
| swap 1 strawberry -> wheat (seed already held) | -1,281 |
| drop 1 strawberry planting entirely | -1,220 |
| buy seed + plant 1 tomato | -15,192 |

**The $50 purchase is the whole loss.** The tape commits $2,830 of its $3,000 on day 0 and runs the
opening on a $0-9 minimum, so any unplanned spend starves a later HIRE — and `_do_hire` silently
no-ops when it cannot pay, which is the death spiral (a single dropped hire measures -88,691).

Gating the same purchase on `day >= 12 and money >= 5000` takes it from **-13,836 to -50** — exactly
the price of the seed.

**This confounded several earlier verdicts.** Every crop experiment bought seed early, so they were
all partly measuring this instead of the crop. Re-tested with gating:
- wheat -> carrot: was -28,275, now **-399** for +5 carrot (still negative, but 70x smaller)
- strawberry -> tomato: was -34,034, now **-100**

The crop conclusions survive (grafting another agent's crop mix onto this tape still loses), but the
magnitudes were wrong. **Rule: never let an experiment spend cash before ~day 8 without checking the
opening separately.**

## The opening is a tuned cash schedule — perturbing it EITHER WAY is catastrophic

Follow-up to the $50 cash trap. If an unplanned $50 spend costs $14k, does *withholding* spend gain?
No — it is far worse. Retested against the shipped build (mirror, margin, holdout seeds):

| perturbation to the opening | margin |
|---|---|
| spend $50 more (one seed) | -13,836 |
| **defer the day-0 animal purchases by one day** | **-119,077** |
| skip any purchase whenever cash < $600 | -40,694 |
| skip any purchase whenever cash < $300 | -6,841 |
| swap early SHEEP->COW (which *saves* $100/head) | -89,164 |

The tape commits $2,830 of its $3,000 on day 0 and every dollar is load-bearing: the animals bought
at step 1 drive production from day 6-8 onward, so delaying them by even a day costs more than the
entire cash cushion is worth. **Do not add to, remove from, or reorder the opening spend.**

Also retested with proper cash gating, since the original verdicts were confounded:
- **land hoist** (buy quadrants on days 5/8 instead of 6/11): was -509, now **-15 / -162**. The
  confound was real — the idea is neutral, not harmful — but it is still not a win.
- **crop substitution**: was -28,275, now -399 (+5 carrot). Still negative.
- **animal mix**: was -6,755, and the cash-positive direction is *worse* (-89,164). Firmly closed.

## Rating mechanics, measured (18 live episodes)

The rating is TrueSkill-like and the per-episode change is genuinely variable — but **not with the
margin of victory**. Isolated by polling our score every 60s and keeping only intervals containing
exactly one new episode:

| result | margin | rating delta |
|---|---|---|
| LOSS | **-596** | **-5.80** (worst penalty of all) |
| LOSS | -16,891 | -4.70 |
| WIN | +416 | +4.30 |
| WIN | **+15,435** | **+3.90** (smallest gain of all) |

Wins: mean +4.33, spread +3.90..+5.20. Losses: mean -4.60, spread -5.80..-3.40.
**Correlation(margin, delta) = -0.43** — slightly inverse, because a large margin signals a weak
opponent and beating a weak opponent is worth less.

**Consequence:** optimise *win probability*, not dollars. Margin is only a proxy, and a good one
solely because in near-mirror games a bigger expected margin means a higher chance of finishing
ahead. It also means a new submission's high sigma makes it swing hard — another reason not to churn.

## Engine fact: watering gives NO yield bonus to ongoing crops

`_apply_unit_action`'s WATER branch gates the yield bonus on `if not crop_data["ongoing"]`.
STRAWBERRY and TOMATO are `ongoing=True`, so watering them **never adds yield** -- it only marks
`watered_today` and prevents the tile turning to weed. Only WHEAT, CARROT and MELON get the bonus,
and only inside `(max_yield_day+1)//2 <= age <= max_yield_day` (doubled if fertilized).

This kills an attractive-looking lead. Measured: 451 plant-days a game end unwatered, of which 143
are inside the yield window -- but **104 of those are strawberry**, where watering is worthless.
A layer that sends idle units to water in-window tiles covered 16 more of them (143 -> 127 missed)
and left total tile yield at **exactly 632** and the bank unchanged. There was never $10k there.

Also measured while chasing it: weeds cost only ~$150/game (1.7 weed tile-days), and idle runs are
mostly length 1 (874 of ~1,180 sampled) -- units are rarely free long enough for a round trip
anyway.

## THE CENTRAL ECONOMIC LAW: you cannot out-produce a shared, fixed demand pool

Four strategy directions were tested on 2026-09-04/05. Three died, and they died for **one common
reason** worth stating once:

> Demand is fixed and shared. Producing more of a valuable product **destroys its price**, and the
> high price of a product you don't make is unreachable. So no supply-side change wins. The only
> wins are (i) capturing more of the fixed pool than the opponent, and (ii) not wasting resources.

Evidence, all mirror-benchmarked:

| direction | test | result |
|---|---|---|
| **Concentrate animals on the high-demand product** | all COW | **-90,638** (0W-48L) — milk crashes to $67 |
| | all SHEEP | **-69,822** (0W-48L) — wool crashes to $105 |
| | demand-aware COW/SHEEP swap | -6,755 on holdout |
| **Sell only on the best price phase** (town eats every 4 turns; phase 1 prices are 1.7-2.9% higher) | defer all off-phase sells | **-103,111** |
| | defer only MILK/STRAW/WOOL | -58,654 |
| **Cut the expensive tail of daily hiring** (11th hire costs $89) | drop last hire | **-88,691** |
| | drop last 2 | -93,503 |

So the tape's fixed 9-cow/9-sheep split is a **deliberate hedge across two demand pools**, not an
oversight — and its hiring is already right, because a hand's labour is worth vastly more than the
fib cost. The one direction that *did* work is the market-contention one, below.

### Demand arithmetic (why shops are everything)

| sink | fires | units |
|---|---|---|
| Town centre | every 24 turns → 30×/game | 1 per product per firing |
| **A single shop** | every 4 turns → up to 180×/game | 1 per product (**2 if single-product**) |

Eight shops fire **936 times a game**; the town centre 30. So a shop is worth **4-7× the entire
town centre** for a product it carries. Special cases: **CARROT** (only PET_CAFE, 2×) and **WOOL**
(only YARN_STORE, 2×), and **MELON is in no shop at all** — its whole season demand is the town
centre's 30 units, though the tape sells ~72.

## THE SLOT-ORDER EXPLOIT — sell from earlier slots than the opponent

Found 2026-09-04 by asking what the monoculture actually *gives* us, rather than how to tune inside it.

`_process_market` settles orders **slot by slot**: our order #i is quoted against their order #i,
and every unit that commits raises the shared inventory. So a unit sold from an earlier slot gets a
strictly better price than the same unit sold from a later one. Two facts make this exploitable:

- Essentially every opponent runs the same published tape we do, so **we know their slot layout**.
- Measured in a mirror game: **100% of our sell value ($172,046) lands on a turn where the opponent
  is selling the same product.** Every dollar is earned in direct contention with them.

Fix is three lines: hoist SELL orders to the front, steepest price curve first (MELON/WOOL collapse
on `sq`, MILK/STRAWBERRY on `linear`, WHEAT/EGG on `log` and barely move).

| test | result |
|---|---|
| search seeds (2200s) | +3,353, 45W-3L |
| **holdout seeds (3300s)** | **+3,476, 47W-1L** |
| **96 fresh mirror seeds** | **+3,474, 96W-0L** |
| vs untuned newtape | +2,723, 48W-0L |
| vs h_over / salem2900 | +151,112 / +12,752, 48W-0L each |
| **falsification control: SELLs pushed LAST** | **-65,942, 0W-48L** |

That last row is the point — reversing the change is catastrophic, so the mechanism is the slot
order and not noise. Worth as much as the entire sell overlay (+3,361) on its own.

Side benefit: selling before HIRE banks the proceeds before `_do_hire` runs, and `_do_hire` silently
no-ops when it cannot pay — the exact failure that ended games at a bank of 0.

`port3/slotorder.py`, shipped in `port3/newtape_slot.py` / `sub_slot.py`.

**The general lesson: in a monoculture, look for what knowing the opponent's exact policy buys you,
not for more tuning inside your own.** Every parameter sweep was exhausted; this was sitting in the
engine's order-settlement loop the whole time.

## What the research says (surveyed 2026-09-04)

Across Kaggle simulation competitions the decisive move is **cloning the top agent from its public
replays**: in Lux AI S1 the #1 agent's records were public and competitors who imitation-learned
from them closed the gap; the Hungry Geese winner behaviour-cloned top-leaderboard episodes and
*re-cloned as the metagame moved*. The Pokémon TCG challenge (Kaggle's other live sim comp) uses the
identical ladder — agents start at 600 and are matched by rating — which independently confirms the
convergence cost of resubmitting.

**Tested here and it does NOT transfer.** Replaying Crop Dusta's own 70 recorded tapes against our
tuned build: **0/70 tapes win, mean margin -113,523.** They are genuinely adaptive (70 distinct
sequences, first divergence at day 1), so their actions are conditioned on shop unlocks and market
state a replay does not reproduce. Their median recorded bank is 89,023 — comparable to ours, so
they do not out-earn us in absolute terms; they out-*margin* the monoculture. Cloning them would
need a real state->action model, which is the from-scratch planner that measured -49,860.

## Crop substitution is DEAD — measured three times now, do not retry

The economics look irresistible. Revenue per tile-turn on the tuned build over 6 games:

| crop | tile-turns | revenue | $/tile-turn |
|---|---|---|---|
| **WHEAT** | **14,091** | 14,850 | **1.1** |
| STRAWBERRY | 12,930 | 45,483 | 3.5 |
| MELON | 2,846 | 15,102 | 5.3 |
| CARROT | 343 | 1,228 | 3.6 |

Wheat takes the most land and pays 3-5x less for it — apparently ~$20k of headroom, and exactly the
edge the top adaptive agent runs on. `port3/cropsub.py` does it the careful way: **carrot only**
(matures in 3 days vs wheat's 4, so the tape's scheduled HARVEST still lands, unlike melon/strawberry
which are slower and strand the tile), seeds pre-bought a turn ahead because unit actions resolve
before `_process_market`, and never more substitutions than held seed covers, because planting is
atomic per crop.

**Result: W0-L32, mean margin -28,275.** It fires correctly (carrot 9 -> 28, wheat 195 -> 176).

**The mechanism is the yield window, not harvest timing.** WATER only adds yield when
`(max_yield_day+1)//2 <= age <= max_yield_day`, and that window is per-crop: carrot's (maxy 4) is
not wheat's (maxy 6). The tape's watering turns are co-tuned to the crop it planted, so a
substituted tile gets watered outside its window and yields poorly. Feeding was *not* the problem —
unfed animal-days actually improved (24 vs 36) while milk orders still fell 470 -> 397.

**Conclusion: the tape's planting, watering and harvest schedules are one co-tuned object.** No
piecemeal crop edit can work; capturing this edge requires re-deriving the whole schedule, which is
the from-scratch planner that measured -49,860 margin at 0% win rate. Three independent attempts
(-$21k, -$49k, -$28k) on two different tapes with two different benchmarks. Closed.

## The mirror-margin optimiser (this is now the main engine)

Because the ladder is a monoculture, the benchmark that predicts rank is: **candidate vs the exact
submitted build, same seeds, both seats, scored by mean margin.** Paired seats cancel almost all
variance — the null control returns *exactly* +0, so any nonzero signal is real. `scratchpad/mirror_tune.py`,
`ablate.py`, `tune2.py`.

**Three disciplines this run made non-negotiable:**

1. **Prove liveness first.** Most of `P` is dead in any given mode. In `lookahead` mode 10 of 20
   knobs did nothing; sweeping them produced a page of "+0" results that look exactly like real
   negative findings. `liveness.py` runs one game per knob and counts turns where the emitted market
   orders differ. Only sweep knobs that move something.
2. **Accept only a strict improvement.** My first sweep took the best value of each parameter's
   trials even when it was *worse than the running best* — it accepted `fert_keep=5` at +1,623 over
   a running best of +1,755, and accepted four parameters whose values all tied exactly (inert).
   Ablation removed 5 of the 9 "accepted" parameters as no-ops.
3. **Hold out seeds.** 30 configs were searched against seeds 2000-2023, so that set is burned.
   The number that counts is a disjoint set.

Result (first pass): minimal contributing set is **`mode=model`, `fert_keep=5`, `guard_protect=0`,
`wheat_start=450`** — tune seeds +2,878 (48W-0L), **holdout +2,616 (64W-0L)**, and it also beats
h_over by +160,840, salem2900 by +14,656 and indarkarhana's top-10 package by +5,270. Note
`mode=model` was previously *unreachable* dead code; switching to it changes which knobs are live
(re-run liveness after any mode change — only 8 of 30 are live in model mode).

## yhay81 published a NEWER tape (2026-09-03) — and swapping it needs two other changes

`yhay81/three-day-shop-router` (2026-09-03) ships a different `source/tape.inc` from the one we
ported: 50,332 encoded integers against our 50,522, same per-turn token format, 2 routes x 719
turns. `rivals2/yhay_tape_new.b85` is it, re-encoded for our loader; `port3/hover_newtape.py` is
h_over with it dropped in.

**Two things move with the tape and will silently mis-play if you only swap the data:**

| | tape we ported | 2026-09-03 tape |
|---|---|---|
| `kDecisionStep` | **216** | **360** |
| `select_route` | 3 shops == ICE_CREAM/FARMERS/FARMERS, then rival GOOSE tiles > 1 | shop[0]==BAKERY and market FERTILIZER stock <= 10232.5, **or** shop[0]==PET_CAFE and rival PLANT tiles <= 64.5 |

The route selector is a *different decision rule*, not a retuned one, and it reads market inventory
and rival plant tiles — neither of which the old `_StateView` carried. `port3/hover_newtape.py`
adds `market_inventory`, `rival_plant_tiles()`, `T_PLANT`, `SHOP_BAKERY`, `SHOP_PET_CAFE`.

Note also that `kSegmentTurns` stayed 72, so the six-day budget guard ports across unchanged.

### It is a very large upgrade, and it explains our bank-0 losses

| new tape vs | result |
|---|---|
| h_over (our tape + sell overlay) | **100W-0L**, mean bank **151,985 vs 0** |
| bare port | **20W-0L** |
| itself (self-play sanity) | symmetric, 49k-127k a side — not a degenerate exploit |

The zeros are not crashes (status DONE, no errors). Tracing a game shows the new tape **inflicting
the death spiral on h_over**: h_over is down to $3 by day 8 and $0 with zero hands by day 12, and
sits on 19 weeds and 4 empty pastures for the rest of the season. The new tape meanwhile expands to
~77 tiles (3-4 quadrants) against our ~24 and banks nearly the entire ~$206k seasonal demand pool.

**This reframes our own bank-0 games on the ladder.** They are not bad luck or a self-inflicted
cash bug — they are this attack being run on us by opponents on the newer tape. The cash guard was
treating a symptom of being out-expanded, which is also why it bought nothing.

### The published vote count is not a strength signal
Two heavily-upvoted notebooks, benchmarked head-to-head on 80 games each against h_over:

| notebook | result vs h_over |
|---|---|
| `salemali7/kaggriculture-2900` ("2900+") | **4W-76L (5%)**, margin -14,497 |
| `pilkwang/kaggriculture-structured-economic-policy` | **0W-80L**, margin -27,931 |

A title claiming a ladder score says nothing about head-to-head strength; both lose badly to a tape
that was itself only worth 2610. Always benchmark before adopting.

## The top of the ladder IS our tape — and one adaptive agent beats it 71%

Profiling all 70 of Crop Dusta's opponents (`mine/beats_top.py`) shows the rest of the top ladder
runs the **same public tape we do**: cows 6-11, sheep 5-11, wheat planted 185-187, strawberry 32-38,
carrot 6-9, land on days 6 and 11, CARE ~365, wheat bought ~164. Crop Dusta is the lone outlier and
takes 50-20 (71%) off that monoculture.

Their distinguishing features versus the tape:

| | tape (us + rest of top) | Crop Dusta |
|---|---|---|
| land days | 6 and 11 | **5 and 8** (~75 extra tile-days) |
| wheat planted | ~186 | **131** |
| wheat bought (order volume) | ~164 | **~1800** |
| carrot planted | ~9 | **~34** |
| CARE actions | ~365 | **~114** |

Reading: they buy their feed instead of growing it, which frees tiles from $60/tile-day wheat for
$80+/tile-day carrot, and they take the land earlier. Note this is the same direction the loss
analysis pointed at, and that substituting wheat->carrot *inside the fixed tape* failed (-$21k to
-$49k) — a tape's resource flows cascade, but a planner that sizes its own purchases may be able to
make the trade. That is the hypothesis the adaptive build is testing.


## Foundation for a planning agent: a validated forward model (`plan/fastsim.py`)

Our own farm evolves deterministically from our own actions — the only external inputs are seeded
weed spawns and the shared market price. So we can simulate our own future exactly and *plan*,
instead of guessing with heuristics. Nobody in the field does this, and we have the budget for it:
we use **0.113 ms of a 1 s/turn allowance** (~719 s unused per episode).

`plan/validate.py` replays real episodes and diffs every field against the engine:

| | result |
|---|---|
| tiles — growth, animal production, care bonus, decay, weeds | **exact** (1 divergence in 3x718 turns) |
| shed and seeds | **exact** |
| money | mean error **$5**, median **$0**, max $288 against banks of $59-99k |

The residual money error is the opponent's simultaneous market orders moving prices inside the
per-unit lockstep — inherent and unknowable, and only 0.006% of the bank. Production is exact;
revenue is a forecast. That is precisely the split a planner needs, since candidate plans are
compared against the same market uncertainty.

Usable as: resync from the observation each turn, then roll candidate plans forward to the end of the
season and pick the best. `apply_market` walks prices exactly as the engine does (SELL quoted at the
pre-sell inventory, BUY_PRODUCT at the post-buy, so a round trip is exactly zero).

---

# 2026-09-06 — the instruments were broken, and the fix was a new base

## What the day actually established

**1. Our whole build ranking was inside the noise.** `sub_hover.py` and `sub_ab_control.py` are the
same file (md5 `0b37a0fc…`) and scored **2609.9 / 2202.9**. `sub_cushion.py` and `sub_ab_guard.py`
are the same file and scored **2314.0 / 2020.6**. Convergence explains part of it (the low scorer
had fewer episodes each time), but the converged spread across our family was 2271–2610 — wider
than every difference we had been shipping.

**2. Nothing we shipped since the tape swap did anything.** Against a fixed rival pool the four
newtape builds score **+15,242 / +15,594 / +15,626 / +15,839** margin and **0.943–0.946** win rate.
sub_tuned, sub_slot, sub_impact, sub_final are the same agent. All four were selected on *mirror*
margin, which optimises "beats a copy of me".

**3. Ladder win rate ranks our builds backwards.** 287 fetched episodes: sub_slot 79.4% at rating
2304, sub_tuned 35.3% at 2573. Matchmaking pairs by rating, so win rate equilibrates to ~50%
regardless of strength. It is not a quality signal and never was.

**4. The tape swap was justified by a crash.** `sub_newtape` was accepted on "100W-0L vs h_over
(mean 151,985 **vs 0**)". Re-run in the **official** environment: h_over scores 0.0 with status DONE
against every newtape build, and 75,621 against itself. Its opening ends day 0 with exactly $0, so
the $1 first hire on day 1 silently no-ops, it holds 0 hands for two days and the farm dies — any
opponent whose day-0 market activity moves buy prices by a few dollars kills it. Logged C11.

## What replaced it

`thomastschinkel/kaggriculture-public-state-router-74-5-win-rate` (published 2026-09-05, 53 votes).
Four recorded tails with byte-identical prefixes, routed at t=226/360/433 on public state only,
plus three repairs (weed_dig / dead_stock / clamp_sells). This is the "policy DAG with shared
prefixes" architecture the external reviewers proposed and I had written off as unbuildable.

| | vs current-meta pool (10 strongest public agents) |
|---|---|
| **router** | **+13,283 margin, 0.787 wr, 95,768 bank** |
| sub_final (was live) | +4,956, 0.656, 87,749 |
| sub_tuned | +3,919, 0.644, 87,146 |

Head-to-head over 80 games we lose to it **13–67, mean −5,491**. It beats every pool member,
including the two that beat us.

## How much is left in that architecture

320-cell panel (20 seeds x 8 live opponents x both seats, all four tails run to completion):

| | margin |
|---|---|
| best single tail (MAIN) | +12,407 |
| published routing rule | +14,949 |
| **per-cell oracle** | **+15,881** |

So the three decisions are worth +2,542 over the best fixed tail, and *perfect* routing would add
only **+932** more. The routing is near the ceiling of its own tail set; more gain needs more tails.

One real defect found: **MILK_GLUT fires 122/320 times and is the best tail only 55.** Margin is
monotone increasing in its threshold (+12,894 at 0 → +14,949 at the published 10067 → +15,148 where
it never fires). Monotone, so not a grid-search artifact. Probable cause: the author's 968-game
panel replays *recorded* routes, and a milk glut against a fixed tape is a different signal than
against an agent reacting to the same market. The px_CARROT threshold was left alone — its panel
optimum is 38 but the curve is flat and non-monotone, i.e. noise.

## Shipped

- `sub_router.py` — the router verbatim, credit thomastschinkel.
- `sub_router2.py` — same, milk branch retired + price-impact slot ordering. Holdout (seeds 3000-19,
  unused in fitting): **+14,191 vs +14,036**, better against 8 of 9 opponents. Real but small
  (~+117/game against a per-game σ of ~6,000), so it will not be separable on the ladder. Submitted
  alongside the unmodified router deliberately, as a live A/B with a safe baseline.

## Instrument rules added (MISTAKES C10/C11, checklist 8-10)

- A benchmark must be shown able to rank: spread across known-different agents > its noise floor.
- Opponents must be strong enough to beat us sometimes; a pool that loses by 15-27k ranks nothing.
- A 0, or a final bank equal to starting cash, invalidates the comparison. It is not a win.
- Re-check for newer public tapes **before** tuning the current one.

## Still open

- More tails. The oracle over the current four caps us at +932; a fifth tail covering a regime the
  four handle badly is the only large lever left inside this architecture.
- Hardest opponents in the pool are `v65` and `tetsutani-new` (+5.6k, 0.85) — where the top of the
  ladder actually lives.

## Addendum — the monoculture bill came due the same day

An episode ended **84,557 vs 84,557** against "Igor V". Cause: **719 of 720 actions identical** —
they are running the same public router notebook. The only divergence is step 718, where our
`weed_dig` repair fires and theirs does not.

Base rate, measured across 325 fetched episodes:

| era | n | near-identical tapes | exact ties |
|---|---|---|---|
| newtape (older two thirds) | 216 | 0 | 0 |
| router (today) | 109 | 3 (2 external + 1 self) | 2 |

**Zero external clones in 287 newtape games; 2 in 38 router games (5.3%).** The clone problem is a
*cost of adopting the public router*, not a pre-existing condition — and it will grow, since the
notebook is one day old with 53 votes. It matters more than a normal loss column: in the final
**Bradley-Terry fit an identical-agent cluster shares a single theta**, so we cannot rise above the
cluster without beating it.

### The mirror decomposes cleanly (120 games vs a plain-router clone)

| variant | margin | win | tie | loss |
|---|---|---|---|---|
| **+ slot ordering only** | **+541** | **0.93** | 0.00 | 0.07 |
| + milk-branch removal only | −387 | 0.08 | 0.70 | 0.22 |
| + both (submitted earlier) | +316 | 0.80 | 0.00 | 0.20 |

Slot ordering is the anti-clone weapon, and the mechanism is exactly the contested case it was
built for: **in a mirror both agents submit identical orders on identical turns**, orders settle
slot-by-slot, and each unit moves the shared price — so ranking sells by
`qty x (px_now - px_after_burst)` decides every contested slot. Retiring the milk branch, by
contrast, *reintroduces* ties (0.70) and loses more than it wins when it does bite.

Against the field on identical seeds the three are indistinguishable: **+14,150 (slot only) /
+14,191 (both) / +14,036 (plain)**. So slot-only strictly dominates — same field performance, far
better mirror — and it is what is now live.

### Correction to my own earlier call

I dismissed the mirror win as a C9 tie-break artifact. That was wrong *here*, and the distinction is
sharp: a C9 artifact is a coin-flip perturbation winning by $3-6 with a ~0.50 win rate. This is
**0.93 with +541**, produced by a mechanism that specifically targets mirror matches. C9 still holds
for random perturbations; it does not cover a change aimed at the contested case.


---

# 2026-09-07 — debugging 69 losses: one diagnosis, one falsified fix, one real gain

Refetched every lost episode in FULL (`losstrace.py`). The earlier fetcher reduced replays to action
tapes and discarded the observations, which is why re-simulation never reproduced an episode -- the
raw replay already carries both farms' money, shed, tiles and the shared market at every turn.

## Shape of the losses (69 traced)

| shape | n | median final | flips at |
|---|---|---|---|
| never ahead | 33 | -6,928 | day 16 |
| blown lead | 27 | -2,226 | day 21 |
| late collapse | 9 | -88 | day 29 |

Margin is ~0 through day 12 in every category: **the opening is fine, the damage is all late.**

## The diagnosis: our farm ignores the shop draw

| #YARN_STORE | n | our SHEEP | their SHEEP | our COW | their COW | our wool | their wool | median margin |
|---|---|---|---|---|---|---|---|---|
| 0 | 15 | 5 | 5 | 9 | 9 | 131 | 131 | -1,412 |
| 1 | 29 | 8 | 8 | 9 | 9 | 195 | 196 | -2,053 |
| 2 | 16 | 8 | 9 | 9 | 8 | 196 | 270 | -2,764 |
| 3 | 6 | **8** | **12** | **9** | **6** | 196 | 301 | **-16,062** |
| 4 | 3 | **8** | **11** | **9** | **6** | 196 | 278 | **-19,652** |

Confirmed offline: on seeds finishing with 3+ YARN_STOREs the router wins **50%** against a
strong pool, versus **79%** on random seeds. About **7% of games are coin-flips for us.**

## The fix that failed (logged C12)

Swapping cows for sheep is **-7,758 on high-yarn seeds and -2,564 on random seeds**. It fires
correctly; the lever is simply wrong. Cause below.

## The constraint nobody was looking at

`_drop_inventories_to_shed` takes only `room = capacity - current`, so **anything above the 100-item
shed cap is silently discarded.** The base route already runs at 76-100 through days 18-25 -- it is
throwing away production -- while placing market orders on **89 of 719 turns** and rarely using more
than a few of its ten slots. The swap variant pinned the shed at 100 for six days, so the extra wool
was destroyed on arrival and wool *sold* fell 196 -> 191.

## The gain: shed vent (SHIPPED)

Append SELL orders for whatever is crowding the shed into slots the tape left empty -- only at
>=80/100 occupancy, above a price floor, and always AFTER the tape's own orders so it never
displaces a scheduled sale or its slot position.

| | FIT (50 seeds) | HOLDOUT (60 unseen) |
|---|---|---|
| vent, shed>=80 | +238 | **+277** |
| winrate | 0.920 vs 0.907 | **0.894 vs 0.889** |

All eight configs at threshold 80/90 land within 16 of each other -- a broad plateau, and min_px and
max_qty barely matter. Venting at 70 is **-520 to -1,342**: it competes with the tape's own schedule.
The plateau is why this is believable where the tape patches were not.

## Tooling built today

- `losstrace.py` / `lossdebug.py` / `lossone.py` -- full per-turn autopsy of any episode
- `mixgap.py`, `animalgap.py` -- sell mix and purchases vs the shop draw, decoded from tapes
- `seedindex.py` -- index seeds by shop draw. NOTE: the draw is **not** a pure function of the seed;
  `_end_of_day` shares one RNG between `_spawn_weeds` (one call per EMPTY tile, both farms) and the
  shop choice, so play shifts the stream. It has to be simulated.
- `mkvent.py`, `mkswap.py`, `ventsweep.py`, `swapbench.py`, `btrating.py`, `bands.py`

## Where we stand

sub_router_slot converged at ~2600 (best we have had); top-10 cutoff has risen 2774 -> 2799.8 in a
day. **We are ~190 short and the field is moving.** Every overlay measured this week is +68 / +117 /
+277 against a per-game sigma of ~6,000 -- stacked, maybe 30-50 rating points. The only thing that
has ever moved us is adopting a better base (683 -> 2513 -> 2610 -> router, +190).


## Later on 2026-09-07 — re-baseline check, and the market model does not transfer

**Re-baseline (should be daily).** Screened 8 agents published in the previous 24h against our live
build. None beats it: closest are `y3uanm/market-impact-router-v4` (+926), `flexonafft` (+704),
`yamakawanin/king-v4e-rc4` (+628) -- and we win **100%** against all three. Their banks land within
~1k of ours, which suggests they are router-derived too. No free upgrade available.

**Market-model port: dead.** The h_over sell overlay (town-drain estimate, future-unlock projection,
price-after-drain forecast, shed target) was worth +3,361 on the old tape and had never been tried on
the router. Ported it (`mkmodel.py`), caught C14 (714/719 NameErrors, silently falling back), fixed
it, verified it genuinely fires (0 exceptions, 57-66 turns modified, ~200 units added per game):

| candidate | FIT | HOLDOUT | holdout wr |
|---|---|---|---|
| + slot + vent (`sub_vent`, live) | +346 | **+374** | **0.912** |
| router bare | 0 | 0 | 0.844 |
| + slot + market model | +21 | **-6** | 0.854 |
| + slot + model + vent | -1 | **-52** | 0.850 |

The model adds nothing, and **combined with the vent it destroys it** (+374 -> -52): its metering
suppresses exactly the overflow sales that earn the money.

**The lesson worth keeping:** the crude policy beats the sophisticated one here because forecasting
demand was never the binding problem. The binding problem is the 100-item shed cap with
discard-on-overflow. A model that meters sales *down* is solving the wrong constraint.

**The vent now has two independent holdouts** -- +277 (60 seeds, 3 opponents) and +374 (60 different
seeds, 4 opponents, one of them newly published), win rate 0.844 -> 0.912. That is the strongest
validation anything in this project has had.

**Open with the user:** retiring `sub_router_slot` (2541.5, 202 eps) needs a submission, and there is
no candidate better than `sub_vent` (2505.0, 93 eps, still climbing). Recommended waiting for it to
converge rather than spending a slot on an indistinguishable twin.


## 2026-09-07 (late) — the husbandry rewrite worked; the micro-farm died on arithmetic

### Herd chain conversion — SHIPPED as sub_herd.py

The engine makes composition changes far cheaper than a compiler. Only three actions are
species-bound -- BUY_ANIMAL, PICKUP and PLACE -- and FEED/CARE take no argument at all, acting on
whatever animal occupies the tile. COW and SHEEP share PASTURE. **So the husbandry schedule needs no
changes; a conversion is a rename of three actions in one chain.** Renaming only the purchase (the
round-4 failure) leaves PICKUP hunting a species the shed no longer holds.

Extracted the tape's 9 cow chains (BUY -> PICKUP(unit) -> PLACE(unit), identical across all four
tails). Verified the animals arrive: 10 sheep / 7 cows vs 8/9, wool sold 196 -> 253.

Scored by PAIRED WIN RATE, because the ladder and the final BT fit see only wins -- and our own
three converged submissions rank by offline win rate but NOT by margin:

| gate | high-yarn dWR | random dWR | weighted WR |
|---|---|---|---|
| yarn>=1, convert 2 | -0.025 | **-0.021** (z=-2.14) | 0.8205 |
| yarn>=1, convert 3 | +0.014 (z=1.22) | -0.013 | 0.8308 |
| **yarn>=2, convert 3** | **+0.014 (z=+2.25)** | **0.000, 0/480 cells** | **0.8425** |
| vent alone | -- | -- | 0.8416 |

Shipped the tight gate: provably neutral on 93.5% of games, +1.4 win-rate points on the 6.5% it
targets. **Margin was actively misleading here** -- the ungated variant has 6x the margin (+2,901 vs
+455) and is significantly WORSE on win rate.

Weighted, this is +0.0009 win rate, perhaps 1-2 rating points. Real, free, and small.

### Sheep micro-farm — BUILT, VERIFIED, AND NEGATIVE

Designed to avoid positional coupling entirely: SE quadrant ($4,000, the only land the tape never
buys, whose corner (5,5) is a shed-access tile), free BUILD_PASTURE, one extra HIRE appended after
the tape's own, feed bought via BUY_PRODUCT WHEAT, sales appended after the tape's orders.

**The machinery works.** Verified, not assumed: land bought, 4 pastures built, 4 sheep placed on
days 11-12, hands 12 -> 13, total FEED 361 -> 431 (+70 = 4 sheep x 18 days exactly), total HARVEST
468 -> 487 (+19 of 20 possible), all 4 sheep alive from day 12 to 29, and **byte-identical to its
base on every seed where the trigger does not fire.**

It still loses $4k-19k, and the reason is arithmetic none of us checked:

> **`_daily_refresh_animals` adds `base = 1` unit per interval.** `max_held: 6` is the STORAGE CAP,
> not the yield. A sheep produces 1 wool per 3 days (2 with the care bonus), not 6.

So four sheep produce ~38 units over the season, not the ~114 assumed -- which is exactly the +38
wool actually sold, and why the wool price barely moved (247.5 -> 244.3). At $245 that is ~$9,300
of revenue against $4,000 land + $2,000 sheep + ~$3,000 marginal hires + ~$2,500 feed = $11,500.

**A sheep is worth roughly $1,100-2,400 gross over the back half of a game and costs $1,130.** No
amount of controller polish fixes that, and the fixed overhead of a quadrant plus a dedicated hand
cannot be amortised over animals that thin. The constraint was never storage, sell rates, or
husbandry -- it is that livestock output is small.

This also retires the reviewers' shared premise (and mine) that opponents at "12 sheep selling 301
wool" were out-producing us. At 1 unit per 3 days, 12 sheep cannot produce 301 wool; that figure is
a whole-season total across a herd plus care bonuses, not evidence of a production edge.


# 2026-09-08 — new base, and the cost of shipping noise

## The damage first

Submitting `sub_vent` and `sub_herd` dropped us from **rank 77 to rank 685** (2611 -> 2288). The
leaderboard scores only the LATEST TWO submissions, so retiring agents sitting at 2502 and 2576.7
for ones that converged to 2288/2283 cost ~290 points of displayed rank -- and there is no undo,
because resubmitting a file restarts it at 600.

The offline evidence for both was real and held up (see below): `sub_vent` +0.0037 and `sub_herd`
+0.0075 win rate over `sub_router_slot`, both positive. **The mistake was not the measurement, it
was shipping changes worth ~0.5 win-rate points into a metric with a +/-200 noise floor**, twice,
while holding the only two live slots.

## The new base: yhay81 "Shop Router 0908"

Published 2026-09-08, 61 votes on day one, same author as every previous real gain
(683 -> 2513 -> 2610). A **learned** router: a decision tree over shop history, own farm state,
prices and market stock, selecting among complete recorded tapes at staged decision points -- against
our four tails and three hand-set thresholds.

800 paired games (80 unused seeds x 5 current-meta opponents x both seats), scored by win rate:

| candidate | winrate | margin | dWR vs our best | z |
|---|---|---|---|---|
| **yhay81 0908** | **0.9213** | **+8,157** | **+0.0275** | **+2.47** |
| sub_router_slot | 0.8938 | +3,932 | 0 | -- |
| sub_herd | 0.9012 | +4,304 | +0.0075 | +2.46 |
| sub_vent | 0.8975 | +4,075 | +0.0037 | +1.34 |
| sub_router2 | 0.8738 | +3,875 | -0.0200 | -4.04 |

Direct head-to-head it beats **every** build we have: 0.919 / 0.938 / 0.894 / 0.887, by ~$6,000.

Ships as a tar.gz (main.py + observation.py + model.json + actions.json) and recovers its own
directory through `agent.__code__.co_filename`, since Kaggle's loader omits `__file__`. Submitted
plain (slot A) and with our price-impact slot ordering (slot B) -- the latter because a 61-vote
notebook will be widely cloned and that overlay wins 93% of mirror matches.

## Standing policy from here

**Re-baseline only.** Check newly published notebooks daily, head-to-head anything promising, ship
only what clears the current base by more than the noise floor. That check has now paid three times;
nothing hand-built this week has cleared +0.01 win rate.
