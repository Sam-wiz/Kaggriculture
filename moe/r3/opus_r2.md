# MoE r3 — Opus round 2 (cross-examination), 2026-09-25 19:20–19:50 UTC

Clock note: `date -u` on this machine reads 09-25 19:2x UTC as I write. Fable's header ("09-26 ~01:00 UTC")
and its choreography table are in **IST labelled as UTC** (+5:30). Shift Fable's times back 5.5 h.

## 0. New evidence I ran this round (2 workers, ~8 CPU-min, scratch in `/tmp/opus_r3b/`)

Recipes are in the appendix so they can be rerun (/tmp is not durable).

| id | test | result |
|---|---|---|
| **E-A** | **PREDICT ablation, closed-loop.** Shepherd vs public `rivals4/kaggriculture-yummers` on the 14 recorded WLV seeds and seats (kagsim). `_V92_P_K` and `_V92_Q_K` set to 10^9. | PREDICT on: **+$1,525/g, 13–1**. Off: +$193/g, 8–6. **Paired +$1,332/g** (median +916, SE 369, 13/14 positive). PREDICT fires 21×/game, 146 units/game. The PREDICT2 wrapper (`_V92_Q`) fired **0 times**, so it is dead code in shepherd. The baseline reproduces my round-1 `wl_closed.jsonl` numbers exactly. |
| **E-B** | Library fingerprint (`_V92_P_BLOB`/`_INDEX`) | Shepherd = hyb2965 = sir2 = **hybu** = pipe18: one library (md5 f9af90ba, **2,398 streams**). The WL family (yummers, a-wonderful-life, 2950-peak, song-of-ice-and-fire) carries a **different** library (386fdddb, **1,998 streams**). All share the same `_R108_DATA` tape and all carry `_v92_predict`. |
| **E-C** | **Library swap, closed-loop, same 14 seeds** | (i) Shepherd with WL's library vs yummers: **+$2,104/g, 14–0**, paired +$578 over stock shepherd (median only +$51, SE 234). (ii) Stock shepherd vs WL with **our** library: shepherd still **14–0, +$1,966/g**; WL gets *worse* by $441. |
| **E-D** | Fable's `moneytrace.json`, split by opponent opening (≥2200 mirrors) | **(5,0) = WLV**: n=9, 1–8, mean −$871; **d13-24 −$651**, d25-29 −$336. (20,15): n=11, 2–9, −$335; d13-24 −$123. (8,3): n=5, 1–4, −$186; d13-24 −$137. **WLV is 63% of all dollars lost** to ≥2200 mirrors (−$7.8k of −$12.4k) and 74% of the d13-24 drip. |
| **E-E** | Re-read of Claude Code's `identify_pilot.jsonl` | The best candidate reaches **prefix 53** on 4 of 5 games: leoprovorov song-of-ice-and-fire (WL family) on 113387637/113364432, and subV_sir2 on 113363678/113349528. It reaches **121** (hyb/pipe family) on 113352134. **Shepherd itself diverges at step 0 on 5/5.** The pilot pool was rivals7 + 3 of our builds; rivals1–6 WL copies were not in it. |
| **E-F** | Claude Code's `wlv_pull.md` / `wlv_exact.log` (read at 19:37 UTC) | **NEGATIVE.** The current 09-26 versions of a-wonderful-life and 2950-peak diverge at **step 53** on all 14 WLV games, the same as the old copies. **WLV is private beyond t=53.** A second private family (7 opponents, 2158–2560: luyinn, takaygiiiiiiii, Sathwik, …) matches `leoprovorov/four-turn-forecast-v2` to **step 91**. |

What these results mean:
- **PREDICT is not a whisker.** It is the single highest-leverage layer we have measured closed-loop (E-A).
- **Library content moves money by hundreds of $/game, but noisily and not in a predictable direction** (E-C).
- **The WL→WLV ~$2k delta is not "WL + our library"** (E-C ii). That fits the step-53 **unit-level** divergence (hand 0 idles): WLV changed non-market layers too.

---

## 1. Agree

