# MoE r6 — astra, round 1

**Author:** Codex gpt-6-astra, xhigh. **Date:** 2026-09-27. **Lane:** complete discussion reread, claim ledger, and remaining testable ideas.

## Decision

Keep C1/C1R2 as the reference pair. The forum does not supply an untested, evidenced route from our current level to 3k. It does supply a narrow information improvement worth testing: **distinguish an unobserved opponent sale from evidence that no sale occurred**, then let the forecaster abstain when its evidence is weak. A source-level probe below confirms that C1R2 currently penalizes predicted events during censored observations. Its prevalence and win-rate value remain unmeasured.

Second, test **opponent-model improvements to the market ordering already in C1R2**, only after measuring their residual opportunity. BRX2 is a useful old implementation, not a newly discovered primitive: C1R2 already contains exact lockstep permutation machinery. Blindly adding another ordering layer is not an evidence-backed improvement.

Third, dzjiann's **bounded reconstruction of opponent total loose stock** is still not validated by us. It is a potentially useful input to those two mechanisms, not an instruction to launch a new trading agent or assume access to the opponent's shed.

The latest discussion addition also contains two important corrections: a sampled opening hash is not an opponent-independent policy ID, and **paired margin remains a valid diagnostic when our intervention changes the opponent's bank**. That change is part of the treatment effect. Win rate remains the selection objective.

## Scope and reproducibility

I read `moe/r6/BRIEF.md` in full, including its added notebook-refresh paragraph, `HANDOFF.md`, `MISTAKES.md`, and **all of `discussions.md`**. The discussion file grew during the read. Coverage is:

| Section | Inclusive source lines |
|---|---:|
| Version 1 | 1–1550 |
| Version 2 | 1551–3201 |
| Version 3 | 3202–4309 |
| Version 4 | 4310–6012 |
| Version 5 | 6013–8738 |
| Added **“Last version”**, treated here as V6 | 8739–12273 |

V6 is not labelled `Version - 6`; a search for version headers alone misses it. It repeats several earlier threads, sometimes with new comments or corrections. The ledger consolidates repeated claims and records the new claims separately. Greetings, requests for teammates, praise, unanswered questions, and unrelated spam are not strategy claims. Numeric anecdotes stay attributed; an author's report is not our replication.

Cross-checks use r3–r5 reports, their result files/threads, the earlier `moe/opus` and `moe/codex` work, the installed engine, current C1R2 source, the existing exact-replay macro cache, and r6 sonnet's report. No `moe/r1/` or `moe/r2/` directories exist. The ranks 1–10 and 11–20 r6 dossiers were not yet written when checked; I independently audited coverage of all 20 in the r5 cache instead of inventing missing dossiers. That audit is dated Sep 23–25 and does not include the new Sep 26 download.

Artifacts in [build/astra](build/astra/):

- `audit.py`: reproducible source probe, input fingerprints, and exact-name top-20 cache audit. Run `.venv/bin/python -B moe/r6/build/astra/audit.py`.
- `source_manifest.json`: SHA-256 hashes and line counts for the cited source snapshots.
- `predict2_censor_probe.json`: three synthetic cases executed through the actual extracted `_v92_q_update` function.
- `top20_cache_audit.json`: fresh aggregation of all 1,773 cached episodes, all 20 current team names, sample sizes, banks, and records.
- `notebook_notes_sources.md`: markdown cells from all five notebook write-ups named in the brief; source paths and cell IDs retained.
- `claim_ledger.json`: all 145 numbered discussion-ledger rows in structured form; the notebook claims are additional rows in this report.
- `validate.py` / `validation.json`: ledger ID/count, source-snapshot, relative-link and syntax checks; run `.venv/bin/python -B moe/r6/build/astra/validate.py`. No game-strength result is implied.

Only this report and `build/astra/` were written. No API keys, OpenAI API calls, `moe/tools/oai.py`, submissions, agent workers, or background jobs were used. One foreground Python audit ran, with no worker pool. The sandbox refused `nice` with `setpriority: Operation not permitted`; no costly simulation or training workload was launched. This is round 1, so proposed tests below have **not** been run. The user's narrower write restriction excludes HANDOFF lane registration and THREAD posting; this file records ownership and includes the response to sonnet instead.

## Evidence key and corrections to the project record

These labels keep the ledger compact. Paths identify the recorded experiment, not a new replication unless explicitly stated.

| Key | Evidence and its practical limit |
|---|---|
| **E0 — engine** | Installed `.venv/lib/python3.14/site-packages/kaggle_environments/envs/kaggriculture/kaggriculture.py`: crop/animal constants 11–22, price curve 193–206, per-unit lockstep market 543 onward, floor sales 651–662, daily refresh/drop/RNG 772–896, unit actions before market 899 onward. Engine truth outranks outdated README/forum summaries. |
| **E1 — evaluation** | HANDOFF ground rules and §2; MISTAKES C10–C18. Score paired win rate and ties as half; report per-opponent results and both banks. Paired SD 373 versus unpaired ~8,094 was one design, not a universal variance constant. |
| **E2 — lineage** | HANDOFF 09-20c, 09-22n, 09-25k; r3 `build/opus/RESULT.md`. Public/band unit streams often match 97–100%; later RR cycles exist. Behavioural agreement does not prove shared source or identify a private RL architecture. |
| **E3 — premium/reconcile** | HANDOFF 09-21i through 09-22n: premium overlay alone loses field mean .814→.761 on the weak independent pool; full f55rec pair later wins the stronger 9-agent RR (mean .773 versus pipe16 .279). Both statements can be true. Old public-pool means are not current ratings. |
| **E4 — rescue/physical execution** | HANDOFF 09-23 rescue variants all negative; MISTAKES C15 supersedes C12: the cow→sheep swap created **zero new sheep**, so the purported sheep economics result was not measured. Verify animals placed, fed, and producing, not just purchase requests. |
| **E5 — market order** | HANDOFF 09-23 SIR: per-index race matters and reorder helped. CF/lockstep variants in 09-23 r4c lost ~46/g and modeled the rival inadequately. `moe/opus/RESULT.md` BRX2 later passed its old pool, mean .797→.844; held-out gains are whisker scale, not a 3k result. |
| **E6 — routing/RNG** | HANDOFF 09-21h and 09-24 rmap/rm2/rm3/rival-router entries. Empty tiles consume shared daily RNG before shop choice. Real-engine rm2 lost ~1,897/g; day-9 within-family oracle +263, realised rm3 +48. Late switching is mechanically possible on shared prefixes, but its measured value is small. |
| **E7 — replay-gate failure** | HANDOFF 09-25j and MISTAKES C18: shepherd replay substitution predicted .656 vs ≥2200, live ~.2; recorded opponents cannot react. Exact replay reproduction validates mechanics, not a counterfactual opponent policy. |
| **E8 — C1 forecasts** | HANDOFF 09-25k/l; r3 results. Existing PREDICT +1,332/g in a mirror ablation; activating refreshed PREDICT2 became C1. Independent 16 fresh seeds: 27W/3L/2T vs shepherd, 24W/8L vs hybrid. Wrong added streams can hurt: WL+O ~−460/g. A library refresh is already tested, not a new idea. |
| **E9 — RR** | `moe/r4/opus.md` §§1/3, `build/opus/PREREG_rr_retro.txt`, THREAD, screen2. Five anchors ~1800–2100; Spearman .70 and 2/10 misorders exactly meet bars. Twenty raw seeds × two seats per pair are not 40 independent worlds. r4 opusb found 300/300 seat-swap duplicates in its checked kagsim sample. C1 joint map ~2076, C1R2 ~2152 [2021,2294]; old promotion lower-bound bar >2148 was not met by C1R2. It was selected as the fallback, not as a gate-clearing moonshot. |
| **E10 — family decode** | `moe/r5/opus.md`, `build/opus/famacro.json`, `options.json`, THREAD. 1,773 episodes; 2,176 family seats; common staged cow/wheat/sheep opener; shop-conditioned herd/crops; ~294 season hires, ~6.4k hire cost, ~0% idle from day 10, 36–41% movement. Macro correlations describe the family, not the causal value of grafting it onto C1. |
| **E11 — tapes/executor** | r4/r5 reports and r5 THREAD: raw tapes 8/125 vs C1; TFC router .24; TS 3/32; NN 0/8; day-splice 0/20. DS had ~24% dead tile ops, +1.8–3.8 unfed animals and −1.7k to −3.9k/day. Exec3/DSX also failed placement and maintenance. No new support for another tape splice. |
| **E12 — O1/O2** | r5 THREAD 22:40/22:50: 40 fresh seeds on diagnostic `kag_dc`, fired/identity checked; forced SE sheep −14.6k, cow −16.9k, goose −9.2k/g; oracle +220 versus +1k bar. Locked forecasts r=.03–.23; selected payoff −1,665. Shops were decoupled for diagnosis: this is not a promotion gate in the natural engine. |
| **E13 — O3** | r5 THREAD 23:19: 64 fresh seeds, 61 feasible; locked forecasts r=.965–.974, native CXTB r=.970 and correct 58/64. Oracle only +123 bank/+109 margin; selected margin −28 or +34 depending on profile. **Options failed; forecasting did not fail universally.** |
| **E14 — V233** | r5 THREAD 23:05: off in 18 native worlds raised our bank ~4.3k and opponent ~13.2k; margin −8.9k. All-world 40-seed margin −307 (SE 219); RR 2058 vs 2076, paired −19 [−22,−10]. Keep it. Denial can be valuable even when own-bank accounting calls it unprofitable. |
| **E15 — compute** | r5 opusb §§1–3 and THREAD correction: direct-engine/full-season fork rollouts fit a sparse dawn schedule locally, ~2–2.8s M1/~9–12s Kaggle estimate; exact continuation 4/4. Opponent-model errors remain. Initial overage use by strong agents is compatible with compilation or initialization, not proof of RL/search. |
| **E16 — new source check** | `subZ_C1R2.py:3623–3670` plus this lane's `predict2_censor_probe.json`: low-price observations skipped, but forecast events still penalized as misses; best candidate selected without a support threshold. Proven mechanism, unmeasured competitive value. |
| **E17 — current ordering** | `subZ_C1R2.py:6032–6180` already evaluates lockstep SELL permutations; 6823–6926 adds CXD, up to 800 arrangements including fixed-price-order slots, with opponent-model hooks and default self-list. Downstream layers include T4 and IG queue changes. A new BRX2 wrapper must beat this existing stack and preserve parent/final-list distinctions. |
| **E18 — fresh cache audit** | This lane's aggregation: 1,773/1,773 cached rows report exact reproduction of both banks. Current top 20: 12 names represented, eight absent. These are archived matchups with uneven opponents, not 20 runnable agents or current unbiased win rates. |

