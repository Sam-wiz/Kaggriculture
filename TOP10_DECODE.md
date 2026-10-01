# TOP-10 DECODE — what separates ~2900–3100 Kaggriculture agents from `subV_sirxP.py` (~2750)

Compiled 2026-09-23. All claims cite source lines in this repo or measured entries in HANDOFF.md.
Target for comparison: `subV_sirxP.py` (6807 lines, final callable `agent = _sir_agent`, line 6807).

---

## 0. TL;DR

Almost every "headline" mechanism found in the high-rated rivals is **already inside
`subV_sirxP.py`** — often verbatim, since it descends from the same public v9/3 lineage
(thomastschinkel / ahmedberatozer / yhay81 Shop-Router chassis). The rivals that beat us
do not win on a mechanism we lack; they win on **(a) tape/sell-schedule quality in the
last ~70 steps**, **(b) one confidence-gated production-mix decision** (herd swaps), and
**(c) fresher tapes → lower clone density on the live ladder** (HANDOFF 09-20k/09-20e).

The genuinely missing or materially weaker mechanisms, ranked:

1. **Confidence-gated herd swap (shiiin9 `_CXO`)** — a multinomial-over-remaining-shop-draws
   decision rule for COW↔SHEEP `BUY_ANIMAL` substitution. We have only the older,
   strictly weaker one-directional version (`_y_target`). **Highest expected value per
   unit of risk** of anything found — but it touches production, which is historically
   where our overlays die.
2. **Sell-schedule / late-route quality (koshinm route-2)** — not a mechanism, better tape
   content. Our measured residual vs koshinm is ~$700–1000/game in days 24–29 price
   capture (HANDOFF 09-23 SIR entry). This is a *tuning* gap, not an architecture gap.
3. **Opponent-family counters keyed on public farm state** (rank-top10 `_v17_r5_counter` /
   `_v17_md_counter`) — detect the rival family from animal counts at step 24/160 and
   pre-sell against an embedded copy of *their* tape. Detection is earlier than our
   V92 stream-matching (which needs observed sales first).
4. **Simulated-feasibility order frontloading** (uninhibitedscholar `frontload`) — reorder
   SELLs ahead of non-blocking orders (HIRE/BUY_SEED) only when a solo simulation proves
   the reordered list still fully executes. Our V44Y permutes within contiguous SELL
   blocks only; SIR keeps sells inside `≤ last-sell` slots — neither crosses order types.
5. **Learned late re-route (mzcao7 LightGBM+XGB @ step 648)** — conditions the day-27 route
   on full public+private state, not just the shop pair. Compatible with our existing
   `route=2` switch point, but HANDOFF 09-18g/§5.24 warn that later switches physically
   diverge; treat as a research item, not a port.
6. **EXP303 resource-valuation terminal planner** (shiiin9) — proposes 1–2 resource-bundle
   closures replacing the E182 baseline suffix in the last 7 turns. A refinement of
   machinery we already have; small residual.

Everything else inspected is either already present, dormant in the source too, or on
the falsified list (§5 of HANDOFF.md).

---

## 1. Engine facts every mechanism exploits

(Verified in `sim.hpp`/interpreter per HANDOFF 09-20f, 09-23-r3; AGENTS.md rules.)

- Market resolves **order-index-by-index in per-unit lockstep** between the two players;
  earlier indices win same-item races; each item's price curve integrates independently.
- **Unit actions run before market each step** → a same-turn DROP/harvest feeds a
  same-turn projected-shed SELL.
- SELL quantities are **caps**, not fills — overshoot produces zero-fill orders that
  desync financing; sells must precede the buys they fund.
- Shop unlocks: 8 total, fixed schedule (1 by day 4 … 8 by day 24), uniform draws with
  replacement — so `8 − len(unlocked_shops)` is exactly the number of draws left
  (shiiin9 exploits this; see §4.11).
- Day 29 has no end-of-day refresh → FEED/CARE/WATER-ongoing/FERTILIZE after day 28
  are dead ops. Last payable production day = 28. Terminal window starts ~step 712.

---

## 2. `subV_sirxP.py` — definitive inventory (what we already have)

Router & tapes:

