# Strategy MoE round 2 — Opus (2026-09-25, ~10:50 UTC)

Evidence cut-off: `moe/screen_lock.log` and `claude_r2.md` as of 10:45 UTC. Nothing else from
round 2 was used.

**Short answer.** I ran a bounded version of the deciding experiment for our biggest disagreement:
did our post-09-23 layers regress us (Claude: P≈0.6, revert), or did the field move (my round 1)?

**The test.** Re-run recorded live games from after the lock, keeping the opponent's recorded
actions exactly as they were and swapping which agent plays our seat.

**The answer.**
- Against the post-lock field, **exact pipe16 is clearly worse than our sir_V1 stack**:
  - −$739/game over 66 games;
  - outcome flips 20:2 in sir_V1's favour (z=3.84);
  - −250 Elo (90% 157-351);
  - a held-out second batch of 31 games replicates the first 35.
- **Stripping only the reclaim layer changes nothing measurable** (see §0).
- So "revert to the pre-09-23 stack" is the wrong move, and the live pipe16 control should read
  *below* our stack.

**What I retract.** My round-1 argument for field drift (E2/E3) was not valid evidence: reclaim and
the post-lock field are perfectly aliased in that data. I had the right conclusion for the wrong
reason. The same instrument, replayed against the real field, should replace the public-pool gate
for every remaining decision.

**Revised confidence:** 3k+ 0.3%, top-10 2%. Almost all of it rests on a lock-window kernel beating
our stack against the recorded field (§5, move 1).

---

## 0. New evidence produced for round 2

Scratch scripts are in `/tmp/opus_r2/`; the core script is reproduced in §4. Everything ran as one
niced worker, ~17 CPU-min in total.

### Instrument validity

- **Setup.** Our seat runs agent file X live. The opponent seat replays its recorded actions
  open-loop, via the `ledger_eps.py` tape idiom.
- **The recorded build reproduces its live margin to the dollar,** with the opponent's bank moving
  **$0**:
  - 3/3 sir-V1 games;
  - **12/12 of pipe16's own 09-20 games**, so `subK_pipe16.py` is behaviourally identical to the
    09-20 live pipe16.

### Post-lock field: A/B on recorded L96-V1 games

- **Games.** The first 70 recorded L96-V1 games (09-23/24, by episode id) against opponents rated
  ≥2200 on `lb_now.json` (09-24 20:35 UTC).
- **Batches.** Games 1-37 were the bounded run. Games 38-70 were run afterwards as a **held-out
  replication**.
- **Filter.** 66 games have every arm reproducing the recorded 8-shop draw; 40 of those 66 were
  played in seat 1. The builds share pipe16's tile plan, so the weed/shop random stream stays
  aligned.
- **Rating scale.** Implied Elo is the maximum-likelihood fit against the opponents' 09-24 ratings,
  with a 90% bootstrap interval.

| arm in our seat (n=66) | WR | mean margin | median | implied Elo (90%) | opponent bank vs recording |
|---|---|---|---|---|---|
| recorded (L96-V1 live) | 0.500 | −10 | +9 | 2417 (2339-2494) | 0 |
| sir_V1 (`subV_sir2.py`) | 0.470 | +35 | −69 | 2393 (2324-2472) | +22 |
| **exact pipe16** (`subK_pipe16.py`) | **0.197** | −704 | **−738** | **2151 (2043-2227)** | **+1,191** |

**sir_V1 minus pipe16, paired per game:**

| batch | mean margin | outcome flips | z |
|---|---|---|---|
| 1-37 (35 aligned) | +$606 | 12:1 | 3.05 |
| **38-70, held out (31 aligned)** | **+$890** | **8:1** | **2.33** |
| **all 66** | **+$739** (sd 1,203) | **20:2** | **3.84** |

**ΔElo, all 66:** +250 (paired bootstrap, 90% 157-351).

**Mechanism.** pipe16 earns about **$430 more for itself** but lets the frozen opponent earn about
**$1,170 more**. Our overlay stack (clamp, premium layer, SIR) wins by pre-empting the rival's
premium sales, not by producing more.