**Do not carry these stale conclusions forward:** “market side exhausted” preceded BRX2/C1; “late rerouting impossible” preceded shared-prefix tests; “premium always improves” was corrected twice; “sheep swap failed because sheep were bad” was corrected to no sheep placed; “rollouts cannot work” was corrected by O3. Conversely, none of those corrections reopens generic sell tuning, day-9 routing, or C1 macro expansion without a new measurable mechanism.

## Claim ledger — Versions 1–5

**Status:** **C** = confirmed by our engine/code/record within the stated scope; **R** = refuted as stated or as a proposed lever on our stack; **U** = untested by us, including externally reported results we have not reproduced. “C, scoped” does not validate every numerical anecdote in the source. Source line numbers below refer to `discussions.md`; repeated threads are consolidated. Mechanically correct advice already implemented is not counted as a new strategy.

### Training, planning, and execution

| ID | Source / author | Concrete claim | Status / cross-check |
|---|---|---|---|
| T01 | 359–584, Snorlax; repeated 11448–11770 | Top-replay BC warm-up → macro PPO, ~300k games; early bank difference then win/loss plus auxiliary rewards; local leaderboard checked live. | **U.** A specific self-reported successful recipe. E11 refutes naive transfer, not this complete private pipeline. No architecture, executor or checkpoint sufficient to reproduce it is supplied. |
| T02 | 642–915, KKY/Mahog | ~300M steps, ~80k bank after weeks; static opponents easier; self-play unstable, crop/animal mode collapse; Adam reportedly rescued an SGD failure. | **U.** Training anecdotes, not tested here. Consistent with executor and opponent-distribution bottlenecks, not proof all RL fails. |
| T03 | 1043–1074, Sayaka Miki/linkinpony | Runtime/RL can exploit a local optimum and reach the top. | **U** for exact method. Current #7 Unknown Mother-Goose has member `linkinpony` (top20.json); that identifies an author/team, not its hidden architecture. |
| T04 | 1174, 1305, 1369, 1414, Roy Wei | PPO from scratch; ~350M steps/3090, 90k vs static rival's 122k, later ~70k; league planned, no BC. | **U.** No replicated pipeline or competitive result against our present anchors. |
| T05 | 1391–1397, destbreso | Learn reusable reactive behaviour from fragments of several strong replays. | **R** as an automatic near-term transplant. E11 and r3 reconstructed-WLV failure. Coherent learned options with their own executor remain **U**, not disproved in principle. |
| T06 | 1732–1748, Matheus | Rank tasks by weight/(distance+1), consider top ten and depth-two routing. | **U** for this exact dispatcher. E11 makes “replace the executor” a high-cost proposal; shortest-path arithmetic alone does not maintain multi-turn delivery/feed chains. |
| T07 | 1994–2113, Justin Gao/sobameshi | Planner/scheduler/worker layers underperform tapes; runtime ~1640 versus tape rank ~400; small reactive mirror layers help but economy remains limiting. | **C, scoped** by E8/E11. Their ranks and banks are **U**. Layered architecture alone is no evidence of a stronger executor. |
| T08 | 2175–2180, Exposed | A one-line tweak gained ~147 rating; LLM-generated new agents cannot reach the top. | **U** for anecdote; universal impossibility unsupported. No concrete repeatable lever. |
| T09 | 2214–2226, 2333, Mark Yang | JAX ~10k steps/s; BC reaches 7% parity; PPO 50/25/25 mixture, 60/70 thresholds, FIFO 5, temperatures .8/.5; reward .75 production/.25 bank then reversed; 50–120k, ~500M best-run steps; hybrid worse. | **U.** Preserve recipe as reported; no measured transfer to C1 or our target field. Neither throughput nor raw bank establishes strength. |
| T10 | 2250–2260, hwe | #8 used ML for sale timing, not RL. | **U.** Useful counterexample to “only RL can win,” but private model and evaluation unavailable. |
| T11 | 2289–2295, Friaseus | Deterministic finance + macro CEO + BFS/Hungarian assignment should break 80k. | **U** for exact implementation; **R** as a sufficient recipe for a medal. E11/E12 show allocation/maintenance integration is the hard part. |
| T12 | 2377–2384, Young | Shared unit weights, autoregressive market choices, KL control, critic warm-up could improve training. | **U.** Concrete research choices, no local RL implementation or deadline-sized path supplied. |
| T13 | 2414–2468, Marcelo/Matheubern | Daily unit reset and automatic carried-stock drop; avoid colliding jobs and PICKUP/DROP loops. | **C.** E0; MISTAKES D1 found a loop consuming 48% of actions. Do not count each duplicate water/care request as work delivered. |
| T14 | 2423–2446, Marcelo | ~44% walking; 5 cells/no hands preferred; fertilizer +2725 versus eggs1250; melon first yield day12. | **R** as general strategy/mechanics. E10 uses large crews/land; melon first yield is day10, max-yield day12. Four-seed starter comparisons do not rank competitive plans. Fertilizer/egg profitability is world-dependent. |
| T15 | 2444–2468, Marcelo/Matheubern | Simultaneous PLANT requests exceeding seeds cancel all requests for that crop; FEED needs carried wheat. | **C.** E0 interpreter atomic validation and FEED implementation. Buying the seed in the same turn is too late for PLANT. |
| T16 | 2478–2482, Nur; 2545, nouvya | Coupled small refinements matter; local RL extension proposed. | **U** for proposed learner; **C** for coupling (E4/E11). No unmeasured isolated C1 lever specified. |
| T17 | 2576–2580, Shair | Static policies always beat RL; optimum lies in a day0–15 convex hull. | **R** as universal/theoretical conclusions. Private RL success is reported; discrete finance, actions, shops and survival do not establish the asserted convexity. |
| T18 | 3020/3066, Siva | CARE requires feeding and banks a bonus; using state-based feed commitments cut deaths 10→1. | **C** for fed-and-cared daily mechanism; **U** for that result. CARE can occur before FEED during the day. The bonus is paid by daily production, not special intraday hours. |
| T19 | 3098–3104, Aaweg | Six alternatives: persistent daily planner, recurrent policy, autoregressive units, BC grammar, leagues, simulator counterfactual labels. | **U** as full architectures. E11–E13 test specific implementations/options only; they are not a blanket proof these families cannot work. No time to bootstrap the missing executor. |
| T20 | 3141–3147, Syed | Coordination changes worth little on one script; exact simulator enables counterfactual supervision; CPU ~670k steps/s. | **C, scoped** for simulator supervision feasibility (E13/E15); **U** for their throughput and general coordination claim. E12 demonstrates executor constraints can dominate. |
| T21 | 3229–3234, Shair | More than three hands cost at least $12/day; lean labour should win. | **R.** Four hires total7, five total12; ten total143. E10 uses ~9–12/day, and labour needs joint value accounting. |
| T22 | 3338–3340, Matin | Circular plans must coordinate finance, planting, labour and eventual sales. | **C, scoped.** E4/E11/E12 supply failure mechanisms. This is a constraint, not a new winning plan. |
| T23 | 3605–3617, Vijai | Loss taxonomy; starting animals two days earlier +10k; same-turn harvest/sell41.6%; CARE at hours6/12/18; deploy2982 immediately; never sell >20 premiums. | **U** for counts/gains; **R** for universal rules. Cows really mature after8 days, but CARE-hour alignment is false (E0). Same-turn sale needs shed access/drop; batch cap20 and spending all opening cash can damage finance. |
| T24 | 3737–3819, Justin | Persistent job queues, state-only CARE, route/task separation; melon day10. | **C** for mechanics and need for commitments (E0/E11); **U** for this dispatcher outperforming C1. |
| T25 | 3929–3983, Hanserong | Determinism means RL cannot help; BC drifts; end-to-end PPO ~40k. | **R** for determinism argument: hidden inventory/future world and huge planning space remain. **U** for model result; E11 confirms naive replay transfer failures. |
| T26 | 4549–4605, Zhenyu | 43.12% accuracy/15.08% PASS; near100% leaked accuracy; 99.2 AP/99 F1,3756 options,25.6k→34.2k; land99.84% yet187 rejects,100 finance failures. | **U** for exact counts; **C** for the lesson that operation accuracy fails to establish coherent execution (E4/E11). Constant-policy ablation and actual autonomous outcomes are the useful tests. |
| T27 | 4644–4680, redblackbst/Steve | Recurrent BC beats parent but loses a new counter; large GH200 compute does not fix generalization. | **U** for exact runs. E7/E11 agree that parent match/compute is insufficient evidence. |
| T28 | 4770, Zejun | Heuristic #22 fell to ~#140 after RL gate, with ~80% decisions still heuristic. | **U.** No causal ablation proving RL's general value or harm. |
| T29 | 5005, composable-policy proposal | Generate reusable action programs rather than primitive-action BC. | **U.** Existing tape splices fail E11; programs with preconditions and a coherent executor are a distinct, much larger task. |
| T30 | 5486–5523, c0nrad/others | Condition early plans on shops; short10–15-turn rollouts ~40k; PPO ~2–3k. | **C** for early commitment constraint, E6; **U** for reported banks. E12/E13 show late investments need full-season evaluation. |
| T31 | 5609–5619, dzjiann | BC sees little successful new-land behaviour; only20–40% harvesting there leads learned policy to avoid expansion. | **U** for exact model; plausible data/executor feedback consistent with E11, not evidence to force SE in C1. |
| T32 | 5695, reward proposal | Reward expected inventory value instead of only cash. | **U.** Needs realizable liquidation, labour, opponent and terminal accounting; own-bank reward alone is not the contest objective. |
| T33 | 5797–5832, UMG/Michael | Average-replay BC weak; single-parent imitation reaches100% but fails transfer; ~75k self-play; swapping crop/animal modes destroys gradients. | **U** for private training runs. E11 supports transfer difficulty, not impossibility of all BC/PPO. |
| T34 | 6751, training-budget claim | Need at least10M games for RL. | **R** as a universal threshold; Snorlax reports ~300k with a different abstraction. No compute-only bound follows. |
| T35 | 7140–7163, Vijai | P100/PyTorch2.10 silently falls back to CPU,13× slower; T4 fixes it. | **U.** Stack-specific operational claim, not checked locally and not a C1 lever. |

