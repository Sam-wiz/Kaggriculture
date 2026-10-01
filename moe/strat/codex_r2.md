# CODEX strategy expert — round 2, September 25

**My revised position: field drift is more credible than I allowed in round 1, but neither a wholesale rollback nor a new market layer has earned a submission.** Read the existing contemporary control, finish the existing candidate comparisons, and audit the remaining public-source coverage. The new capture holdout weakens the strongest concrete improvement story from round 1.

I read all three round-1 positions and checked their underlying local artifacts. I recomputed leaderboard changes, historical fitted-rating point estimates, loss medians, and the completed candidate gate. No simulations, authenticated requests, or submissions were made. Only this file was written; in particular, I did not update HANDOFF or run analysis scripts that write into another expert's directory. References below are repository-relative unless linked. The control gate and BRX gate were still pending at this readout.

**1. Agree**

- **With Opus:** the independent evidence for field drift is substantial. Comparing `data/lb.json` (September 22, 19:20 UTC) with `live_eps/lb_now.json` (September 24, 20:35 UTC), I reproduce rank-10 **2977.1 → 2929.5**, rank-100 **2758.4 → 2689.1**, and rank-1000 **2374.6 → 2295.8**. Nathan Jacob falls **2566.6 → 2176.3**, KoshinM **2317.7 → 2040.6**. This is broader than our own code changes. Three teams exceed 3000 in that September 24 snapshot; that is a dated observation, not a claim about today's live board.
- **With Opus:** the early sir-V1 record is badly confounded by weak opposition. Using `moe/opus/eps_index.json`, `data/ep_pipe16.jsonl`, and the September 22 team-rating snapshot, I reproduce Elo-400 fitted point estimates **pipe16 2657.7/88 games**, **f55rec-V2 2588.9/109**, **f55rec-V1 2536.4/103**, **sir-V2 2469.5/84**, **sir-V1 2413.3/90**, and **L96-V1 2340.7/184**. Sir-V1's median opponent label is **1770.15**. Its 0.88 raw win rate cannot select the final agent. These are descriptive fits, with the limitations below; I did not reproduce Opus's bootstrap intervals.
- **With Claude:** reclaim's CARE deadlock is a real, traced defect, and its relevance depends on the selected parent. Repairing an introduced defect is different from improving clean pipe16. Neither removing every later layer nor porting capture onto an unaffected parent follows from the trace.
- **With both:** protect the existing control pair, stop quota-driven churn, and do not start a new scheduler, RL system, route fit, or production graft this week. The better-of-two rule rewards a credible complementary agent, while the latest-two rule makes replacement costly.
- **With Opus, changing my priority:** a bounded audit of the final public-sharing window is more worthwhile than another broad overlay search. Our own large gains came from stronger bases. This should begin with source/version coverage and deduplication, not a 354-agent simulation campaign.

**2. Dispute**

**Opus's weakest claim is causal: “It is not a layer we can fix.”** Its E2/E3 evidence does not identify that conclusion. Build and play date change together. Assigning every historical opponent a September 22 *team* rating freezes a numeric label; it does not freeze the opposing submission, policy, shop draw, or matchmaking population. `moe/opus/index_eps.py` joins ratings by team name, not opposing submission ID. Same-day sibling comparisons also share the suspect layers, so their small differences do not estimate those layers' effects.

Consequently, the reproduced 2657.7 fit does **not** establish that pipe16's displayed 2787 was specifically a freshness overshoot. Nor does one fitted/displayed agreement for L96 validate the method across changing policies. Rising own bank does not rule out a relative market regression: a wrong sale order can increase the rival's receipts, and the two bank medians come from different games. Field drift and an execution regression can coexist. A contemporary control advantage would support reverting to that policy, without disproving field drift or identifying reclaim as the sole cause.

There is also a numerical correction to Opus E1. In the stated snapshots, **164**, not approximately 320, teams initially rated 2200–2600 fell by 400–600. There are **930** matched teams in that initial band; their median change is **−234.4**. Across all initial ratings, **219** teams fell by 400–600. This still supports a substantial population shift, but the stated count overstates it. These counts come directly from matching the two JSON dictionaries by team name.

**Opus's proposed weighted gate is useful only within its coverage.** Farm-operation identity does not establish market-policy identity—the disputed edge is precisely in the market. Matching 70–90% of field operations to a public family cannot assign that family an exact native queue or a public opponent's matchup cell. Keep unmatched/private opponents as an explicit unknown category; do not redistribute their mass over the known library. Estimate weights from wins and losses, and hold out episodes for validation.