**Absolute level vs gap.** The absolute level is inflated: these are L96-V1's early band games,
while all 189 of its games fit 2239. The gap is the robust quantity.

### Reclaim-only arm (Claude's specific mechanism)

- **Arm.** sir_V1 with the reclaim branch disabled: `if step>=240:` → `if step>=10**9:`, one line.
- **Games.** The first 37 (35 shop-aligned), compared paired with the sir_V1 arm.
- **Result:** sir_V1 without reclaim minus sir_V1 = **+$37 per game** (sd 274, SE ≈ 46; median +7).
  - WR is identical (0.514 vs 0.514); outcome flips 2 each way.
  - The opponent's bank drift is the same.
  - **Reclaim is not a measurable regression against the live field.** Either the Codex stall is
    real but small (≲$40/game), or it is offset elsewhere.

### Swap / bias probe: sir_V1 on pipe16's own 09-20 games

- **Question.** Open-loop replay could favour the agent whose recording it is (the "home" agent).
  Here pipe16 is home.
- **Games.** 12 games against opponents rated ≥2200 on the 09-22 snapshot. 10 are clean; 2 were
  dropped because the opponent's bank moved −$9.9k and −$48k, a tape desync (probably a shop
  re-roll, which this probe did not log).
- **Result:**
  - Margin: sir_V1 − recorded pipe16 = **−$72** per game (sd 1,213; median −130).
  - Outcome flips: 1 each way.
  - Split: sir_V1 again takes about $830 from the opponent and gives up about $900 of its own bank.

**How to read the two runs together.**
- **Pure home-bias model.** Take the post-lock gap (+739) as true + bias, and the 09-20 gap (−72)
  as true − bias. That gives true ≈ **+$330** and bias ≈ $400.
- **Field-dependent model.** The layers are worth ~$0 against the 09-20 field and +$740 against the
  SIR/premium-heavy post-lock field.
- **Either way, sir_V1 ≥ pipe16 in today's field by $330-740/game.** At the clone-band rate of
  ~$300 per 100 Elo, that is +110..+250 Elo.
- **No reading supports a revert.**
- **Caveat:** the swap probe is n=10 with SE ≈ $380, so it bounds the bias only loosely. The full
  run in §4 takes it to ~60 games.

### Loss distribution

Source: `moe/opus/pergame_band.json`, 197 band games (79W / 118L / 0T).

- **Median loss is −$708**; the median of all margins is −$207.
- **Losses within $100 / $200 / $300 / $1,000:** 10 / 18 / 29 / 74 of 118.
- **Wins within $100 / $200:** 6 / 12.

### Codex fresh gate

Source: `moe/codex/gate_candidates.log`, seeds [906:930], 48 games per cell.

- **The worker fix adds nothing.** `capture` ≡ `delivery` in every cell (0.801 mean for both).
- **Against koshinm:** 0.50 (24W/24L, +$28 on fresh seeds), against the development result of
  10W/2L (+$944).
- **Controls pending.** The matched-control gate (`gate_controls.log`) and my sibling's BRX gate
  (`gate_brx_v1_1000_50.log`) were still running at 10:45 UTC.

### E1 recheck: `data/lb.json` (09-22) vs `live_eps/lb_now.json` (09-24)

| 09-22 band | median change | p10 |
|---|---|---|
| 2800+ | −97 | −374 |
| 2600-2800 | −188 | −495 |
| 2400-2600 | −242 | −491 |
| 2200-2400 | −217 | −406 |
| 2000-2200 | −236 | −355 |

The whole middle of the board deflated. There is **no separate "collapse mode"**, which I wrongly
claimed in round 1. 244 new teams appeared in the window.

---

## 1. Agree

**With Codex:**
- **Median loss is −$708, not −$200** (verified above).
  - Claude's "median loss ~−$200" is actually the −$199 median *gap* in identical-wheat games,
    wins included.
  - This matters for sizing any whisker lever.
- **The team-name join is a real limitation.** It joins `index_eps.py` to `lb_now` by team name,
  and it applies to my own round-1 E2/E3 as well.
  - It is small for post-lock games against a contemporaneous snapshot: L96-V1 fits 2239 against a
    display of 2216-2225.
  - It is not small for 09-20 games joined to the 09-22 ratings.