- **Fable F1 / my round-1 §3: pre-deadline churn is ~free**, because the final ranking is a static BT fit. My confidence in *why* has changed (§4), but not in the conclusion.
- **Fable 1b.** The unit channel replays exactly (54/54 banks to the dollar), and the whole ranking sits in the d13-29 market channel. E-D refines this: most of that money is one family.
- **Fable 1d.** PREDICT is the lever, and our library is one frozen snapshot. E-A confirms the lever at +$1.3k/g on/off.
- **Fable 1d.** hyb2965 is **not** a chassis hedge: it has the same library and the same tape as shepherd (E-B). I withdraw "hedge" and keep it only as the control arm.
- **Claude §2.1.** Exact closed-loop reproduction, on the recorded seed, is the identification test. This is my instrument A, and I agree with pre-registering validation before it ranks anything.
- **All three.** Stop using the public-pool gate and open-loop replay to rank market layers. Medal cutoffs on the 09-25 16:12 snapshot are 2239 (bronze) and 2437 (silver).

## 2. Dispute — the weakest claim in each position

### Fable

1. **"The (5,0) family matches no public agent we hold; stop trying to identify the mirrors."** Half right: E-F confirms the code is private beyond t=53. But the premise and the recommendation are both wrong.
   - Seven library files open `BUY_PRODUCT WHEAT 5`: rivals/, rivals4/, rivals5/ copies of a-wonderful-life, yummers and 2950-peak, plus rivals7 leoprovorov (`opus_scratch/wl_games.json`, field `cands`).
   - All seven match every one of the 14 WLV games **to exactly step 53**.
   - Fable ran only 5 agents (hybu, pipe18, v15stack, V57, hyb2965), none from the WL family.
   - Identification is how we know that **63% of our band losses are one agent with a known public prefix** (E-D). That is what makes a rebuild targetable. Stopping it would throw away the only concentration we have.

2. **SCL tier 1 (price-conditioned tape) cannot pass V2 for the family that matters.**
   - Every band agent carries `_v92_predict` (E-B). They react to *our* sale stream through the library, not to price.
   - E-A shows that reaction is worth ~$1.3k/g, so tier 1 models the wrong trigger.
   - Tier 3 is "run the actual v9 overlay against us". That is my instrument A with a reproduced opponent. SCL therefore collapses into A, and A needs the WLV code or a rebuild.

3. **C1 (refresh our PREDICT library) as the first build.** The lever is real (E-A), but the claimed gain is not supported by any validated number:
   - "Half of the d13-29 loss ≈ +$400/g" assumes the refresh recovers WLV's edge. E-C shows a library change moves results by ±$500/g with median ≈ $50, and changes the sign game by game.
   - Its only offline check, the leave-one-out forecast hit-rate, measures forecast accuracy. It does not measure dollars after the rival's own PREDICT reacts.
   - So C1 can be validated only live (SE ±65 per read, so effects ≥+150 only), or closed-loop against a reproduced WLV. **Either way, WLV reproduction comes first.**

4. **The hybu probe (C6).** Not worth a slot.
   - It has our library and our tape (E-B), and the (20,15) opening already live as hyb2965.
   - Its gate result was +0.046, z=0.93 (HANDOFF l.915). Its "+$385 vs shepherd" is one seed.
   - Cost: it evicts shepherd now, so the first real candidate then evicts hyb2965 before hyb2965's read completes (~09-26 03:00 UTC).
   - P(≥+150 over shepherd) ≲10%.

### Claude Code

1. **"The band is shepherd + a market overlay; X is plausibly a public overlay we hold."** Refuted by Claude's own pilot and by the openings.
   - Shepherd diverges at **step 0 on 5/5** pilot games (E-E).
   - Shepherd's own (8,3) opening appears in only 5 of 34 ≥2200 games. The rest are WLV (5,0) and the (20,15) family.
   - ≥97% unit-op identity does not mean "shepherd". It measures the **shared tape** (`_R108_DATA`, identical in ≥9 files: WL×4, shepherd, hyb2965, sir2, hybu, pipe18).
   - Instrument step 2.1 (shepherd + X_i) therefore puts every candidate on the wrong chassis for ~85% of the band, and would identify ~0 games by construction.

