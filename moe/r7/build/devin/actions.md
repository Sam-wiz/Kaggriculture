# Kaggriculture action space — complete enumeration

Source: `kaggle_environments 1.32.7` engine
(`.venv/lib/python3.14/site-packages/kaggle_environments/envs/kaggriculture/kaggriculture.py`,
line refs below) + repo `AGENTS.md` game reference. Engine-exact.

## Shape of one turn

```py
{
  "farmer": [op, *args],          # exactly one op for the main farmer
  "hands":  [[op, *args], ...],   # one op per hired hand, in hands order
  "market": [[op, *args], ...],   # ordered orders, <= maxMarketOrdersPerTurn = 10
}
```

Order of resolution per step (`interpreter`, :894-946):
for each player (seat 0 then 1): farmer op, then each hand op (in `hands`
list order); then `_process_market` for both players; then town drains;
then plant decay; then end-of-day if `(step+1) % 24 == 0`. So **unit ops
always run before market orders within a step** — goods dropped at the
shed this turn are sellable this turn.

Every invalid action is a **silent no-op** (no error, no cost). Illegal
PLANT requests are the exception with a twist: if total PLANT demands for
a crop across all your units this turn exceed your seed stock, ALL of that
crop's PLANTs become PASS (:920-933).

## Farmer / hand ops (`farmer` + each entry of `hands`)

All positional ops act on the tile the unit stands on. `tiles[y][x]`,
x=column east→, y=row south↓. Movement is 1 tile orthogonally; board edge
= no-op; LOCKED tiles are passable for movement but reject every tile op
(:323-332, :414).

| op | args | preconditions | effect |
|---|---|---|---|
| `NORTH`/`SOUTH`/`EAST`/`WEST` | — | target inside 10×10 | move 1 tile (LOCKED passable) |
| `PASS` | — | — | nothing |
| `PICKUP` | item, [n=1] | on a shed tile (4,4)/(5,4)/(4,5)/(5,5); item in shed | take min(n, stock) into unit inv; seeds never enter shed (can't be picked up) (:358) |
| `PLACE` | item, [n=1] | (a) standing on empty matching structure + item in inv → places animal; (b) shed-adjacent → deposit n of item (capacity-clipped, remainder stays in inv) (:377) | animal→tile or item→shed |
| `DROP` | — | shed-adjacent | dump ENTIRE inv to shed; overflow past shedCapacity=100 is **discarded** (item deleted from inv even if it didn't fit) (:343) |
| `PLANT` | crop | tile empty (None), unlocked, seeds[crop]>0 | -1 seed → PLANT; `consecutive_unwatered=1`, `yield_units=1` (one-time) or 0 (ongoing); `max_lifespan_step=(day+max_yield_day+1)*24` one-time / -1 ongoing (:417) |
| `WATER` | — | PLANT tile, not `watered_today` | watered_today=True; one-time crops with `(max_yield_day+1)//2 <= age <= max_yield_day`: +1 yield (or +2 if fertilized), capped at max_yield (:431) |
| `HARVEST` | — | tile `yield_units`>0; PLANT: `age>=first_yield_day`; animal tile: harvests product | yield → unit inv; one-time PLANT tile → None after harvest (:446) |
| `FERTILIZE` | — | PLANT tile, ≥1 FERTILIZER in unit inv | `fertilized_until_day=max(prev, day+2)` — 3 days inclusive (:475) |
| `DIG` | — | tile not None, no animal on it | clears PLANT/WEED/empty COOP/PASTURE → None (:484) |
| `BUILD_COOP`/`BUILD_PASTURE` | — | tile None (empty, unlocked) | structure (:493,:499) |
| `FEED` | — | animal tile, not `fed_today`, ≥1 WHEAT in inv | -1 WHEAT → fed_today (:505) |
| `COLLECT_FERTILIZER` | — | animal tile, `fertilizer_available` | +1 FERTILIZER to inv (:515) |
| `CARE` | — | animal tile, not `cared_today` | cared_today; banks +1 `pending_care_bonus` only if also fed today (:524,:829) |

Hands spawn on the least-occupied shed-access tile, NWSE order (:533).
Hands/hires reset every end-of-day: positions cleared, `hires_today`→0,
inventories → shed (cap 100, overflow discarded), farmer re-spawns (:860-883).

## Market ops (`market`, ≤10/player/turn)

`_process_market` (:544-628): index-by-index **lockstep** between the two
players. At each index: `HIRE`/`BUY_LAND` resolve atomically in player
order; SELL/BUY_* then run **per-unit** — both players are quoted at the
SAME pre-commit inventory for that unit, then both commits attempt. An
order that fails once is dropped entirely. Sells fund buys placed behind
them *in the same list* (money commits immediately). Extras beyond index
9 silently dropped.

| order | args | preconditions | price / effect |
|---|---|---|---|
| `BUY_SEED` | crop, n | money ≥ price per unit | fixed `CROPS[crop].seed`; → private.seeds |
| `BUY_PRODUCT` | item, n | **item ∈ {WHEAT, FERTILIZER} only** (others rejected, slot voided); money ≥ price; shed room | `market_price(item, inv-1)` per unit (post-buy quote → buy/sell round-trip nets ~zero); item→shed, market inv -1 |
| `BUY_ANIMAL` | animal, n | money ≥ cost; **shed room** (animals land in shed!) | fixed GOOSE 300 / COW 400 / SHEEP 500 |
| `SELL` | item, n | shed[item]>0 per unit (stops at empty) | `market_price(item, inv)` per unit; money += price; inv +1 **only if price>1** ($1-floor sells don't re-add supply) |
| `HIRE` | — | money ≥ `fib(hires_today)` (1,1,2,3,5,…; 12 hands=$376/day) | hand spawns same turn |
| `BUY_LAND` | — | money ≥ next price | unlock order fixed NE $1k → SW $2k → SE $4k |

Sale price: `price(inv) = base ± amp·shape(|inv−10000|)`, floor $1; shape
per product per side (sqrt/log/sq/linear/hinge — hinge runs away past
knee T). See `islandga/engine_facts.py` for the verbatim table.

## Turn-level sequencing facts that constrain any agent

- Unit ops BEFORE market each step (your same-turn shed deliveries can fund/fill sells).
- Atomic PLANT rule: crop-level all-or-nothing per turn vs seed stock.
- Market settles per list index: order = priority; sells must precede the buys they fund.
- End-of-day (after hour 23): unwatered→weed at 2 consecutive; unfed→escape at 2;
  ongoing production step; weed spawn (one rng draw per EMPTY tile, both farms,
  then the every-3-day shop draw from the SAME stream); inventories→shed;
  hands cleared; hires reset; shop unlock w/ replacement (≤8 instances).
- Step 718 = last step; **day 29 gets no end-of-day refresh** — FEED/WATER/
  CARE/FERTILIZE on day 29 are wasted ops (last payable production = day 28).
- Town drains after market each step: shops consume their products every
  4 steps (2× for single-product shops), town center 1 of each
  non-fertilizer product every 24 steps. FERTILIZER drains nowhere.
