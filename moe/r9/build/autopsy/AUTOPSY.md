# MoE r9 — autopsy lane: m30b live-loss analysis

**Data** (all fetched 09-30 ~13:20-13:35 UTC):
- m30b = subAB_m30b.py, submission 56698987, submitted 06:05 UTC, LB 1735.4.
- 62 of its ~87 episodes downloaded+reduced to `replays/*.json.gz` (fetch.py,
  fetch_oldest.py; raw JSONs deleted, reduced keep teams/rewards/seed/actions/statuses).
- v8hh = 56707845, submitted 12:52 UTC: all 7 episodes fetched (6 public + 1 validation).
- Opponent ratings from full LB CSV `kaggriculture-publicleaderboard-2026-09-30T13:23:13.csv`.
- Analysis script: `analyze.py` -> `analysis.json`; per-game dump: `deep.py`.

## Headline

**m30b has NO crash/timeout failure mode.** All 69 sampled episodes (62 m30b +
7 v8hh) ran the full 720 turns; per-step statuses are ACTIVE/DONE for both
agents in every game. Zero ERROR/INVALID. No hedge-triggering "agent died"
scenario exists — losses are real economic losses.

Record in sample (61 inter-team games + 1 intra-team validation):
**38W-22L-1T** (62% WR). Median win ~+243, median loss ~−489, mean loss ~−2481
(one −33k blowout skews mean).

## The field at ~1735 is a clone monoculture — but variants beat us, not clones

Unit-op identity (farmer+hand ops per turn, position-independent) vs opponents:

| band | games | W-L | note |
|---|---|---|---|
| ident >= 0.95 | 38 | **28-9** | literal clones — m30b WINS 74% of pure mirrors |
| ident 0.85-0.95 | 7 | **1-6** | near-clones w/ small tweaks — we lose |
| ident 0.5-0.85 | 7 | **1-6** | same skeleton, real upgrades — we lose |
| ident < 0.5 | 9 | **8-1** | non-clones crushed (all <1410 LB except Yusaku) |

~85% of opponents share the Harvest-V78-lineage chassis (identical land-buy
turns 151/266, ~270-300 hires on a fixed schedule, same herds, same
plant/water/care cadence). **m30b wins the pure-clone mirrors but loses almost
every game vs same-skeleton VARIANTS** (2-12 in the 0.5-0.95 bands). The
dangerous field slice is the chassis + a better overlay, not the chassis.

## Loss taxonomy (22 losses)

| class | n | examples (margin, opp LB) | verdict |
|---|---|---|---|
| Coinflip mirror (<300) | 8 | Kaan −4, Asterios −30, Shunsuke −83, Anh Tu −88, Abish −126, Jordi −191, qinsuikang −219, Evgeny −256 | noise-scale; overlay decides |
| Mid same-chassis (300-2000) | 9 | haseryo −267, y3uanm −411, Lonan −489, Dlyra −560, IUT −595, JinboWang −805, Sourabh −1117, Fabian −1120, Rômulo −1762 | variant overlay out-traded us |
| Big same-chassis (>2000) | 3 | Anubisyy −3036 (1882), Lonan −3814 (1706), Seungjun −4277 (1800) | same volumes, better sell timing |
| Blowout non-clone | 1 | Yusaku Muroya −33029 (2367) | tuned variant: FERTILIZE x201 (we use 0), 2nd land t199 vs t266, 385 vs 230 SELL ops |
| Private-tier (MMPQ/DSM/DECEM) | 0 | — | not faced at this rating |
| Crash/timeout | 0 | — | does not exist |

vs opponents rated >=1900: 5W-6L. vs >=2000: 2W-4L. No seat artifact (11 L seat0,
10 L seat1 in the first 50; oldest-12 games add 1 more L at seat1).

## What winning variants do differently (deep.py on loss replays)

Same farm, different market layer. Across Rômulo (−1762, ident 0.97) and
Sourabh (−1117, ident 0.89): unit ops, hires, land turns, animal buys are
near-identical; the difference is order flow:
- **WHEAT volume**: Rômulo sold 5004 vs our 3693; Sourabh sold 3761 vs our 396.
- **FERTILIZER dumping**: Sourabh sold 2361 vs our 351.
- **BUY_PRODUCT arbitrage**: Rômulo 203 orders vs our 106; Sourabh 137 vs 70.
- **Sell-entry fingerprint**: winning clones' first WHEAT sell ~t50, first
  CARROT sell ~t674. m30b: WHEAT t1, CARROT t218.
- Anubisyy/Seungjun losses: near-identical sell *volumes* — the −3k/−4.3k gap
  is pure sell *timing/order placement* (who captures price before the other).

So m30b's losses are dominated by **same-chassis variants whose market overlay
(sell timing + order priority + wheat/fert flow + arb) captures a few hundred
coins more per game** — while it wins the pure-clone coinflips. It is not
out-farmed; it is out-traded. Fixing this on the same chassis = the
clone-overlay arms race the r3 notes already described.

## v8hh live sample (6 public games — tiny)

| opponent | opp LB | margin | ident |
|---|---|---|---|
| sawe | 431 | +126005 | 0.03 |
| korpo | 488 | +15035 | 0.03 |
| cracksbot | 421 | +49638 | 0.03 |
| Lorenzo Grattarola | 519 | +16808 | 0.02 |
| soumic 1088 | 540 | **−9946** | 0.03 |
| Engel Ai Labs | 658 | **−23148** | 0.02 |
| (validation vs m30b) | — | +5210 | 0.44 |

v8hh is a fully different chassis (BUY_LAND at t1, hire bursts of 25, milk-heavy
14-cow economy). Alarming: both its losses are to **<700-rated non-clone**
agents who simply out-farmed it (soumic: 37 animals bought; Engel: wool-heavy).
Small sample — but its failure mode is visibly DIFFERENT from m30b's:
m30b only loses to >=1630-rated clone-overlay opponents; v8hh lost to bottom-tier
off-meta farms.

## Hedge verdict

- m30b's losses = same-skeleton variants beating it on market microstructure +
  a residue of pure-clone coinflips. A hedge on a *different chassis* never
  enters the mirror contest at all — its games are decided by real economics,
  hence maximally decorrelated. **v8hh structurally fits**; its observed failure
  mode (out-farmed by off-meta bottom-tier farms) is disjoint from m30b's
  (out-traded by clone variants). Open risk: n=6 live games, and losing to
  540-658-rated agents suggests a low floor — needs matrix-lane RR vs the
  clone band before trusting it as the >-anchor path.
- A same-chassis hedge with a better market overlay (metav4/f55 sell-race)
  would fight the *same* coinflips with correlated outcomes — plus f55
  resubmits already decayed to ~1800-1930. Poor decorrelation.
- shepherd-family: different chassis too (decorrelated), but last era's read
  was ~2100 fresh pre-decay; no current-era evidence.
- The only non-mirror threat observed (Yusaku-class 2300+ tuned variants) is
  ~1/50 games at this rating — uncovered by any hedge, acceptable tail risk.

## Caveats
- Sample = 62/87 m30b episodes (all COMPLETED; remaining ~25 unfetched are all
  in the same 06:50-09:45 window, same opponent pool), + 7/7 v8hh episodes.
- ident metric = per-turn Counter equality of unit ops (positions ignored);
  ≥0.85 = clone-band.
- Rewards-based margins include rating-relevant noise; sub-100-coin margins are
  effectively ties.
- v8hh numbers are 6 public games vs bottom-tier matchmaking (fresh-sub rating
  ~500-600) — its clone-band performance is unmeasured live; matrix lane owns
  that question.