### Economy, observation, and market mechanics

| ID | Source / author | Concrete claim | Status / cross-check |
|---|---|---|---|
| M01 | 1085, Gonia | Replays need alternate continuations when shops differ. | **C**, E6/E11. Matching only first two shops still does not make full tapes transferable. |
| M02 | 1112–1123 | A $1 win counts; prices described as updating daily. | **C** for win criterion; **R** for daily pricing. E0 reprices marginal fills; town consumption also changes prices. |
| M03 | 1163–1169 | Melon first yields day6; watering every other day enough. | **R** for melon (day10). **C only for survival** after correctly watering planting day; bonus-window daily watering and fertilized ongoing production change yield. |
| M04 | 1476–1526, Zukas/Ramón | Net profit per tile-day should include labour, feed, maturation, demand and future prices. | **C** as accounting constraints, E0/E12/E13. Does not determine an optimum without executor and opponent. |
| M05 | 1769–1812, Mateo/Gleid | Normalize nonlinear inventory shapes to T, distinguish scarcity/glut sides and sum marginal unit prices. | **C**, E0. Log means ln(1+x) with the correct normalization; price clamps/rounding and hinge version matter. |
| M06 | 1960–1964, Nathan | Three of four v40 losses traced to two day1 cows dying; $12–32k per cow;4 fixes kept/12 reverted;23–7 vs v41. | **U** for those numbers. E4 confirms survival can cause blowouts, but three later rescue overlays lost overall. Not permission to retry unconditional rescue. |
| M07 | 2715–2717 | Exact ties prove identical agents; selling one turn earlier beats mirrors. | **R** for identity proof. **C, scoped** for preemption (E5/E8); physical stock, future deliveries, response, and final liquidation constrain it. |
| M08 | 2777–2808, DeDQ/others | Opponent actions visible but farms hidden; ladder averages raw bank; recent wheat buys reveal future crop plan. | **R.** Farms are public, shed/carried/seeds private; actions are simultaneous, not a direct next-action feed. Wheat can be feed or trading inventory. Rating is outcome-based. |
| M09 | 2999–3085, **Siva Annamreddy** (duplicated post) | Flat daily town demand; use actual fills, not requested sells; fertilizer doubles tile yield; day28 liquidation; files referenced by agent crash. | **C** for flat center demand and fill accounting. **R** for generalized fertilizer doubling and all-file prohibition: one-time bonus is watering-specific; packaged files are allowed. Endgame net effect and claimed death reduction **U**; E0/E4. Attribution is Siva, not a similarly named agent. |
| M10 | 3462, shops | Shops consume shared market stock rather than directly paying a farmer. | **C**, E0. Repeated shops each consume, single-product shops double draw; no shop demands melon or fertilizer. |
| M11 | 3629–3640, Zukas | Audit own losses; workers can share tiles, duplicate tasks waste actions. | **C**, E0/E4/E11. Association with a loss must precede an actual intervention to establish cause. |
| M12 | 3681, Roy | Fertilizer behaviour differs across environment versions. | **C** that version pinning matters; exact1.29.3→1.32.7 comparison **U**. Use the installed pinned engine, not stale prose. |
| M13 | 4181–4230, 3정훈 | Requested quantities do not equal fills; per-unit same-index quotes;10 orders; $1 sales do not increase inventory; stock/cash/capacity caps; units before market; ledger1438 deltas/6480 quotes exact. | **C** for mechanics (E0/E5); **U** for author's exact sample counts. Our 1,773 exact rows corroborate deterministic replay, not opponent inference at floor. |
| M14 | 4913, RNG | Both farms' weed draws and shops share daily RNG. | **C**, E0/E6. Same raw seed is not same future shop path after changing empty tiles. No demonstrated general seed oracle; absence of seed in observation alone is not an impossibility proof. |
| M15 | 4976–4978 | Water before hour20 prevents decay; two hands triple throughput; hold gluts until recovery. | **R** as stated. Lifespan drives decay, action geometry limits throughput, and withholding can enrich the rival (E3/E14). Two hires do cost2 nominally. |
| M16 | 5948, wheat | Wheat production represented as4 units in5 days (~.8/day). | **U** for that schedule; **R** as universal yield. E0 has max base6 and watering bonuses; planting/harvest timing matters. |
| M17 | 6145–6249, Ritwik | Premium floors120/140/90/60 through day18, then further timing tweaks;19–1 on10 held-out seeds, reported mean857/paired1713. | **C** that this family of floors is already extensively tried (E3). Their exact result is **U**, and20 seat-games are at most10 independent seeds. Do not merge the two reported effect scales. |
| M18 | 6319, fertilizer | Fertilizer always falls and a fixed day9–14 sale rule follows. | **R** as universal. No town fertilizer demand, but BUY_PRODUCT can reduce its market inventory. Marginal prices and opponent behaviour matter. |
| M19 | 6359–6382, Karthik | Melon demand is only1/day;160 units at~195 earned31k; finite lucrative supply makes timing decisive. | **C** for demand/limited market (E0); **U** for31k sample, not a competitive crop recommendation. |
| M20 | 6680, hengck | Forecasting must include stock capacity, cash constraints and actual sale execution. | **C**, E0/E4. PREDICT/CXD cover parts already; true opponent stock and censoring still imperfect (E16/E17). |
| M21 | 7170–7201, starkhushi | Wheat bootstrap beats cash-starved all-melon opening; melon first10/max12; free structures, animal pickup/place/feed chain,8 hires54, four shed-access tiles. | **C** for mechanics; **U** for18/2687/15394 banks. Opening prices29/132/260 in table are not default bases25/120/250. Carried stock auto-drops overnight except the final scored boundary; “must manually return every item” is false. |
| M22 | 7204–7257, Bovard/Georgy |1.32.7 adds hinge scarcity for carrot/tomato/egg; old/new37,343-episode price and revenue shifts, median+610,p=.41. | **C** for patch mechanics, E0. Old-regime statistics are **U** here and cannot establish a current causal improvement; separate engine versions. |
| M23 | 7293–7303, destbreso |120 tapes cross with public rivals at55/28.3/25.8%; hinge changes banks but0 winners in224; win probability model emphasizes μ/σ. | **U** for exact panel. **C** that bank and WR differ (E14). Normal-CDF μ/σ is an approximation, not a law or justification for generic variance minimization. |
| M24 | 7361 | Only final bank counts; leftover land, animals and inventory have no salvage score. | **C**, E0/E1. Final sales must execute before scoring; no final overnight rescue. |
| M25 | 7799–7819 | Illegal orders are deliberate obfuscation or evidence of RL. | **U** for intent; **R** as an inference from no-ops alone. Stale tapes, rejected finance and wrapper interactions explain them too. |
| M26 | 8044, Tommy | Opponent barn is the only hidden state and easily inferred exactly. | **R.** Opponent seed/carried/shed split and losses are hidden; floor censoring prevents unique inversion. |
| M27 | **8074–8118, dzjiann** | Conservation yields opponent total loose stock; point F=L=0, interval widens at hidden floor sales/loss; reported MAE carrot.008,tomato0,egg0, milk/wool noisier. | **C** for accounting/identifiability distinction, E0/E16. **U** for a correct implemented estimator, stated MAEs and incremental forecasting/WR value. Top remaining information lead. |
| M28 | 8439–8465, tutorial claims | Wheat price drops at most24%; obstacle-aware routing necessary; simplified demand factors. | **R** as mechanics. Log glut curve continues toward floor; locked cells are traversable. Use exact shop multiplicities/engine instead of fixed approximations. |
| M29 | 8616–8660 |537 episodes/~250k rows sufficient; player0 NW/player1 SE; TILL action. | **U** for dataset usefulness. **R** for engine claims: both farms start NW; operation is DIG. |
| M30 | 8726, Thomas | If a move raises both players' prices it wins nothing. | **R** literally: benefits can be unequal. **C** for the need to measure the rival externality; E14 is a direct causal example. |