The proposed back-prediction that “pipe16 should come out well above f55rec on the September 20 field” lacks a contemporaneous live f55rec outcome to predict. It would risk calibrating the instrument to the historical ordering under dispute. A better validation is predicting held-out outcomes for actual identified submissions, then the ongoing contemporary control comparison. Also, 150 episodes × 354 full candidate rollouts is **53,100 games**, before screening new kernels. Use cheap source hashes and signatures to shortlist; exact replay should resolve a few ambiguous candidates.

I accept a **coverage audit**, not the proven existence of a missed stronger kernel. The older `rivals` directories do end around September 21, but mtimes cannot establish publication/version coverage. During this round another session refreshed `data/kernels.json` and began `rivals7/` at approximately 10:20 UTC. Consume that work rather than duplicate it. The inspected kernel metadata has missing `last_run` values, so an empty date-filtered missing list is not sufficient evidence that the window is covered.

**Opus's slot policy has an operational error.** Starting from older **sir-V2 56547525**, newer **pipe16 56547613**, one upload always evicts sir-V2. Its “field-driven” branch cannot replace pipe16 while preserving the current sir-V2 submission in one upload. Achieving that pair requires another upload and retiring both current references. The second slot has no averaging penalty, but selecting it still has replacement and evidence costs. Likewise, the promised September 25, 22:00 readout with at least 80 games per arm and final 700 games/±25 uncertainty are assumptions, not guaranteed service rates or calibrated error bars. `discussions.md` V5 reports **0.7–7.2 episodes/hour** across submissions.

**Claude's weakest claim is that uniqueness itself supplies strength.** A private edit prevents copying of that exact file; it does not remove opponents running the same production lineage. The edit must improve outcomes. A deliberately different losing sell order is also unique. Lower clone identity after a patch can merely measure the patch's changed actions, rather than a favorable change in the opponent population. There is no checked evidence that the final Bradley–Terry window will contain fewer clone mirrors or independently reward private code. Those claims should contribute zero to the forecast.

**Claude's rollback trigger and gain are too optimistic.** A control at 2500 would leave approximately **440 points** to the supplied 2940 cutoff, not restore a 150-point gap. Testing vanilla pipe16 also does not validate pipe16 **plus clamp and prem**, or the old subP2 build. HANDOFF 09-22m/n shows that these layers trade matchup strengths; whole-stack choices need contemporary support. The **+500–900 with confidence 0.6** budget is not justified by old versus new submissions measured in different fields.

**Claude overstates the transfer from exact clones to the band.** The build expert's **88% relative SELL-order agreement** is not next-turn queue prediction accuracy. It excludes uncertainty about quantities, missing orders, buy indices, and available stock. The same expert reports only **−$29/game net index-price disadvantage for SIR** (`moe/opus/NOTES.md`, checkpoint 3). This does not cap an oracle's possible gain, but it defeats the inference that 18 lost races are 18 freely recoverable wins. The existing BRX experiment is a legitimate bounded test because it models a rival queue, unlike the falsified generic-pressure selector. Its public-clone performance alone still cannot establish live transfer.

One factual correction to Claude and the brief: `moe/opus/pergame_band.json` gives **median loss −$708**, with 118 losses; **−$207** is the median across all 197 games. The approximately −$199 figure belongs to the 169-game similar-wheat subset, including wins. Small losses are plentiful, but these denominators must stay separate.

**3. Changed my mind**

My round-1 second priority emphasized the delivery/CARE correction, with the $944 development result as its strongest mechanism example. The new evidence demotes the **incremental CARE fix** and favors evaluating the simpler delivery arm first.

I independently aggregated `moe/codex/gate_candidates_records.jsonl`: **816 games, zero failed results**, seed-index **[906:930]**, 24 seeds in both seats per matchup. Delivery and capture have identical outcome records against every pool opponent:

| Opponent | Each candidate's W/T/L | Win score |
|---|---:|---:|
| sir-V1 parent | 39/4/5 | 0.8542 |
| f55rec-V2 | 46/0/2 | 0.9583 |
| sir-V2 | 46/0/2 | 0.9583 |
| koshinm | 24/0/24 | 0.5000 |

Across **384 matched pool games**, capture changes delivery's margin in only **two**: seed **900906**, both seats, against **2802**, **+$1227** each. That is **+$51.13** averaged over that matchup, with no outcome flips. Direct delivery versus capture is **4W/40T/4L, mean $0**. The large worker effect on the six development seeds did not replicate against koshinm. This is not proof the fix is useless; it is strong reason to stop treating $944 as its expected field effect.