2. **ADDENDUM 2, "all diverge at step 0-1".** This misreads `identify_pilot.jsonl`: the best prefixes are 53/53/53/53/121.
   - The low match fractions (0.68–0.81) are the closed-loop tail after divergence, not evidence of a different agent.
   - Please retract it in HANDOFF. It is feeding Fable's "stop identifying".

3. **"Freeze 09-28 12:00" and "protect the anchor."** Neither has a rationale under a static BT fit (§4). Recency eviction is only a scheduling constraint on reads.

### My own round 1

1. I stated **"the final BT fit uses post-deadline games only"** and "ratings reset to 600" as fact. That is not established (§4).
2. **"WLV ≈ WL wrapper + herd layer(s)"** was a guess with no test. E-C now rules out the cheapest alternative (WL + our library). The library-with-*our*-streams variant is still open (§5).
3. **"Stop building overlays measured against public opponents; ≤+35."** That was right for BRX2 and delivery, and wrong as a blanket rule. PREDICT-class layers are worth $10²–10³/g closed-loop.

## 3. Changed my mind

- **Fable's lever is real.** PREDICT on/off = +$1,332/g closed-loop (13/14), against an opponent that also runs PREDICT. I rank "tune the PREDICT layer" as #2, not "stop". It is tuned only against reproduced band opponents, never against public ones.
- **Fable's asymmetry hypothesis (1d) is now the most important open question.** It says the band's library contains *our* public streams, so they pre-empt us and we cannot pre-empt them.
  - If true, it is the same fact as "WLV beats us 11–3", seen from the mechanism side.
  - It is directly testable closed-loop with code we hold (§5). That test is cheaper than either full build.
- **WLV exact is dead** (E-F). My round-1 #1, which I gave ~45%, is gone. WLV can only be rebuilt, and the rebuild must now reproduce a private delta.
- **hyb2965 is a control, not a hedge** (Fable).
- **BT window:** confidence in "post-deadline only" drops from ~95% to ~60% (§4). The conclusion "churn is free" stays at ~95%.

## 4. Do pre-deadline episodes enter the final BT fit? (checked in `discussions.md`)

**What the sources say:**

| source | line | what it says | weight |
|---|---|---|---|
| Staff (María Cruz) | 103 | Submissions keep running for two weeks after the deadline, then "a single Bradley-Terry Tournament". **Silent on the data window.** | primary, but ambiguous |
| Kavinkumar | 128 | Asks exactly this question, 5 days ago | **no staff answer** in the dump |
| Alex Paul | 139 | Asks exactly this question, 14 h ago | **no staff answer** in the dump |
| aisamhottman | 4314 | Paraphrases topic 732931 as a fit "over episodes between agents that are both still active at the deadline" | user paraphrase, not staff wording |
| Staff (Addison Howard) | 4343–4347 | Answers team score and ties; does not correct the paraphrase | weak support |
| Users | 4889, 5317 | "Reset to 600" | user lore |
| Users | 8303 vs 8316 | Disagree on whether Orbit Wars reset | contradictory precedent |

**My probabilities:**
- Post-deadline games only: **~60%**.
- All games between agents active at the deadline, including pre-deadline: **~35%**.
- Full history, including evicted agents: **~5%**.

**The operational conclusion holds under all three (~95%):**
- BT is a static fit. There is no path dependence and no "start at 600" penalty.
- A final agent's pre-deadline games are unbiased samples of its strength. At most ~300 games against ≥2,000 post-deadline (7 games/h/slot × 336 h, more if the rate is raised).
- Probes evicted before the deadline drop out in the two likeliest readings.

**The one practical difference:** under the 35% reading, uploading the final agent earlier adds a few percent more games to its fit, with no bias. That is not worth trading information for, so it does not change the plan.

## 5. Deciding experiment — WLV-first (Opus) vs library-refresh-first (Fable)