- **Oracle before BRX,** and a +5pp paired-outcome continuation bar.
- **Capture is not submit-worthy.** The fresh gate now shows its worker fix is worth exactly zero
  over `delivery`. The +$944 against koshinm was winner's curse on 12 development games.
- **Eviction order is a real constraint** (Codex §3).
  - The active pair is [sir_V2 56547525, pipe16 56547613], and sir_V2 is 7 minutes older.
  - **The next upload therefore evicts sir_V2, not the control.**
  - Retiring the control takes two uploads.

**With Claude:**
- **Freeze the final pair by 09-28** and stop churning.
- **The second slot should be a different chassis.**
- **Freshness is worth something:** the 09-20k clone-rate data.
- **The replanner is out of reach.**
- **§5: the top-11 edge is structural.**
- **Moderator's 09-25f entry.** The control was the right *live* experiment to launch. We now simply
  have a faster, paired, cheaper one.

**With both:** no submission before the control reads.

## 2. Dispute

### Claude — weakest claim: "revert to the pre-09-23 stack", P=0.6, +500..+900

**Refuted offline:**
- Against the very opponents our post-lock builds met, exact pipe16 is **−$739/game and −250 Elo**
  relative to sir_V1 (n=66, 20:2 flips). The held-out half alone gives 8:1.
- Under the most pessimistic bias reading it is still **−$330/game**.
- The reclaim-only arm shows stripping reclaim is worth +$37 ± 46/game with 2:2 flips. That is
  noise, not the 600-900 point regression the 50-submission history seemed to show.

**Why the 50-submission history cannot carry this claim:**
- **Every build submitted from 09-23 carries reclaim *and* faced the post-lock field.** HANDOFF
  09-25 (lines 760-761) confirms that even the resubmitted f55rec files gained reclaim on
  09-23 00:32. So "2552/2489 → 1930/1793" is two changes at once.
- **Same-code-later-date drops of 400-1,100 have happened here before:**
  - 09-06: byte-identical files scored 2609.9 and 2202.9;
  - 09-11: historical bests 2609.9 → 1400.5 and 2576.7 → 1524.5.
- **The public-lineage authors' own teams fell 218-390 in the same 49 h,** and they never had our
  reclaim layer:
  - Nathan Jacob 2567→2176;
  - KoshinM 2318→2041;
  - pig7selene 2285→2066;
  - ToastUz 2723→2444;
  - jojo 2763→2503.

**The 09-25f decision rule is also wrong in its second half.** It says: "if control ≥2.5k → revert
all reclaim/SIR layers." But:
- The layers on top of pipe16 (clamp, premium, SIR) are exactly what is worth +$740/game against
  this field.
- A single high control read is within documented identical-file noise (250-500).
- **Never strip SIR/premium on a live read alone.**

### Claude — BRX (best-response SELL permutation) at +55, confidence 0.35

**+55 Elo needs ≈ +$165/game of relative margin,** at the ~$300 per 100 Elo clone-band calibration
(memory: route-oracle-confound). That is about +8pp band WR.