Delivery/capture's six-opponent remainder mean is **0.8160**. It must be compared with the controls on these same seeds and opponents, not the historical sir-V1 **0.830** over a different slice and opponent denominator, as Opus's move-3 threshold proposes. `gate_controls.json` was absent at inspection. Both candidates beat the two older gate-labelled LIVE builds, but **vanilla pipe16 is absent from this pool**, so neither has cleared the actual current-pair decision.

I also lower my favorable-baseline prior: Opus's independently moving author ratings and reproduced adjusted records make a simple recovery to 2700–2800 less likely. I retain uncertainty about causation. My new top three put the public-coverage audit ahead of further SELL-permutation development; the already-running BRX test should finish, but it does not automatically earn another tuning round.

**4. Deciding experiment**

The consequential disagreement is **whether clean pipe16 is materially stronger than the current sir-V2 against contemporary opponents**, making rollback useful, or whether reverting offers little recovery. The cheapest credible experiment is a **read of the two existing live arms**, not another upload or public-pool match. It settles the policy choice more directly than the historical cause; because the arms also differ in chassis and several layers, it cannot isolate reclaim.

Below is an exact read-only command for the credentialed orchestrator. I did **not** run its authenticated calls. I checked the installed SDK's `competition_list_episodes` method and episode/agent fields. It makes two episode-list reads, writes no files, and computes a comparison within **opposing submission ID × UTC date × our seat**, so a replacement submission cannot inherit its predecessor's identity. It counts ties as half wins, resamples opposing submissions as clusters, and prints all included episode metadata for review. Runtime is ordinarily seconds plus network latency; one Python process, no simulations.

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python - <<'PY'
from collections import defaultdict
from datetime import timezone
import json, random, statistics
from kaggle.api.kaggle_api_extended import KaggleApi

arms = {'pipe16': 56547613, 'sir_V2': 56547525}
api = KaggleApi()
api.authenticate()
rows, bad = [], []

def utc(t):
    return (t.replace(tzinfo=timezone.utc) if t.tzinfo is None
            else t.astimezone(timezone.utc))

for arm, sid in arms.items():
    seen = set()
    for e in api.competition_list_episodes(sid):
        if e.id in seen or e.state.value != 2 or e.type.value != 1:
            continue
        seen.add(e.id)
        a = next((x for x in e.agents if x.submission_id == sid), None)
        rivals = [x for x in e.agents if x.submission_id != sid]
        if a is None or len(rivals) != 1 or not e.create_time or not e.end_time:
            continue
        b = rivals[0]
        if a.state.value != 2 or b.state.value != 2:
            bad.append((arm, e.id, a.state.name, b.state.name))
            continue
        if b.team_id == a.team_id:
            continue
        y = 1.0 if a.reward > b.reward else 0.5 if a.reward == b.reward else 0.0
        rows.append(dict(arm=arm, ep=e.id, opp=b.submission_id,
                         seat=a.index, start=utc(e.create_time),
                         end=utc(e.end_time), y=y))

print('non-complete agent statuses:', bad)
if bad:
    raise SystemExit('UNRESOLVED: audit error outcomes before comparing strength.')
if any(not any(r['arm'] == a for r in rows) for a in arms):
    raise SystemExit('UNRESOLVED: an arm has no eligible completed games.')
start = max(min(r['start'] for r in rows if r['arm'] == a) for a in arms)
end = min(max(r['end'] for r in rows if r['arm'] == a) for a in arms)
rows = [r for r in rows if r['start'] >= start and r['end'] <= end]
for r in rows:
    print(json.dumps(r, default=str))
print('common window:', start, end)
print('eligible counts:', {a: sum(r['arm'] == a for r in rows) for a in arms})

cells = defaultdict(lambda: defaultdict(list))
for r in rows:
    cells[r['opp'], r['start'].date(), r['seat']][r['arm']].append(r['y'])
blocks = defaultdict(lambda: [0.0, 0.0])
matched = defaultdict(int)
for (opp, day, seat), c in cells.items():
    if set(c) != set(arms):
        continue
    weight = min(len(c[a]) for a in arms)
    delta = statistics.mean(c['pipe16']) - statistics.mean(c['sir_V2'])
    blocks[opp][0] += weight * delta
    blocks[opp][1] += weight
    for a in arms:
        matched[a] += len(c[a])
print('matched games:', dict(matched), 'distinct opposing submissions:', len(blocks))
if len(blocks) < 10:
    raise SystemExit('UNRESOLVED: insufficient opposing-submission overlap.')