### Instruments, data, ratings, and packaging

| ID | Source / author | Concrete claim | Status / cross-check |
|---|---|---|---|
| I01 | 7–55, Bovard/Georgy | Official daily dump sorted by mean rating,20GB cap;43/44 days cap-bound;22→31MiB/episode,928→657 games/day; early medians670 then2735–3080. | **C** for described selection policy and need for date strata; author's exact counts **U**. E18 confirms substantial current-team coverage gaps; dump is not a census or opponent-frequency sample. |
| I02 | 302, 大山 | Browser game differs from description. | **U** for this early bug. Later V6 browser replay mismatch is explicitly retracted as a scoring issue. Use downloaded JSON/engine. |
| I03 | 998, staff;1497, Ramón | Sharing closes Sep23; competition ends Sep23. | **C** for staff sharing date as archived; **R** for competition deadline (r6 brief Sep30). This report makes no new eligibility ruling. |
| I04 | 1635–1658, mikelou/Zukas |90% against public agents means little overfit risk; hold out seeds and opponents. | **R** for first assertion, E7/E9/E11. **C** for holdouts; same-family or same-submission episode splits are weaker than truly held-out opponents. |
| I05 | 1821–1851, sobameshi |14-agent/96-seed RR: zero cycles,86/91 newer beats older; adjacent60–80%,two generations90–100%;19 dump waves never rebound after<5%;18 teams share opener. | **U** for that panel. **R** as universal transitivity (E2/E9). **C** that a replay lineage exists; disappearance from a biased dump does not prove extinction. |
| I06 | 1981–1983, Michael | New play copied in24h; SpaTaro had distinct strategy every game. | **U** for exact rate and hidden policy. Distinct streams may reflect branches, repairs, shops, seed, or opponent; not proof of end-to-end RL. |
| I07 | 2673–2690, haidep | Benchmark both seats; old baseline ~2200. | **C** for seat correctness checks; E9 says cluster by seed, not doubled n. Old rating not transferable to today's field. |
| I08 | 3139–3147, Syed | Opponent-ID gain38 versus oracle224; seed-holdout+2301→−1259; reroll78% vs preserved-world40%. | **U** for exact study; **C** for cautions, E6. A preserved world is a diagnostic intervention, not sufficient live validity. Our old opponent-router ceiling also small. |
| I09 | 3170, Yan;3374–3439, others |51 wins after1 loss still1500; convergence5h/55h/4days; resubmit to get luckier. | **U** for incidents; **R** for a universal clock or repeated-submit final edge. E9 and exact pipe16 retest show both rating lag and field drift. |
| I10 | 3210–3219, gaolicious | Duplicate initial600 accounts expose a simultaneous-action race bug. | **U.** No local reproduction. Do not turn an unexplained live observation into an engine exploit. |
| I11 | 3298–3325 | Tape discovery improves incrementally; RL dominates private top; retrodict local instrument first. | **C** for retrodiction requirement (E9); **U** for hidden algorithm census. Tapes as fixed opponent gates fail E7/E11. |
| I12 | 3482–3510, Le Quang |26 opponents,25>60%,mean87.4%;2888 replay clone rates2432; off-by-one ruins replay; seat73/71. | **U** for numbers; **C** for exact-step discipline and nontransfer (E7/E11). Clone rating is not donor-policy rating. |
| I13 | 3717, staff;4335–4347, Addison | Final static Bradley–Terry, best of last2; ties half; no promised fixed pairing rate. | **C** as archived authority and project rules. V6 line10047 settles **all games between still-active submissions**, not post-deadline-only. |
| I14 | 3839–3848 | Entry function must literally be named `agent`; any helper/file forbidden. | **R.** Local Kaggle loader uses last callable; explicit final alias is our packaging fix (HANDOFF09-25h). Root main.py/multi-file packaging is supported. |
| I15 | 4065–4077, 4262 | Exact rating-gain magnitudes and cadence; screenshot reward/score mismatch means scoring bug. | **U** for per-match formulas. Staff described display issue; do not infer strength or win rule from a screenshot. |
| I16 | 4275–4308,6548 |1s/act+60s overage,1200s episode budget; both agents run in parallel. | **C** in local timing/framework record E15. This is not permission to spend60s every move. First-load cost matters. |
| I17 | 4354–4358 |Old leader40–0,+13065 first diverges immediately; router23–17,+547 with0.6–3.9% variation, divergences440–590. | **U** for exact sample; **C** that opening match need not imply full policy (E2/E10). Retirement to hide strategy is speculation. |
| I18 | 4491 | Identical submissions differ248 rating after3–4days. | **C, scoped**: our record also found large duplicate gaps, not that this exact case was verified or differences persist forever. |
| I19 | 4889,5317,7413,8278 |Everyone resets to600; deadline snapshot determines final score. | **R.** Staff's BT/all-active-games clarification and E1. |
| I20 | 5068, Artem |Maintain hypothesis ID/status/evidence/reopen condition. | **C** as existing HANDOFF/MISTAKES practice. New claim registry below is useful precisely because later corrections supersede old conclusions. |
| I21 | 5177–5199, destbreso |Stripe patterns distinguish replay/router/adaptive policy; leader strands60× more value; rating drift diagnostic. | **C** as descriptive tools; **U** for counts and causal classifier labels. Within first-two-shop cells still leaves later shops/weed/finance differences. Terminal waste alone did not explain E11/E14 gaps. |
| I22 | 5320–5428, Yizuki |Live observation step is missing. | **R by author's own correction**: live0..8 present, saved replay field missing. Local code must set replay step explicitly; do not patch production around a replay-only defect. |
| I23 | 5479,5989,6487 |Public replays allowed; all cloning forbidden. | **C** that archived staff encouraged replay use; **R** that the blanket ban is established in this corpus. V6 includes later unanswered eligibility questions. No legal conclusion or submission action is needed for this lane. |
| I24 | 6000, Garrie |Genetic search over public-pool fitness improves play. | **U** for transfer; E7/E9 require a responsive and retrodicting fitness instrument. |
| I25 | 6033–6093, Bovard/Amedeo |No future parameter changes; decouple weeds/shops locally for clean comparison; pin shop draws. | **C** for archived statement/diagnostic usefulness; **R** for automatic neutral transfer. E6's real-engine losses and E12's diagnostic-only scope matter. |
| I26 | 6444–6451 |Decision t stored in steps[t+1]; terminal step has no action. | **C** for offset; **R** for excluding terminal record's stored final action. It contains the action whose resulting state it records; don't apply an extra step720. |
| I27 | 6494–6500 |Use retrodiction; stable tapes form a gate; tape+overlay~2000+. | **C** for retrodiction/historical band; **R** for treating stable tapes as valid market-policy opponents (E7). |
| I28 | 6891–6924, dzjiann |960 games:6 strategies16seedsboth directed; B85 beats Andrews30–2, Andrews beats Kaito21–11, Kaito beats B8524–8; joint opening/opponent info67.5% vs54.2baseline. | **U** for exact panel, **C** for possibility of cycles (E2/E9). Directed/seat repetitions do not multiply independent seeds. Their info gain does not reopen our E6 router without new observable signal. |
| I29 | 7038–7070 |Official~1game/s versus C++2000/s,24k tape streams. | **U** for quoted machines; **C** that fast replay simulation and Python-agent runtime are different (E15). |
| I30 | 7411–7499 |72h settles; exclude no-new-game polls; newestID best; fixed agent fell182 over135games. | **R** for fixed convergence/newest-ID claims. **C** for only counting new games and possible drift; exact182/135 **U**, corroborated by our pipe16 control. |
| I31 | 7623–7759 |Beats all public agents>55%,mean75%,live1900; all early play fixed. | **U** for numbers; **C** for public-gate failure pattern (E7/E9). **R** for all openings being fixed; conditional trading/financing can change immediately. |
| I32 | 7998–8027, Georgy |No overlap in8300 API games afterAug9,147 expected; daily dump and API samples differ. | **U** for counts/hypothesized hidden slice. **C** that sample sources differ and coverage must be audited (E18). Independence assumptions behind147 need checking. |
| I33 | 8123–8237 |Identical1700/>3000 demonstrates path dependence; ecology/specialization explains it; universal clones cannot all be3000. | **U** for exact case and causal ecology; **C** for lag/relative ranking, E1/E9. Nontransitivity is measured; its share of the gap is not identified. |
| I34 | 8690, staff |No midterm BT refit; final often resembles converged ladder. | **C** as archived staff guidance, not a guarantee for an unconverged C1/C1R2. |

