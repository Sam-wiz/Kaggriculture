# Mistakes log

Every error that cost real time on this competition, what it looked like, why it happened, and the
rule that now prevents it. Kept separate from `NOTES.md` (which records *findings*) because these are
**process** failures — they recur across competitions, and most of them were silent.

The common thread: **almost every one of these produced a plausible-looking number rather than an
error.** That is the thing to defend against. A crash costs an hour; a wrong number that looks right
costs a day and can send the whole strategy the wrong way.

---

## A. Silent-corruption mistakes (the expensive class)

### A1. Benchmarked on the wrong engine version for hours
A subagent's `pip install` silently downgraded `kaggle-environments` 1.32.7 → 1.32.6. The two are not
equivalent: CARROT/TOMATO/EGG use `hinge` scarcity curves in .7 and `log`/`linear` in .6, so every
price-sensitive number I had measured was wrong. Nothing errored — the benchmarks just returned
different, believable values.
**Rule:** `requirements-lock.txt` pins the engine; `harness.py` asserts the version on import. Any
agent I delegate to is told never to touch the environment. Re-verify the version before trusting a
number that disagrees with a previous measurement.

### A2. My own tuner leaked parameters between trials
The module was cached per worker and the parameter dict `P` was never reset, so trial N ran with
trial N−1's settings. Early ablations were meaningless and I had already drawn conclusions from them.
**Rule:** `load_module` snapshots pristine defaults and restores them per trial. Any tuner must prove
isolation with a null test (same config twice → bit-identical result) before its output is believed.

### A3. String-surgery edits that silently did nothing
Repeated heredoc `assert old in src` edits failed on wrong anchor text, producing unchanged files.
The ablation then "measured" the unmodified agent and reported no effect — a perfect false negative.
**Rule:** use Read+Edit tooling, not string surgery. If a script must patch text, the assert must be
fatal *and* the result diffed. Never accept "no effect" from an ablation without confirming the file
actually changed.

### A4. Name shadowing between layers → 3000-bank no-op with status DONE
The cash guard defined `ANIMAL_COST` as a dict; the underlying tape used the same name as a tuple.
Result: `KeyError: 1`, caught by a broad `except`, agent returned nothing all game, final bank exactly
the $3,000 starting cash, status `DONE`, no error surfaced.
**Rule:** every overlay namespaces its globals (`_G_ANIMAL`, `_G_SEED`, `PG`, `_gfib`). A final bank
of exactly the starting cash is a **bug signature, not a bad game** — treat it as a crash.

---

### A5. Edited a file that a running benchmark was re-reading
`harness.load_agent` re-execs the source file on every call, so a benchmark launched in the
background picks up edits **mid-run**. I patched the route selector while a 100-game benchmark was
using that file; the first games ran the old build and the rest the new one, in one averaged number.
**Rule:** copy the candidate to a frozen path and benchmark the copy. Never edit a file that a
running measurement reads.

## B. Packaging / submission mistakes

### B1. `__file__` is undefined on Kaggle
The first tar.gz submission errored with `NameError` because the bootstrap used
`os.path.dirname(os.path.abspath(__file__))`.
**Rule:** single-file submissions only; data embedded as base85+zlib. `kaggle_load_check.py` executes
the file with `__file__` deliberately absent.

### B2. Kaggle takes the LAST callable, ignoring the name `agent`
`get_last_callable` is `[v for v in env.values() if callable(v)][-1]` — insertion order, not name. My
helper `_gfib` was defined after `agent`, so Kaggle ran *that*, and the submission died with
`TypeError: 'Struct' object cannot be interpreted as an integer`.
**Worse: my own pre-flight checker gave it a false pass** because it looked up `agent` by name.
**Rule:** every file ends with `del agent; agent = _my_agent`. The checker now mirrors
`get_last_callable` exactly, errors loudly if the selected callable isn't the intended one, and
finishes with a real `kaggle_environments.make().run()`. **A checker that doesn't reproduce the
loader is worse than no checker** — it converts a loud failure into a silent one.