values = list(blocks.values())
def estimate(v):
    return sum(x[0] for x in v) / sum(x[1] for x in v)
rng = random.Random(92502)
draws = sorted(estimate(rng.choices(values, k=len(values))) for _ in range(5000))
print('pipe16 minus sir_V2 matched win-score difference:', estimate(values))
print('exploratory 95% opponent-cluster bootstrap interval:', draws[125], draws[4874])
PY
```

Pre-register one decision read when each arm has at least **80 eligible games**, rather than testing significance after every new episode. Ten shared opponents is merely a minimum reporting safeguard; the interval, overlap coverage, and stability across dates still determine whether the comparison is informative. The matched subset estimates performance on that overlap, not automatically the whole ladder. Sparse overlap or errors produces **unresolved**, not a fabricated answer. Additional data may take longer than three hours to arrive; the live-data read itself does not.

- **Claude's recovery direction wins** if pipe16 has a large positive matched effect—pre-register **at least +0.15 win score**, with the interval above zero—and the broader contemporary opponent-adjusted read agrees. Recovery specifically to 2700–2800 still requires evidence against opponents of that current strength. This result would favor the clean control, not prove every later layer harmful.
- **Opus's no-material-recovery direction wins** if the interval lies inside **[−0.10, +0.10]**, or clearly favors sir-V2, while the broader current results also show no old-strength recovery. That supports declining a rollback; it does not prove the CARE defect nonexistent.
- A point estimate near zero with a wide interval settles neither side. A positive effect between these thresholds can justify preferring the control without establishing the large recovery Claude budgets. These are operational win-score thresholds, not a claim that +0.15 maps universally to +150 rating.

The existing fresh team-rating fit can accompany this read as a secondary view, with its snapshot date and coverage stated. It should not replace exact opposing-submission overlap or be presented as a causal estimate.

**5. Revised ranked plan**

| Priority | Concrete next move | Expected value and stop condition |
|---|---|---|
| 1 | Preserve **[sir-V2 56547525, pipe16 56547613]** and read the ongoing control as above. | Measurement adds zero playing strength. Large recovery remains possible, but is unproven. Stop interpreting frozen-versus-current numbers as treatment effects; retain the pair if the read is unresolved. |
| 2 | Consume the ongoing public-source refresh; audit final-window versions, deduplicate executable payloads, and fingerprint a small representative post-lock sample using all action channels. | No assumed gain; a new base is the remaining plausible large-upside discovery. Cap the first audit at **three hours and one worker**. Continue only for a runnable, distinct candidate or a demonstrable gap in coverage. Do not launch the full 53,100-game matching exercise or fit field weights until identities and unknown mass are credible. |
| 3 | Finish the already-running delivery/capture controls and BRX gate; select the smallest supported change and compare it with **clean pipe16 and current sir-V2**. | Budget **0–75 points**, judgmentally, for a transferable narrow correction; no measured rating gain yet. Prefer delivery over capture provisionally because the added worker fix produces no held-out outcome gain. BRX gets more work only if the existing result transfers beyond exact-parent mirrors and its predictor/one-turn headroom survives inspection. Kill further tuning if these gates fail. |

For move 3, freeze hashes, pair seeds and seats, count failures, and report gains against the same opponents. A high parent-mirror win rate with a $117 margin is useful evidence of a tie-breaking effect, not proof of a large rating improvement. Neither a **0.60** minimum gate nor the currently observed **0.8542** against the parent alone supplies that proof. A candidate should preserve broader outcomes and then earn limited live validation.

The next eligible single challenger replaces **sir-V2**, leaving **[pipe16, challenger]**. A second upload would retire pipe16. Make that second move only if the surviving challenger has earned the anchor role; otherwise retain the pair. Aim to settle the pair by September 28, with later changes reserved for a demonstrated defect or decisive strength evidence. September 28 is an operational default, not a mathematical reason to reject a clearly stronger policy before the actual deadline. Final scoring uses the post-deadline games.

I reduce my round-1 forecasts from **4%/8% to 2%/4%**. These remain subjective probabilities: the evidence for public-lineage deterioration strengthened, the broad CARE-recovery story weakened, and the clean control has not yet demonstrated contemporary strength. The favorable tail is a substantial control recovery or an overlooked stronger base, followed by a correction that transfers. Privacy, convergence time, and a favorable Bradley–Terry refit are not independent sources of policy strength.

CONFIDENCE 3k+ by 09-30: 2%
CONFIDENCE top-10: 4%
