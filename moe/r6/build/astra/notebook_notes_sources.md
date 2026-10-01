# Source: rivals9/leoprovorov_kaggricult-man-reverse-engineering/kaggricult-man-reverse-engineering.ipynb

### Cell 0
![Kaggriculture-Man pointing meme](attachment:kaggriculture-man-meme.png)

### Cell 1
# 🕷️ Kaggriculture-Man: Reverse-Engineering Top-Agents Meta

### A replay laboratory, an exact agent map, and one bounded market-timing intervention

<div style="background:#171a14;color:#ffffff;border:4px solid #d1a256;border-radius:14px;padding:20px 24px;margin:20px 0">
  <div style="color:#d1a256;font-size:22px;font-weight:800;letter-spacing:.04em">BEFORE YOU CONTINUE</div>
  <p><b>If this work is useful, please upvote the notebook, download the companion datasets, and leave a concrete idea or counterexample in the comments.</b></p>
  <p>I can run the same diagnostics on public agents and public replays. Add a public notebook or episode link in the comments if you want its failure points mapped.</p>
  
  <p style="margin-bottom:0"><b>This notebook combines an article, a research instrument, and a reproducible agent build.</b> The analysis cells are not required to run the submitted agent.</p>
<p style="margin-bottom:12px;">
  <b>Related parts of this research:</b>
</p>

<p style="margin-bottom:6px;">
  <b>
    This part, covering the general overview and analysis is available here:
  </b>
</p>

<a href="https://www.kaggle.com/code/leoprovorov/kaggricult-man-reverse-engineering-part-1"
   target="_blank"
   style="
     display:inline-block;
     padding:10px 16px;
     margin-bottom:18px;
     background:#20BEFF;
     color:#000000;
     font-weight:700;
     text-decoration:none;
     border-radius:6px;
   ">
   → Open Part 1: General Overview & Analysis
</a>


<p style="margin-bottom:6px;">
  <b>
    The second part, focused on the possibility of hacking the in-game store, is available here:
  </b>
</p>

<a href="https://www.kaggle.com/code/leoprovorov/god-s-mode-hacked-stores/notebook?scriptVersionId=349839124"
   target="_blank"
   style="
     display:inline-block;
     padding:10px 16px;
     margin-bottom:18px;
     background:#20BEFF;
     color:#000000;
     font-weight:700;
     text-decoration:none;
     border-radius:6px;
   ">
   → Open Part 2: Hacking the Store

</a>



      
  <p style="margin-bottom:0"><b>Enjoy!</p>

### Cell 2
## Mathematical model

Each formula is shown with its meaning and symbol definitions directly beside it.

### Cell 3
![Mathematical model](attachment:kaggriculture-mathematical-model.webp)

### Cell 4
## Why the Spider-Man meme is not just a joke

Kaggriculture is unusually open. Competitors publish strong notebooks, and everyone can watch public replays of leading agents. This makes **behavioral reverse engineering** possible: not recovering source code, but reconstructing strategy from repeated observable actions.

Every strong public release becomes a base for the next participant. If a nearly optimal agent appears openly, many competitors can reuse it. The difference between first place and the thousandth participant may then become very small, while much of the work done by the original leaders stops being visible.

That is why I suggest upvoting every notebook with substantial individual work, even when it did not produce the strongest agent. The research effort should not disappear when somebody else turns it into a stronger public baseline.