---

## C. Measurement-design mistakes

### C1. Compared a live agent against a frozen one
I read live `cushion` (2313, still climbing from 600) against frozen `hover` (2610) and nearly
concluded the cash guard was harmful — it was simply younger. Elo from a cold start is not comparable
to a converged rating.
**Rule:** to compare two agents on the ladder, submit **both** as the active pair so they climb under
the same conditions. Never compare a climbing rating to a settled one.

### C2. Displaced a climbing agent by submitting on top of it
Only the latest 2 submissions are matched. Submitting two new agents froze `sub_safe` mid-climb
(600 → 1948 over 17 episodes), destroying the sample I was waiting on.
**Rule:** never submit more than one new agent while an existing one is still climbing.

### C3. Trusted a saturated benchmark
`h_over` scores 54/54 against the local pool. At that point pool win-rate carries no information and
every candidate looks equally perfect.
**Rule:** once a benchmark saturates, switch to head-to-head margin against the current champion on
two disjoint seed sets. A 100% score is a signal the ruler is too short, not that the work is done.

### C4. Judged a safety layer by mean score instead of by its failure mode
The cash guard is worth ~$0 on games that were fine anyway; its entire value is removing the ~7% of
games that end at bank 0. Averages hide that completely.
**Rule:** for any layer meant to prevent a catastrophe, the metric is **catastrophe rate**, not mean.
Measure the tail you are targeting.

### C5. Assumed a trigger condition without measuring its base rate
The survival override fired on "≤2 hands" — but **every day legitimately has one 0-hand turn** at
hour 0, before the hires land. It hijacked the tape's morning turn 30 times a game and dropped the
score from 89,408 to 0.
**Rule:** before shipping a conditional override, histogram how often the condition fires in *normal*
play. The fix here was `hour >= 3`, and the proof was 32/32 bit-identical games.

---

### C6. Read a confounded A/B backwards and wrote the wrong conclusion into NOTES
Live A/B: guard 21W-4L, control 21W-5L, and the guard had zero bank-0 games. I concluded the guard
was better and that its lower Elo was a matchmaking artifact. **The opposite was true.** The guard's
opponents banked 71,029 on average; the control's banked 80,558. Similar win counts against weaker
opposition is the *worse* result. Four frozen submissions agreed (unguarded 2610/2514, guarded
2314/2271) and I had already seen those numbers.
**Rule:** never compare win/loss across arms without conditioning on opponent strength — matchmaking
guarantees the weaker arm draws weaker opponents, which manufactures a flattering record. Check the
record against every other independent signal *before* writing a conclusion down, not after.

### C7. "Bit-identical in 32/32 games" proved only that the code never ran
The cash guard is bit-identical to its base locally — because self-play never produces the cash
shortfall that triggers it. I read that as "free when not needed" and shipped it. On the ladder it
does fire, and it appears to cost ~300 rating.
**Rule:** a neutrality test only tests the code path it exercises. Before trusting a conditional
layer, confirm the trigger actually fires in the test set; if it never fires, the layer is
**unmeasured**, not safe. Count the firings as part of the test.

### C8. (Habit that worked) A too-good result got verified before it was believed
The newer public tape came back **100W-0L with the opponent on exactly 0.0 every game**. An opponent
at a round zero in 100/100 games is the signature of a crashed agent, not a beaten one, so I checked
before acting: statuses were `DONE`, errors `None`, self-play was symmetric (49k-127k a side), and a
turn-by-turn trace showed the opponent genuinely dying on day 12. The result was real — but the
check cost two minutes and would have caught a fabricated headline.
**Rule:** any result that would be the best of the day gets one falsification pass before it is
acted on — statuses/errors, a self-play sanity run, and a trace of the mechanism. This is the
counterpart to A4: exact round numbers (0, or the starting bank) are bug signatures until proven
otherwise.