**Measured available room:**
- The index-race deficit is −$29/g for SIR builds and −$70/g for f55 builds, price-only.
- Only 10/118 losses are within $100.
- A uniform +$100 lifts the band score only 40.1% → 45.2% (Codex's table).

**So the credible range is +0..+25.**

**Concession.** §0 shows that the *existing* market stack moves ~$1k/game between us and the rival
in the live field. So market microstructure is not intrinsically "tens of dollars" as I said in
round 1. The open question is whether BRX adds anything *on top of* SIR. The substitution gate can
answer that in 30 min.

### Claude — "offline vs exact clones is valid HERE"

The whisker is decided in the market layer, and that is exactly where the band differs:
- the 88% figure is order agreement on multi-item contested turns only, not quantities or timing;
- clone cells are exactly seat-symmetric (Opus NOTES checkpoint 4), so 48 games = 24 observations;
- ≥2700 opponents are non-clones (5/30).

**Moot now:** replay against the recorded field instead of a clone.

### Claude — confidence 12% top-10

**Our best measured strength against the post-lock field is ~2240-2420 implied.** That is
L96-V1's full-set fit, and sir_V1 on the band subset above. The cutoff is ~2940. The gap is
+500..+700, i.e. ~95% head-to-head.

"BT on fewer clone mirrors favours a private build" names no mechanism with a size. I'd put it at
~2%, and only through a stronger base (§5, move 1). Claude's round 2 has since moved to 3% on the
same basis.

### Codex — weakest claim: the 30% favourable branch

**The claim.** Conditional 12% for 3k+ and 25% for top-10, giving 4% / 8%.

**The favourable branch is "pipe16 recovers its old standing".** The substitution puts it at ≤5%:
pipe16 is the *weaker* agent against today's field.

**Even inside the branch, no lever in Codex's plan is sized above +100:**
- capture's fresh effect is +$28 against koshinm, and the worker fix adds zero;
- the sell-order upper bound is ~+25.

**So 12% conditional for 3k+ has nothing under it.** Revised: ≤0.5% / ≤2%.

### Codex — live control as the primary instrument (80-120 games, 24-48 h, else "unresolved")

**The live read is too slow and too noisy to be primary:**
- One live arm carries ±80 SE, plus identical-file spreads of 250-500 (09-06; V4 djschmit 248).
- "Resolved" arrives ~09-27, leaving one rotation.

**The paired offline read is faster and tighter:**
- Per-game difference sd is ~$1,170.
- SE is ≈$200 (≈65 Elo) at n=35, in minutes.
- SE is ≈$117 (≈40 Elo) at n=100, in under an hour of one worker.
- It has no identical-file lottery.

**Division of labour:**
- **Use the live control as the out-of-sample check of the instrument**, not as the decider.
- The pre-registered prediction for that check is in §4.

### Codex — "delivery is the leading submission option"

**Its evidence is near-mirror public-pool cells:** 0.85 against sir_V1 at a +$117 mean margin,
which is a whisker effect. The public-pool gate ranked pipe16 7th/9.

**What §0 adds:**
- The pool ordering sir_V1 ≫ pipe16 was actually right. The live "contradiction" was the time
  confound.
- The pool therefore orders our own lineage correctly, but by margins that are not live-sized.

**What delivery needs next.** Delivery changes premium sell timing from step 504, which is exactly
the channel whose value is field-dependent (§0). It must pass the substitution gate against the
recorded post-lock field before it is "leading".

### My own round 1 — attacking my weakest claims

- **E2 (smooth decline with date) and E3 (bank held) did not discriminate.**
  - Reclaim is in every post-09-23 build, so date and layer are aliased.
  - Bank medians at ±5k noise cannot see a $500-1,000/game defect, which is exactly the size that
    decides whisker games.
- **E1's "distinct −400..−500 mode" is false.** The whole band deflated, with medians of −190 to
  −240.
- **Move 3 (capture +30-60) is dead** (worker fix = 0).
- **"Every other lever is worth +30-80"** was wrong in kind. The market stack is worth ~+250 Elo
  over pipe16 in this field. New *increments* on top of it are what is small.

## 3. Changed my mind

1. **Why "no revert".** The reason is no longer "field drift, per E2/E3". It is **direct paired
   evidence that our stack beats exact pipe16 against the recorded post-lock field.**
   - My round-1 P(control ≥ sir_V2+150) of 20% becomes **≤7%**.
2. **The instrument.** My round-1 move 2 was a fingerprint→library→48-game-cell "live-weighted gate".
   **Replay-substitution supersedes it:**
   - it uses the actual recorded opponents, prevalence-weighted by construction;
   - it needs no classifier;
   - it costs ~8-20 s per game-arm.
   - Its weakness is open-loop opponents. The swap probe puts that bias at ≤~$400/game, loosely
     (n=10). Even at that size, sir_V1's edge survives.
3. **Capture.** Downgraded from +30-60 to ~0. The fresh gate shows the worker fix ≡ 0.
4. **Market microstructure is the big live lever.** It is what separates our stack from pipe16 by
   ~$740/game. New market increments still have to beat that stack, not pipe16.
5. **The public-pool gate is not useless.** It ordered sir_V1 ≫ pipe16 correctly. It is only
   uncalibrated in *size*.
6. **E1.** Board-wide deflation, not a collapse mode.

## 4. Deciding experiment

**The disagreement.** Regression vs drift: does removing our post-09-22 layers (pipe16 exact), or
only reclaim, beat our stack against today's field? This decides whether the final pair is a
revert or the current lineage. It also decides whether anything built since 09-22 is worth keeping.

**Cost.** ≤3 h, one worker. I ran it bounded: 70 post-lock games plus 12 swap games, including a
held-out replication. The full version is below.

```bash
# 1) arms (reclaim strip is one line)
sed 's/        if step>=240:/        if step>=10**9:/' subV_sir2.py > /tmp/opus_r2/sirV1_norecl.py
# 2) post-lock pipe16-chassis games vs rated band (~200 games with RMIN=2000), 3 arms, 1 worker, ~70 min
RMIN=2000 nice .venv/bin/python /tmp/opus_r2/subst.py /tmp/opus_r2/full.jsonl \
  L96-V1,sirxP-V1,f55rec2-V1 0 p16=subK_pipe16.py sirV1=subV_sir2.py norecl=/tmp/opus_r2/sirV1_norecl.py
# 3) bias probe: pipe16's own 09-20 games (109 tapes in mine/opp), R>=2200, same arms
RMIN=2200 nice .venv/bin/python /tmp/opus_r2/swap.py swap_full.jsonl 60 p16=subK_pipe16.py sirV1=subV_sir2.py
# 4) summary
.venv/bin/python /tmp/opus_r2/analyze.py /tmp/opus_r2/full.jsonl recorded,sirV1,p16,norecl
```

**Core of `subst.py`** (tape idiom from `moe/opus/ledger_eps.py`; the out path must be absolute
because the script `chdir`s to the repo):

```python
rows = [r for r in json.load(open("moe/opus/eps_index.json"))
        if r["build"] in builds and r["ours"] is not None and (r["R"] or 0) >= RMIN]
def tape(acts, seat):                       # steps[t] holds the action that PRODUCED step t
    return lambda obs: (acts[obs["step"] + 1][seat] if obs["step"] + 1 < len(acts) else None) or PASS
for row in rows:
    acts, seed, rew = load(row)             # full replay or mine/opp reduced archive
    us, them = row["seat"], 1 - row["seat"]
    for name, path in arms:
        me = harness.load_agent(path, name=f"arm_{name}_{row['ep']}")   # fresh module state per game
        a, b = (me, tape(acts, them)) if us == 0 else (tape(acts, them), me)
        r = harness.run_episode(a, b, seed=seed, copy_obs=True)
        rec[name] = r["reward"][us] - r["reward"][them]; rec[name + "_opp"] = r["reward"][them] - rew[them]
        rec[name + "_shopok"] = final_shops(r) == recorded_shops(row)   # drop desynced games
```

For reduced archives, which carry no shops, treat |opponent bank drift| > $5k as a desync.

**Claude is right (regression) if either:**
- WR(p16) − WR(sirV1) ≥ +0.08 with outcome-flip z ≥ 2 → revert to pipe16; or
- WR(norecl) − WR(sirV1) ≥ +0.05 with z ≥ 2 → strip reclaim only.

**I am right (drift; keep the stack) if:**
- sirV1 ≥ p16 with z ≥ 2 on the post-lock set;
- |norecl − sirV1| < 0.03; and
- on the swap set sirV1 is ≥ −$350/game against pipe16's home results. That is the bias bound; a
  bigger home deficit would mean the instrument is biased, and we fall back to live.

**Bounded result so far: my side on all three.**
- p16 vs sirV1: z = 3.84 against pipe16 (20:2 flips, n=66).
- norecl: +$37 ± 46, flips 2:2.
- Swap: −$72.

**Out-of-sample live check, pre-registered.** Each arm fitted on one fresh leaderboard snapshot once
it has ≥80 games:
- the pipe16 control's fitted rating is **≤ sir_V2's (80%)** and **≤ sir_V2 − 100 (55%)**;
- **≥ sir_V2 + 150: ≤7%**;
- the control's display at 24 h is **1850-2200 (70%)**.

If the control lands ≥ sir_V2 + 150 anyway, the open-loop instrument is missing something
closed-loop, and I defer to live.

## 5. Revised ranked plan (top 3)

### 1. Lock-window kernels through replay-substitution against sir_V1

This is the **only move with a +250 tail**.

**What Claude found after round 1** (`moe/screen_lock.log`, 12 games vs pipe16 in the public pool):
- **29 of 41 pulled kernels are runnable; 15 win 10-12 of 12.**
- **Biggest margins:** hybu +$1,741; v15stack, v15stack-nb and late-purchase-v16 all at an
  identical +$1,683 (one agent); shepherds-ledger +$1,665; 2965-hybrid +$1,052;
  herd-safe-v3 +$952.
- **The bar is sir_V1, not pipe16.** sir_V1 is already +$740 over pipe16 against the live field.
- **The authors' teams I can match** sit at 2080-2620 on 09-24 (shiiin9 2624, Abhinav0370 2576,
  sunil 2384, prvsiyan 2294, statma 2078), not near 2940.