| mechanism | lines | status |
|---|---|---|
| R108 route set + `_R108_SHOP_ROUTES` day-6 shop-pair map | 945–947, 966–971 | active |
| EXP240-vs-V39 binary expert split on first-2-shop YARN count | 968–970 | active |
| `_V92_TABLE` yarn-override (any yarn in first 2 → route 9) | 956, 971 | active |
| `_V93_ROUTE_BY_RIVAL` rival fingerprint → route 128 (step-2 `(money, wheat_inv)` key) | 958, 960–965, 972–973 | active |
| Unconditional late route `route=2` at step ≥ 648 | 975–977 | active — **same as koshinm** |
| `_R42_OPENING` step-0 wheat round-trip injected into all tapes | 980–983 | active |
| `_alt_install('HybridOpening')` — opening tape surgery on route 0 (extra seed buy, hand re-tasking days 0–2) | 6473–6516 | active |

Chassis settings (line 949): `hand_align, weed_repair, sell_lead, clamp_sells` ON;
`budget_guard, room_guard, dead_stock, terminal_liquidation, front_run` OFF
(the off ones were individually measured harmful — HANDOFF 09-18d/§5).

Wrapper chain (each verified in the live chain; final `agent = _sir_agent`):

| layer | lines | what it does |
|---|---|---|
| E182 terminal planner | 1020 (exec'd) | 7-turn physical closure planner, steps 712–718 |
| Terminal projected-shed liquidation fallback | 998–1012 | step≥718 DROP-all + price-sorted SELLs |
| V219 finite tomato investment + V13V skip-days | 1240–1465, 6428–6468 | late tomato annex with dedicated hired workers; relaxes watering days 19/21/23 |
| V231 cattle controller | 1544–1650 | carried-animal tracking |
| R36 sale reservation + R37/R44 similarity probe | 1653–1948 | tape-following SELL reservations; `_r37_reorder_sales` quote-priority sort |
| V233 six-sheep SE investment | 1952–2145 | financed, hired-hand sheep annex |
| R51 input planner (wheat/carrot) | 2148–2286 | finite-harvest input scheduling |
| `_r97_supply` / `_r97_budget` | 2773–2890 | per-turn supply guard: budget check + delivery-loss accounting on proposed orders |
| V9 COURIER | 2900–3032 | same-day premium-cargo delivery before midnight |
| GOOSE→species rewrite | 3189–3209 | `BUY_ANIMAL GOOSE` → other species at step≥216 |
| V92 predictive sale-stream library | 3405+ (`_V92_P_BLOB` 3419) | recorded rival sale streams scored vs observed market deltas, ±1 turn tolerance |
| V9_RACE rival-sale recovery + dynamic horizon 40/48/12 | 3746–3882 | infers opponent sales from inventory deltas; sets per-item horizons |
| V9_RACEPX price-gated sell_lead | 3911–3959 | suppresses lead-sells into already-depressed books |
| V9_RACEGATE price-gated reserve | 3980–4056 | same gate on `_r36_reserve` |
| OR2 second rival-sale estimator | 4730+ | independent `own` accounting |
| `_v44y_lockstep` + `_v44y_reorder` + `_v44y_clone_gate` | 6033–6177 | **full per-unit lockstep simulator**; permutes contiguous SELL blocks (2–6) when simulated own-minus-mirror revenue improves >0.5; gated step≥216 + clone evidence |
| `_y_agent_shopherd` (v44y shop-aware herd) | 6181–6305 | cash-checked `BUY_ANIMAL` substitution days 8–11 + PICKUP/PLACE/BUILD_COOP follow-up rewrites + sell-boost. **Reactive only** — see §4.11 for the gap |
| `_e334_compact`/`_e335` | 6326–6398 | merges/deletes useless cash-product SELL slots (≥step 144) |
| `_prm_agent` premium overlay | 6594–6634 | fills FREE market slots with floor-priced premium sells off `projected_shed` |
| `_rec_agent` own-sale reconcile + dead-op reclaim | 6637–6720 | fixes V9_RACE/OR2 `own` after overlay appends; converts dead PASS/FEED/CARE→HARVEST/COLLECT (step≥240, shed-room guarded) |
| `_sir_agent` SIR sell-impact reorder | 6722–6807 | permutes SELLs only, self-impact score `qty·(p_now−p_after)` + demand-urgency α=0.25; non-SELL indices preserved |

Net: the local file is a **superset** of every v9/3-lineage rival inspected
(subJ_2945, demystifying, the-2950, metav4, and most of shiiin9).

---

## 3. What actually separates the top of the ladder

From HANDOFF evidence (not speculation):

- **Top-11 live agents are private reactive policies** sharing our skeleton but with
  demand-matched herds (~10 cows vs our 6–8), strawberry from day 2, tick-timed premium
  sells, ~8 pastures not 14 (09-21 PM; pig7selene's `where_the_gap_is.md`: the ~13k gap
  is **sell mix/timing, not scale** — they sell premium goods at price-index 1.01–1.02
  vs V43-family 0.61).
- **Clone density is the rating ceiling**: subJ_2945 drew 50.8% near-clone opponents and
  won only 0.349 of those; fresher pipe16 drew 17.7% and won 0.766 (09-20k). Every
  published-agent adoption converges to the *cloner-crowd average* ~2400–2600
  (Le Quang Canh, discussions V3) — **mechanism novelty within the tape paradigm is
  worth less than tape freshness**.
- **The largest measured single lever to date is SIR** (+~300–550 honest margin vs mid-band,
  est. +100–180 Elo; 09-23). It is already shipped.
- **The one open measured cell is koshinm** (beats both live builds 0.58/0.63; residual
  ~$700–1000/game in days-24–29 price capture; 09-22n, 09-23).

---

## 4. Source-by-source decode

### 4.1 `subJ_2945.py` — our sibling/ancestor
Public V39 + v9 layers (RACEPX gate, RACE reservation from step 192 h40/m12, COURIER,
CARROT, HERD), R108 routes, identical `_router` (144 shop-pair → V92_TABLE → V93 rival →
648 route 2), `_SETTINGS` with clamp_sells **False** (line 949). Strictly weaker than
subV_sirxP — it lacks clamp, shopherd, E334, v44y, prem, rec, SIR. **Nothing to port.**

### 4.2 `rivals/demystifying-2900-meta-reflex-engine-and-bot/_orig_main.py`
Same lineage — literally the same `_R108_DATA` blob, same `_V92_TABLE`/`_V93`/router at
lines 945–978, same layer stack. Its RACE machinery (dynamic lead horizon via recovered
opponent sales, town-demand inference, planned-tape matching) is the **same code we
carry at lines 3746–3882**. **Nothing to port — it is us.**

### 4.3 `rivals/rank-top10-read-the-market-choose-the-farm/_orig_main.py` (= indarkarhana copy)
Architecture: two FULL tapes — `_E279_LOW_ACTIONS` (Boatlee BL-V17-R1-RC2) and
`_E279_HIGH_ACTIONS` (Kawashigi ep 92521336 seat-0 tape), identical through step 167;
at `_E279_DECISION_STEP = 168` pick "high" iff `YARN_STORE ∈ first-2 shops` and not
`(ICE_CREAM, YARN)` dominated (lines 937–994). Layers: weed repair, `_repay_shift`,
`_rank_sell_slots` (SIR-family scoring), `_preempt_shift` (**`_PREEMPT_ENABLED=False` —
dormant**), `_v17_r5_counter`, `_v17_md_counter`, `_v17_room_guard`, `_terminal_liquidation`.

The interesting parts:
- `_v17_r5_counter` (396–447): detects sheep-heavy opponent (sheep≥4 & cows≤3, step≥24)
  → reads `_V17_R5_MARKETS[step+2]` (an embedded copy of *that family's* future sells)
  → pre-sells `planned × 1.0` of our stock early, town-demand gated.
- `_v17_md_counter` (625–666): same for cow-heavy (quadrants≥2 & cows≥4 & sheep≤2, or
  cows≥9; step≥160) → `_V17_MD_MARKETS[step+1]` × **2.0** fraction.
- `_public_signature`/`_clone_distance` (151–182): farm-tile histogram distance — the
  preemption gate input.

**Gap vs us:** detection is off *public farm state* at step 24 — far earlier than our
V92 stream matching which needs an observed sale first. The `_repay_shift` debt tracker
(suppress next-step tape sells by pre-sold qty) is what salemali7 also carries.
E279 expert-switch ≈ our EXP240/V39 day-6 split — same mechanism class, ours fires earlier.

### 4.4 `rivals/the-2950-peak-farm/_orig_main.py`
Same v9/3 chassis (`_SETTINGS` 949 all guards off except hand_align/weed_repair/sell_lead;
`clamp_sells` False), `_router` day-27 → route 2 (975–984), `_r97_supply`, RACEPX
(`_V9_RACEPX_LEAD` 3913–3950), V219, V233, `_VE` day-11 budget check (4318–4362),
E182 terminal. **Subset of ours.**

### 4.5 `rivals/salemali7_kaggriculture-2900/main.py`
Minimalist: ONE tape + `_weed_repair_action` + `_front_run` + `_repay`.
`_front_run` (204–233): pulls **our own tape's** step+1 SELL quantities for
MELON/MILK/STRAWBERRY/WOOL into the current turn when `_town_demand_now == 0`
(no shop/center drain this step), shed-and-reserve clamped; `_repay` (181–201) then
suppresses the next-step tape sell by the advanced amount. This is exactly our
`sell_lead` family — ours additionally price-gates it (RACEPX) and reserves through
RACE. **Strictly a subset; nothing to port.** (Rated "2900" in its title — a data
point that a lean tape+lead agent reaches ~2900 in its window.)

### 4.6 `rivals/koshinm_kaggriculture-local-best-2026-09-21/_entry.py` + operator library
The wrapper is 58 lines: embedded base (native chassis with its own route tapes) +
**exactly one operator wired**: `_OPERATOR = _OP_NS['sell_impact_reorder']`,
`{'sell_impact_demand_alpha': 0.25}` (lines 15–16). `_selected_tape` (31–46) supplies
the operator with the parent's tape, with `route = 2 if step >= 648` — the same
day-27 dedicated route we already have. The membership set at 51–56 only decides
whether to pass the tape; **it does not activate the other operators.**

The decoded operator library (`/tmp/koshinm_operator.py`) contains:
`adaptive_market_tape_guard` (~653), `market_queue_lockstep` (~1130),
`opponent_front_run` (~1556), `racegate_reservation` (~1729), `sale_advance` (~1857),
`sale_advance_policy` (~2346), `budget_guard` (~2567), `room_guard` (~2767),
`supply_prefetch` (~2970), `sell_impact_reorder` (~3142), `sale_advance_pressure` (~3208).
A second dated variant wires `sale_advance` instead (`/tmp/koshinm_base.py` line 15:
lookahead 10, items STRAWBERRY/MELON/MILK/WOOL, abstain-on-weed). HANDOFF 09-23 flags
`opponent_front_run`/`sale_advance_pressure` as having accounting bugs (own-sell
recording pre-append — same bug class our `_rec_agent` fixes); `market_queue_lockstep`
and `adaptive_market_tape_guard` are the only others possibly worth screening.

**Conclusion:** our SIR port already neutralizes the active operator. The residual
~$700–1000/game is koshinm's **native route-2 tape content and late sell schedule** —
they capture ~+$11/unit more on wool in days 24–29 (HANDOFF 09-23). Not an operator gap.

### 4.7 Titan — `rivals/titan-kaggriculture-frontier-source/*.ipynb`, `tokenjunkielabs_…/submission.tar.gz`
Notebook markdown only (no readable code cells; payload is a sha256-pinned tarball at
`tokenjunkielabs_…/submission.tar.gz`, `79b407d6…`). Per its own README cell: *"TITAN is
an Apache-2.0 derivative of Kaito Fukami's public v43 SparseShopHybrid agent… preserves
the production/router policy and **conditionally advances finished-product sales using
observable farm state**"* — i.e. the same conditional-sale-advance family as
kaitofukami (§4.9). V43-class chassis. Nothing new mechanically; the tarball could be
extracted for exactness but the mechanism is already enumerated.

### 4.8 `rivals/mzcao7_kaggriculture-2476-8-peak-lightgbm-xgboost/_orig_main.py`
Learned late router (lines 82–119): `EnsembleAgent` wraps `router_base.py` Router;
at **step 648** extracts ~40 state features (early route, shop counts/first-shop flags,
both farms' money, hands, land, weeds, crop/animal counts, shed/carried inventory,
market prices+inventory, seeds — `state_features` 40–67) and scores **4 candidate
routes** through portable LightGBM+XGBoost tree ensembles; switches only if
`predicted[best] − predicted[baseline] > minimum_gain` (98–118). `router_base.py` is
*not* in the bundle — asset-dir dependency means the extracted agent needs the
notebook's data dir. **Genuinely different mechanism** (state-conditioned re-route vs
our unconditional `route=2`), but HANDOFF 09-18g/§5.19/5.24: later switching is only
safe at tape-shared state points, and day-6 information is the binding constraint.
Medium-value research item; do not blind-port.

### 4.9 `rivals/kaitofukami_177-180-fresh-top-30-v21-1-conditional-memory/_orig_main.py`
Conditional memory: `_public_route_signature` of the opponent farm → `_signature_distance`
to stored `_PROTOTYPES` → `_conditional_reorder` moves only *predicted-collision* sells
to the front (shed-clamped, totals preserved) when a known family is matched →
`_terminal_market` scores liquidation by opponent-exposure/glut/price/log1p(qty).
Overlaps our `_V93_ROUTE_BY_RIVAL` fingerprint + V92 stream matching + SIR, but the
*signature-distance-to-prototype* trigger is different from our exact-key fingerprint.
Marginal add — our coverage is arguably broader.

### 4.10 `rivals/lynnsakurai_farming-score-a-mathematical-approach/_orig_main.py` (V46)
Clone-phase detection (steps ~160–260), horizon-6 bounded sale shifting restricted to
STRAWBERRY/MELON/MILK/WOOL/FERTILIZER (deliberately excludes WHEAT/CARROT inputs),
excess-quantity caps; plus a latched `yarn_third` route gate on shop order + opponent
animal counts. Demonstrates the *bounded, replay-calibrated* version of adaptive sale
shifting. Mechanism class present in ours (RACE/reserve/sell_lead); the
product-whitelist discipline is worth copying **into** any future shift layer.

### 4.11 `rivals/shiiin9_beat-v48-100-0-your-herd-is-decided-on-day-6/_orig_main.py` — the standout
Same chassis family, router with day-6 (step 144) EXP240/V39 split + day-27 route 2
(952–962) — but three additions we lack:

**(a) `_CXO` confidence-gated herd swap (4044–4279) — the "decided on day 6" layer.**
Rewrites `BUY_ANIMAL` COW↔SHEEP orders (shared PASTURE structure → no schedule/build
moves). Decision rule: enumerate all towns the remaining shop draws can produce —
multinomial over `8 − len(shops)` slots, each milk-shop w.p. 3/8, yarn w.p. 1/8
(`_cxo_futures` 4134–4155) → score each future with a *measured* shop-count→second-half-
price table (`_CXO_PRICES` 4104–4105: WOOL {0:4,1:89,2:129}, MILK {0:1…6:261}) ×
remaining production `_cxo_units` (4124–4131) − cost. Swap only when the substitute
wins in **≥95% of reachable futures AND mean_gain ≥ 300** (`_cxo_better` 4191–4205) —
explicitly a *confidence* test, not EV, because the ladder pays W/L not margin.
State-aware PICKUP/PLACE follow-up (`_cxo_apply` 4208–4266) + `placements_left >
waiting` room check. Author's own measurement note: a swap right 4-in-5 still hands
back one certain win in five; ships 0.95 and 1.00 variants; cites +10,662 episode.

**Our coverage:** `_y_agent_shopherd` (6181–6305) is the *predecessor* — `_y_target`
fires only when the deciding shop is *already unlocked* (COW→SHEEP iff YARN_STORE out,
GOOSE→SHEEP iff yarn). No SHEEP→COW direction, no milk counting, no futures, no
confidence gate. HANDOFF 09-19b(g) confirms this is the same machinery but the CXO
decision rule is strictly stronger — it can act **before** the decisive shop appears
and can refuse marginal swaps. **This is the single best "missing mechanism" candidate.**
Caveats: it edits `BUY_ANIMAL` + physical PICKUP/PLACE — §5.16's herd-swap failure was
exactly an incomplete pickup/place rewrite; CXO's state-aware version is designed
around that failure, and our file already contains `_y_controller`'s credit tracker to
reuse.

**(b) `EXP303` resource-valuation terminal planner (3365+):** in the last-7-turn window,
proposes 1–2 *resource-bundle* closures (harvest/fertilizer valued at current prices)
replacing the E182 baseline suffix. We have E182 but not the proposal generator.
Small residual; the terminal window is already heavily worked.

**(c) `_R128` service-swap machinery (3113–3180):** pre-positioned animal swaps between
shed and pasture with next-step prefetch tracking — exists only to serve (a)'s swapped
animals. Not separately valuable.

Also carries `_R53_LABOR` (day-26–28 hire management — we have it at 2370), `_E334`
(present), v44y shopherd (present).

### 4.12 `rivals/avioon_kaggriculture-apex-v7-god-emperor/` — native C++ policy plugin
`source/policy.cpp` + `submission_bridge.cpp` + `agent.dylib`: `kEncodedTapes` decoded
per route; `kDecisionStep = 360` (day 15), `select_route` (61–72): route 1 iff
`shops[0]==BAKERY & FERTILIZER inventory ≤ 10232.5` or `shops[0]==PET_CAFE & opponent
plant_tiles ≤ 64.5`. `six_day_budget_guard.hpp` (153–217): every `kSegmentTurns=72`
steps, compute next-segment requirements (seeds/animals/feed/land/hires), if
cash+scheduled-sales < requirements, sell highest-priced inventory **above protected
static reserves** (protects items the tape will consume), min unit price 15, then
`budget_sales_first` moves SELLs ahead of non-SELLs. **Our `_r97_budget`/`_r97_supply`
is a per-turn *check*; this is a proactive *funding* seller.** But HANDOFF §5 lists
broad budget guards as measured-harmful (0-80, −26.7k in the layer-flip panel) — mark
low priority.

### 4.13 `rivals/uninhibitedscholar_kaggriculture-beyond-48-order-sequencing/_orig_main.py` (= jaxa623 K0006, the 2802 family)
V43 parent + three wrappers:
- `frontload` (146–183): groups orders A=non-wash SELLs, B=BUY_PRODUCT+wash-SELLs,
  C=other; tries permutations; keeps original **unless a solo simulation of cash/shed
  execution says the reorder fully executes** (`_simulate` 94–144: price model, hire
  fib costs, shed cap, land). This is the safe way to move SELLs ahead of HIRE/BUY_SEED.
- `advance_sales` (201–258): one-turn advance of pure-cash product sells (never WHEAT/
  FERTILIZER/inputs, never on the dawn turn `step%24==23` where the overflow contract
  inspects the shed) — relies on SELL-as-cap semantics so the parent's own step+1 sell
  just sells the residue.
- Step-0 single-order wheat round trip + widened reservation horizon 24.

**Our coverage:** `_v44y_reorder` permutes contiguous SELL blocks under a real lockstep
sim — but only within SELL blocks and against a self-mirror opponent schedule; SIR
moves sells only into slots ≤ last-sell. Neither crosses order-type boundaries with a
feasibility proof. The *concept* is present; the *scope* (sells before non-market-moving
orders, sim-verified) is genuinely narrower. **Worth measuring** — this family is the
known pipe16 counter-class, and it's a market-only change (zero tape divergence risk).

### 4.14 `rivals/llccqq624_kaggriculture-top-5-meta-ensemble/_orig_main.py`
Five embedded modules, but `agent` (91–105) is **pure failover** — `_AGENTS[0]` then
first valid fallback. `_market_mix` (59–88: peer-vote SELL reorder + route-distance
gate) is **dead code — never called**. Nothing to port.

### 4.15 `rivals/thomastschinkel_the-metav4-farm-submission-v13/_orig_main.py`
Our other live base. Same R108 chassis + router; `_SETTINGS` clamp_sells False.
subV_sirxP ⊃ metav4 layers.

---

## 5. Genuinely missing or materially weaker — ranked

| # | mechanism | source | expected impact | confidence | complexity | tape-compat | failure risk | scope |
|---|---|---|---|---|---|---|---|---|
| 1 | **CXO confidence-gated COW↔SHEEP swap** (multinomial futures over remaining shop draws × measured price table; ≥0.95 conf + ≥300 mean gain; state-aware PICKUP/PLACE) | shiiin9 4044–4279 | medium-high (~±3k/animal, fires on a subset of games; author's win-logic sound for W/L scoring) | medium-high (author cites +10.7k episode; ships 1.00 variant) | medium (port ~200 lines; our `_y_controller` credit/shed machinery reusable) | edits BUY_ANIMAL + pickup/place — **the §5.16 failure zone**; CXO's design is specifically the fix for that failure | medium | production mix (bounded window, days 8–11) |
| 2 | **Koshinm route-2 late sell schedule** — better days-24–29 timing; ~+$11/unit wool capture | koshinm base + HANDOFF 09-23 | ~$700–1000/game in the koshinm cell specifically | high (measured residual, ours trails +80@480 → −1k@end) | low-medium (tune/graft a route-2 tail, or shift premium sells to post-drain steps) | market-only if done as sell-timing; tape only if a new route | low-medium | endgame sell timing |
| 3 | **Animal-signature family counters** (sheep≥4/cows≤3 → R5-tape pre-sell ×1.0 @+2; cows≥4/quadrants≥2 → MD-tape ×2.0 @+1; town-demand gated) | rank-top10 340–447, 567–666 | medium (fires vs known families only; complementary to V92) | medium | medium (need embedded rival tapes + signature gate) | market-only | low-medium | market sales |
| 4 | **Sim-verified cross-type frontloading** (SELLs ahead of HIRE/BUY_SEED only if solo-sim proves full execution) | uninhibitedscholar 94–183 | low-medium (positional, ~$2/turn class like SIR) | medium (this family farms pipe16 live) | medium (cash/shed sim; our `_v44y_lockstep` is a starting point) | market-only | low (sim gates adoption) | market order list |
| 5 | **Learned step-648 route reselection** (LightGBM+XGB on ~40 state features, minimum-gain gate) | mzcao7 82–119 | unknown — ceiling is the oracle-gap question HANDOFF already sized | low (09-18g falsified day-9+ rerouting; 648 is a legal shared-state point but tapes diverge physically) | high (data collection + fit + validation) | route state — the dangerous axis | high | route |
| 6 | **EXP303 bundle-closure terminal planner** | shiiin9 3365+ | low | medium | medium | physical ops in 712–718 window | low-medium | terminal |
| 7 | **Conditional prototype memory** (signature→prototype→collision-only reorder) | kaitofukami | low (overlaps V92/V93/SIR) | medium | medium | market-only | low | market |
| 8 | **Proactive 72-turn funding budget guard** (avioon) | avioon six_day_budget_guard.hpp | low — **HANDOFF measured budget guards harmful** (0-80, −26.7k) | n/a | medium | market-only | medium | market/purchases |
| 9 | **Bounded clone-phase sale shift, product-whitelisted** (V46) | lynnsakurai | low | medium | low | market-only | low | market |

Not recommended: anything on HANDOFF §5 (herd swaps without command rewrite,
route remap on day-6 pairs, day-9+ switching, demand-adaptive animal co-pilot,
buy/sell reordering that breaks financing, generic rescue overlays, elastic sell
quantities, deferred opening purchases, premium-off-late variants).

---

## 6. Recommended measurement order

1. **Port `_CXO` as an optional config on `_y_agent_shopherd`** — reuse the existing
   credit tracker (`state['credit']`, `coop_swap`, `pending`) and gate it
   `confidence≥0.95 & mean_gain≥300` with the 1.00 variant as the conservative arm.
   Verify it fires (`_CXO_REPORT` counters) before measuring; ≥200 paired games vs
   subV_sirxP twin + pipe16 + melon + koshinm, both seats, fresh seeds.
   Watch specifically: `_cxo_placements_left` room check and the owed-animal ledger —
   §5.16 says an incomplete PICKUP/PLACE rewrite kills cows.
2. **Close the koshinm cell by sell timing, not operators**: instrument the days-24–29
   premium sells (per-item captured price vs post-drain peak) on paired seeds; test
   shifting our premium lots to the `step%4∈{1,2}` post-drain indices *within* the
   existing projected-shed framework. HANDOFF already localized the residual.
3. **Screen `market_queue_lockstep` + `adaptive_market_tape_guard`** (the only koshinm
   operators the round-table flagged as possibly safe) — cheap ports, measure on the
   same 224–261 seed block SIR used.
4. **Prototype the family counters** as a market-only layer: embed one R5-family and
   one MD-family tape, gate on the animal signature, measure on a seed panel seeded
   to include those families.
5. Defer learned re-routing until after the deadline unless a cheap win emerges —
   the data-collection cost is real and the divergence risk is documented.