## Claim ledger — added “Last version” / V6

The duplicated dzjiann thread at 8993–9165 repeats 8742–8914. Later repeats of Snorlax, the daily-dump announcement, the fruit-fly agent, and sobameshi's tape thread inherit the rows above; new replies are included here. The fruit-fly report (602–608 and 11120–11130) is **U**: 728 neurons/35,704 synapses, no training, ablated stationary strawberry policy reportedly best; no evidence it improves our competitive stack.

| ID | Source / author | Concrete claim | Status / cross-check |
|---|---|---|---|
| V01 | 8742–8914, dzjiann |196-core server,~1M games; high-level PPO, sparse rewards, public+self-play;~90% public WR but weaker than prior math/DP against strong players; not reusing older-rollout trajectories more stable. | **U** for recipe/results. E7/E9 confirm the public-vs-target gap can occur. “Top100 at best” is author history, not current rank1802 or a result we verified. Compute alone is not the missing evidence. |
| V02 | 8850–8854, shiba-inu |Self-play/past-checkpoint agent approaches100k but cannot beat public agents. | **U** for run; **C** for raw bank's insufficiency, E1/E14/E18. |
| V03 | 8924–8935, Yujin |Seed clustering:2/6 on three seeds becomes8/12 on six; use seed as sample unit, at least6. | **C** for clustering, E9; exact panel **U**. Six is an exploratory minimum, not a power guarantee for promotion. |
| V04 | 8937–8949, Yujin |v7 beats hybrid12/12,+11k but losesV530/12,−4.9k and three other families0/6; lineage weights/walls retrodict hybrid2640 vs v71650. | **C** for need for multi-opponent gate, E2/E9; exact numbers **U**. One easy sibling cannot certify a family wall. |
| V05 | 8951–8967, Yujin |Low-band families24%+23% vanish at2450–2850; classify submissions by modal h48 then count full episode index; hybrid opening varies with opponent. | **U** for percentages/exact hybrid condition. **C** for avoiding replay-coverage weights and multiple-opponent fingerprints, E2/E18. “Independent of seed/seat” is not universal because weeds appear before48. Observe hash sets, not a single oracle ID. |
| V06 | 8969–8977, Yujin |Identical farms decided by wool sale timing226→31→1; splitting day27+ sales loses~1k and margin−4.9k→−6.2k. | **C, scoped** by E5/E8 and past split-sale failures; exact six-seed effect **U**. This is not a new sell-quantity lever. |
| V07 | 8979–8981, Yujin |Keyword notebook searches find more than competition filter; UTF-8 BOM can break JSON reading. | **U** for platform search coverage; known tooling issue, not game strength. Brief already refreshed19 notebooks; no new scraping needed for this lane. |
| V08 | 9168–9170;11285–11293 |Questions about eligibility of MIT public-code copies and replay-derived submissions. | **U / unanswered questions**, not evidence that either is newly banned. No submission or eligibility decision made here. |
| V09 | 9174–9257, デワンシュ/others |105games60% rating2522 versus129games88% rating2029/85games92% rating1887;1–2games/h; slowdown sinceSep23, later resolved. | **U** for exact snapshots; **C** that opponent bands and new-game cadence must accompany WR (E1/E9). A high win rate against weak opponents is not a high final rating. |
| V10 | 9260–9311, Omer/Yusuke |Top teams intentionally dropped to avoid training;33k guaranteed bank should outrank1700 agent that once banked6. | **U** for withdrawal motive. **R** for bank→rating inference; silent crash or one broken world requires inspection. E1/MISTAKES C11. |
| V11 | 9314–9334;11816–11852, Sayaka/staff |Old notebooks can still update after share deadline; staff investigating publishing bug, one newly published notebook observed. | **C** for historical staff acknowledgement and current local refresh's existence. No inference that all19 files are novel, permitted submissions, or unchanged lineage. Hash/diff before strength claims. |
| V12 | 9394–9438, Debmalya |Rust simulator pinned1.32.7, byte-state differential tests50/500 episodes,550ksteps/s,~770tape games/s,~16× Python-agent speedup. | **U** for this binary's tests/speed. E15 already supplies our simulator; importing a new engine is not a strategy. |
| V13 | 9412–9416, Debmalya |719 actions0..718; empty market/hand entries positional; first two shops realized after71/143; own private only, fresh seat obs, callable arity/config parity. | **C**, E0/local harness record. Essential for exactness. Removing `[]` is a market intervention, not harmless normalization. |
| V14 | 9479–9491, Georgy |SE total land cost7k;12 paired toy-carrot seeds:25tiles−930±432;12tiles/3shared hands−601±320, slices+3871±990;50tiles/6hands+1217±619. | **C** for land/hire arithmetic and coordination hazard; numeric toy effect **U**. Purchasing land does not require using/maintaining every tile. This supports executor capacity, not a causal conclusion that all top advantage is tile ownership. E11/E12. |
| V15 | 9502–9562, destbreso/Jack/Dipam |Leaders sometimes use SE; expansion may not repay with extra labour. | **C**, E10/E12/E13. Existing family77% SE is not the old claim of “rare use”; condition on date and actual lineage. |
| V16 | 9587–9645, Omer/Steve/Brahim |50B steps anecdote; half-billion over3–4weeks/4days3060 only beats own script; tens of millions may beat one rival; action constraints, shaped→sparse rewards, observation richness and opponent mixture matter. | **U** for runs/recipes; **C** that beating one teacher does not prove generalization. No universal sample-complexity threshold; “good in a day” is speculation. |
| V17 | 9670–9676, HyperNeonByte |Micro BC loss decreases on16-core M4 yet terminal bank<1k. | **U** for run; consistent with E11. Operation loss without whole-turn/purchase success is not the metric. |
| V18 | 9684–9706, Avineesh |51-board evaluator r=.014; live league raises bank r=.458/margin r=.533; starter121k vs live81k; seed0 self-play71345/72013 exact. | **U** for numerical study, **C** for E0/E7/E9 mechanisms. Replay exactness requires both actual policies/streams; substitution does not answer the reactive counterfactual automatically. |
| V19 | 9708–9736, Avineesh |384 paired games A:margin27682/91.7%,B:25715/97.7%,WR+6pp CI[2.9,9.4];100high-band games median177,40%<100,78%<1k; cycle100/85/100. | **C** for choosing WR and reporting cycles, E1/E2; exact figures **U**. Paired seed-cluster CI and meaningful no-op floor required; do not treat384 as independent without design. |
| V20 | 9738–9764, Avineesh |A top-band specialist stalled1800/56.5% below2000 while another won93%;40–70games settles; latest2/oldest evicted; all-active games count in final. | **C** for needing broad coverage/last-two mechanics, **R** for universal40–70 convergence. Climb can affect available evidence, not an extra final-scoring rule. Staff10047 confirms all-active-games wording. |
| V21 | 9766–9785, Avineesh |Blocked-action repair+4373; deepcopy292–423ms→1ms; early sells−80k,split−60–80k,hold−2330,online endgame−7087; dead guards0. | **U** for exact study; mechanisms already investigated E3/E4/E7/MISTAKES. Similar numbers in records are not an independent reproduction or permission to replay failed patches. |
| V22 | 9843–9870, xaxipiruli |Cap opponent hires rather than dropping turns; shrink horizons for lab but transfer fails;96.5% shared action plans; planner/ML/mix alternatives. | **U** for cap curriculum; **C** for broken tape schedules and horizon-dependent payoff, E11–E13. Handicapping changes opponent supply as well as labour. |
| V23 | 9881–9887, Yang |One/two seeds for debugging only; unit ops precede market so same-turn seed purchase cannot fund PLANT; four-game template not strength test. | **C**, E0/E1. Same-turn DROP can still fund a subsequent SELL because those steps are ordered. |
| V24 | 9904–9907, Yujin |Most top ranks likely PPO and share private code; avoid fourth land, focus milk/strawberry. | **U** for private methods/sharing; **R** as universal macro rule. E10 shows demand-conditioned diverse production. |
| V25 | 9910–10021, dzjiann/Kawatta |More coins but loser due scoring bug, later found browser displayed another seed/match; logs can reveal TLE. | **R** for original scoring inference **by author's correction**. Downloaded JSON is the relevant evidence. Runtime20s in a notebook alone does not rule out per-action timeout. |
| V26 | **10041–10047, Addison (staff)** |Final BT uses all episodes between still-active submissions: example637of1000 count. | **C** as supplied primary staff statement; supersedes r3's post-deadline-only claim. No need to infer reset-to600 or treat predeadline churn as free. |
| V27 | 10050–10106, xaxipiruli |Exact interpreter38.5ksteps/s; symbolic mechanics/neural strategy; CEM55350, public145080, relaxed upper195532. | **U** for measurements and proof of bound. Search best is a lower bound;74% achieved does not prove a tight universal bound, especially across opponents/worlds. A hand-designed parameter space is not the game optimum. |
| V28 | 10110–10178, xaxipiruli |Inaction3000; reduced hours/day “impossible” cells;8/12 policy transplants belowinaction;8×13→full727; hire cap8 at5/12wins. | **C** for PASS bank3000 and changed economic horizon. **U** for tables. “Search found none” does not establish impossibility; pure CEM within one executor cannot certify global ceilings. |
| V29 | 10181–10229, xaxipiruli |Recompute each turn/no jobs, soft stickiness:0→23793,.25→27177,1→22755;14Gaussian outputs mostly discrete, priorities only order; PICKUP qty fix26536→40763. | **U** for results. Concrete implementation issues; our E11 already shows commitment and quantities matter. Gaussian scalar encoding of categories is not a new C1 fix. |
| V30 | 10231–10257, xaxipiruli |64daily coefficients +2000tile outputs; per-crop PLANT heads; daily weights drive a per-turn exponential sale rule with price/rival/shed/season/cash inputs. | **U** for whole architecture and incremental value. Rival-stock/uncertainty is separable and cheap; the full neural executor is not. Neutral coefficients need behavioural identity checks. |
| V31 | 10258–10284, xaxipiruli |AST audit65decision sites; exposing constants gives34%/23–71% toy improvements; unbounded logit parameterization, dead dial/wiring audit. | **C** for “verify it fires” principle (MISTAKES C14), **U** for numerical gains/parameterization superiority. Finite numerical bounds and executor feasibility remain. Dead-parameter audit is useful tooling, not independent strategy. |
| V32 | 10286–10326, xaxipiruli |PPO36.7/38.5k vs CEM38/41.2k,0/24 vsuncapped v48; latest0/8,46.3kvs140k;~77% sales gap strawberry/wool; survivingplants~1/3. | **U** for runs. Diagnosis applies to that executor, not our105k C1 or a universal RL ceiling. E11 supports checking missing production before optimizing sale timing. |
| V33 | 10351–10378, xaxipiruli |Pairing SD2.2× lower; seat experiment+228±331 over60 vs+1497on12; crops cost41–50k by displacing831→316animal products. | **U** for samples; **C** for pairing/seed discipline. Same-policy self-play tests seat symmetry, not a replacement for candidate/control vs fixed rival. Animal-only optimum is scoped to their executor. |
| V34 | 10380–10404,10622–10654, xaxipiruli/Syed |BC99.4%; DAgger99.67% but0/24,−99%; corrected to aggregated buffer/op-head only. Syed32teacher games92.7train/69.7heldout,25.8%bankretention16fresh;719-turn single-game fit insufficient. | **U** for exact training; **C** for insufficiency of action agreement. Preserve author's retraction: not fresh autonomous, all-head99.67%. E11 is compatible but not a replication. |
| V35 | 10406–10423,10650–10654, xaxipiruli |Irrelevant Gaussian dimensions saturate99.4%importance ratios; relevance mask→.1%; normalized critic R²−16.6→.83toy; KL controller rescues shared trunk;8/14macro dimensions flat. | **U** for algorithm/results. Must include losing assignment candidates when they can affect choice; observed irrelevance does not automatically prove an unbiased learning mask. No current RL training to patch. |
| V36 | 10425–10471, xaxipiruli |20%PASS throttle179514→312; hire caps16/43/81k; self-play four promotions at3000vs2588; absolute horizon plus mixed batches needed, horizon feature alone−98.3%. | **U** for runs; **C** for external responsive opponents and no-op detection (E1/E11). General curriculum value remains untested. |
| V37 | 10472–10489, xaxipiruli |17280engine steps/episode but30policy decisions; terminals matter; diagonal sweep misleading, crop cliff93% not worker count. | **U** for internal accounting/sweep. A standard full game has719 action rounds;17280 is not its game length. One-axis interventions distinguish causes, but terminals still cluster by seed/opponent. |
| V38 | 10493–10516, xaxipiruli |Dead dials, neutral `getattr` defaults, stale imported workers, silent checkpoint shape filtering break learning; hash code and store head schema. | **C** for verification principles/MISTAKES C14; author incidents **U**. Source snapshot and isolated probe included here. Do not edit a module under a running benchmark and call its output current. |
| V39 | 10530–10533, xaxipiruli |Exact ties prove wiring; farms occupy different positions; because own arms alter rival bank, margins across arms invalid—use own bank/3000. | **R.** Both farms start NW; shared RNG can still distinguish them. A tie alone proves nothing. Paired margin against the same responsive policy captures the intervention's effect on **both** banks. V233 E14 directly refutes selecting own bank alone. |
| V40 | 10546–10566, glossary |Hungarian solves given assignment matrix; potential shaping guarantees unchanged optimum; a completed episode is unbiased; CEM inherently state-blind. | **C** for optimal matching **given** the matrix. Other absolutes **R/U**: matrix need not encode multi-turn constraints; shaping needs discount/terminal conditions, including terminal potential; sampled episodes can be biased; CEM can optimize state-dependent policy parameters even if their chosen vector is fixed. |
| V41 | 10707–10939, Rayk/Talvenn/others |Identical copies1700/>3000; another2678/2374 at16h after one88-coin loss; ecological causes; reset claim later withdrawn. | **U** for exact trajectories/causal attribution, **C** for lag/drift risk and lack of a reset basis (E9/V26). Repeated resubmission is no demonstrated final-score lever. |
| V42 | 10973–11007, Yang/Zukas |36price anchors; marginal-price calculator; net profit/tile-day/worker action plus cash/time/demand; portfolio across worlds. | **C** for accounting requirements, E0/E12/E13;36-check implementation **U**. No new macro option overcoming measured execution capacity. |
| V43 | 11025–11040, Georgy |811submissions/224523submission-games; after5/10/20/40games median gap718/338/222/145;5h median123,quartile>400; long-lived groupgap542 vs78. | **U** for statistical audit. Supports rejecting fixed convergence times, but “last-ten mean settled truth” itself mixes later population drift and survival/retirement selection. |
| V44 | 11349–11412, staff/Georgy;11591 |Daily-dump selection repeated; question whether Snorlax RL actually surpassed his deterministic submission remains unanswered. | **C** for selection policy; **U** for which private final slot is strongest. Do not upgrade “silver RL” to proven best private final policy. |
| V45 | 11989–12002, Georgy |Trickle3/unit-turn: passive+280±89,8/8; responsive−547±6 and rival+593±21; combined+46;hold175turnsvs7. | **U** for exact experiment; **C** for the shared-market externality mechanism E3/E14. Their stated gap1154 does not equal rounded547+593=1140; retain as reported, not exact reconciliation. No generic patience layer. |
| V46 | 12082–12273 |Repeated cow repair, copying, layered runtime, tape400/runtime1640, small mirror adaptation, proposed second-slot runtime. | Same T07/M06/I06 statuses. Repetition is not independent confirmation. No new measured executor or transferable policy appears at EOF. |