**Run:**
- the top 5 distinct families;
- **seat-1, shop-aligned post-lock band games only.** These kernels change the tile plan; as farm 1
  our weed draws come after the opponent's, so their tape stays valid.
- ~40 games per kernel for the screen, then 100 for the top 1-2;
- 1 worker, ~1.5 h.

**Pass:** ΔWR ≥ +0.05 vs sir_V1 with z ≥ 2.

**Kill:** all five are ≤ sir_V1 + 0.

**Expected:** P(some kernel beats sir_V1 by ≥$500/game live) ≈ 15-20%. That would be worth
+150-300 Elo. It still leaves the cutoff +300..+500 away.

### 2. Our own candidates through the same gate

**Arms, against sir_V1 on ≥100 post-lock band games:**
- `delivery`;
- BRX (`cand_brx.py`);
- sir_V1 − reclaim;
- sir_V2. It is a metav4 tile plan, so the seat-1 + shop-aligned rule applies.

`capture` is dropped: its worker fix ≡ 0.

**Pass:** ΔWR ≥ +0.05 and z ≥ 2, and not negative on the pipe16-home swap set.

**Cost:** ~1.5 CPU-h, done by 09-26 12:00 UTC.

**Expected:**
- +0..+50 Elo over sir_V1;
- most likely outcome: sir_V1 unchanged.
- The winner of move 1 or 2 is X. The best *different* passer, or sir_V2, is Y.