The disagreement reduces to one mechanism question: **does WLV beat us because its library forecasts *our* stream (Fable 1d), or because of non-library layers (my step-53 evidence)?** E-C already rules out "WL + our f9af library". The remaining library hypothesis is **"WL + a library containing shepherd's streams"**. That is what any fork built after 09-22 could have recorded by running shepherd locally.

**Budget and preconditions:** ≤2.5 h wall, 2 workers, no submissions. `wlv_pull.md` is negative (E-F), so both arms run.

1. **W1, 0:00–0:40. Record shepherd's streams.**
   - Run shepherd self-play on ~200 fresh seeds in kagsim (~5 s/game), covering every shop pair ≥3×.
   - Recover each seat's premium sales with the exact `_v92_p_update` rule (MILK/WOOL/STRAWBERRY/EGG/MELON, price >3, ≥2 units).
   - Encode them into the `_V92_P_BLOB` format keyed by the first two shops (the decoder is `_v92_p_pair`; the encoder is its inverse).
2. **W1, 0:40–1:00. Build WL+S.** Take public yummers and append the shepherd streams to its 1,998-stream library. Keep a control: **WL+R**, the same count of streams from *random other* band agents (sir2/hyb2965 self-play).
3. **W1 + W2, 1:00–1:30. Closed-loop test.** Shepherd vs WL+S and vs WL+R on the 14 WLV seeds and seats, plus 20 fresh seeds (68 games).
4. **W2 in parallel, 0:00–2:30. Rebuild bisection (note B of round 1).**
   - Graft shepherd's non-market layers into yummers one at a time, in wrapper order (`herdsafe_forecast_agent`/`_HP_*`, the `_HS4` stack, `rescue_agent`, `_y_controller`).
   - Metric: median first-divergence step vs the recorded WLV actions (`opus_scratch/exact2.py`).
   - Continue by bisection until t=53–58 and t=84–91 match.

**Pre-registered reading** (live target: shepherd 3–11, −$546/g vs WLV; baseline vs public WL: 13–1, +$1,525):

| outcome | who is right | first build |
|---|---|---|
| Shepherd vs **WL+S** ≤6/14 with mean ≤ −$200, **and** WL+R stays ≥11/14 for shepherd | **Fable** (asymmetry confirmed: a library with our stream flips a $1.5k win into a live-sized loss) | (a) **C1-prime:** our library + band streams, **plus stream decorrelation** (shift our premium sale ticks off the public shepherd schedule so rival libraries mis-forecast us). (b) WL+S+herd becomes the WLV instrument. |
| WL+S moves < $500/g, or WL+R moves as much as WL+S | **Opus** (the edge is non-library) | WLV rebuild via W2 bisection. C1 stays behind it, tuned against the rebuild. |
| W2 reaches median divergence ≥600 **and** shepherd vs the rebuild ≤5/14 | **Opus** regardless of step 3 | Rebuild ships as a probe (gates in §6). |
| Both | Both | WLV+S (rebuild with a shepherd-aware library) is the candidate; C1-prime is tuned against it. |
| Neither | Neither | No upload. The hyb2965 read decides; live-only probes need a written ≥+150 prior. |

Either result gives a validated closed-loop opponent for the dominant family. That is exactly what C1 lacks today.

## 6. Revised top-3 plan (owners; times UTC)

**Owners:**
- **CC** = Claude Code: orchestrator, and the only one with Kaggle credentials and uploads.
- **W1, W2** = the two builder workers. Opus/Fable may take either.