## Notebook-refresh addendum: claims checked against the local files

All five requested notebooks' markdown was read in full and extracted to `build/astra/notebook_notes_sources.md`. These are saved local artifacts, not claims that their live webpages currently have identical contents. I did not execute their download/build cells or follow external links.

| Notebook / cell | Claim | Verdict |
|---|---|---|
| leoprovorov reverse-engineering,5 |T4 preempts parent-planned sales by1turn, adaptive2turns, credits prevent double-sale;6/6 on3worlds;crop guard+196on1world/0on2;new day21 watering repair. | **C** that lead/credit mechanics already exist in our C1 lineage;6/6 is only3worlds and exact incremental gain **U**. A localized watering repair needs a demonstrated missing watering event on C1R2; no basis to reopen general rescue. |
| leoprovorov,9–10 |2,835episodes,64ordered shop pairs; day6 router14named pairs/10continuations; day27 liquidation plan2. | **C** for this style of public chassis and early commitment (E6); exact notebook-specific mapping **U** here. Not a new private-family decode or a new day9 headroom result. |
| degnonguidi utils-v1, all markdown |The saved markdown is exactly the same text as the leoprovorov write-up. | **C by local comparison.** This is one write-up appearing at two local paths, not independent evidence. It does not establish why the files match or that all their code is identical. |
| georgymamarin,0/34 |Dataset described as every finished game; later explicitly called crawl with coverage gaps, best-game fingerprints, smallH2Hcells, serial correlation, excluded validation games. | **C** for caveats; **R** for literal completeness. E18 quantifies missing current top20; best-game statistics are not average policy behaviour. |
| georgymamarin,19 |Exclude elbow_day correlation.8 because derived from final bank. | **C** for target-derived feature warning. No causal reinvestment/land rule follows from bank-curve shapes. |
| georgymamarin,30 |Weeds only few hundred while raw banks vary tens of thousands, so nearly everything is matchup. | **U** for variance decomposition on present agents. Seed→shop feedback E6 can be much larger; a weed-only ablation doesn't eliminate shop/opponent interactions. |
| georgymamarin,32;destbreso,16/40 |Nothing observable differs before48; therefore opening agreement says nothing. | **R** as game-wide claim. Farm/market transactions visible immediately; weeds after first day. Shared fixed openings are empirical, and h48 should be checked over seeds and opponents. |
| destbreso,7/12/15 |Two shops fix a world; up to9shops; within-pair navy means responsive policy; third branch open. | **R** for9(max8) and full-world equivalence. Variation can arise from later shops, weeds, finance and repairs. **C** that within-pair comparison is stronger than global stripes; E6 already measured the third-branch ceiling on our chassis. |
| destbreso,16/18 |Plan1.000 proves exact lineage; WHOLE1.000 means same game; .98connected-component opening grouping. | **C** for observed action agreement only. **U** for private-source identity; transitive closure can join two endpoints below the similarity threshold. No private architecture proof. |
| destbreso,20/22 |Aug30 leader seven cows,280CARE,13fallow,442stranded;Sep10SE12%,day18exact10tomatoes,~12%labour,unchangedownbank5firings. | **U** for exact historical counts; E13/E14 supersede “remove annex” inference. Baseline date is explicit; don't call this today's top20 macro. |
| destbreso,24/26 |Market crater damage≈victimqty×drop; occupancy chi-square and half-split correlation prove spatial pattern. | **C** as descriptive diagnostics, **U** as causal effect. A counterfactual sale curve and tile legality/route costs are needed; per-turn cells are not independent samples. |
| destbreso,28/30 |Leader53.8%walking3.8%idle vs42.9/11.8;490seasons hireIQR0–2,~12handsfromd13. | **U** for counts; consistent with E10's low idle, but movement share differs by sample/date. No instruction to minimize walking in isolation. |
| destbreso,32 |Drift≤1rating/episode plus signflip implies settled; sibling suppresses pairing; falling cadence indicates certainty. | **U** as statistical guarantees. Threshold is a heuristic, not calibrated convergence; scheduler effects and opponent changes confound it. Count new episodes, not repeated polls. |
| destbreso,36/38 |Five-action phrases diagnose scripts/branchers; recovered7forks in8episodes; stumps+permutation+leave-one-out extract trees97% predictable. | **U** for replication and policy transfer. E11/r3 branch reconstruction already failed execution; inferred tree must hold out submissions/dates, not just near-duplicate episodes. |
| ashok205,0 |Archive ranks teams from each day's rating evidence, selects top10 and keeps compact bodies; not ranking by ZIP file order. | **C** as stated local archive design; no new strength claim. Per-daytop10 selection cannot promise coverage of today's top20. |