### C9. Nearly shipped a tie-break artifact by switching to win-rate
Reasoning: "the ladder scores win/loss only, so a reliable +$5 win is worth as much as +$5,000."
That argument is *correct about the ladder* and *wrong about the mirror benchmark*. In the mirror the
opponent is our own build, so an unchanged candidate ties **exactly** (88-114 of 128 games were ties).
Any behavioural perturbation breaks those ties and wins ~96% of the decided games by $3-6 —
`drain_gate` 1, 3 and 5 all scored 92W-4L, in opposite directions from the shipped value.
Against a genuinely different opponent the same change was worth **−$2 ± $2**, on a margin of
+$2,766 with a stdev of $914.
**Rule:** in the mirror, score by **margin**, never win-rate — win-rate is degenerate when the
baseline is a tie. A high win rate with a negligible margin is a tie-break artifact. The ladder's
win/loss scoring is still what matters, but it is decided against *different* opponents where the
natural spread is ~$900-3,000, so only edges of that order can move it.
**Corollary:** when several settings in *opposite* directions all score identically well, that is a
signature of measuring the deviation rather than the improvement.

### C10. Two weeks of "improvements" were measured against instruments that could not see them

Ladder noise, measured directly. `sub_hover.py` and `sub_ab_control.py` are the **same file**
(md5 `0b37a0fc...`) and scored **2609.9 and 2202.9**. `sub_cushion.py` and `sub_ab_guard.py` are
also identical and scored **2314.0 and 2020.6**. Convergence explains much of both gaps (the low
scorer had 51 and 35 episodes vs 129 and 144), but among *converged* submissions of the same
family the spread is still 2271-2610.

So the whole shipped sequence -- sub_tuned +2,616, sub_slot +3,121, sub_impact +729,
sub_final +211, all "measured" in the mirror -- moved the ladder by **less than its own noise**.
Confirmed offline: against a pool of published rivals the four newtape builds score
+15,242 / +15,839 / +15,626 / +15,594 margin and 0.943-0.946 win rate. **They are the same agent.**

Three instruments, three different failures:

| instrument | why it lied |
|---|---|
| **mirror margin** (candidate vs our own build) | optimises "beats a copy of me", which is not "beats the field". Every accepted patch was worth $200-700 against ourselves and $0 against anyone else. |
| **ladder win rate** | matchmaking pairs by rating, so win rate equilibrates to ~50% regardless of strength. Ours ranked the builds *backwards*: sub_slot 79% at rating 2304, sub_tuned 35% at 2573. |
| **weak rival pool** | every member loses by 15-27k, so it cannot discriminate. It rated `h_over` best (+27,382, 100%) -- an agent that scores **exactly 0** against any aggressive opponent. |

**Rule:** before trusting any benchmark to rank candidates, check that it *can* rank them --
that its spread across known-different agents exceeds its noise, and that its opponents are
strong enough to lose to. A benchmark on which everything scores the same is measuring nothing.

### C11. The switch to the "newer tape" was justified by a crash, not by a comparison

`sub_newtape` was accepted on "100W-0L vs h_over (mean 151,985 **vs 0**)". A mean of 0 is the
signature of a dead agent, not a beaten one -- checklist item 5 says exactly this and I did not
apply it to my own result. Re-measured in the **official** environment: h_over scores 0.0 with
status DONE against every newtape build, and 75,621 against itself.

The cause is real, not a harness bug: h_over's opening ends day 0 with **exactly $0**, so the
$1 first hire on day 1 silently no-ops, it has 0 hands for two days, and the farm dies. Any
opponent whose day-0 market activity moves buy prices by a few dollars kills it.

**Rule:** a 0, or any final bank equal to starting cash, is a bug report about the *comparison*,
not a win. Re-run it in the official environment before it decides anything.

### C12. Inferred a causal lever from an observational difference between two different agents

Tracing 69 losses showed our herd frozen at 8 SHEEP / 9 COW in every draw while opponents shifted to
12/6 as YARN_STOREs unlocked, with margin falling -1,412 -> -16,062 -> -19,652 as the count rose.
COW and SHEEP share PASTURE, so swapping looked free, and the correlation was strong and monotone.