| # | item | owner | gates |
|---|---|---|---|
| 1 | **WLV reproduction via §5.** WL+S if the asymmetry test confirms, else the layer-graft rebuild. Exact is dead (E-F). The same bisection can later target the four-turn-forecast-v2 family (divergence at t=91). | W1/W2 (build), CC (upload) | Median divergence ≥600, **or** WL+S passing its §5 row. **Plus** retrodiction: shepherd vs it ≤5/14 on the WLV seeds. Plus `kaggle_load_check`. As a *probe*, it must also beat shepherd and hyb2965 closed-loop on 24 fresh seeds. |
| 2 | **PREDICT-lever tuning (Fable C1, generalised).** Library = f9af + post-lock band streams (860 tapes) ± WL's 386f; sweep K ∈ {3, 4, 6}, H ∈ {24, 48, 96}; optional sale-tick decorrelation. Carrier = #1 if it exists, else hyb2965/shepherd. | W2 after §5, then W1 | Fable's kill test 1 (leave-one-out forecast +10 pp). **And** closed-loop vs the #1 opponent plus exact hyb2965/metav4-v13 games: ≥ +$150/g paired over the carrier. Tuning against public WL is **not** allowed. |
| 3 | **hyb2965 as control; no hybu probe.** Read it at ~03:00 on one fixed LB snapshot, with a per-family WR table. | CC | If its fit vs ≥2000 is <2150 at ≥20 band games, shepherd or the best read replaces it as the fallback finalist. |

**Timeline:**

| time (UTC) | action |
|---|---|
| **09-25 19:50** | W1/W2: start §5. The pull is already done: negative. CC: log E-A…E-F in HANDOFF (append-only), and retract ADDENDUM 2's "diverge at 0-1". No upload tonight. |
| **~22:30** | §5 read-out, written into HANDOFF. If the rebuild or WL+S passes its gates, CC uploads it no earlier than 09-26 03:00, so hyb2965's read completes first. |
| **09-26 03:00** | CC: read hyb2965 (~20+ band games). Then upload #1, or the first #2 build that passed, evicting the older slot. |
| **09-26 → 09-29** | ≤2 uploads/day, ≥8 h apart. Each probe gets a written prediction (WR vs WLV, WR vs ≥2200, fit vs ≥2000) and a read at +8 h and +16 h. Kill rule: fit < best −100 and WLV WR ≤ best's at +8 h. CC re-fetches every ~8 h; W1/W2 iterate #2 against the reproduced opponents. |
| **09-30 06:00** | CC uploads the hedge: the best-read build from a *different* market family or library than the finalist. |
| **09-30 12:00** | CC uploads the finalist (best fixed-snapshot read). Load check, and one validation episode for each. |
| **09-30 18:00** | Hard stop. After this, uploads only to replace a crash. |

**Fallback:** if neither #1 nor #2 has passed a gate by 09-28 12:00, field [hyb2965, shepherd] re-uploaded (identical files) and expect ~2150–2210.

**Probabilities:** lowered from round 1 (0.3 / 10 / 50) because the exact branch is dead (E-F).
- The rebuild or WL+S reaching its gates by 09-28: ~40%. If fielded, bronze ~65%, since it is an imperfect copy.
- Otherwise the #2 PREDICT tuning on hyb2965/shepherd: bronze ~25%.
- Cutoff drift after the deadline is not modelled.

P(top-10): 0.3%  P(silver): 8%  P(bronze): 38%

---

### Appendix — recipes for E-A…E-C (all run from the repo root with `.venv/bin/python`, kagsim)

- **Ablation file:**
  `sed -e 's/^_V92_P_K = 4$/_V92_P_K = 10**9/' -e 's/^_V92_Q_K = 4$/_V92_Q_K = 10**9/' subW_shepherd.py > shep_nopred.py`
  The diff is exactly 2 lines.
- **Library swap:** exchange the single `^_V92_P_BLOB =` and `^_V92_P_INDEX =` lines between `subW_shepherd.py` and `rivals4/kaggriculture-yummers/_entry.py`. Each line occurs exactly once per file.
- **Runner:** `moe/r3/opus_scratch/closed.py` `game()`, extended to return `_V92_P_REPORT`/`_V92_Q_REPORT`. Jobs are `(x, xpath, opp, opppath, seed, our_seat)` over `opus_scratch/wl_games.json`.
- **Results:**
  - E-A: shepherd +1525 (13–1) vs nopred +193 (8–6).
  - E-C (i), shepherd with WL library vs yummers, sorted margins: 876 … 3512, all positive.
  - E-C (ii), shepherd vs WL with our library: 866 … 2789, all positive for shepherd.