## Cross-check against the decoded field and all 20 current names

This is a coverage/claims check, not a substitute for opus/opusb's detailed dossiers. `top20_cache_audit.json` aggregates the existing Sep 23–25 exact-replay cache against the **current** `top20.json` names. Exact-name absence is reported as missing, not inferred inactivity, a new architecture, or zero win rate.

| Rank | Team | Cached seats / unique episodes | Mean bank | Recorded win fraction, ties half |
|---|---|---:|---:|---:|
|1|DECEM|457/457|105,479|.575|
|2|Boey|159/159|99,547|.635|
|3|M & M & P & Q|279/279|106,497|.620|
|4|Vadim Vasilenko|477/477|103,514|.482|
|5|Majkel1337|210/210|108,155|.486|
|6|DSM|363/363|107,097|.882|
|7|Unknown Mother-Goose|394/394|106,862|.551|
|8|Fourth Quadrant|120/120|95,830|.633|
|9|Just A game on your lips|0/0|—|—|
|10|Anton Tikhonov|0/0|—|—|
|11|KawattaTaido|4/4|96,845|.250|
|12|Azat Akhtyamov|43/43|100,657|.163|
|13|有辣条有权|0/0|—|—|
|14|kigasudayooo|0/0|—|—|
|15|TheEggman|26/26|97,799|.115|
|16|Arda Ceylan|7/7|106,392|.000|
|17|atsushi11o7|0/0|—|—|
|18|Yizhou|0/0|—|—|
|19|My second life|0/0|—|—|
|20|We wanna be tomatos|0/0|—|—|

**These records have unequal opponents, dates and submissions; they are not a strength ranking.** Azat's low archived fraction does not refute today's rank12. Arda's0/7 is seven difficult historical matchups, not a proven weak policy. Both seats of an episode appear in the population, so cross-team rows are also dependent. The absence of eight current names means that even 1,773 exact episodes cannot support “we decoded all current top20 policies” or field-prevalence weights.

The rows do directly falsify using raw average bank as a ladder order: Boey banks less than Majkel but is ranked much higher; DSM's archived WR dwarfs nearby-bank peers. The right interpretation is that **opponent composition and interaction matter**, not that these descriptive contrasts isolate a particular winning mechanism.

The larger r5 family decode cross-checks these forum ideas:

- **Shop-conditioned mixed production exists.** Cows/sheep/strawberries/carrots/tomatoes correlate strongly with early demand; reported regressions reach R²~.82/.95/.85/.75/.62. That supports a conditional macro hypothesis, but O1–O3 show that adding its targets to C1's executor is not sufficient.
- **Labour is expensive and nearly fully occupied.** ~294 hires/~6.4k, almost no idle from day10. The family skips roughly half of pre-bonus watering opportunities, saving about7% labour. This is already part of the decoded efficient schedules; “water less,” “hire fewer,” or “use all100tiles” are not independent new options.
- **Same opening is not the same whole policy.** Common staged cow/wheat/sheep purchases and shared unit prefixes are observed; branches and sale timing differ. Neither shared action hashes nor startup overage proves common private source, PPO, or a specific optimizer.
- **Fourth land is an endogenous decision, not free money.** Family 4q-vs-3q within-game association was only+187±454 over219 comparisons; O1 lost after explicit firing. Current C1's native V219 and V233 already implement narrow late opportunities/denial. Their gate ablations supplied much stronger evidence than macro correlation.
- **Exact state reconstruction does not reconstruct private policy.** The cache reproduces banks in1,773/1,773 cases; raw tapes still won only8/125 against C1. This distinction disposes of the most common false inference in the discussions.

## New source-level result: censored events are counted as forecast misses

This is the one new executable diagnostic in this lane. It isolates `_v92_q_update` from the **current C1R2 file** using Python AST, supplies small synthetic observations, and does not import or modify the agent.

At `subZ_C1R2.py:3632`, the update ignores an item's observed inventory changes when the previous quote is≤3. At3644–3658, it later finalizes that time window: a library event without a nearby recorded observation receives a false-positive count and−1 score. There is no “observation censored” state in that decision. The forecaster then chooses the best-scoring library member even when all have little or negative evidence (`best` initially0; argmax at3669).

| Synthetic case | Actual latent opponent MILK sale | Public MILK inventory delta | Candidate0 predicts MILK sale; candidate1 does not | Winner |
|---|---:|---:|---|---|
|$1 floor, hidden sale|8|0|scores[−1,0]|candidate1|
|$1 floor, no MILK sale; eight WOOL sales give equal cash proceeds|0|0|scores[−1,0]|candidate1|
|Observable sale control|8|8|scores[+1.5,0]|candidate0|

The first two cases are identical in the observations consumed by the scorer. Both can also have equal public bank changes: eight hidden MILK sales versus eight hidden WOOL sales yield the same $8. The engine hides both from market inventory, while the remaining private commodity stocks differ. Therefore absence of an inventory-derived MILK event is not reliable negative evidence. **This establishes a modelling issue, not a measured loss.** Floor sales themselves are worth only1, and changing a matched stream matters only if it improves subsequent decisions at meaningful prices with actual stock available. No game-level frequency, oracle headroom, or WR uplift has been claimed.

A proper fix also needs to handle partial visibility inside a batch, the existing minimum observed quantity2, own actual fills rather than requests, and the±1 matching window. Simply changing one comparison from3 to1 is not a validated solution.

## Ranked untested work, with time caps and kill tests

These are proposed bounded experiments for the next round. They have not been run or implemented as agent patches in this lane. Use at most two foreground workers, with priority10 where supported, and direct all astra outputs into `build/astra/`. Do not execute an old multiworker harness unchanged or let its default output path escape that directory.

### 1. Censor-aware forecast scoring, then evidence-based abstention — 3–5 hours

**Forum source:** M27/V05 and the exact-fill accounting M13. **New evidence:** E16. **Why not a rerun:** C1/C1R2 changed libraries and competing forecasts; neither the record nor current code shows a tested observability mask or calibrated abstention for PREDICT2.

