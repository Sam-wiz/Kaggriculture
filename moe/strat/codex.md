The most credible path is **recover a trustworthy contemporary baseline, then improve the conversion of existing production into money**. It is not a five-day rewrite. A durable 3k agent is a low-probability outcome from the evidence available. If exact pipe16 still performs around 2700–2800, the two build experts have plausible mechanisms to investigate the remaining gap. If it settles around 1900–2200 against contemporary opposition, neither proposed patch is evidence of a solution to the much larger deficit.

This is an independent strategy assessment as of the supplied September 25 snapshot. I read the full strategy brief, HANDOFF and falsifications, MISTAKES, the build brief and both build experts' notes, relevant discussion threads across Versions 1–5, and the underlying measurement code and artifacts. I recalculated statistics from existing JSON; I ran no simulations, contacted no Kaggle API, and made no submission. The candidate holdout was still pending when checked. Only this file was written.

**1. Diagnosis: there are three different gaps, and they must not be added together.**

First, the recent deterioration is unresolved. The 50-submission history summarized in [HANDOFF, 09-25f](../../HANDOFF.md) puts the break at the addition of reclaim and subsequent layers, contemporaneous with field change. I verified that `subK_pipe16.py` has the reported MD5 `d74874abc7e6c826ca711c91169656fa`. `subK2_pipe16.py` differs only by a trailing resubmission comment; their parsed Python syntax trees are identical. Thus ref **56547613** is a valid policy control. The historical 2787 is not an established September 25 baseline, and the 2843 peak is even less useful for sizing the current gap. I verified the local control equivalence, not an independently downloaded copy of the historical submission or the complete 50-row export.

A high contemporary control rating would support regression in our subsequent stack. A low control rating would support deterioration of the baseline's position in the field. Neither observation alone proves an exclusive explanation: regression, matchmaking history, and field drift can coexist. In particular, removing a demonstrated reclaim bug does not establish that reclaim caused the entire 600–900-point historical difference.

Second, **our attainable, well-observed weakness is narrow losses within the public lineage**. Recalculation of [pergame_band.json](../opus/pergame_band.json) gives 197 unique episodes against 169 teams: **79 wins, 118 losses, no ties**. There are 74 losses within $1000; eight losses below −$5000 carry 51.5% of the aggregate loss deficit. The median of all margins is −$207; the median *loss* is **−$708**, not −$200. The brief's approximately $200 figure describes a narrower near-clone comparison, not all losses.

The existing [ledger](../opus/ledger_band.json) records exact reward reproduction for 197/197 episodes. Reaggregating it gives harvested wheat 555.1 versus 554.7 units/game, hires 274.50 versus 274.35, and closely matching herd purchases. That supports a delivery/price-capture diagnosis for this corpus. It does not mean every strong opponent has our production policy. The corpus pools eight builds, contains only **seven sir-V1 games**, and contains **no vanilla pipe16 games**.

There is another qualification: [index_eps.py](../opus/index_eps.py) assigns opponent strength using `lb_now.json`, joined by **team name**. Consequently “2400–2900” means the team's snapshot rating, not necessarily the particular opposing submission's rating when it played. Use these games to identify mechanisms; do not treat their pooled win rate as a calibrated contemporary strength estimate. Matching the same team across dates is weaker than matching the same opposing submission in the same period.

