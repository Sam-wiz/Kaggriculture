"""Pure-Python port of ``the-35-0-tape-a-causal-shop-router``.

Exact, self-contained re-implementation of the native (C++/ctypes) policy that
shipped with that kernel:

  * ``source/policy.cpp``                    -- tape replay + route selection
  * ``source/include/six_day_budget_guard.hpp`` -- the only adaptive logic
  * ``source/include/sim.hpp``               -- enums / static data / ``fib``
  * ``submission_bridge.cpp``                -- per-seat session reset rule
  * ``_entry.py``                            -- observation packing / action unpacking

No ctypes, no local imports, and no use of ``__file__`` (Kaggle's raw-python
loader ``exec``s the submission with ``__file__`` undefined).

The two 719-turn action tapes are embedded below as zlib+base85 of the exact
space-separated text that lived in ``source/tape.inc``.
"""

import base64
import math
import zlib
from collections.abc import Mapping

# --------------------------------------------------------------------------
# sim.hpp: item space
# --------------------------------------------------------------------------
_ITEMS = (
    "WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG",
    "MILK", "WOOL", "FERTILIZER", "GOOSE", "COW", "SHEEP",
)
_PRODUCTS = _ITEMS[:9]
_CROPS = _ITEMS[:5]
_ITEM_ID = {name: index for index, name in enumerate(_ITEMS)}

N_ITEMS = 12
N_PRODUCTS = 9
N_CROPS = 5
WHEAT = 0
FERTILIZER = 8
GOOSE = 9

# sim.hpp: unit ops (index == enum Op value)
_UNIT_OPS = (
    "PASS", "NORTH", "SOUTH", "EAST", "WEST", "PICKUP", "DROP",
    "PLACE", "PLANT", "WATER", "HARVEST", "FERTILIZE", "DIG",
    "BUILD_COOP", "BUILD_PASTURE", "FEED", "COLLECT_FERTILIZER", "CARE",
)
OP_PLACE = 7
OP_PLANT = 8
OP_FERTILIZE = 11
OP_FEED = 15

# sim.hpp: market ops (index == enum MOp value)
_MARKET_OPS = ("PASS", "HIRE", "BUY_LAND", "BUY_SEED", "BUY_PRODUCT", "BUY_ANIMAL", "SELL")
M_HIRE = 1
M_BUY_LAND = 2
M_BUY_SEED = 3
M_BUY_PRODUCT = 4
M_BUY_ANIMAL = 5
M_SELL = 6

# sim.hpp: static economic data
CROP_SEED_COST = (10, 20, 50, 100, 80)          # CROPS[i].seed
ANIMAL_COST = (300, 400, 500)                    # ANIMALS[i].cost, i = item - GOOSE
LAND_PRICES = (1000, 2000, 4000)

# sim.hpp: shops, in sorted(SHOPS) order
_SHOPS = (
    "BAKERY", "BRUNCH_SPOT", "FARMERS_MARKET", "ICE_CREAM_SHOP",
    "PET_CAFE", "PIZZA_SHOP", "SMOOTHIE_SHOP", "YARN_STORE",
)
_SHOP_ID = {name: index for index, name in enumerate(_SHOPS)}
SHOP_FARMERS_MARKET = 2
SHOP_ICE_CREAM_SHOP = 3

# _entry.py: tile-kind packing (index == enum TileKind value)
_KIND_ID = {
    None: 0, "EMPTY": 0, "SOIL": 0, "LOCKED": 1, "WEED": 2,
    "COOP": 3, "PASTURE": 4, "PLANT": 5,
}
T_COOP = 3
T_PASTURE = 4

BOARD = 10
MAX_UNITS = 40
MAX_SHOP_INSTANCES = 8

# policy.cpp
K_TURNS = 719
K_ROUTES = 2
K_SEGMENT_TURNS = 72
K_DECISION_STEP = 216

# kag::Config defaults used by the policy (submission_bridge.cpp only ever
# overrides ``episode_steps``, which the policy never reads).
CFG_HIRE_MULT = 1
CFG_MAX_ORDERS = 10

# six_day_budget_guard.hpp: SixDayBudgetGuardSettings, as set by policy.cpp
GUARD_INTERVAL_TURNS = K_SEGMENT_TURNS
GUARD_MIN_UNIT_PRICE = 2
GUARD_SALES_FIRST = True
GUARD_PROTECT_STATIC_CONSUMPTION = True