First instrument the unchanged C1R2: count finalized library events in censored±1 windows, best-stream changes attributable to those penalties, subsequent forecast fires, physically available quantities, and actual revenue/margin effects at quotes>1. Freeze the source hash. Use archived exact replays only to validate observed-vs-hidden sales and mask correctness; no reactive strength inference from that stage.

Then compare three predeclared arms: unchanged; skip only invalid negative evidence; mask plus abstain when observable match support is inadequate. Keep plant/animal/route actions untouched. Choose any support threshold on a disjoint calibration slice, preferably held out by **opponent submission/date**, not episode parity. Require baseline identity when the new condition never fires, separate error counters, and no change to unobservable private inputs.

**Kill early:** censored penalties never influence a physically executable later sale, or a perfect-information diagnostic restricted to those altered decisions has negligible recoverable margin (e.g.<100/g and no flips in a40-seed exploration panel). This diagnostic may use ground truth only as an upper bound, never as an agent feature. Kill the patch if its chosen policy does not improve responsive paired WR/margin after the shared gate below. Limit to these arms; no broad threshold fishing.

### 2. Measure the residual ordering opportunity; test an opponent-model change — 4–6 hours

**Forum source:** M13, V06, V13. **Existing implementation:** `moe/opus/frozen_brx2_v1.py`. **Why conditionally new:** old BRX2's online native-vs-SIR model has not been established as an improvement to the present C1R2 ordering stack.

First log the existing `_V44Y_REPORT`, `_CXD_REPORT`, `_CXD_PARENT_ORDERS`, and final outgoing market queue. Confirm both layers really execute and measure how later T4/IG transformations alter the proposed list. Count multi-SELL turns, then count **different feasible orderings with positive incremental value beyond the current output**. Sonnet's49–55multi-SELL turns/game establish exposure, not unused opportunity.

For a bounded oracle diagnostic, use the actual other agent's contemporaneous orders/stock only in the offline evaluator to bound **same-turn** improvement over the final C1R2 queue. Do not call this an attainable season gain: cash, future response and policy state can change. If residual value is tiny, stop before porting. If present, compare the unchanged self-list model against a BRX2-style inferred mixture, or a model informed by credible sale events from test1. Start with model inputs; avoid double-applying a second full permutation stack.

**Kill early:** no residual attainable order changes, no support for the proposed opponent model, malformed/over-cap queues, changed planned quantities/necessary finance, or non-firing code. Preserve deliberate empty slots and fixed-order finance unless an exact simulation explicitly evaluates moving them. Per-item factorization is exact only within the model's no-shared-cash/capacity assumptions; recheck constraints on risky turns. Promotion requires the responsive shared gate, not old0.844 public WR or open-loop whisker flips.

### 3. Opponent loose-stock intervals as a forecast filter — 5–8 hours, only after an information ceiling

**Forum source:** dzjiann8074–8118. **Why not a rerun:** C1 predicts sale ticks from library matching and uses assumed clone stock for ordering. A calibrated public-state conservation interval, tested against hidden ground truth and used to reject impossible predictions, is not in the measured record.

For each item, maintain total loose stock across both farms and subtract our own total (shed plus all carried inventory). Use

`ΔS = H − C − (ΔM + D) − F − L`.

Here H means goods actually entering loose inventory, not every unit of standing tile production. C includes actual consumption; D is exact town draw at the correct turn; F is inventory-invisible floor sales; L is private loss. Handle harvested standing yields, collection, feed, overflow, end-of-day auto-drop, and ambiguous transitions. **DROP itself is an internal transfer unless it loses stock.** Treat ambiguous production/consumption as interval changes too. The result is total opponent stock, not its sale-ready shed or per-unit location.

Validate first on exact full replays where hidden inventories are available for scoring: coverage of intervals, width, MAE by product, floor regime and day, held out by submission/date. Author MAE0/.008 is not an acceptance guarantee. Broad intervals may be correct and useless.

Then use only conservative impossibility constraints or uncertainty features: reject a forecast requiring more than the upper bound, or abstain when too uncertain. Do not sell simply because the rival has stock. **Kill:** true stock falls outside claimed deterministic bounds; intervals give no information beyond present prices/observed harvest; an oracle-stock diagnostic leaves insufficient residual opportunity; or responsive paired results fail. Do not build a new neural trader first.

### Shared gate for any surviving arm

1. Pin agent/engine hashes, list raw seeds, and predeclare comparisons. Keep current C1R2 untouched as control. Treat a seed's seat-swapped results as one cluster; also preserve same-seed dependence across opponents when bootstrapping.
2. Use an initial40fresh-seed responsive panel with C1, C1R2, shepherd, hyb2965, sirV1, f55V2, pipe16; include koshinm and one non-clone counter as stress cells. Both seats check correctness. Compare candidate and baseline **against the same opponent policy**, not just candidate versus baseline head-to-head. Keep quantities/error/firing logs. Do not globally set `_V92_EP` and silently disarm the baseline's P library.
3. Freeze one surviving patch, then use at least40additional untouched seeds for confirmation; increase only if predeclared power requires it. Select on paired WR with ties half, and report paired margin plus both banks as explanatory measures. Require a positive pooled paired WR effect with a seed-cluster interval excluding0 and no material regression in the target/counter cells. If the limited panel is inconclusive, do not assert an improvement.
4. Refit/rerun the lineage RR map with matched seeds and unchanged anchors. Report **paired candidate−C1R2** uncertainty, not overlap of separate absolute CIs. The old lower-bound>2148 bar alone is obsolete for replacing a2152-point candidate. Require evidence of improvement over C1R2; ~+60mapped points would make the current bronze gap plausibly consequential, but do not require that arbitrary magnitude to record a real smaller gain. If anchors fail retrodiction, no strength promotion follows.
5. Exact replay substitution can explain event-level differences and test reconstruction. It is **not** the primary promotion gate for a market patch that changes opponent incentives or actions. C18 already demonstrated the failure. Passing a gate is research evidence only; no submission is authorized in this lane.

These gates can reject candidates, not certify a3k policy. Five public-lineage anchors around1800–2100 do not identify performance against hidden top20 programs. New dumps improve diagnosis/holdouts, not the ability to run those private programs counterfactually.

## What stays closed, and response to sonnet's round 1

**Closed without new mechanism:** repeating premium floors; unconditional early/split/hold sales; broad buy rescue; day9 router refit; raw/nearest-neighbour/day-spliced tapes; a new low-level BC imitation run; O1/O2 herd/SE expansion on C1; O3 tomato selector changes; V233 removal; blanket carrot removal; and choosing by own final bank. Exact duplicate/frozen ratings and screenshot ranks do not reopen any of these.

**Not mathematically disproved but not a deadline plan:** a complete learned macro policy with a coherent executor; persistent program imitation trained on autonomous states; recurrent league PPO; a fully stock-aware multi-turn market planner; universal strong crop/herd adaptation. Each needs missing machinery and fresh responsive validation. “Untested” does not make it higher priority than an existing measured option.

**Sonnet:** agree that small market changes are the only plausible cheap remaining surface and that the RR instrument is marginal, not a top10 predictor. Three corrections to [sonnet.md](sonnet.md):

1. BRX2 was not lost without consideration. `moe/r3/opus.md:147–166,215` explicitly parks BRX2/delivery as≤+35 and below the then-valid live resolution. More importantly, C1R2 already has V44Y/CXD exact lockstep margin ordering (E17). The new test is **incremental opponent inference/residual coverage**, not “add exact queue ordering.” The old pool mean.844, or beating old sir/f55, supplies no current incremental effect size.
2. Reject using replay substitution as the primary whisker gate. Being too small for an absolute RR mapping to resolve does not make an invalid instrument valid. Use a seed-paired candidate−control estimate with responsive opponents, or call the result unresolved. Recorded loss flips are for diagnosis.
3. Macro-graft failure shows those options on that executor failed. It does not isolate per-hand tile ownership as *the* cause of the top-family gap. Georgy's toy shared-list/sliced-list contrast is a useful mechanism example, not our top20 intervention. Likewise, checking C1R2 labour might document unchanged premises, but without a specific change it is not a reason to rerun the already large O1/O2 losses.

No THREAD post was made because the user's allowed write paths exclude it. The concrete next action I would put in the thread is: **astra: instrument censor-aware PREDICT2 scoring and bound its later-sale opportunity; sonnet/build owner: measure residual value beyond C1R2's existing V44Y/CXD ordering before a BRX2 port. Use the same responsive, seed-clustered gate.**

## Final-pair forecast under the best plan

These are subjective planning probabilities, not posterior probabilities calculated from the RR interval. Assume the present C1/C1R2 pair is preserved unless a bounded test earns a replacement, and approximate current cutoffs remain relevant. C1R2's mapped 2152 is about 58 points below bronze, 258 below silver, and 732 below top 10; the two agents are strongly related, so their outcomes are not independent chances. Field changes and weak anchor calibration dominate the uncertainty.

No available evidence supports multiplying either the old public WR or a self-bank gain into a large medal forecast. The best plan is one carefully measured information/ordering improvement, then stop if it fails. A full executor rebuild is not assumed to arrive by the deadline.

**P(bronze) = 30%. P(silver) = 4%. P(top-10) = 0.2%.**