Measured, it is **-7,758 on exactly the high-yarn seeds it was designed for** and -2,564 on random
seeds. The swap fires correctly (herd goes 5/12, matching the opponents), so this is not a trigger
bug -- the lever itself is wrong.

The mechanism: the shed caps at 100 and overflow is discarded, so the extra wool was destroyed on
arrival. Wool *sold* went DOWN 196 -> 191 while milk collapsed 261 -> 157.

**Rule:** a behavioural difference between two agents that win differently is not a lever you can
transplant. The opponents build their whole schedule around a bigger flock from turn 0; copying the
purchase without the schedule copies the cost and none of the benefit. Before building any fix
derived this way, ask what *else* has to be true for it to pay -- and check the binding constraint
(here, shed capacity and a fixed sell schedule) before the input.

### C13. Reading decay into regression from a remembered peak

A converged agent that had been seen at ~2650 was sitting at 2598 and looked like it was
"depleting". But the peak of a noisy series always sits above its mean, so drifting down from an
observed maximum is the expected shape, not decay. On this ladder `sub_final` moved 2437.4 -> 2421.8
while **frozen and playing nothing**, and two byte-identical files scored 2609.9 and 2202.9 (C10).
A 50-point move is inside the instrument. The tell that it was noise: the sibling submission moved
*up* 29 points over the same window.

**Rule:** compare against the noise floor and against a sibling, never against the best number you
remember seeing.

### C14. A ported layer threw on 714 of 719 turns and looked like a working null result

Porting the h_over market-model sell overlay onto the router produced small positive deltas and
loaded cleanly. Instrumenting it showed **714 NameErrors across 719 turns**: two lookup tables
(`_OV_CROPS`, `_OV_ANIMALS`) sat just above the extraction boundary, so the overlay raised on almost
every turn and both `except Exception` layers silently degraded it to the bare route. The deltas
were the slot/vent layers underneath it.

Those `except` blocks are correct in a submission -- a crash forfeits the game -- and lethal in a
benchmark, because **a layer that throws every turn is indistinguishable from a layer that decided
to do nothing.** Had I benchmarked it as-is I would have concluded "the market model does not
transfer to the router", which is the conclusion the fixed version also reaches, by a completely
different and wrong route -- and I would have believed it for the wrong reason.

**Rule:** any layer wrapped in `except Exception` must be instrumented before it is measured. Count
turns entered, turns that changed the action, and exceptions raised, and require all three to be
consistent with the intended behaviour. "It ran and the number moved a little" is not evidence the
layer ran.

### C15. Three wrong explanations for one failure, because nobody counted the animals