The final evaluation is still uncertain, but not because Kaggriculture has a normal hidden private test partition. The competition uses continued agent matches and a final Bradley-Terry recomputation. The real unknown is the future opponent population: which agents remain active, how the public meta converges, and which matchups dominate the post-deadline evidence. See the official [Evaluation page](https://www.kaggle.com/competitions/kaggriculture/overview/evaluation).

### Cell 5
> **Version update.** The submission is now **MarketShock-M1-WR1K**, with one audited day-21 local watering repair and exact parent pass-through everywhere else. The original experiment record below is unchanged.

## What was built

The base is a frozen Seven-Turn Rescue agent. The research layer reconstructs matches turn by turn and separates route selection from economic execution.

T4 adds one bounded mechanism. In likely mirror games it can sell selected parent-planned inventory one turn earlier. If a real probe shows that the opponent also preempts sales, the lead can become two turns. Every moved unit becomes a credit against the original sale, so the overlay cannot liquidate the same stock twice.

In three fixed worlds, lead-1 beat the untouched control in all six seat-swapped games. Adaptive lead-2 then beat lead-1 in all six. The crop-value guard added +196 in one world and exactly 0 in two, so I treat it as weak and world-specific rather than a general breakthrough.

```python
if mirror_gate_is_open and 336 <= step < 647:
    lead = 2 if counter_preemption_was_observed else 1
    for item, qty in parent_sales(step + lead):
        qty = min(qty, projected_shed[item])
        if 4 <= qty < 100 and market_order_slot_exists:
            sell_now(item, qty)
            credit_original_sale(item, qty)

parent_sale[item] -= credited_quantity[item]
```

The parent remains frozen. The intervention has a narrow gate, and every activation is logged.

### Cell 6
## The full analysis surface

These are exact full-page captures from the live research server on 10 September 2026. They are not recreated charts and they do not use synthetic values.

**Field Ledger** finds the turn where value starts leaking. **Field Skeleton** exposes the agent's actual routing graph. **Field Worlds** measures all possible shop worlds and the replay coverage of each one.

### Cell 7
## Field Ledger

One match, every economic layer: projected score, trend, market execution, revenue, spending, free cash, idle hands, planted value, and the final harvest book.

![Field Ledger](attachment:field-ledger.webp)

### Cell 8
## Field Skeleton

The actual agent map: the day-6 routing branch, observed route frequency and outcomes, route economics, and the games attached to each plan.

![Field Skeleton](attachment:field-skeleton.webp)

### Cell 9
## Field Worlds

All 64 possible shop worlds measured across 2,835 public episodes and cross-checked against the agent's own replay sample.

![Field Worlds](attachment:field-worlds.webp)

### Cell 10
## Reading the agent map

The shared opener runs until **day 6, step 144**. The agent then reads the first two unlocked shops as an ordered pair. Fourteen named pairs select ten distinct continuations; every unlisted pair falls back to plan 0. At **day 27, step 648**, every route enters plan 2 for final liquidation.

The useful unit of analysis is therefore a route inside a world, not one global win rate. The map exposes missing worlds, low-sample branches, route-specific economics, and the exact matches behind each plan.

### Cell 11
## Build the exact agent

The hidden cell writes `/kaggle/working/submission.tar.gz` and verifies the deterministic archive hash.

### Cell 13
## Continue the experiment

Upvote if you want the full toolkit and more replay studies published. Put public notebook links, episode links, and concrete mechanism ideas in the comments. For collaboration, contact me on Kaggle or [LinkedIn](https://rs.linkedin.com/in/aleksei-provorov-832050308).

# Source: rivals9/georgymamarin_kaggriculture-what-2600-farms-do-differently/kaggriculture-what-2600-farms-do-differently.ipynb

### Cell 0
*By [Georgy Mamarin](https://www.kaggle.com/georgymamarin)*

What the top of the board does, set against the middle of the same window: what they plant, when they
buy land, how big a crew they run. The page reruns on each new dataset version and reports which of
those the two bands actually differ on, which some days is none of them. Then the same comparison for
your own submission. Both read my
[Kaggriculture Episodes](https://www.kaggle.com/datasets/georgymamarin/kaggriculture-episodes)
dataset: every finished [Kaggriculture](https://www.kaggle.com/competitions/kaggriculture)
game in full, 720 turns, both players, every action.

### Cell 2
<a id="s11"></a>
## Your submission against the ladder

The part worth forking. Put your own submission id in the cell below and you get a personal
report: where your best game lands in the whole field, and how your strategy fingerprint
compares with the record holder's. That is one farm rather than the band above, and single names
at the top turn over within hours, so treat it as a reference point. Find
your id in `episodes.csv`, or leave the default to see the record holder's own report.

Before spending a real submission slot, dry-run the agent: destbreso's
[benchmark](https://www.kaggle.com/datasets/destbreso/kaggriculture-benchmark-matchups) replays
45k recorded pairings seed for seed, and his
[Measure Your Agent](https://www.kaggle.com/code/destbreso/kaggriculture-measure-your-agent)
harness tells you what a local score can and cannot promise about the ladder.

### Cell 6
**A live report, not a snapshot.** It re-runs on a schedule with the dataset, so every number in
the text below is computed at run time. Come back tomorrow and the ladder you see will be the
ladder as it is tomorrow.

<div class="alert alert-info" style="border-left: 5px solid #2196f3; padding: 12px 16px; border-radius: 4px;">
<b>Two companions, two jobs.</b> This one is about the data and the state of the ladder. My guide
<a href="https://www.kaggle.com/code/georgymamarin/kaggriculture-visualized-what-every-crop-pays">Kaggriculture, Visualized</a>
is about the game itself, with every rule and price curve drawn out plus a starter bot. Read that
one first if the mechanics are new to you.
</div>

**Built on this data, by the community:** a [replayable benchmark](https://www.kaggle.com/datasets/destbreso/kaggriculture-benchmark-matchups) of 45k matchups with resolved seeds (CC0), an [agent-testing harness](https://www.kaggle.com/code/destbreso/kaggriculture-measure-your-agent), a [no-OOM replay reader](https://www.kaggle.com/code/lucashmateo/kaggriculture-replays-no-oom-3-dataframes), and a [research series on openings, lineages and noise](https://www.kaggle.com/code/destbreso/everyone-is-playing-the-same-opening) — by destbreso and Lucas Mateo. The dataset stopped being a solo project; this page stays its daily pulse.

### In this notebook

Above: the fresh cohort at the top of the board and your own submission against it. Below,
the season in depth.

**Part I — the data.** Know what you are standing on before you quote it.
- [1. What is in the dataset today](#s1) — size, coverage, and how fast the corpus grows

**Part II — the ladder.** Nine views of the same 30-day season, from every recorded win down to pure luck.
- [2. The ladder right now](#s2) — every recorded win on one chart
- [3. The shape of a big game](#s3) — top coin curves against a median game
- [4. Strategy fingerprints](#s4) — crew, land and crops: leaders vs the mid-ladder
- [5. What separates a big bank from a small one](#s5) — measured across every replayed game
- [6. The market they create together](#s6) — every episode's price swings, then one game up close
- [7. How fast the bar is moving](#s7) — the meta clock, and who moved this week
- [8. Who beats whom](#s8) — head-to-head win rates the ratings hide
- [9. How much of this is luck](#s9) — same bot, different games
- [10. The openings they share](#s10) — byte-identical lines, measured by stream hashes

Plus [the honest caveats](#s12) behind every chart, and the [takeaways](#s13).

**Want this for your own bot?** Fork, put your submission id in the one marked line near the top,
and the personal report reruns for you: where your best game lands in the whole field, and how
your strategy compares with the record holder's.

### Cell 7
# Part I — the data

### Cell 8
<a id="s1"></a>
## 1. What is in the dataset today

Before the strategy talk, the shape of the data itself: how much of the ladder is captured, how
deep the replay coverage goes, and how fast the corpus grows. Column-level docs live on the
[dataset page](https://www.kaggle.com/datasets/georgymamarin/kaggriculture-episodes).

### Cell 11
# Part II — the ladder

### Cell 12
<a id="s2"></a>
## 2. The ladder right now

Winners' final banks across the recorded ladder games, one dot per episode. The spread is the
story of this competition: the same board and the same rules produce farms that differ by an
order of magnitude.

### Cell 14
<a id="s3"></a>
## 3. The shape of a big game

Coin curves of the biggest wins on record against a median game. Top games share a silhouette:
the bank stays near zero deep into the season while everything is reinvested, then compounding
takes over once the farm is built.

### Cell 16
<a id="s4"></a>
## 4. Strategy fingerprints

Replays store actions, not just scores, so you can compare bots by what they do. Those
fingerprints already sit in `episode_features.csv`, one row per seat for every episode that has
a replay, and section 1 prints how deep that coverage runs, so you rarely need to open a replay
yourself. The cell below is the method behind the crew, land and crop columns; bank shape and
prices get measured in sections 3 and 6. It stays open on purpose: it defines exactly what
`peak_crew` or `first_land_day` mean, and it is where to start if you want to measure something
I did not. Leaders against the middle of the ladder:

### Cell 19
<a id="s5"></a>
## 5. What actually separates a big bank from a small one

The fingerprints above describe single games. With `episode_features.csv` we can ask the blunter
question across every replayed episode at once: which measurable choices track a large final
bank, and which ones only feel important?

One column is deliberately missing from this chart. `elbow_day` correlates with the bank at 0.8,
but it is derived from the bank itself (the day a farm crosses a tenth of its own final total),
so a weak farm crosses its small tenth early and a strong one crosses late. That is arithmetic,
not strategy, and including it would be the most confident wrong claim in this notebook.

### Cell 21
<a id="s6"></a>
## 6. The market they create together

Prices are shared between the two players of an episode, and `episode_features.csv` records
every episode's low and high for all nine goods. First the whole corpus, so you can see which
markets actually move; then one game up close, where you can watch them being moved.

### Cell 25
<a id="s7"></a>
## 7. How fast the bar is moving

The number every competitor wants: how much the ladder improves while you sleep. Median
winning bank per time slice, against the record so far. Skip a few days and this is the gap you
come back to. Below the clock: the movers, teams whose rating travelled furthest over the last
seven days of recorded games.

### Cell 28
<a id="s8"></a>
## 8. Who beats whom

Ratings compress everything into one number, and that hides the interesting part: matchups don't
have to be transitive. Head-to-head win rates between the busiest teams; read a row as the row
team's share of wins against the column team.

### Cell 30
<a id="s9"></a>
## 9. How much of this is luck

Same bot, different games: how wide is its spread? This decides how many submissions you need
before believing a result, and whether that one great game was skill or a lucky matchup.
A useful floor for reading the chart: in
[destbreso's weed-spawn ablation](https://www.kaggle.com/code/destbreso/kaggriculture-the-free-experiment-you-already-ran)
the environment alone moves a bank by a few hundred coins, while the spreads below run in the
tens of thousands. Nearly everything you see here is matchup, not dice.

### Cell 32
<a id="s10"></a>
## 10. The openings they share

Two seats with the same stream hash at turn N played byte-identical actions for N straight
turns: a shared opening is an observation, not a similarity threshold. Two honest limits, both
measured by destbreso: nothing observable differs before turn 48, so early agreement is partly
the engine's determinism rather than evidence of copying, and the full-game hash identifies the
episode rather than the agent, so lineage lives in the prefixes, never in `stream_h719` alone.
The hashes ship in the dataset's `stream_hashes.csv`, proposed by
[destbreso in the dataset discussion](https://www.kaggle.com/datasets/georgymamarin/kaggriculture-episodes/discussion/734833).
This section computes itself only when stream-hash coverage clears its 95% gate: on a partial,
time-ordered slice these rates would measure the nightly hash backfill, not the meta.

### Cell 34
<a id="s12"></a>
## Before you quote these numbers

The honest edges of this snapshot, so the charts above don't overclaim:

- Fingerprints read one best game per submission: a sketch of a strategy at its peak, not its
  average behavior.
- The corpus is a crawl, not a census. Episodes are discovered through pairings, so a brand-new
  submission can lag behind the ladder by a few hours; section 1 prints the exact replay
  coverage.
- Head-to-head cells stand on a handful of games. The count is printed inside every cell; a 100%
  built on two games is an anecdote, not a verdict.
- Spread estimates use submissions with four or more games each, a modest per-bot sample even
  on a mature ladder; treat them as order-of-magnitude.
- Daily time series mix real change with crawler drift: which submissions the crawl services
  shifts over time, so day-over-day movement partly reflects the lens, not the ladder
  (destbreso measures the split with a fixed panel of teams).
- The two banks of one episode share its market and weather and correlate at +0.73, so
  cross-episode comparisons of raw banks carry shared-world variance; within-episode margins
  are the cleaner ruler ([measured here](https://www.kaggle.com/code/destbreso/kaggriculture-what-kind-of-game-is-this)).
- A submission's consecutive games are serially correlated (matchmaking chains opponents), so
  win-rate confidence intervals built on "n independent games" are narrower than the truth;
  [Know Your Noise](https://www.kaggle.com/code/destbreso/kaggriculture-know-your-noise)
  measures by how much.
- Validation (self-play) episodes are excluded from every strength comparison; section 1 shows
  their share of the raw data.

# Source: rivals9/destbreso_x-ray-your-agent/x-ray-your-agent.ipynb

### Cell 0
The leaderboard gives your agent one number. Its replays give away everything else: whether it is a script anyone can copy verbatim, which opponents already play your exact plan, where its economy trails the leader, and whether the number under your name has even settled. This notebook reads all of it, for any submission. By default it hunts down **whoever is number one right now**, resolved at run time by climbing the live ladder, and x-rays them; **fork it and put your own id in the next cell to x-ray yourself.** Scheduled daily, this page is always the reigning king's x-ray, never a stale one.

One run answers, in order:

* **How is it doing?** The win-loss-tie ledger and the margin of every episode, in play order.
* **What does it actually play?** The stripe panels: one plan or several, and where it deviates from its own mode.
* **What kind of agent is it?** Pure replay, script with repairs, shop router, or live policy, classified globally and within each world so routing is not mistaken for reactivity.
* **Who have you been playing?** The kinship spectrum: which opponents run your exact lineage, which are siblings, and whether mirrors are finding you.
* **What did your economy do?** Land timing, herd, care, endgame hygiene and money by day, each against the measured shape of the leader.
* **Can the rating be quoted yet?** Drift per episode, sign flips, and a verdict with its threshold stated.

No API token and no attached data: the episode list comes from the competition's public episode service and the replays from the public CDN (the fork needs the notebook's Internet toggle, which ships on here and which Kaggle gates behind phone verification), the same route [georgymamarin's kaggriculture-episodes dataset](https://www.kaggle.com/datasets/georgymamarin/kaggriculture-episodes) crawls nightly, credit to his scraper for the endpoint. Fetching is the slow part, about 25 MB per replay, so the default caps at 40 episodes and a run takes a few minutes.

The view behind it is the stripe texture I have used to read other people's agents for weeks ([a DNA test for agents](https://www.kaggle.com/code/destbreso/a-dna-test-for-agents), [a week-four X-ray of the top twelve](https://www.kaggle.com/code/destbreso/a-week-four-x-ray-of-the-top-twelve)): one row per real episode, one column per turn, three colors:

* **green** where the episode plays its submission's own modal action at that turn,
* **amber** where only the market channel differs,
* **navy** where the plan itself (farmer or hands) differs.

The first run against my own live agent found **four opponents running my exact lineage**, three of them action-identical on all 719 turns, an endgame stranding **sixty times less money at the bell than the leader tolerates**, and a rating still moving at 1.3 points a game, which by my own threshold is not yet a number worth quoting. One run.

### Cell 1
## 1. The submission and its ledger

Put a submission id below, or leave "KING" to read today's number one. The listing alone already answers the first questions: how many games, the win-loss-tie ledger, and the margin of every episode in play order.

**How to read the bars.** Runs of one color are the interesting part: a green streak is a band or a world the agent owns, a red streak says the matchmaker found its level. Short red bars clustered near zero are close losses, the kind one small improvement flips wholesale; a single deep red spike among greens is one world or one rival, and section 1b below will name which.


### Cell 7
### 1b. The ledger, split by world and rival strength

One number per submission is what the leaderboard gives; one number per EPISODE is still blind to structure. This table splits every game two ways at once: the WORLD (the two town shops revealed, which fix what the season can sell) down the rows, and the rival's rating band at the moment of the game across the columns. Each cell is wins/games.

Two things to read in it. **Across**: if the win rate decays smoothly with band, the agent has a ceiling inside the sampled range; if it stays flat, its ceiling is above every band it met. **Down**: the weak rows are where the agent bleeds, and they are usually few and specific: a route that never learned one world's demand. The weak-row list is printed under the table.

### Cell 9
## 2. The stripes

The stripe matrix compares every episode against the submission's own mode, turn by turn. Order inside the market list is meaningful in this game (orders settle index by index), so it is compared as a sequence, never sorted away.

### Cell 12
## 3. How to read the panels

The chart comes twice, because two orderings answer two different questions.

A **WORLD** here is the ordered pair of the FIRST TWO town shops the episode revealed, at turns 72 and 144. The town keeps unlocking a shop every three days, up to nine in a season, so two is not a magic number and deserves its justification:

* **Timing against sunk cost.** Land, herd and construction commit in the first week, so a shop revealed on day 3 or 6 can still steer them; one revealed on day 9 or later meets a farm that is mostly committed.
* **The marginal is measured, not assumed.** The strongest public router conditions on exactly these two, and its author priced the second branch at **+0.136 points of rating per game** over his own 24,000-game census.
* **Each further branch multiplies the space by eight.** Two shops make 64 worlds, three make 512, and the episodes available to validate a plan per world collapse accordingly.

Whether a third branch pays is **an open question, not a settled no**.

* The **first panel** groups rows by world, white lines between worlds, so route structure reads as blocks instead of noise.
* The **second panel** puts the same rows in play order, oldest at the top: the view where TIME shows, a submission that changed behaviour mid-life, a mirror population arriving, or matchmaking walking you into a different neighbourhood of opponents.

How to read what you got.

A solid green panel is a pure replay: the submission plays the same recorded game every time, and everything it will ever do is already public in its first episode.

A green panel with amber columns is a script with repairs: one plan, and a market channel that answers the day. Most of the field looks like this.

A green opening that forks into navy blocks at turns 72 or 144 is a shop router: the plan itself is chosen by which shops the town revealed, and each block is one world's route. The white lines separate shop pairs precisely so this reads as structure instead of noise.

A panel that goes navy as the season ages, inside the same shop pair, is a live policy: the plan itself responds to the opponent, and no single recording of it tells you what it will do next time.

### Cell 13
## 4. Classification

The texture has a name, and one number lies about a router, so I classify twice.

**GLOBAL** compares all episodes together. **WITHIN-WORLD** groups episodes by the shop pair the town actually revealed and compares only inside each group. A shop router forks its plan at turns 72 and 144 with the draw, so it reads as wildly adaptive globally while each world's games are near-identical. A genuinely live policy diverges inside a world too. **The gap between the two readings is the diagnosis.**

**How to read the chart.** One bar per world, its height the variation INSIDE that world's episodes. Low bars everywhere with a high global reading is the shop-router signature: the agent forks with the town draw and nothing else. One tall bar among low ones marks the world where the plan actually moves: either the one live branch the agent has, or an opponent there forcing it off script, and the difference is worth chasing in section 12.


### Cell 15
What each class means for the agent you are looking at.

* **PURE_REPLAY**: byte-identical streams. Everything this submission will ever do is already public in its first episode, and anyone can replay it verbatim.
* **REPAIRING_SCRIPT**: one plan, small localised differences, usually market-only. Most of the field looks like this, and the plan half is still harvestable.
* **ADAPTIVE**: the plan itself moves between episodes of the SAME world. A recording of it answered one opponent and one seed, and replaying it plays a game it never played.

One honest limit: two episodes differ both because the agent reacted and because the seed differs, and streams alone cannot fully separate the two. That is exactly why the within-world grouping exists, it removes the largest seed effect there is, the shop draw, before reading anything as reactivity.

### Cell 16
## 5. Kinship with the opponents

A duel leaves both streams in the replay, so the same download that x-rayed you also holds every opponent you faced, and kinship between agents is measurable from actions alone.

Three numbers per opponent:

* **PLAN agreement**, the fraction of turns where farmer and hands are identical, finds the family: shared chassis, shared notebook, shared route.
* **WHOLE agreement** adds the market channel, and 1.000 there means you two played the same recorded game.
* **The BARCODE** is thirty per-day signatures of the plan channel over hours 1 to 4 of each day, the resynchronisation anchor this engine gives every morning, and the first differing band localises WHERE two related routes fork, to the day.

An opponent at plan 1.000 is **your mirror**: it runs your exact lineage, and everything you will do is as public to it as its play is to you. High plan with a low whole is a sibling that changed only its selling. Agreement confined to the first two or three days is not kinship at all, nothing observable differs before turn 48 in this game, so every agent agrees at dawn.

**How to read the spectrum.** Points at 1.000 on WHOLE are your own copies met in the wild: exact ties come from these. A cluster high on PLAN but low on WHOLE is the telling one: same chassis, different market layer, which makes them your closest predators and prey at once. Points low on both are original opposition, and if most of the chart sits there, your lineage is rare where you play.


### Cell 18
And the opponents themselves fall into **genetic groups**. Two rivals from different worlds can still share a lineage, they just fork at the shop branches, so I group them by plan agreement over the OPENING window, the turns before the second branch at t=144, at a 0.98 threshold: connected components of "plays the same opening". Per group, the statistics that matter in a duel: how often you met it, the record against it, and the margins.

The group your own lineage belongs to is marked. A large group with a negative median margin is a population problem, not a bad day; a group you only tie is your own chassis looking back at you.

**How to read it.** Size of the amber group first: large means your lineage is crowded, and mirror games with ties are structural, not bad luck. Then the record columns per group: a foreign group you consistently lose to is a targeting list of one entry, and the margins column says whether the gap is a defect or a class difference.


### Cell 20
## 6. The macroeconomic x-ray

The stripes show WHAT you play; the macroeconomic x-ray shows what your economy DID. When the second quadrant arrived, how much CARE the herd got, whether the endgame left tiles fallow and stock stranded at the bell, and how money accumulated day by day, one line per episode.

The reference column is the shape of the number one **as of my 2026-08-30 capture**, measured in [my macroeconomic x-ray of the meta](https://www.kaggle.com/code/destbreso/a-macroeconomic-x-ray-of-the-kaggriculture-meta), and a rank is a timestamp, not a property, so re-read it there if you are far from that date: second quadrant on **day 5**, **seven cows**, about **280 CARE actions**, and it leaves **13 tiles fallow** late and **442 dollars stranded**, so those two are not targets, they are what the strongest agent happens to tolerate.

**How to read the money lines.** A tight braid of lines is a world-independent economy; a wide fan says the season's worth depends on the draw. Kinks in the first two days are financing loops (buy-sell pairs), long plateaus are production waiting for demand, and the late hockey stick is endgame liquidation. Where the orange median crosses the blue is the day your economy starts leading or trailing the leader's, and the macro table above says which line item did it.


### Cell 22
And the same farm indicators as DISTRIBUTIONS rather than points, one dot per episode, jittered, alpha so concentration reads as density. The blue cloud is the leader of my 2026-08-30 macroeconomic x-ray capture, one dot per each of its 245 real episodes, embedded here so the chart works without extra downloads; the orange cloud is the submission you are reading. Everything is a multiple of the leader median for that row, the vertical line at 1, and the thick tick above each cloud is that side's median. A row where your cloud is missing means your agent never did the thing, which for the third quadrant is itself a reading.

The **fourth quadrant** row is new, and most agents will leave it empty. I added it because the line is being played: in a census of public replays I ran on 2026-09-10, an agent in the top thirty unlocks the fourth quadrant in 12 percent of its games, always on **day 18**, and always plants exactly ten tiles of it with tomato. That is the dashed tick on the row. There is no blue cloud there because the agent I measured on 2026-08-30 never bought the fourth quadrant at all, so the row is scaled against that leader's third-quadrant day and the three quadrant rows share one axis.

Worth knowing before you copy the idea: in the games I measured, the program leaves nothing stranded and costs about **12 percent of a season's worker-turns**, and its owner's own bank does not move. Its margin is better in those games, but that is the opponent banking less, on five firings, and the trigger fires when cash allows, which is also when a game is already going well. So the row is an instrument, not a recommendation.

### Cell 24
### Actions on money, and the craters under the rival

The bank curve above says *when* the money arrived. This chart says **what was done to make it move**, on the single most decisive episode of the sample (the largest margin either way): both money curves, every market order as a marker **sized by its dollar weight** (circle sell, square structural purchase, triangle other), so the buys that financed the season and the sells that paid for them sit on the curve they moved.

And the market is shared, so a sell is also a **weapon**. When one side dumps a product the book reprices it for both. A shaded span marks a **crater**: one side's large sell drops a product's price and the other side sells the same product into the depressed window within a day. **Red: the rival sold into our crater. Blue: we sold into theirs.** The damage figure is first-order, victim quantity times the price drop they ate, so read it as the size of the hole rather than as a causal transfer. The lower panel shows the price paths of exactly the products the craters touched.


### Cell 26
## 7. How the board is used

Everything above reads a farm as a **bag**: how many tiles of wheat, how many animals, how much banked. The farm is a **10x10 grid** and the engine charges for distance, so *where* a thing sits is a decision that a bag cannot see.

Two maps, and two controls that decide whether either is worth reading.

**Occupancy** is what stands on a cell, per turn. **Presence** is where the farmer and the hands actually are. The season is split into three ten-day panels beside the whole-season map, because an opening board and an endgame board are different animals.

**A heat map always looks structured to the eye**, so neither is reported without:

- a **chi-square against uniform** over the cells that were ever unlocked, and the share of the mass in the ten busiest cells against the share a flat board would give;
- a **half-split correlation**: the episodes are dealt alternately into two piles and the two maps compared. A map whose halves disagree is one season's noise wearing a label.

**How to read the maps.** Occupancy hugging the shed is a carry-cheap layout; occupancy far from it taxes every haul. Presence that mirrors occupancy means the crew works where things stand; presence smeared across empty cells is walking. In the third panel (days 20-30), an emptying ring around the center is normal endgame fallow, while an emptying CENTER says the layout is being abandoned early.


### Cell 28
## 8. Productivity in time, against the leader's own band

Every unit-turn goes into exactly one of four buckets: **work** (plant, water, harvest, feed, care, fertilize, dig, build), **carry** (pickup, place, drop), **move** (the four compass steps) and **idle** (PASS). The buckets are exhaustive on purpose, and anything the engine emits that is not in them is printed rather than dropped, so a new verb announces itself instead of disappearing into a rounding error.

The comparison is against **today's number one, as a band rather than a line**. One agent's season is one sample, and a baseline drawn as a single line invites reading normal variation as a difference. The band is the 10th to 90th percentile of the leader's own episodes, per day. Every day your curve leaves it is circled.

**Read `move` before calling anything wasted.** Measured on 40 episodes of a leader against 40 of a mid-table agent, the leader spent **53.8 % of all its unit-turns walking and 3.8 % standing still**, against 42.9 % and 11.8 % for the other. The ten points of movement the weaker agent did not spend came back as idling in place. Movement is the cost of reaching a wide board; PASS is the thing with nothing on the other side of it.

**How to read it.** Idle rising before day 28 while work exists is the unbought-complement signature: freed hands with nothing queued. A carry share sitting above the leader band is the board layout taxing the season, and the map in section 7 usually shows where.


### Cell 30
### Staffing in time, against the rivals you actually met

The field agrees on hiring more than on anything else it does. Measured over **490 seat-seasons** (both seats of 245 full replays, many distinct teams), the interquartile spread of hands-on-the-board is **0-2 hands on every day of the season**: four hands to day 4, a ramp through 8 to eleven by day 10, and **twelve from day 13 to the bell**. A consensus that tight is a heuristic bound: a staffing curve outside it is a claim that needs evidence, not a style.

The band here is built from the **rivals these very episodes were played against**, so it is the consensus of the field you actually met. Days where your median leaves the band are circled.


### Cell 32
## 9. Convergence

Before quoting the rating this submission holds, ask whether the number has stopped moving, and measure that in the only unit that works here: **the EPISODE, never the minute**. The leaderboard updates in batches, so dividing by wall-clock time counts minutes in which nothing happened; I have watched a per-hour average say a rating was crawling while per-episode sampling showed it climbing six points a game.

Three numbers together, never one:

* **DRIFT**, the mean rating change per new episode over the recent window.
* **SIGN FLIPS**, how often consecutive per-episode deltas change direction.
* **n**, the episodes played. Warming up is drift above the threshold with no flips, the number still travelling one way and misstating the agent. Settled is drift at or below the threshold with at least one flip. The threshold is a decision, not a constant: one point per episode here, stated with the verdict, and **a verdict quoted without its threshold is not a verdict**.

The pairing rate is its own diagnostic, and it is **not part of the verdict on purpose**. The matchmaker sets how often you play by its own placement uncertainty, so a fresh or badly placed submission gets paired hard and a settled one cools down: the rate chart usually starts hot and decays, and a falling rate is itself evidence the system thinks it knows where you belong. The drift is measured per EPISODE precisely so the verdict does not depend on that schedule; weighting convergence by frequency would re-import the wall-clock error this section exists to avoid. What frequency is for is the calendar: episodes-to-settle divided by the current rate is how long to wait before reading the number again, and I print that conversion below.

The rating curve is colored by its own speed, the rolling per-episode |drift|: **warm stretches are above the threshold and still travelling, cool stretches are below it and settling**, so each moment of the curve declares its regime at a glance.

**And the pairing-rate chart underneath**: pairing decays when a sibling submission arrives (the newer one suppresses the older) and stops at eviction. A cliff with no sibling and no eviction is the scheduler breathing, not your agent failing.


### Cell 34
## 10. The report

Everything above in one block, the exact format my local instrument writes to **report.txt**: ledger, texture, classification, worlds, kinship, macro profile and convergence, ready to paste or diff.

### Cell 36
## 11. Which language does your agent speak?

One more axis, complementary to section 4: instead of asking how much your agent varies within one world, ask how much of its play repeats ACROSS its own games. Treat turns as utterances and runs of five consecutive non-empty turns as phrases; drop movement (phonetics), quantities (sizing) and empty turns; then, per day band, measure the median share of an episode's phrases that recur in at least half of the agent's other episodes. A frozen script reads 1.0 everywhere, an agent that composes per game reads near 0.0, and a brancher holds a trunk and then melts.

Calibration, measured 2026-09-04 on public replays: four field tapes read 1.00 / 0.91-1.00 / 0.74-0.91 across days 6-11 / 12-19 / 20-29; カワシギ reads 0.89 / 0.15 / 0.00 (branches, then composes); keiz 0.75 / 0.00 / 0.00 (a trunk, then melts); tetsuya & yuanzhe zhou 0.02 / 0.00 / 0.00 and Crop Dusta 0.00 / 0.00 / 0.00 (composed per game). Blind validation: on eight episodes of an agent I had reverse engineered by hand beforehand, this cross-episode machinery recovered all seven known branch turns at exact precision with zero misses and zero false alarms.

The derivation, the anchors with their chart, a census of the current top 15 and a dated, preregistered prediction live in the companion notebook: [Which language does your agent speak?](https://www.kaggle.com/code/destbreso/which-language-does-your-agent-speak). Below, the two numbers for the submission on this page, computed from the streams already pulled.

### Cell 38
## 12. If it is a BRANCHER: its decision tree, extracted

When section 11 reads the submission as a BRANCHER, its plan is a trunk with a few readable choice points, and those can be extracted from the episodes already on this page: the turns where the games stop agreeing are the forks, a decision-stump search over what the agent could see (its money, the rival's money, every product price) names the likeliest variable at each fork, a permutation test throws out forks that any feature would separate by luck, and leave-one-out prediction says whether the tree is real. The full derivation, two ground-truth validations and the field study live in the companion notebook: [97% predictable: Extracting decision trees](https://www.kaggle.com/code/destbreso/97-predictable-extracting-decision-trees).

The cell is conditional: on a SCRIPT, SCHEDULER or MIXED read it explains itself and stands down.

### Cell 40
## 13. Caveats and credits

* **The mode is computed from the episodes shown**, so with very few episodes the mode itself is weak.
* **Nothing observable differs before turn 48** in this game, so early agreement between ANY two agents is the engine's determinism, not evidence of anything.
* **The turn convention**: the action decided at turn t is stored at steps[t + 1] of the replay, and the day is turn // 24. Use the raw index and the whole picture shifts by one turn.

If this found something odd in your agent, the follow-ups are in [a DNA test for agents](https://www.kaggle.com/code/destbreso/a-dna-test-for-agents). And the replay route I fetch from is the one [georgymamarin's dataset](https://www.kaggle.com/datasets/georgymamarin/kaggriculture-episodes) crawls nightly: vote for it, his scraper is where I learned the endpoint.

# Source: rivals9/degnonguidi_kaggriculture-utils-v1/kaggriculture-utils-v1.ipynb

### Cell 0
![Kaggriculture-Man pointing meme](attachment:kaggriculture-man-meme.png)

### Cell 1
# 🕷️ Kaggriculture-Man: Reverse-Engineering Top-Agents Meta

### A replay laboratory, an exact agent map, and one bounded market-timing intervention

<div style="background:#171a14;color:#ffffff;border:4px solid #d1a256;border-radius:14px;padding:20px 24px;margin:20px 0">
  <div style="color:#d1a256;font-size:22px;font-weight:800;letter-spacing:.04em">BEFORE YOU CONTINUE</div>
  <p><b>If this work is useful, please upvote the notebook, download the companion datasets, and leave a concrete idea or counterexample in the comments.</b></p>
  <p>I can run the same diagnostics on public agents and public replays. Add a public notebook or episode link in the comments if you want its failure points mapped.</p>
  
  <p style="margin-bottom:0"><b>This notebook combines an article, a research instrument, and a reproducible agent build.</b> The analysis cells are not required to run the submitted agent.</p>
<p style="margin-bottom:12px;">
  <b>Related parts of this research:</b>
</p>

<p style="margin-bottom:6px;">
  <b>
    This part, covering the general overview and analysis is available here:
  </b>
</p>

<a href="https://www.kaggle.com/code/leoprovorov/kaggricult-man-reverse-engineering-part-1"
   target="_blank"
   style="
     display:inline-block;
     padding:10px 16px;
     margin-bottom:18px;
     background:#20BEFF;
     color:#000000;
     font-weight:700;
     text-decoration:none;
     border-radius:6px;
   ">
   → Open Part 1: General Overview & Analysis
</a>


<p style="margin-bottom:6px;">
  <b>
    The second part, focused on the possibility of hacking the in-game store, is available here:
  </b>
</p>

<a href="https://www.kaggle.com/code/leoprovorov/god-s-mode-hacked-stores/notebook?scriptVersionId=349839124"
   target="_blank"
   style="
     display:inline-block;
     padding:10px 16px;
     margin-bottom:18px;
     background:#20BEFF;
     color:#000000;
     font-weight:700;
     text-decoration:none;
     border-radius:6px;
   ">
   → Open Part 2: Hacking the Store

</a>



      
  <p style="margin-bottom:0"><b>Enjoy!</p>

### Cell 2
## Mathematical model

Each formula is shown with its meaning and symbol definitions directly beside it.

### Cell 3
![Mathematical model](attachment:kaggriculture-mathematical-model.webp)

### Cell 4
## Why the Spider-Man meme is not just a joke

Kaggriculture is unusually open. Competitors publish strong notebooks, and everyone can watch public replays of leading agents. This makes **behavioral reverse engineering** possible: not recovering source code, but reconstructing strategy from repeated observable actions.

Every strong public release becomes a base for the next participant. If a nearly optimal agent appears openly, many competitors can reuse it. The difference between first place and the thousandth participant may then become very small, while much of the work done by the original leaders stops being visible.

That is why I suggest upvoting every notebook with substantial individual work, even when it did not produce the strongest agent. The research effort should not disappear when somebody else turns it into a stronger public baseline.

The final evaluation is still uncertain, but not because Kaggriculture has a normal hidden private test partition. The competition uses continued agent matches and a final Bradley-Terry recomputation. The real unknown is the future opponent population: which agents remain active, how the public meta converges, and which matchups dominate the post-deadline evidence. See the official [Evaluation page](https://www.kaggle.com/competitions/kaggriculture/overview/evaluation).

### Cell 5
> **Version update.** The submission is now **MarketShock-M1-WR1K**, with one audited day-21 local watering repair and exact parent pass-through everywhere else. The original experiment record below is unchanged.

## What was built

The base is a frozen Seven-Turn Rescue agent. The research layer reconstructs matches turn by turn and separates route selection from economic execution.

T4 adds one bounded mechanism. In likely mirror games it can sell selected parent-planned inventory one turn earlier. If a real probe shows that the opponent also preempts sales, the lead can become two turns. Every moved unit becomes a credit against the original sale, so the overlay cannot liquidate the same stock twice.

In three fixed worlds, lead-1 beat the untouched control in all six seat-swapped games. Adaptive lead-2 then beat lead-1 in all six. The crop-value guard added +196 in one world and exactly 0 in two, so I treat it as weak and world-specific rather than a general breakthrough.

```python
if mirror_gate_is_open and 336 <= step < 647:
    lead = 2 if counter_preemption_was_observed else 1
    for item, qty in parent_sales(step + lead):
        qty = min(qty, projected_shed[item])
        if 4 <= qty < 100 and market_order_slot_exists:
            sell_now(item, qty)
            credit_original_sale(item, qty)

parent_sale[item] -= credited_quantity[item]
```

The parent remains frozen. The intervention has a narrow gate, and every activation is logged.

### Cell 6
## The full analysis surface

These are exact full-page captures from the live research server on 10 September 2026. They are not recreated charts and they do not use synthetic values.

**Field Ledger** finds the turn where value starts leaking. **Field Skeleton** exposes the agent's actual routing graph. **Field Worlds** measures all possible shop worlds and the replay coverage of each one.

### Cell 7
## Field Ledger

One match, every economic layer: projected score, trend, market execution, revenue, spending, free cash, idle hands, planted value, and the final harvest book.

![Field Ledger](attachment:field-ledger.webp)

### Cell 8
## Field Skeleton

The actual agent map: the day-6 routing branch, observed route frequency and outcomes, route economics, and the games attached to each plan.

![Field Skeleton](attachment:field-skeleton.webp)

### Cell 9
## Field Worlds

All 64 possible shop worlds measured across 2,835 public episodes and cross-checked against the agent's own replay sample.

![Field Worlds](attachment:field-worlds.webp)

### Cell 10
## Reading the agent map

The shared opener runs until **day 6, step 144**. The agent then reads the first two unlocked shops as an ordered pair. Fourteen named pairs select ten distinct continuations; every unlisted pair falls back to plan 0. At **day 27, step 648**, every route enters plan 2 for final liquidation.

The useful unit of analysis is therefore a route inside a world, not one global win rate. The map exposes missing worlds, low-sample branches, route-specific economics, and the exact matches behind each plan.

### Cell 11
## Build the exact agent

The hidden cell writes `/kaggle/working/submission.tar.gz` and verifies the deterministic archive hash.

### Cell 13
## Continue the experiment

Upvote if you want the full toolkit and more replay studies published. Put public notebook links, episode links, and concrete mechanism ideas in the comments. For collaboration, contact me on Kaggle or [LinkedIn](https://rs.linkedin.com/in/aleksei-provorov-832050308).

# Source: rivals9/ashok205_top10-replay-dataset-archive/top10-replay-dataset-archive.ipynb

### Cell 0
# Kaggriculture Daily Top-10 Replay Archive Maintainer

This notebook has one job: maintain a compact append-only archive of official Kaggriculture daily replay data involving the ten strongest teams observed in each source day.

It does **not** use daily file ordering as a player ranking. For each official daily dataset it reads `manifest.csv`, scans only the small replay headers to recover `TeamNames`, ranks teams from that day's official rating evidence, stores full replay bodies only for the selected top-10 teams, then deletes the large temporary ZIP before processing the next day.

The attached `kaggle/kaggriculture-episodes-index` dataset is the authoritative day list and the notebook's **Data updates (once daily)** scheduling trigger.