### 3. Slot mechanics at the control readout (~09-26 06:00-12:00 UTC, fitted not displayed)

**Control < sir_V2 + 150 (expected; ≥93%):**
1. Upload X = the gate winner (default sir_V1 bytes + a comment). This **evicts sir_V2**, the older
   submission.
2. ≥12 h later, upload Y = the best *different* build: sir_V2 re-upload, or a kernel from move 1.
   This evicts the control.
3. Final pair [X, Y] live by 09-27 12:00 UTC.

**Control ≥ sir_V2 + 150 (instrument falsified):** keep the control and upload only X, which evicts
sir_V2.

**Either way:**
- **freeze at 09-28 12:00 UTC**;
- after that, replace only a crashed or timed-out agent;
- never strip SIR or the premium layer on a live read.

**Expected:** this retires a slot predicted at ~1950-2200 and restores a best-measured pair. Its
value is protecting the team's best-of-two, not new strength.

**Do not reopen** anything already closed: replanner, route refits, rescue grafts, sell-phase
shifts, alpha/prem sweeps.

**Confidence.** All of the remaining mass sits in move 1, a kernel that beats sir_V1 by
≥$1.5k/game live. Our own lineage is measured at ~2240-2420 against today's field.

CONFIDENCE 3k+ by 09-30: 0.3%
CONFIDENCE top-10: 2%