The cow->sheep swap lost 7,758 in the games it targeted. I explained it as shed overflow ("the extra
wool is discarded"). Three external reviewers explained it as the tape's fixed sell quantities being
unable to order the surplus. Both were wrong, and both were plausible enough that two rounds of work
were built on them.

Counting the animals actually standing in the pasture at the end:

| | sheep alive | cows alive |
|---|---|---|
| base | 8 | 9 |
| swap | **8** | **5** |

**The swapped purchases never became living sheep.** The variant destroyed four cows and created
nothing. That alone is the whole -7,758; the shed and the sell schedule are irrelevant to it.

What made the wrong explanations survive: every downstream number was consistent with them. Wool
sold did fall (196 -> 191). The shed did pin at 100 for six days. Discards did rise (4.5 -> 7.5).
All true, all effects of having fewer animals, none of them the cause.

**Rule:** when an intervention changes what the agent BUYS, verify the thing was actually acquired
before explaining the outcome. Count the entity, not its downstream traces. One `on_step` that
counts animals on tiles would have ended this in ten minutes, two rounds of reviews ago.

### C16. I quoted a power figure that was wrong by a factor of twenty

I repeatedly wrote that a +277 improvement is "undetectable against a per-game sigma of ~6,000",
and used it to argue our overlays could never matter. Measured on 360 paired cells:

| | mean | sd |
|---|---|---|
| unpaired margin | +4,213 | 8,094 |
| **paired difference** (same seed, opponent, seat) | **+279** | **373** |

Pairing removes **99.8% of the variance**. A +277 effect needs ~14 paired cells, not thousands; our
holdout ran at effect/SE = 14.2. The sigma-6,000 figure describes the LADDER, where games are
unpaired and opponents vary — there a +277 shift is worth roughly 1.4% win rate. Both facts are
true; I had been quoting the ladder number to dismiss offline results.

**Rule:** state which design a variance figure belongs to. An unpaired sigma says nothing about the
power of a paired benchmark.

## D. Modelling mistakes

### D1. DROP↔PICKUP infinite loop burning 48% of all actions
`shed_supply` dropped goods a unit then immediately picked them back up. Cost was invisible because
the agent still "worked" — it just did half as much. Removing mid-day DROP: $70k → $99k.
**Rule:** profile the action histogram of any agent. If a single op pair dominates, it is a loop.

### D2. Built a from-scratch agent for weeks before measuring it against the real pool
`v22` reached ~$112k against the starter and went **0/72** against actual rivals. Beating a weak
reference measures nothing.
**Rule:** benchmark against the strongest available opponent from day one. Absolute score against a
punching bag is not evidence.

---

## E. Standing checklist (run before every submission)

1. `.venv/bin/python kaggle_load_check.py <file>` — passes, and names the intended callable.
2. Engine version is 1.32.7 (`requirements-lock.txt`).
3. New layer is **bit-identical** to its base on ≥32 seeds of normal play.
4. New layer's **target failure mode** measurably improves (rate, not mean).
5. A final bank equal to the starting cash anywhere in testing = crash, investigate.
6. Not displacing an agent that is still climbing.
7. Head-to-head vs the current champion on two disjoint seed sets, not pool win-rate.
8. The benchmark's opponents must be strong enough to beat us sometimes. If every opponent
   loses by a wide margin, the benchmark cannot rank candidates (C10).
9. Any opponent scoring 0 or exactly the starting cash invalidates the comparison (C11).
10. Instrument any `except Exception`-wrapped layer and confirm it fires without raising (C14).
11. Re-check for newer public tapes before tuning the current one -- every real gain we have
    made came from a better base, never from tuning (683 -> 2513 -> 2610 -> router).

## C17 - Predicted a broken instrument, found a working one (2026-09-21)

I argued the mirror overlay's 0.225 score was an artifact: it moves HIRE orders behind SELLs and
truncates to 10 slots, and pipe16 is hire-sensitive. I was confident enough to call the earlier
result a misread. Instrumented it: hires 278 vs 278, orders 863 vs 863, max slots exactly 10 -- the
truncation is unreachable and hiring is untouched. The original measurement was right.

The tell I ignored: a -73 margin on 121k is not what a disabled subsystem looks like. Losing your
hiring would cost thousands, not 0.06%. I had the magnitude in front of me and reached for the
dramatic mechanism anyway.

C10-C16 were cases of trusting a broken tool. This is the mirror failure -- distrusting a sound one
because a dramatic mechanism was available. The fix is the same either way: measure the mechanism
(count the hires) before re-litigating the conclusion, and check that the effect SIZE matches the
mechanism you are proposing.

## C18 - Trusted an open-loop replay gate for a market-timing agent (2026-09-25)

Replay-substitution (opponent's recorded actions replayed, only our seat swapped) reproduced
recorded games to the dollar, so I treated it as a validated instrument and submitted two agents on
it (shepherd: predicted WR 0.656 vs >=2200 opponents, z=3.28). Live: 0.27 vs 2200-2400, 0.15 vs
2400+. Reproducing the recorded game only proves the replay is faithful for the RECORDED agent. It
says nothing about how a frozen opponent differs from a reactive one once our actions change, and
nothing about whether the recorded opponents still exist. Validate an instrument on the thing it is
used to decide: a candidate that CHANGES the market interaction, checked against a later live read,
before letting it gate submissions.