The reclaim defect is unusually credible because it has a traced causal mechanism. It converts unpayable CARE into PASS while the sheep controller continues requesting CARE; workers stop advancing to delivery. [Codex's development artifacts](../codex/trace_analysis.json) show capture improving margin by **$944 versus koshinm**, 10–2 rather than baseline 6–6, and by $412 versus f55rec-V2, where both baseline and candidate already win 12–0. Each matchup uses only six seeds in both seats. On the inspected seed, equal production accompanies a large reversal in wool receipts. The engine source also confirms that production pays before that day's new care bonus is banked. This is evidence for correcting execution, not evidence for copying a different route-2 tape; the decoded routes are identical.

Third, **the historical top-tier gap is coordinated economic planning**. The September 21 top-11 observations and pig7selene's cached `experiments/where_the_gap_is.md` describe different production timing, herd commitments and crop choices. Its 1.01–1.02 versus 0.61 premium-price indices are observational comparisons of different policies and markets, not a 65% revenue improvement available from an order permutation. Its full timeline also records failed crop substitutions, failed corrective trajectory replay, and failed extra-worker schemes. Our own HANDOFF records the same failures and the from-scratch executor's competitive collapse. Roman-class opponents demonstrate another direction—continuous conversion of staples—but buy/sell volume is not profit, and wheat/fertilizer round trips have no free arbitrage. These observations motivate coordinated replanning; they do not license another herd swap, crop graft, rescue layer, or route refit.

The forum evidence is consistent with this distinction. V2's sobameshi reports a much weaker runtime agent despite substantial work, and V1's RL report describes 350 million environment steps without competitive convergence. V3's Le Quang Cảnh shows how copied lineage performance settles below its source's old score. V4 documents private strong agents being withdrawn. The sharing lock does not freeze opponents' private development. None of these establishes a mathematical 2800 ceiling for tapes, but together they argue against budgeting a competitive new architecture in five days. See [discussions.md](../../discussions.md).

To quantify the task, under the brief's approximate normal performance model, `P(win) = Phi(gap / (sqrt(2) * 200))`:

| Assumed current baseline | Required improvement | Approximate head-to-head win probability |
|---|---:|---:|
| 2787 → today's supplied 2940 cutoff | +153 | 70.6% |
| 2787 → 3000 | +213 | 77.4% |
| 2500 → 3000 | +500 | 96.1% |
| 2000 → 3000 | +1000 | 99.98% |

These are scale illustrations, not forecasts or the final Bradley–Terry scoring formula. Intransitivity and a changing opponent population invalidate a literal translation from a public-agent matchup to live rating. Beating an ancestor 60% is only about +72 points even under this simplifying model, not proof of +200.

**2. Ranked plan: three moves, with explicit stop conditions.**

All rating ranges below are judgmental planning estimates, not measured results. Recovery of lost strength and improvement beyond pipe16 are different quantities. The ranges are not additive.

| Priority and move | Expected rating effect | Confidence | Work allocation | Offline-only risk |
|---|---|---|---|---|
| 1. Finish the existing live control and repair the comparison | Measurement itself: 0. If regression dominates, perhaps recover 300–800 relative to the recent weak builds; no demonstrated gain above old pipe16 | High value of information; low confidence in amount recovered | 0.25–0.5 analyst day, plus passive live observation | Low if contemporaneous submissions are compared; high if old frozen ratings are reused |
| 2. Validate the smallest delivery/CARE correction | Budget 0–100 points over an affected layered parent; 100–150 is an optimistic outcome. Gain over clean pipe16 is unmeasured | High confidence in the local defect; low-to-medium in field transfer | 0.5–1 day using the build expert's existing candidate and traces | Medium-to-high: development opponent and selected failure mode are close relatives |
| 3. Test opponent-aware same-turn SELL ordering, only if an oracle shows worthwhile headroom | Budget 0–75 additional points; +150–200 is a low-probability upside requiring much stronger field evidence | Low; a falsifiable hypothesis, not a discovered edge | 0.5 day to bound it; at most another 1 day if the bound survives | High: prediction errors, quantities and existing wrappers can erase the apparent race advantage |

For **move 1**, hold `[sir_V2 56547525, pipe16 56547613]`. Record completed episodes, opponent submission IDs, date, seat, outcome, and available pre-game ratings. Use the same time window for both arms. Check software errors and the demonstrated delivery failure separately from rating. Assess performance by opponent class and shared opponents where available; retain uncertainty where the samples do not overlap. Do not interpret raw overall win rate as agent strength.

Within 24 hours, a substantial positive opponent-adjusted separation and a control climbing toward 2500+ would favor the regression explanation. Similar low performance against comparable opponents would weaken the hypothesis that reverting layers alone restores the old level. The **2700–2800** branch is what makes the three-thousand target plausible; a recovery merely to 2500 still leaves a much larger problem. If there are too few informative episodes, the correct result is “unresolved,” not another upload. Aim for roughly 80–120 total episodes and 20–30 against relevant stronger opposition before a firm interpretation, while checking actual drift rather than assuming those counts guarantee convergence.

For **move 2**, use the ongoing capture gate as the first screen. Isolate the CARE correction from same-turn projected-stock selling and empty-slot compaction, so the decision does not depend on a bundled result. Compare with its actual sir parent **and clean pipe16**, not just the filenames marked LIVE in `moe/gate.py`: that file's default LIVE labels refer to an earlier pair and omit vanilla pipe16. A correction to a bug we introduced can recover the ancestor's behavior without exceeding it.

The 24-hour confirmation is: the controller advances in reproduced live failure states; its pre-intervention behavior remains identical; CARE that can still pay remains intact; and an untouched-seed comparison improves win outcomes against several relevant families without introducing failures elsewhere. Record eligible games and changed turns, not just total calls. The kill condition is no gain outside koshinm/affected mirrors, a regression against clean pipe16, or gains caused by another change in the bundle. The fresh gate is still pending, so **capture is not submit-worthy on present evidence**.

For **move 3**, the new evidence warranting a narrowly defined retry is the build expert's reported native-order agreement and explicit SELL-index races. It differs from the previously failed selector that modeled opponent supply as a generic +1 inventory pressure. But **88% relative-order agreement is not 88% accuracy for the opponent's next full queue, quantities, or available stock**. The agreement script compares realized lists across games; it is not yet a validated online forecast.

First calculate an **exact one-turn diagnostic oracle** on original replay states: preserve our order quantities and non-SELL indices, enumerate feasible SELL-slot permutations, and score realized relative cash under the recorded opposing queue with the engine's actual lockstep rules. The recorded opposing action is permissible for this offline ceiling calculation, never as an agent input. Apply it to wins as well as losses. Do not add independent per-turn oracle gains and call the sum a realizable season result.

If that diagnostic shows useful headroom, test a causal predictor using only information available before acting: native-list and SIR-list hypotheses, public farm state and past inferred fills. Require an improvement robust to plausible rival quantities, preserve the baseline choice under uncertainty, and measure full rollouts. Do not defer sales to a drain tick, reorder buys, or change production to make the hypothesis work; those are separately falsified interventions.

Within 24 hours, require evidence that the oracle can affect outcomes across a material fraction of distinct opponents, then that the causal rule retains a meaningful portion. My proposed continuation threshold is roughly **+5 percentage points in representative paired outcomes**, with uncertainty reported; a possible 3k claim needs nearer **+20 points of improvement around parity**. Kill the substantial-rating hypothesis if even the oracle is only tens of dollars/game, or if the causal rule loses its gain on held-out opponent families. The reported −$29/game net index-price gap for SIR is a caution: 18 lost races does not imply that 18 profitable races can be recovered without giving up other wins.

For scale, I applied hypothetical uniform margin increments to the existing 197-game ledger:

| Imagined gain in every game, with no downside | Resulting score versus this recorded sample |
|---:|---:|
| $0 | 40.1% |
| $100 | 45.2% |
| $300 | 55.1% |
| $500 | 64.0% |
| $944 | 76.1% |

This is a sensitivity calculation, **not a candidate evaluation**. It explains why a transferable few hundred dollars matters and why $944 against one development opponent cannot simply be carried onto the ladder. The $300 and $500 shifts correspond to approximately +107 and +172 local performance points under the illustrative normal model, but the sample is mixed and excludes the private top tier.

All confirmation must hold out seeds **and opponent families**, freeze source hashes, use both seats, and count ties as half wins. Forty-eight games in the existing gate are 24 seed clusters, not 48 independent shop experiments. Even ignoring that dependence, 29/48 wins has an approximate 95% Wilson interval of **46–73%**. The requested 60% gate is a useful minimum screen, not statistical proof of live superiority. Replay modifications establish exact one-turn effects only on the original state; a private opponent's recorded continuation cannot react to our changed policy, so a full fixed-replay rollout is supporting evidence, not a replacement for live validation.

I would not start RL, a new scheduler, another route-map fit, generic liquidation, production grafts, or a broad parameter sweep. The third move is already the speculative option. If its headroom fails, stop adding mechanisms.

**3. Slot policy through September 30.**

The better-of-two rule is verified in the staff response at [discussions.md, Version 4](../../discussions.md): the weaker active agent does not average down the stronger one's score. It does not mean every replacement is free: an upload evicts the older active submission, and a frozen historical score is not selectable for the final tournament. Nor does it require different architectures at any cost. Choose the second agent for credible complementary success, not different naming or low correlation alone. For success events A and B, the relevant objective is `P(A or B)`, not the average of their individual ratings.

| UTC period | Policy |
|---|---|
| Sep 25–26 | Keep the current control pair intact. Collect live evidence while finishing the two narrow investigations. No quota-filling submissions. |
| Sep 27–28 | At most one planned challenger upload, after its evidence justifies replacing **older sir_V2**. This preserves newer exact pipe16. If no candidate clears the evidence threshold, keep the current pair. |
| Sep 29–30 | Freeze the selected pair by default; inspect actual episodes and loading/runtime status. Replace only for a demonstrated defect or decisive new evidence, not a noisy dip or a public-pool ranking. |

After the first challenger upload, **pipe16 becomes the older submission**. Another upload would evict the control, not the failed challenger. Do not assume the two slots can be independently edited. Retire that control only if the surviving challenger has earned the anchor role; otherwise keep the pair. I would not repeatedly resubmit the anchor merely to work around this ordering and destroy its observation history.

I reject 4–8 hours as a guaranteed convergence time. It is an initial health/climb checkpoint. V3 includes approximately 55-hour convergence estimates and multi-day reversals; V5's destbreso measures episode rates from 0.7 to 7.2 per hour and recommends tracking score change per completed episode by submission ID. Plan for 24–48+ hours of useful validation where possible. Do not discard a clearly better validated agent solely because a late upload would start low: final scoring uses the post-deadline evaluation window. Conversely, a lucky pre-deadline 3000 tick does not secure the prize.

**4. The single thing I would do in the next 12 hours.**

Produce **one frozen decision sheet for the existing pipe16 control**, without spending another slot. Join its and sir_V2's new episodes to opposing submission IDs and timestamps; report observed strength by opponent class, the amount of unresolved uncertainty, and whether the historical delivery defect appears. Attach the already-running capture holdout once complete, explicitly showing its gain over clean pipe16 as well as its damaged parent if that comparison is available. If not, mark it missing. The output must distinguish “a baseline has been restored” from “we have improved on that baseline.” That decision has higher expected value than another candidate built against a pool whose best-ranked member recently settled near 1900.

**5. The strongest argument against 3k by September 30.**

We may be treating an obsolete 2787 snapshot as current strength while the actual public lineage is now hundreds of points weaker relative to private entrants. The verified candidate repairs a defect in our own overlay, and its attractive $944 result comes from six development seeds against a close relative; it has not beaten the contemporary private field. Every attempted shortcut to adaptive production has failed, and our earlier new executor failed against real opposition despite respectable solo income. Meanwhile the final field can include strong private submissions not represented in today's public pool. Five days allows a causal repair and a limited live check, not a credible replacement of the economic planner. If the control remains weak and the narrow fixes do not transfer, maximize the small remaining top-10 probability by retaining the strongest contemporaneously supported agent plus the best evidenced hedge, then stop churning. Reducing estimator noise alone cannot turn a weak policy into a prize contender; equally, chasing a noisy peak is especially unhelpful before a two-week final refit.

The probabilities below are subjective, not fitted confidence levels. My planning split assigns about 30% probability to the favorable branch—pipe16 substantially recovers its old standing and narrow-loss improvements transfer—and 70% to a substantially harder field/mixed-regression branch. Conditional chances of durable 3k are roughly 12% versus 0.5%; final top-10 chances roughly 25% versus 0.7%. This gives rounded forecasts of 4% and 8%. Update them sharply when the control and untouched holdouts arrive. “3k” here means credible underlying strength by the deadline, not a transient displayed maximum; “top-10” means the final post-deadline team ranking.

CONFIDENCE 3k+ by 09-30: 4%
CONFIDENCE top-10: 8%
