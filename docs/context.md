Description
This simulation competition is a turn-based farming game where two players compete on separate farms to see who can earn the most profit by the end of a 30-day season (720 turns).

Your agent acts as the main farmer and can strategically hire farm hands to scale up operations. To succeed, your agent must:

Plant, water, fertilize, and harvest a variety of crops.
Buy, feed, and care for animals to produce eggs, milk, and wool.
Collect and utilize fertilizer to boost crop yields.
Buy neighboring quadrants of land to expand your farm's footprint.
Trade smart on a dynamic market where prices react to your sales and town demand.
Kaggriculture represents a highly complex environment that models the exact same dynamics found in real-world supply chains, dynamic market pricing, and industrial resource allocation under uncertainty. Underlying mechanics like scheduling resources, optimizing labor, adjusting to supply/demand price changes, and making long-horizon capital investments, serve as a high-fidelity sandbox for training AI to solve complex enterprise operations.
![alt text](image.png)
imeline
July 29, 2026 - Start Date.

September 23, 2026 - Entry Deadline. You must accept the competition rules before this date in order to compete.

September 23, 2026 - Team Merger Deadline. This is the last day participants may join or merge teams.

September 30, 2026 - Final Submission Deadline.

October 1, 2026 to (approx) October 15, 2026 - We will continue to run games, or until the leaderboard has reached convergence. At the conclusion of this period, the leaderboard is final.

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.

Evaluation
Each day your team is able to submit up to 5 agents (bots) to the competition. Each submission will play Episodes (games) against other bots on the ladder that have a similar skill rating. Over time, skill ratings will go up with wins or down with losses, and even out with ties. To reduce the number of bots playing and ensure high-quality matching, only the latest 2 submissions are tracked. The latest 2 submissions are also used for final leaderboard evaluation.

Every bot submitted will continue to play episodes until the end of the competition, with newer bots playing a much more frequent number of episodes. On the leaderboard, only your best-scoring bot will be shown, but you can track the progress of all of your submissions on your Submissions page.

When you upload a submission, a Validation Episode is run where your agent plays against a copy of itself to ensure it runs without errors. If the episode fails, the submission is marked as Error, and you can download the agent logs to debug. Otherwise, the submission is initialized with a default rating and joins the matchmaking pool.

Ranking System
Each submission is assigned a skill rating. When your agent plays an episode against an opponent:

Winning the match (having the most coins in the bank at the end of 720 turns) increases your skill rating, while losing decreases it.
The amount your rating changes depends on the rating difference between you and your opponent. Beating a highly-rated agent will boost your rating more than beating a lower-rated one.
Ties will generally pull ratings closer together.
The actual coin difference in a match does not affect the rating change—only the win, loss, or tie outcome matters.
Final Evaluation
At the submission deadline, additional submissions will be locked. Games will continue to run for approximately two weeks to continue to reduce uncertainty, especially for new agents. A final Bradley-Terry tournament will be run on those episodes to produce the final leaderboard.

Prizes
1st Place - $5,000
2nd Place - $5,000
3rd Place - $5,000
4th Place - $5,000
5th Place - $5,000
6th Place - $5,000
7th Place - $5,000
8th Place - $5,000
9th Place - $5,000
10th Place - $5,000

How to Play
Overview
Each player starts with an empty farm and a small amount of income (seed money, if you will). Each turn, they can perform actions such as moving around the board, purchasing seeds or livestock, planting seeds, watering plants, harvesting produce or animal products, and selling that produce at the market. The game runs for a fixed amount of time representing one season, and the winner is determined by who has the most money in the bank at the end.

Object Types
Type	Yield Type	Seed Cost	Base Market Price	Time to First Yield	Time to Max Yield	Subsequent Yields	Max Yield	Action Cost	Yield / tile / day
Wheat	One-time	10	25	2 days	4 days	none	6 (4 unfertilized)	1	0.80
Carrot	One-time	20	35	2 days	3 days	none	4 (3 unfertilized)	1	0.75
Tomato	Ongoing	50	60	8 days	11 days	every day ×4	4	1	0.33
Strawberry	Ongoing	100	120	10 days	16 days	every other day ×4	4	1	0.24
Melon	One-time	80	250	10 days	10 days	none	6	1	0.55
Goose/Egg	Ongoing	300	50	4 days	NA	every day, indefinitely	4 held	1 + 1 (build coop)	1.00
Cow/Milk	Ongoing	400	160	8 days	NA	every two days, indefinitely	6 held	1 + 1 (build pasture)	0.50
Sheep/Wool	Ongoing	500	200	6 days	NA	every three days, indefinitely	6 held	1 + 1 (build pasture)	0.33
Fertilizer	NA	100	X		X	X		1	
For crops, "Yield / tile / day" is total units harvested divided by the days the tile is occupied, watering daily and harvesting at peak yield. For animals it is the steady-state production rate (1 / interval) once the first yield lands; animals keep producing for as long as they are fed, so there is no fixed occupancy to divide by. "Max Yield" for animals is max_held, the cap on unharvested product sitting on the tile, not a lifetime total.

Crop "Time to Max Yield" is the age at which yield stops increasing under daily watering, which is not always the end of the bonus window:

Melon's bonus window is ages 6–12, but base 1 plus one unit per watered day reaches the cap of 6 at age 10, so ages 11–12 add nothing. Fertilizing reaches the cap at age 8.
Wheat and Carrot only reach their listed Max Yield of 6 and 4 with fertilizer; watering alone peaks at 4 and 3.
Tomato and Strawberry are ongoing but not indefinite: production is capped at 4 scheduled yields (tomato at ages 8–11, strawberry at ages 10, 12, 14, 16), after which the plant decays into a weed.
All plants must be watered every day. They will turn into weeds if they are not watered for two successive days. All animals must be fed every day using wheat. They will escape and be unrecoverable if they are not fed for two successive days. Wheat is also available to buy at the market and can be purchased at the current market price.

Actions
Each turn, the player may take one action. There are 24 turns per day, and 30 days in the season - 720 total turns.

Farmer / Farm Hand Action
Each Farmer / Farm Hand can be given an action every turn. Farmer/Farm Hand CAN occupy the same space.

Movement
NORTH, SOUTH, EAST, WEST — Move one cell in that direction. Moves off the edge of the board are no-ops. Locked tiles are passable: a unit may move onto and across unbought quadrants, but tile actions (PLANT, WATER, BUILD_*, etc.) all no-op on a locked tile and consume nothing. The exception is the shed actions PICKUP, DROP, and PLACE-into-shed, which work from any shed-access tile even while that tile is locked — they use the tile only as a standing position and never change it.
Shed
Picks up an item from the shed (must be orthogonally adjacent) into the inventory

PICKUP <item> [n] — move up to n of <item> (default 1) from the shed into the active farmer/hand's inventory. Any item present in the shed is valid (animals, fertilizer, harvested produce, etc.). Seeds live in a separate slot and are never picked up — PLANT consumes them directly.
DROP — orthogonally adjacent to the shed, dump the active farmer/hand's entire current inventory into the shed. Overflow past shedCapacity is discarded. No-op if not shed-adjacent.
Plants
PLANT — Plant a seed purchased from the market
Seeds are automatically available to all Farmers / Farm Hands
If you try to plant too many in a specific turn, none are planted
ie if you have 1 melon seed, but two units do the PLANT MELON command
WATER — Water a plant. This only needs to be done once per day, and subsequent waterings on the same day are a no-op.
HARVEST — Gather produce from a plant. If the plant does not have subsequent yields, it will be removed from the map. Each harvest action will yield at least one unit of the crop, with the potential of additional yield depending on watering and fertilizer (the formula differs by crop type — see harvest yields below). Harvested items are added to the inventory.
FERTILIZE — Fertilize a plant to increase its potential yield (see harvest yields below).
Doubles the per-day yield bonus for the next 3 days. The bonus only applies on days the plant is also watered (basic needs first).
Animals
PLACE <item> [n] — Drop items from the active farmer/hand inventory into either a tile or the shed:
Animal placement: standing on a matching unoccupied structure (GOOSE on a coop, SHEEP/COW on a pasture) places one animal from inventory onto the tile. The n argument is ignored.
Shed drop: standing orthogonally adjacent to the shed moves up to n (default 1) of <item> from inventory into the shed. Capped by shedCapacity; excess stays in inventory.
FEED — Feed an animal using wheat (only needs to be done once per day)
HARVEST — Collect the eggs/milk/wool produced by the animal.
COLLECT_FERTILIZER — Collect 1 fertilizer from the animal. Every surviving animal makes 1 available at the end of each day, whether or not it was fed or cared for. Uncollected fertilizer does not accumulate, so an animal left alone for five days still yields 1 unit.
CARE — Care for an animal (once per day, no-op if already cared for). See animal care below.
Animal Care
CARE banks a yield bonus that is paid out on the animal's next scheduled production:

At end of day, if the animal was both fed AND cared for that day, pending_care_bonus increments by 1. Days where the animal was unfed do not bank a bonus (basic needs first).
On a scheduled production day, if the animal is fed, the entire banked bonus is added to that production's yield (in addition to the base 1) and the bank resets to 0.
If the animal is unfed on the production day, the base 1 unit is still produced, but the banked bonus is not applied and the bank resets to 0.
pending_care_bonus is capped indirectly by the per-animal max_held cap on yield_units.
Terrain
BUILD_COOP - adds a coop to an unoccupied tile
BUILD_PASTURE - add pasture to an unoccupied tile
DIG — Remove a plant from a square to free up space OR remove a weed from a square (does not yield any produce) OR remove an empty goose coop / pasture. A coop or pasture with an animal on it cannot be dug; the DIG is a no-op.
Other
PASS — Default if there is nothing to do (optional)
Market Action
Each turn you can submit up to maxMarketOrdersPerTurn (default 10) market actions; any orders past that limit are silently dropped. This is an ordered list and market orders will be processed in order simultaneously (one from each player) while both players have orders.

BUY_SEED — Purchase N units of a single item from the market.
BUY_SEED WHEAT 1
BUY_ANIMAL -
BUY_ANIMAL GOOSE 1
BUY_PRODUCT
BUY_PRODUCT WHEAT 1
BUY_PRODUCT FERTILIZER 1
SELL — Sell N units of a single item to the market.
SELL WHEAT 1
HIRE — Hire a farm hand for the day. Cost increases for each extra hand hired on the same day.
BUY_LAND - unlock a new 5x5 segment of land to plant on. Increasing in cost.
Costs are: $1k, $2k, $4k
Watering / Animal Feed
Plants (and animals) must be watered/fed a minimum of every other day. Watering only needs to be done once per day, and subsequent watering actions are a no-op. In the case of plants not watered for two consecutive days, at the end of the day they turn into a WEED. In the case of animals they escape (unrecoverable).

A new seed starts with consecutive_unwatered = 1 — the planting day itself counts as the first missed day. A seed planted and left unwatered that same day reaches 2 at the end-of-day refresh and becomes a weed that night, before it grows. There is no grace period for fresh plantings.

A newly placed animal starts with consecutive_unfed = 0, so it survives its first day unfed.

Note that watering one-time yield plants during their yield window results in a higher yield. This is NOT true for ongoing yield plants/animals. See below.

Harvest Yields
Plants will potentially have higher yields based on how well they have been cared for.

One-time crops (wheat, carrot, melon): Starting at half the plant's max_yield_day (Time to Max Yield) rounded up, watering during the bonus window will add one unit per day to the total harvestable yield.
Fertilized plants add 2 per day instead.
Ongoing crops (tomato, strawberry): Scheduled production happens at fixed intervals. The base yield is 1 per scheduled production. If the plant is fertilized AND watered that day, yield is doubled to 2.
Once a plant has hit its maximum lifespan, the total yield available on the plant will reduce by 1 every other turn until it hits 0, at which point the plant becomes a weed.
One-time crops reach max lifespan one day after max_yield_day.
Ongoing crops start decay one day after their cumulative production count reaches max_yield (i.e. they've fired enough scheduled productions to hit the cap, regardless of whether the produce has been harvested).
Map Features
Each player has their own farm with a set number of squares. Players are unable to see the state of the other’s shed, but can see the state of their opponent’s farm.

Farm Space
The land near your farm is a boardSize × boardSize grid (default 10×10), divided into four 5×5 quadrants. At first, your farm covers one quadrant (25% of the squares). For an increasingly large fee, you can buy the neighboring quadrants and eventually cover 100% of the squares.
Each plant or animal occupies one square on the farm.
Players can allocate these squares however they choose between crops and livestock. There are no specific limits per type.
Weeds have a chance of spawning on any empty cells on the farm, and must be cleared before the land can be used for other purposes.
Squares on the farm can be either a plant, a coop/pasture, a weed, or empty.
Shed (Inventory)
Functions as an inventory for items that are harvested but not yet sold, or for seeds that have not yet been planted
Farmer and hired farm hands will spawn at the shed at the start of each day
Farmer and hired farm hands drop their inventory at the end of the day in the shed (if there is room)
Limited to 100 items, excluding seeds. Once the shed is full, any further items added (via PLACE mid-day or end-of-day inventory drop) are discarded — there is no overflow holding area, so stockpiling on farmer/hand inventories does not bypass the cap.
The shed sits at the center of the board and is not a tile — it never appears in the tiles array, whose only values are None, "LOCKED", and structure dicts. "Orthogonally adjacent to the shed" means standing on one of the four center tiles, (half-1, half-1), (half, half-1), (half-1, half), (half, half) for half = boardSize // 2. At the default boardSize = 10 those are (4,4), (5,4), (4,5), and (5,5), one in each quadrant. Since only NW starts unlocked, three of those four tiles begin locked; the shed is reachable from all of them regardless, because the shed itself is never locked.

Farmer/Farm Hand
Hiring
Hiring is a market order (HIRE). It costs more every time you want to hire an additional hand each day. At the end of the day all, hands drop inventory at the farm and disappear (need to be re-hired each day)
Cost is farmHandCostMult * fib(n) where n is the number of hires already made today (fib starts 1, 1, 2, 3, 5, 8, 13, …).
With the default farmHandCostMult = 1: 1, 1, 2, 3, 5, 8, 13, 21, etc… (resets at the start of each day)
A hired hand appears orthogonally adjacent to the shed in a free space following NWSE. If there are not open spaces, it looks for the one with the least occupants, breaking ties by NWSE preference
Spawn placement ignores whether the tile is locked. Since the main farmer starts on (4,4), the least-occupied rule sends the first hire of each day to (5,4), which is locked until the NE quadrant is bought. Locked tiles are passable, so a hand spawned on one can move back to unlocked land.
Inventory
When harvesting or picking items up, they are added to inventory.
Can drop items in the shed
At the end of the day, all items in all inventory will be added to shed inventory (if there is room). Anything that doesn't fit is discarded — overflow is lost.
Town Buildings
As the season progresses, new shops unlock at regular intervals (every townShopUnlockInterval days, default 3). Each unlock is drawn uniformly at random with replacement from the full shop table, so the same shop can unlock more than once — a season might end up with three bakeries and no yarn store. Once unlocked, a shop stays active for the rest of the game, and unlocking stops after 8 total instances. Total demand grows monotonically as more shops unlock.

Each unlocked shop instance consumes one of every product it demands every townShopSellInterval turns (default 4). So with the default interval, a shop demanding wheat removes 6 wheat from the market per day, and two copies of that shop remove 12. Single-product shops consume 2x.

In addition, the town center consumes one of every product (excluding fertilizer) every townCenterSellInterval turns (default 24, i.e. once per day). This rate is flat for the whole season — it does not ramp.

Shop Type	Increases Demand For
Bakery	eggs, wheat
Pizza Shop	milk, tomatoes, wheat
Brunch Spot	eggs, wheat, strawberries
Yarn Store	wool (2x)
Ice Cream Shop	strawberries, milk, wheat
Pet Cafe	carrots (2x)
Smoothie Shop	strawberries, milk
Farmers Market	wheat, carrots, tomatoes, strawberries
Market Mechanics
The market has an unlimited supply of seeds and animals at fixed prices. Sell prices, however, move dynamically per resource and persist across days.

Every product (and fertilizer) starts the game with a market inventory of I0 = 10,000 units, far above any single game's realistic production volume so that inventory is essentially guaranteed to stay positive. The sell price for a product is base at I0, rises as inventory falls (players buying or town consumption draining supply), and falls as inventory grows (players selling).

Selling inventory to the market
Players can queue any number of sell or buy orders (for any quantity) in the market action list. Orders are processed concurrently across players, one unit at a time. For example, when both players issue SELL CARROT 10 first, we take the current carrot price, give both players that price for their first carrot, then add 2 carrots to the market (1 from each player) — which may shift the price — and repeat until both orders complete.

If the sell price has been driven down to $1 (the price floor), the unit is still purchased but is not added to market inventory, so the floor remains responsive to subsequent buys.

Buying inventory from the market
Only WHEAT and FERTILIZER can be bought from the market via BUY_PRODUCT (other products are sold at the market but not bought back). Selling is unrestricted: every product, including fertilizer collected from animals, can be sold via SELL. Two things drain market inventory: town buildings (town center and shops, which consume products for free) and player BUY_PRODUCT orders. Buy orders follow the same one-unit-at-a-time concurrent procedure as sell orders. If a player runs out of money mid-order, the order is stopped.

The buy price is quoted at the post-buy inventory and the sell price is quoted at the pre-sell inventory, so an immediate buy followed by a sell of the same item against an otherwise-unchanged market nets exactly zero.

The Price Function
For each resource the curve is defined by a base price, an anchor throughput T, and an independent shape function + target move for each side of the equilibrium:

price(inv) = base + sign · amp · f(|inv − I0|)
  sign = +1  if inv < I0   (scarcity → price up)
  sign = −1  if inv > I0   (glut    → price down)
  amp  = target · base / f(T)        (derived; not stored)
  f    ∈ { linear, sq, sqrt, log, log10, hinge }   (log uses ln(1+x), so f(0)=0)
Floored at $1 and rounded to the nearest dollar.

hinge is the one shape that depends on T rather than on x alone: with u = x / T it evaluates to u + 8 · max(0, u − 1)². Below T it is linear in u; above T the quadratic term takes over and the price climbs steeply. Since f(T) = 1 by construction, target keeps its usual meaning.

T is the production capacity of a single 5×5 field over a 24-day window at optimal watering with no fertilizer (animal totals are pre-discounted by 30% to account for wheat-feed overhead, and allow one day to build the coop or pasture). The 24-day window is a calibration horizon, not the 30-day season length. It is shorter on purpose: the opening days are setup-heavy and yield little.

target says "moving T units past I0 shifts the price by target × base." Picking different f and target on each side lets resources with similar production profiles play very differently strategically — wheat panics on scarcity but absorbs gluts; melon barely reacts to scarcity but crashes hard on overproduction; wool mirrors melon at a smaller scale. Premium resources (base > $100: strawberry, melon, milk, wool) use above_target > 1, so even modest gluts drive them straight to the $1 floor — bundling and timing sales matters more for these than for staples.

Carrot, tomato and egg use hinge on the scarcity side, so their prices stay near base under ordinary demand and rise sharply once demand runs past T. The town shops that consume them are listed in unlocked_shops.

Carrot — hinge at below_target 1.00. Consumed by pet cafes (single-product, so each consumes double) and farmers markets.
Tomato — hinge at below_target 0.40. Consumed by pizza shops and farmers markets.
Egg — hinge at below_target 0.40. Consumed by bakeries and brunch spots.
Tomato and egg keep the below_target of the linear curves they replaced. Because linear's amplitude already normalises to x / T, which is exactly hinge's below-knee branch, their prices from I0 down to I0 − T are unchanged; the curves differ only past the knee.

Resource	Base	I0	T	Below func	Below target	Above func	Above target	P(I0−T)	P(I0+T)	P(I0+2T)
Wheat	25	10,000	400	sqrt	0.80	log	0.20	$45	$20	$19
Carrot	35	10,000	450	hinge	1.00	sqrt	0.70	$70	$10	$1
Tomato	60	10,000	200	hinge	0.40	sqrt	0.60	$84	$24	$9
Strawberry	120	10,000	100	sqrt	0.70	linear	1.60	$204	$1	$1
Melon	250	10,000	300	log	0.20	sq	3.60	$300	$1	$1
Egg	50	10,000	332	hinge	0.40	log	0.20	$70	$40	$39
Milk	160	10,000	122	sqrt	0.60	linear	1.60	$256	$1	$1
Wool	200	10,000	105	log	0.20	sq	3.20	$240	$1	$1
Fertilizer	100	10,000	200	linear	0.40	linear	0.40	$140	$60	$20
The defaults live in MARKET_PARAMS in kaggriculture.py. Per-resource overrides (sparse: any subset of base, I0, T, below_func, below_target, above_func, above_target) can be supplied at episode creation via env.configuration["marketParams"] without touching code, e.g. {"WOOL": {"above_target": 0.95}}.

Turn Processing Order
Action validation — verify action legality
Player actions — record the actions taken by each player (happening simultaneously)
Market actions - process market queue in order by player (described above)
Town buy actions - town center and shops reduce inventory
Update observations
Day refresh — if applicable, update the condition of plants and animals for a new day, and reset their fed/watered to condition to false
Market refresh — modify the price of items on the market based on sells from previous turn
Income update — update the player’s bank based on any buys or sells
Farm update — clear plants that have been harvested, items from the inventory that have been used or sold, add new plants/animals to the farm, etc
Win Conditions
The win condition is simple- whoever has the greatest number of coins at the end of the season is the winner. It is also possible that the two players will tie.

Reward
The player who has the most money in the bank at the end of the game wins. Unsold items in the inventory do not count towards that total.

Observation Format
The top-level observation passed to each agent:

{
  "player": int,           # 0 or 1
  "day":    int,           # 0-indexed in-game day
  "hour":   int,           # 0-indexed turn within the day
  "farms":  [farm, farm],  # public per-player state, indexed by player id (shared)
  "market": {              # shared
    "inventory": { "WHEAT": int, "CARROT": int, ... },
    "prices":    { "WHEAT": int, "CARROT": int, ... },
  },
  "town": {                # shared
    "unlocked_shops": ["BAKERY", "BAKERY", ...],   # may repeat; each entry consumes independently
  },
  "private": {             # this player only; opponent's private state is not visible
    "shed":        { "WHEAT": int, "GOOSE": int, "FERTILIZER": int, ... },
    "seeds":       { "WHEAT": int, "CARROT": int, ... },
    "inventories": [farmer_inv, hand_inv, ...],  # [0] is the main farmer
  },
}
Each farm dict (public, visible to both players):

{
  "money":              float,
  "tiles":              [[tile, ...], ...],   # tiles[y][x]
  "farmer":             [x, y],
  "hands":              [[x, y], ...],         # hired hands for the current day
  "unlocked_quadrants": ["NW", ...],          # subset of {"NW","NE","SW","SE"}
  "hires_today":        int,                  # used to price the next HIRE
}
A tile is one of:

None — empty unlocked tile
"LOCKED" — tile in a quadrant the player has not yet bought
a plant dict:
  {
    "kind":                 "PLANT",
    "crop":                 "WHEAT" | "CARROT" | "TOMATO" | "STRAWBERRY" | "MELON",
    "planted_day":          int,
    "watered_today":        bool,   # reset to False each end-of-day
    "consecutive_unwatered": int,   # 2+ → tile turns to a weed
    "yield_units":          int,    # units currently harvestable
    "max_lifespan_step":    int,    # step at which decay begins; -1 for ongoing crops
    "fertilized_until_day": int,    # last day fertilizer bonus applies; -1 if none
  }
a weed dict: {"kind": "WEED"}
an animal structure dict (coop/pasture, optionally occupied):
  {
    "kind":                 "COOP" | "PASTURE",
    "animal":               "GOOSE" | "COW" | "SHEEP" | None,  # None until PLACEd
    "placed_day":           int,
    "yield_units":          int,
    "fed_today":            bool,
    "consecutive_unfed":    int,    # 2+ → animal escapes
    "cared_today":          bool,
    "fertilizer_available": bool,   # set at end-of-day for every surviving animal; cleared by COLLECT_FERTILIZER
    "pending_care_bonus":   int,    # banked CARE bonus, applied on the next yield tick
  }
Quick Start
from kaggle_environments import make


def my_agent(obs):
    # Buy one wheat seed on the very first turn, then PASS forever after.
    if obs.get("step", 0) == 0:
        return {"farmer": ["PASS"], "market": [["BUY_SEED", "WHEAT", 1]]}
    return {"farmer": ["PASS"], "market": []}


env = make("kaggriculture", configuration={"episodeSteps": 200})
env.run([my_agent, "random"])
env.render(mode="ipython", width=800, height=800)
Configuration Defaults
Per-crop seed costs and per-product base prices are not configurable; they are documented in the Object Types and Price Function tables above. The configurable knobs are:

Parameter	Default	Description
episodeSteps	720	Total turns in the season (24 turns × 30 days)
boardSize	10	Width and height (in tiles) of each player's square farm. Advanced uses 10 = four 5x5 quadrants
startingMoney	3000	Coins each player starts with
maxMarketOrdersPerTurn	10	Maximum number of market orders processed per player per turn; extras are silently dropped
turnsPerDay	24	Number of turns that make up one in-game day
shedCapacity	100	Max non-seed items the shed can hold; overflow at end-of-day drop is discarded
weedSpawnChance	0.005	Per-tile probability of a weed spawning on an empty unlocked tile during end-of-day refresh
townShopUnlockInterval	3	Days between successive town shop unlocks (drawn with replacement, capped at 8 instances)
townShopSellInterval	4	Turns between consumption ticks by every unlocked town shop instance
townCenterSellInterval	24	Turns between consumption ticks by the town center (flat rate, once per day)
seed	null	Optional input seed for deterministic episode generation; cleared from config after read so it stays out of agent observations
Getting Started: Test Locally & Submit
This guide walks you through building an agent, testing it locally, and submitting it to this simulation competition.

Test Locally
Install the environment from PyPI (any recent release that includes Kaggriculture):

pip install -U kaggle-environments
Run a game from Python or a notebook — you can pass agent functions directly, or paths to .py files:

from kaggle_environments import make

env = make("kaggriculture", configuration={"episodeSteps": 720}, debug=True)
env.run([agent, "random"])  # or env.run(["main.py", "random"]) to load from a file

# View result
final = env.steps[-1]
for i, s in enumerate(final):
    print(f"Player {i}: reward={s.reward}, status={s.status}")

# Render in a notebook
env.render(mode="ipython", width=1200, height=800)

# Or dump a replay JSON for the visualizer / offline analysis
import json
with open("replay.json", "w") as f:
    json.dump(env.toJSON(), f)
Three built-in agents are available by name: "pass", "random", and "starter" (a deterministic baseline).

Set Up the Kaggle CLI
Install the CLI:

pip install kaggle
You'll need a Kaggle account — sign up at https://www.kaggle.com if you don't have one. Then download your API credentials at https://www.kaggle.com/settings/api by clicking "Generate New Token" under the "API" section.

Recommended: API token file. Save the token string to ~/.kaggle/access_token:

mkdir -p ~/.kaggle
# Paste the token from the Kaggle settings UI into this file
nano ~/.kaggle/access_token
chmod 600 ~/.kaggle/access_token
Alternative auth methods:

OAuth (browser flow): kaggle auth login
Environment variable: export KAGGLE_API_TOKEN=xxxxxxxxxxxxxx
Verify the CLI is wired up:

kaggle competitions list -s "kaggriculture"
Find the Competition
kaggle competitions list -s "kaggriculture"
kaggle competitions pages kaggriculture
kaggle competitions pages kaggriculture --content
Accept the Competition Rules
Before submitting, you must accept the rules on the Kaggle website. Navigate to https://www.kaggle.com/competitions/kaggriculture and click "Join Competition".

Verify you've joined:

kaggle competitions list --group entered
Download Competition Data
kaggle competitions download kaggriculture -p kaggriculture-data
Submit Your Agent
Your submission must have a main.py at the root with an agent function.

Single file agent:

kaggle competitions submit kaggriculture -f main.py -m "Wheat loop v1"
Multi-file agent — bundle into a tar.gz with main.py at the root:

tar -czf submission.tar.gz main.py helper.py model_weights.pkl
kaggle competitions submit kaggriculture -f submission.tar.gz -m "Multi-file agent v1"
Notebook submission:

kaggle competitions submit kaggriculture -k YOUR_USERNAME/kaggriculture-agent -f submission.tar.gz -v 1 -m "Notebook agent v1"
Monitor Your Submission
Check submission status:

kaggle competitions submissions kaggriculture
Note the submission ID from the output — you'll need it for episodes.

List Episodes
Once your submission has played some games:

kaggle competitions episodes <SUBMISSION_ID>
CSV output for scripting:

kaggle competitions episodes <SUBMISSION_ID> -v
Download Replays and Logs
Download the replay JSON for an episode (for visualization or analysis):

kaggle competitions replay <EPISODE_ID>
kaggle competitions replay <EPISODE_ID> -p ./replays
Download agent logs to debug your agent's behavior:

# Logs for the first agent (index 0)
kaggle competitions logs <EPISODE_ID> 0

# Logs for the second agent (index 1)
kaggle competitions logs <EPISODE_ID> 1 -p ./logs
Check the Leaderboard
kaggle competitions leaderboard kaggriculture -s
Typical Workflow
# Test locally
python -c "
from kaggle_environments import make
env = make('kaggriculture', debug=True)
env.run(['main.py', 'random'])
print([(i, s.reward) for i, s in enumerate(env.steps[-1])])
"

# Submit
kaggle competitions submit kaggriculture -f main.py -m "v1"

# Check status
kaggle competitions submissions kaggriculture

# Review episodes
kaggle competitions episodes <SUBMISSION_ID>

# Download replay and logs
kaggle competitions replay <EPISODE_ID>
kaggle competitions logs <EPISODE_ID> 0

# Check leaderboard
kaggle competitions leaderboard kaggriculture -s
Quick Start Agent
Below is a simple starter agent implementing a basic wheat loop:

def agent(obs):
    player = obs["player"]
    me = obs["farms"][player]
    private = obs["private"]
    fx, fy = me["farmer"]
    tile = me["tiles"][fy][fx]

    market = []

    # Buy a wheat seed if we have none and have enough money
    if private["seeds"].get("WHEAT", 0) == 0 and me["money"] >= 10:
        market.append(["BUY_SEED", "WHEAT", 1])

    # Sell any wheat sitting in the shed
    wheat_in_shed = private["shed"].get("WHEAT", 0)
    if wheat_in_shed > 0:
        market.append(["SELL", "WHEAT", wheat_in_shed])

    # If standing on an empty tile, plant wheat
    if tile is None and private["seeds"].get("WHEAT", 0) > 0:
        return {"farmer": ["PLANT", "WHEAT"], "hands": [], "market": market}

    # If standing on a plant, manage watering and harvesting
    if isinstance(tile, dict) and tile.get("kind") == "PLANT":
        crop_age = obs["day"] - tile["planted_day"]
        if crop_age >= 2:  # Wheat first_yield_day = 2
            return {"farmer": ["HARVEST"], "hands": [], "market": market}
        if not tile["watered_today"]:
            return {"farmer": ["WATER"], "hands": [], "market": market}

    return {"farmer": ["PASS"], "hands": [], "market": market}
Frequently Asked Questions
Submissions
Submissions must be at most 100 MiB
Daily submission limit 5
Only your most recent 2 are active
Your files will be located in /kaggle_simulations/agent/. Ensure all your file imports are set appropriately
Submission Resources
HDD Space: 8 GiB
RAM: 6.5 GiB
vCPUs: 1.6
Submission Size Limit: 100 MiB
For questions about the environment OS or python env, please see:

Docker Image
Citation
Bovard Doerschuk-Tiberi, Domino Weir, and María Cruz. Kaggriculture. https://kaggle.com/competitions/kaggriculture, 2026. Kaggle.


## Current public notebooks
curl --url 'https://www.kaggle.com/api/i/kernels.KernelsService/ListKernels' \
  -H 'accept: application/json' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -b 'ka_sessionid=a2d4835b8739a8f564a29055e4223952; GCLB=CN6J4ovv3O6GGhAD; _ga=GA1.1.574152309.1787680417; CSRF-TOKEN=CfDJ8GNxPX3qpaJEpxfoBSRBZPfD9B70Yqy00PGGKHpGLurJUAf620EVsMlW1RmQl8XcPCvu1Ivnup-CkZi2GE9g9NEgqktIiwSSAeM1Uq47IQ; ACCEPTED_COOKIES=true; __Host-KAGGLEID=CfDJ8ImuQD4OY2pEnVW2WQ-kgnco8cyguLdQxWhJgv-Lt7I7wHCo9RHvMd3Wppks3fWrKIrH_SRK_gRGZjLL3ResvzoBkLRd97pFUY4GANwqnFC8UvqbEdXMN-89n_6nUE4Yxv14gIXgIEjIj4fQ; build-hash=67f4fe2704319bea109698e980cf5b8517600ef4; ka_db=CfDJ8ImuQD4OY2pEnVW2WQ-kgnc0mLEybx6olgJ2O18BPj6wQSwkBqQahffmZ1BoG6NBmjAA5pHeY6CvUUXIHKvKyfD2W5KSdHjcIgPsBnSKnvVAkE4TaQ9NnLxu0KU; XSRF-TOKEN=CfDJ8ImuQD4OY2pEnVW2WQ-kgnfOWJmIKInng9MXYlnMeN_eARvD9_Do6L0XdTHRFCiFelqrGFeh1IGvEBJZknD4VTSTLIi-PnRDM9K__eV5_XBcenUVC8wj1TAskR5QuynZkYFRGwx4SKa-uqxr2g-TTzU; CLIENT-TOKEN=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOiJzYW13aXoiLCJuYnQiOiIyMDI2LTA5LTAyVDE5OjEzOjQ4LjI3MTUxNjVaIiwiaWF0IjoiMjAyNi0wOS0wMlQxOToxMzo0OC4yNzE1MTY1WiIsImp0aSI6ImIwZmU0NGEyLTM5ZDMtNDgwNC04ZTRjLTg1MjBlNDAzODFhMyIsImV4cCI6IjIwMjYtMTAtMDJUMTk6MTM6NDguMjcxNTE2NVoiLCJ1aWQiOjIwMTczMDIyLCJkaXNwbGF5TmFtZSI6IlNhbS13aXoiLCJlbWFpbCI6InNhbXJ1ZGh2dmFuZGFrdWRyaTIwMDVAZ21haWwuY29tIiwidGllciI6ImNvbnRyaWJ1dG9yIiwidmVyaWZpZWQiOnRydWUsInByb2ZpbGVVcmwiOiIvc2Ftd2l6IiwidGh1bWJuYWlsVXJsIjoiaHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL2thZ2dsZS1hdmF0YXJzL3RodW1ibmFpbHMvZGVmYXVsdC10aHVtYi5wbmciLCJmZmgiOiI5MGMxODViMWE5OWNhMjlmMjdiYTE3MDFkMmUzZWExMjdiZjcxZDk2OTFkZjM5ZGM2YjUwYTk2NjQwYmY3M2JiIiwicGlkIjoia2FnZ2xlLTE2MTYwNyIsInN2YyI6IndlYi1mZSIsInNkYWsiOiJBSXphU3lBNGVOcVVkUlJza0pzQ1pXVnotcUw2NTVYYTVKRU1yZUUiLCJibGQiOiI2N2Y0ZmUyNzA0MzE5YmVhMTA5Njk4ZTk4MGNmNWI4NTE3NjAwZWY0In0.; _ga_T7QHS60L4Q=GS2.1.s1788375409$o3$g1$t1788376428$j60$l0$h0' \
  -H 'origin: https://www.kaggle.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.kaggle.com/competitions/kaggriculture/code' \
  -H 'sec-ch-ua: "Not?A_Brand";v="24", "Chromium";v="152"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36' \
  -H 'x-kaggle-build-version: 67f4fe2704319bea109698e980cf5b8517600ef4' \
  -H 'x-xsrf-token: CfDJ8ImuQD4OY2pEnVW2WQ-kgnfOWJmIKInng9MXYlnMeN_eARvD9_Do6L0XdTHRFCiFelqrGFeh1IGvEBJZknD4VTSTLIi-PnRDM9K__eV5_XBcenUVC8wj1TAskR5QuynZkYFRGwx4SKa-uqxr2g-TTzU' \
  --data-raw '{"kernelFilterCriteria":{"search":"","listRequest":{"competitionId":147734,"sortBy":"HOTNESS","pageSize":20,"group":"EVERYONE","page":1,"modelIds":[],"modelInstanceIds":[],"excludeKernelIds":[],"tagIds":"","excludeResultsFilesOutputs":false,"wantOutputFiles":false,"excludeNonAccessedDatasources":true}},"detailFilterCriteria":{"deletedAccessBehavior":"RETURN_NOTHING","unauthorizedAccessBehavior":"RETURN_NOTHING","excludeResultsFilesOutputs":false,"wantOutputFiles":false,"kernelIds":[],"outputFileTypes":[],"includeInvalidDataSources":false},"readMask":"pinnedKernels"}'

  {"totalCount":0,"kernels":[{"author":{"id":31573099,"displayName":"Igor Zharov","userName":"flexonafft","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/31573099-kg.jpg?t=2026-08-01-13-02-23","profileUrl":"/flexonafft","performanceTier":"EXPERT","thumbnailName":"31573099-kg.jpg?t=2026-08-01-13-02-23"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132704576,"scriptVersionId":346757307,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":2226.1,"lastRunExecutionTimeSeconds":21,"medal":"BRONZE","title":"Kaggriculture | Adaptive Farm Intelligence","totalViews":447,"totalVotes":23,"totalLines":635,"currentUrlSlug":"kaggriculture-adaptive-farm-intelligence","scriptVersionDateCreated":"2026-09-02T12:06:24.080Z","dateEvaluated":"2026-09-02T12:06:25.973Z","hasLinkedSubmission":true,"lastRunTime":"2026-09-02T12:06:25.973Z","scriptUrl":"/code/flexonafft/kaggriculture-adaptive-farm-intelligence","scriptCommentsUrl":"/code/flexonafft/kaggriculture-adaptive-farm-intelligence/comments","scriptInputUrl":"/code/flexonafft/kaggriculture-adaptive-farm-intelligence/input","scriptEditUrl":"/code/flexonafft/kaggriculture-adaptive-farm-intelligence/edit","hasDataOutputFiles":true,"dateCreated":"2026-08-31T20:45:09.226500Z"},{"author":{"id":1449764,"displayName":"Yusuke Hayashi","userName":"yhay81","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/1449764-kg.png?t=2026-09-01-06-02-00","profileUrl":"/yhay81","performanceTier":"CONTRIBUTOR","thumbnailName":"1449764-kg.png?t=2026-09-01-06-02-00"},"dataSources":[{"reference":{"sourceType":"DATA_SOURCE_TYPE_DATASET_VERSION","sourceId":19368324},"name":"Six-Day Public-State Agent Source","dataSourceUrl":"/datasets/yhay81/six-day-public-state-agent-source","thumbnailUrl":"https://storage.googleapis.com/kaggle-datasets-images/new-version-temp-images/default-backgrounds-8.png-1449764/dataset-thumbnail.png"},{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132897306,"scriptVersionId":346770213,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":2743.9,"lastRunExecutionTimeSeconds":181,"medal":"BRONZE","categories":[{"id":11105,"name":"education","fullPath":"subject \u003E people and society \u003E education","description":"Education datasets and kernels relate to statistics on student performance, university rankings, and answers for all your homework questions.","datasetCount":36432,"competitionCount":71,"scriptCount":15585,"totalCount":52088,"tagUrl":"/tags/education"}],"title":"Six-Day Public-State Fieldbook","totalViews":162,"totalVotes":20,"totalLines":139,"currentUrlSlug":"six-day-public-state-fieldbook","scriptVersionDateCreated":"2026-09-02T13:13:36.860Z","dateEvaluated":"2026-09-02T13:13:39.267Z","hasLinkedSubmission":true,"lastRunTime":"2026-09-02T13:13:39.267Z","scriptUrl":"/code/yhay81/six-day-public-state-fieldbook","scriptCommentsUrl":"/code/yhay81/six-day-public-state-fieldbook/comments","scriptInputUrl":"/code/yhay81/six-day-public-state-fieldbook/input","scriptEditUrl":"/code/yhay81/six-day-public-state-fieldbook/edit","hasDataOutputFiles":true,"dateCreated":"2026-09-02T12:52:54.425392900Z"},{"author":{"id":35447235,"displayName":"boatlee","userName":"boatlee","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/35447235-kg.png?t=2026-07-04-13-37-42","profileUrl":"/boatlee","performanceTier":"EXPERT","thumbnailName":"35447235-kg.png?t=2026-07-04-13-37-42"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132858221,"scriptVersionId":346682136,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":2646.8,"lastRunExecutionTimeSeconds":24,"medal":"SILVER","title":"V29-R1 | Adaptive Market Hysteresis","totalViews":370,"totalVotes":49,"totalLines":97,"currentUrlSlug":"v29-r1-adaptive-market-hysteresis","scriptVersionDateCreated":"2026-09-02T05:41:59.297Z","dateEvaluated":"2026-09-02T05:42:01.100Z","hasLinkedSubmission":true,"lastRunTime":"2026-09-02T05:42:01.100Z","scriptUrl":"/code/boatlee/v29-r1-adaptive-market-hysteresis","scriptCommentsUrl":"/code/boatlee/v29-r1-adaptive-market-hysteresis/comments","scriptInputUrl":"/code/boatlee/v29-r1-adaptive-market-hysteresis/input","scriptEditUrl":"/code/boatlee/v29-r1-adaptive-market-hysteresis/edit","hasDataOutputFiles":true,"dateCreated":"2026-09-02T05:41:58.486915100Z"},{"author":{"id":15194873,"displayName":"\u0414\u0432\u043E\u0440\u043A\u0438\u043D \u0415\u0432\u0433\u0435\u043D\u0438\u0439 \u0412\u043B\u0430\u0434\u0438\u043C\u0438\u0440\u043E\u0432\u0438\u0447","userName":"evgendvorkin","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/15194873-kg.jpg?t=2025-12-28-12-13-14","profileUrl":"/evgendvorkin","performanceTier":"EXPERT","thumbnailName":"15194873-kg.jpg?t=2025-12-28-12-13-14"},"dataSources":[{"reference":{"sourceType":"DATA_SOURCE_TYPE_DATASET_VERSION","sourceId":19367918},"name":"trajectory","dataSourceUrl":"/datasets/evgendvorkin/trajectory","thumbnailUrl":"https://storage.googleapis.com/kaggle-datasets-images/new-version-temp-images/default-backgrounds-78.png-15194873/dataset-thumbnail.png"},{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132685767,"scriptVersionId":346839484,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":1138.5,"lastRunExecutionTimeSeconds":21,"medal":"BRONZE","title":"Kaggriculture","totalViews":154,"totalVotes":10,"totalLines":1234,"currentUrlSlug":"kaggriculture","scriptVersionDateCreated":"2026-09-02T18:52:29.297Z","dateEvaluated":"2026-09-02T18:52:31.753Z","hasLinkedSubmission":true,"lastRunTime":"2026-09-02T18:52:31.753Z","scriptUrl":"/code/evgendvorkin/kaggriculture","scriptCommentsUrl":"/code/evgendvorkin/kaggriculture/comments","scriptInputUrl":"/code/evgendvorkin/kaggriculture/input","scriptEditUrl":"/code/evgendvorkin/kaggriculture/edit","hasDataOutputFiles":true,"dateCreated":"2026-08-31T16:06:57.901144Z"},{"author":{"id":35366071,"displayName":"destbreso","userName":"destbreso","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/35366071-kg.png?t=2026-08-09-19-10-01","profileUrl":"/destbreso","performanceTier":"EXPERT","thumbnailName":"35366071-kg.png?t=2026-08-09-19-10-01"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132616249,"scriptVersionId":346638531,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"forumTopicId":738892,"lastRunExecutionTimeSeconds":112,"medal":"BRONZE","categories":[{"id":16667,"name":"scheduled","fullPath":"admin \u003E scheduled","description":"","datasetCount":1,"scriptCount":22444,"totalCount":22445,"tagUrl":"/tags/scheduled"}],"title":"X-ray your agent","totalComments":2,"totalViews":336,"totalVotes":10,"totalLines":1101,"currentUrlSlug":"x-ray-your-agent","scriptVersionDateCreated":"2026-09-02T00:45:09.350Z","dateEvaluated":"2026-09-02T00:45:10.547Z","cardImageUrl":"https://www.kaggleusercontent.com/kf/346638531/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..B-KRrOO8oMd0wDX8Vl3Xgg.rKxTDhghUp6HhE151zi28IMNRolGY95EyOP5mEcIk3lZLtmo4g_dmPf3ZmzdAReOMCfowd0QcXBflZEVgS1LjzMS5XowxjUac0gsSwwKRi44M0978keiHhNKOITZoOFbnIWKqvrHyXWYYFoTUlgVxWE1cRh7vOBALXQBqkNC9JrFmAUxCkeb5WIwtaj8PBq2jmpKLJLPobVAbuvYuHRYoYauZ6v9ThNFXFPTML93U0yxel-K5xfgTiNiIVpXDQcytUvqym8516m5ZvuNG0Wy9Bp-RCuapv6k_CwjkmUdo08y_xWyJvri5O2tKjcjgHJ7T8482qkiEGVlD9Z9t_7F5QWGNLuP-ImbGkMtnfaaxNWr788S9-8_Rd_hcS0FLI_tOGjW_S72uHkzEQwxppfXjvBEKQdUrDRj1K_-o-fBAM9z-PsJGLt5IT_oQeeezL0DjsEoqNU8cMNTvoTDG2pzxnPSME4YnwGNu2GoZxqsgbIJoQ6m136KHBbk-4WMI89pvWqCEgAYSaGEWNyIvLKnhf2Cm9GF3JmxboV9QQBgx8Kgnud3A0MygvL4QVV9fUg6wQGyixd9AJAa_23mVMVigFsl7C0YmSlv9PaDRHC3OwatSISf7Co8StaEQLevyB7x.5YyVw-B5_0P47XvugrV-mA/__results___files/__results___12_1.png","lastRunTime":"2026-09-02T00:45:10.547Z","scriptUrl":"/code/destbreso/x-ray-your-agent","scriptCommentsUrl":"/code/destbreso/x-ray-your-agent/comments","scriptInputUrl":"/code/destbreso/x-ray-your-agent/input","scriptEditUrl":"/code/destbreso/x-ray-your-agent/edit","dateCreated":"2026-08-31T02:35:15.482489200Z"},{"author":{"id":1449764,"displayName":"Yusuke Hayashi","userName":"yhay81","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/1449764-kg.png?t=2026-09-01-06-02-00","profileUrl":"/yhay81","performanceTier":"CONTRIBUTOR","thumbnailName":"1449764-kg.png?t=2026-09-01-06-02-00"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132926004,"scriptVersionId":346828363,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":1824.7,"lastRunExecutionTimeSeconds":231,"categories":[{"id":11105,"name":"education","fullPath":"subject \u003E people and society \u003E education","description":"Education datasets and kernels relate to statistics on student performance, university rankings, and answers for all your homework questions.","datasetCount":36432,"competitionCount":71,"scriptCount":15585,"totalCount":52088,"tagUrl":"/tags/education"}],"title":"The 35-0 Tape: A Causal Shop Router","totalViews":25,"totalLines":3433,"currentUrlSlug":"the-35-0-tape-a-causal-shop-router","scriptVersionDateCreated":"2026-09-02T17:46:38.007Z","dateEvaluated":"2026-09-02T17:46:39.580Z","hasLinkedSubmission":true,"lastRunTime":"2026-09-02T17:46:39.580Z","scriptUrl":"/code/yhay81/the-35-0-tape-a-causal-shop-router","scriptCommentsUrl":"/code/yhay81/the-35-0-tape-a-causal-shop-router/comments","scriptInputUrl":"/code/yhay81/the-35-0-tape-a-causal-shop-router/input","scriptEditUrl":"/code/yhay81/the-35-0-tape-a-causal-shop-router/edit","hasDataOutputFiles":true,"dateCreated":"2026-09-02T17:34:55.182676400Z"},{"author":{"id":36087701,"displayName":"Arlene","userName":"lynnsakurai","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/36087701-kg.jpg?t=2026-08-27-01-31-17","profileUrl":"/lynnsakurai","performanceTier":"CONTRIBUTOR","thumbnailName":"36087701-kg.jpg?t=2026-08-27-01-31-17"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132681375,"scriptVersionId":346690058,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":1721.9,"lastRunExecutionTimeSeconds":20,"title":"Farming Score V4: A Better Shop","totalViews":117,"totalVotes":6,"totalLines":604,"currentUrlSlug":"farming-score-v4-a-better-shop","scriptVersionDateCreated":"2026-09-02T06:24:28.533Z","dateEvaluated":"2026-09-02T06:24:29.753Z","hasLinkedSubmission":true,"lastRunTime":"2026-09-02T06:24:29.753Z","scriptUrl":"/code/lynnsakurai/farming-score-v4-a-better-shop","scriptCommentsUrl":"/code/lynnsakurai/farming-score-v4-a-better-shop/comments","scriptInputUrl":"/code/lynnsakurai/farming-score-v4-a-better-shop/input","scriptEditUrl":"/code/lynnsakurai/farming-score-v4-a-better-shop/edit","hasDataOutputFiles":true,"dateCreated":"2026-08-31T15:10:59.045490500Z"},{"author":{"id":35366071,"displayName":"destbreso","userName":"destbreso","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/35366071-kg.png?t=2026-08-09-19-10-01","profileUrl":"/destbreso","performanceTier":"EXPERT","thumbnailName":"35366071-kg.png?t=2026-08-09-19-10-01"},"dataSources":[{"reference":{"sourceType":"DATA_SOURCE_TYPE_DATASET_VERSION","sourceId":19371487},"name":"Kaggriculture donor agents (snapshot 2026-09-02)","dataSourceUrl":"/datasets/destbreso/kaggriculture-donor-agents-20260902","thumbnailUrl":"https://storage.googleapis.com/kaggle-datasets-images/11873849/19371487/ffcb8f2a17fb496fbbec40f536a94c3d/dataset-thumbnail.png?t=2026-09-02-15-54-29"},{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132912560,"scriptVersionId":346805436,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"lastRunExecutionTimeSeconds":93,"categories":[{"id":11105,"name":"education","fullPath":"subject \u003E people and society \u003E education","description":"Education datasets and kernels relate to statistics on student performance, university rankings, and answers for all your homework questions.","datasetCount":36432,"competitionCount":71,"scriptCount":15585,"totalCount":52088,"tagUrl":"/tags/education"},{"id":13210,"name":"statistical analysis","fullPath":"analysis \u003E statistical analysis","datasetCount":1399,"competitionCount":6,"scriptCount":3454,"totalCount":4859,"tagUrl":"/tags/statistical-analysis"}],"title":"Measure Twice, Submit Once, Know Your Error","totalViews":30,"totalVotes":1,"totalLines":858,"currentUrlSlug":"measure-twice-submit-once-know-your-error","scriptVersionDateCreated":"2026-09-02T15:57:03.147Z","dateEvaluated":"2026-09-02T15:57:04.283Z","cardImageUrl":"https://www.kaggleusercontent.com/kf/346805436/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..3Se3vN4YPpKcQp4PyJWhAQ.H-dE4yWfd6DqNY-vl3E4vc5V9yEX8Bi1bv3C6L5avqBMPBrmdHlUHlDXJJtWn8arr2lh1yxrR69Bo-Q-WRYc_iNnL28Old4QzrHot3imrZstSmnyxBAo6eQNVBNpUPF9vLaTN6IcyBKTZts1ADmFRjUcfM5TL4n3gUWnretNBEom4aZ1QPoHfRlIxEkzjKyT3C_MsRE5QPb1pM-aU8KaOxddygKp-NrdSfx-jIPhGfYKTCe5x9SmV7Hk4P-DVJ6l5bhOAPhTNTf_8h_HU-86BH0qX-IdqFGbbF4bq0R68QVIGEuQq0NR9Hrk-l7LNjzoW5CNPfuIsmDfNtKvIbZqnuTJNuOKrShSuIPmyu0sJ9oPRB5boec95ID0Od0rYVP5U6qlfL5NLaFgOwXzridOIu82u5EZJwYVbx7NFDHGi46a-5bRKiU3hAQrCZtQBOVftDORT1h_EhoIwvkSo3BDZQ4hL58-lNY9PfDbOGKfix97N7rO_KQaKj06F3AiG0iIRVE8t00y7yCdtRuHjeWppELDTpun1eOW4CP9JIuLoU1X_5AbtnGaez_2e7O2i3P3Z-225Pg5tATzkA60K1dggNfYmJEMxv2Xf_f3_M8CawOLmBRo312i5tqDCIFM9uy5PphaeIdP1nVUUZvrvgbZ8Q.oMMISCz9QFT0hAVrI0_E3A/__results___files/__results___10_0.png","lastRunTime":"2026-09-02T15:57:04.283Z","scriptUrl":"/code/destbreso/measure-twice-submit-once-know-your-error","scriptCommentsUrl":"/code/destbreso/measure-twice-submit-once-know-your-error/comments","scriptInputUrl":"/code/destbreso/measure-twice-submit-once-know-your-error/input","scriptEditUrl":"/code/destbreso/measure-twice-submit-once-know-your-error/edit","dateCreated":"2026-09-02T15:25:56.368978800Z"},{"author":{"id":35366071,"displayName":"destbreso","userName":"destbreso","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/35366071-kg.png?t=2026-08-09-19-10-01","profileUrl":"/destbreso","performanceTier":"EXPERT","thumbnailName":"35366071-kg.png?t=2026-08-09-19-10-01"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":131830054,"scriptVersionId":346531698,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"lastRunExecutionTimeSeconds":71,"medal":"BRONZE","title":"Island GA | An owned schedule is a moat","totalViews":354,"totalVotes":11,"totalLines":2101,"currentUrlSlug":"island-ga-an-owned-schedule-is-a-moat","scriptVersionDateCreated":"2026-09-01T14:37:07.697Z","dateEvaluated":"2026-09-01T14:37:08.980Z","cardImageUrl":"https://www.kaggleusercontent.com/kf/346531698/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..W2Uxs5WON60PTSWss4gJYQ.D66WRqzKLTJscKMcWbJUS16KZEDYIhXygqVnSB6l6Eqb0SVwUROpGCTPVuEg5P0v-G9374pdFREeMjVzU8y3w0VGAvAPFDQg_BAbf9YVKh9PQKqyAg15kwdRceKsy0rv_yrOpVeU12P5U6FcUGniyK5tSFBj3VEi1F8z9U8vrI4FLJKx-7BAHcrMIgcjp47-xrO170JQsfg9qD-8RMXKdD984ZPaLad4EJgVKN-1OOxHyAzIUoV85efYr4LWGQPX8WtUDdHrjBuVYCF2n5UZs6kaosPGDFOsH4tLjsIkOSREkZkNjsHxkrs1lWymxy5NJVSbJt1awIYRKWI2YufxMr9cMw63K7DlyJOUGyf5fyMP5iaSd3_P8tiX4dN23pE53uIQSwXNlMCd8KFDb_-2b-gBMX--u2fgksCKoMkjmPphygrQ7yyf9f-cHthikKYH63BLaJuYTuTsSm8rcsU9j4wM4Zty6Mws4FcM6yzVdtugR4gM8pfB3BRoyNMJf0AaIr6ikXWkZvgCBoyMvI4Gt0PpOCb7uExuy-GLRAJPkc9rec9RVNjTsvF6hCgQx50p48PpL9CMOMJ1OOiF8u4GLeeHtYGccMrZpjgM6AiIDqq7ZV9oKGzbKXPywzix3E0ZKuIy-aPKuJbOHJu8z-Nhlw.ZMWHb7PCfXBxQ6Of-M3FHQ/__results___files/__results___14_1.png","lastRunTime":"2026-09-01T14:37:08.980Z","scriptUrl":"/code/destbreso/island-ga-an-owned-schedule-is-a-moat","scriptCommentsUrl":"/code/destbreso/island-ga-an-owned-schedule-is-a-moat/comments","scriptInputUrl":"/code/destbreso/island-ga-an-owned-schedule-is-a-moat/input","scriptEditUrl":"/code/destbreso/island-ga-an-owned-schedule-is-a-moat/edit","dateCreated":"2026-08-24T15:44:04.201813100Z"},{"author":{"id":36087701,"displayName":"Arlene","userName":"lynnsakurai","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/36087701-kg.jpg?t=2026-08-27-01-31-17","profileUrl":"/lynnsakurai","performanceTier":"CONTRIBUTOR","thumbnailName":"36087701-kg.jpg?t=2026-08-27-01-31-17"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132738338,"scriptVersionId":346466052,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"lastRunExecutionTimeSeconds":25,"medal":"BRONZE","title":"Farming Score V5: Timing Optimized","totalViews":112,"totalVotes":9,"totalLines":594,"currentUrlSlug":"farming-score-v5-timing-optimized","scriptVersionDateCreated":"2026-09-01T09:07:19.003Z","dateEvaluated":"2026-09-01T09:07:21.673Z","hasLinkedSubmission":true,"lastRunTime":"2026-09-01T09:07:21.673Z","scriptUrl":"/code/lynnsakurai/farming-score-v5-timing-optimized","scriptCommentsUrl":"/code/lynnsakurai/farming-score-v5-timing-optimized/comments","scriptInputUrl":"/code/lynnsakurai/farming-score-v5-timing-optimized/input","scriptEditUrl":"/code/lynnsakurai/farming-score-v5-timing-optimized/edit","hasDataOutputFiles":true,"dateCreated":"2026-09-01T05:41:41.681823600Z"},{"author":{"id":34732831,"displayName":"Prema Ananda","userName":"premaananda108","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/34732831-kg.jpg?t=2026-05-31-11-56-20","profileUrl":"/premaananda108","performanceTier":"CONTRIBUTOR","thumbnailName":"34732831-kg.jpg?t=2026-05-31-11-56-20"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":131369359,"scriptVersionId":346440208,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":774.5,"lastRunExecutionTimeSeconds":100,"medal":"BRONZE","title":"Economics-Driven Rule Agent (EcoBot v7) \u002B Arena","totalViews":1711,"totalVotes":37,"totalLines":2780,"currentUrlSlug":"economics-driven-rule-agent-ecobot-v7-arena","scriptVersionDateCreated":"2026-09-01T06:48:58.903Z","dateEvaluated":"2026-09-01T06:49:00.683Z","hasLinkedSubmission":true,"lastRunTime":"2026-09-01T06:49:00.683Z","scriptUrl":"/code/premaananda108/economics-driven-rule-agent-ecobot-v7-arena","scriptCommentsUrl":"/code/premaananda108/economics-driven-rule-agent-ecobot-v7-arena/comments","scriptInputUrl":"/code/premaananda108/economics-driven-rule-agent-ecobot-v7-arena/input","scriptEditUrl":"/code/premaananda108/economics-driven-rule-agent-ecobot-v7-arena/edit","hasDataOutputFiles":true,"dateCreated":"2026-08-20T09:37:19.376505Z"},{"author":{"id":33436204,"displayName":"Taylor Clark","userName":"taylorclark637","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/default-thumb.png","profileUrl":"/taylorclark637","performanceTier":"CONTRIBUTOR","thumbnailName":"default-thumb.png"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132845046,"scriptVersionId":346663986,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"lastRunExecutionTimeSeconds":27,"categories":[{"id":12001,"name":"agriculture","fullPath":"subject \u003E earth and nature \u003E environment \u003E agriculture","description":"You could be well on your way to creating the next big precision agriculture company with the resources in this tag. At the very least, you can use Weekly Corn Prices to make more informed decisions about your purchases at the store.","datasetCount":2180,"competitionCount":14,"scriptCount":810,"totalCount":3004,"tagUrl":"/tags/agriculture"},{"id":12107,"name":"computer science","fullPath":"subject \u003E science and technology \u003E computer science","description":"There is one thing we can say for sure about computer science: Computer science leads to more computer games which leads to better GPUs which leads to smarter AI.","datasetCount":58072,"competitionCount":16,"scriptCount":1006,"totalCount":59094,"tagUrl":"/tags/computer-science"}],"title":" Kaggriculture: The Biosphere Construct (V22)","totalViews":35,"totalLines":402,"currentUrlSlug":"kaggriculture-the-biosphere-construct-v22","scriptVersionDateCreated":"2026-09-02T03:55:57.903Z","dateEvaluated":"2026-09-02T03:55:59.050Z","lastRunTime":"2026-09-02T03:55:59.050Z","scriptUrl":"/code/taylorclark637/kaggriculture-the-biosphere-construct-v22","scriptCommentsUrl":"/code/taylorclark637/kaggriculture-the-biosphere-construct-v22/comments","scriptInputUrl":"/code/taylorclark637/kaggriculture-the-biosphere-construct-v22/input","scriptEditUrl":"/code/taylorclark637/kaggriculture-the-biosphere-construct-v22/edit","hasDataOutputFiles":true,"dateCreated":"2026-09-02T02:55:14.082099700Z"},{"author":{"id":31770368,"displayName":"Mansi Aggarwal","userName":"mansiaggarwal88","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/31770368-kg.jpg?t=2026-07-09-14-04-54","profileUrl":"/mansiaggarwal88","performanceTier":"EXPERT","thumbnailName":"31770368-kg.jpg?t=2026-07-09-14-04-54"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132799835,"scriptVersionId":346566251,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"lastRunExecutionTimeSeconds":23,"title":"Portfolio Farming: Specialist Module-Kaggriculture","totalViews":31,"totalVotes":2,"totalLines":437,"currentUrlSlug":"portfolio-farming-specialist-module-kaggriculture","scriptVersionDateCreated":"2026-09-01T16:45:07.550Z","dateEvaluated":"2026-09-01T16:45:09.813Z","cardImageUrl":"https://www.kaggleusercontent.com/kf/346566251/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..FX4gtIlfJsq712Y8QU_7Xg.BX1tcLUtZccWDuIbk0EAHTYESNH4_FEp2utd4sC68pP5_9mydZYhzd49YZHq6KdI1oIH6IVleqCZIZznptspWMXQmkESX-h0SiMqKIdz4CZ2v_WiditcQtdJPbsU7UnWPEn0sLNp7MabfIQExa3uyFuBsj7paOOW1twMfqQ5nlTRoXKjr_4kgGvSnbrG96ooDNC5jh7HB5tvFNw81K-xPdVPJhbi81HW5ZeLlEjC6o7X8Sb8-xXW7b7XqWuDJK2Hgy5HFjoAxuY9cV54rZBKHvPaa3i5MoUf56Y07z01sQqXqDDC-gjBeZsJXgxEVHdrQtjtB6KI5MwzRJ3wLEb5p5ofFbTcnQJ8oNqqRqKGGE9-_qobB6Hin8N0UGIeQi3qHnLe33qImHLK2HGCcNx8MV5QuHQzYSZOovhc3wy9imIQsO8LQ5d9YO42TQOMLCMcs9LAP8Kfd6ExlNvqwQBz2qLlcnPYWF-f_oESGzIfNxa3MhNOqkU3CM6JMH9L-4AnoLZj8hDbfXYuo4KtOugmTX_KFmfaqVPrKbE1HoSFeA9p_ZOCr3la_xLlNaRv1wNQ5xhTdbhZ4Iu1Sp8gyWi4Tqmx3QdaKye89mDL6JUSn2qsOkeYzlsNxHw3yDXTgF2GdCprNY7W8fQ3ifU0ys-j2Y282TIimu3DagCcQ_6IvnQ.zlEsk0BNzyxTkGsNoFx68Q/__results___files/__results___5_0.png","lastRunTime":"2026-09-01T16:45:09.813Z","scriptUrl":"/code/mansiaggarwal88/portfolio-farming-specialist-module-kaggriculture","scriptCommentsUrl":"/code/mansiaggarwal88/portfolio-farming-specialist-module-kaggriculture/comments","scriptInputUrl":"/code/mansiaggarwal88/portfolio-farming-specialist-module-kaggriculture/input","scriptEditUrl":"/code/mansiaggarwal88/portfolio-farming-specialist-module-kaggriculture/edit","dateCreated":"2026-09-01T16:37:48.016113900Z"},{"author":{"id":35241251,"displayName":"Dariush Afshar","userName":"dariushafshar","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/35241251-kg.png?t=2026-08-27-18-32-48","profileUrl":"/dariushafshar","performanceTier":"CONTRIBUTOR","thumbnailName":"35241251-kg.png?t=2026-08-27-18-32-48"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132833597,"scriptVersionId":346633690,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"lastRunExecutionTimeSeconds":88,"categories":[{"id":13103,"name":"intermediate","fullPath":"audience \u003E intermediate","datasetCount":6867,"competitionCount":109,"scriptCount":7602,"totalCount":14578,"tagUrl":"/tags/intermediate"}],"title":"Banked $3000 Every Game? The Last-Callable Trap","totalViews":32,"totalLines":133,"currentUrlSlug":"banked-3000-every-game-the-last-callable-trap","scriptVersionDateCreated":"2026-09-02T00:02:51.037Z","dateEvaluated":"2026-09-02T00:02:52.817Z","lastRunTime":"2026-09-02T00:02:52.817Z","scriptUrl":"/code/dariushafshar/banked-3000-every-game-the-last-callable-trap","scriptCommentsUrl":"/code/dariushafshar/banked-3000-every-game-the-last-callable-trap/comments","scriptInputUrl":"/code/dariushafshar/banked-3000-every-game-the-last-callable-trap/input","scriptEditUrl":"/code/dariushafshar/banked-3000-every-game-the-last-callable-trap/edit","hasDataOutputFiles":true,"dateCreated":"2026-09-01T23:59:31.187021Z"},{"author":{"id":23547097,"displayName":"Rafif Ariq Rabbani","userName":"rafifariqrabbani","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/23547097-kg.JPG?t=2025-12-29-17-40-27","profileUrl":"/rafifariqrabbani","performanceTier":"CONTRIBUTOR","thumbnailName":"23547097-kg.JPG?t=2025-12-29-17-40-27"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132495041,"scriptVersionId":346040404,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"lastRunExecutionTimeSeconds":41856,"title":"Kaggriculture: Greedy Optimizer \u002B Staged Frozen RL","totalViews":149,"totalVotes":10,"totalLines":9187,"currentUrlSlug":"kaggriculture-greedy-optimizer-staged-frozen-rl","scriptVersionDateCreated":"2026-08-30T11:38:06.293Z","dateEvaluated":"2026-08-30T11:38:07.457Z","lastRunTime":"2026-08-30T11:38:07.457Z","scriptUrl":"/code/rafifariqrabbani/kaggriculture-greedy-optimizer-staged-frozen-rl","scriptCommentsUrl":"/code/rafifariqrabbani/kaggriculture-greedy-optimizer-staged-frozen-rl/comments","scriptInputUrl":"/code/rafifariqrabbani/kaggriculture-greedy-optimizer-staged-frozen-rl/input","scriptEditUrl":"/code/rafifariqrabbani/kaggriculture-greedy-optimizer-staged-frozen-rl/edit","hasDataOutputFiles":true,"dateCreated":"2026-08-29T22:16:31.073105Z"},{"author":{"id":1449764,"displayName":"Yusuke Hayashi","userName":"yhay81","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/1449764-kg.png?t=2026-09-01-06-02-00","profileUrl":"/yhay81","performanceTier":"CONTRIBUTOR","thumbnailName":"1449764-kg.png?t=2026-09-01-06-02-00"},"dataSources":[{"reference":{"sourceType":"DATA_SOURCE_TYPE_DATASET_VERSION","sourceId":19336056},"name":"ShopForge Fieldbook Tapes","dataSourceUrl":"/datasets/yhay81/shopforge-fieldbook-tapes","thumbnailUrl":"https://storage.googleapis.com/kaggle-datasets-images/new-version-temp-images/default-backgrounds-42.png-1449764/dataset-thumbnail.png"},{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":132723199,"scriptVersionId":346415132,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"lastRunExecutionTimeSeconds":69,"medal":"SILVER","categories":[{"id":11105,"name":"education","fullPath":"subject \u003E people and society \u003E education","description":"Education datasets and kernels relate to statistics on student performance, university rankings, and answers for all your homework questions.","datasetCount":36432,"competitionCount":71,"scriptCount":15585,"totalCount":52088,"tagUrl":"/tags/education"}],"title":"Fieldbook: Commit for Three Days","totalViews":897,"totalVotes":68,"totalLines":695,"currentUrlSlug":"fieldbook-commit-for-three-days","scriptVersionDateCreated":"2026-09-01T04:23:52.620Z","dateEvaluated":"2026-09-01T04:23:53.943Z","hasLinkedSubmission":true,"lastRunTime":"2026-09-01T04:23:53.943Z","scriptUrl":"/code/yhay81/fieldbook-commit-for-three-days","scriptCommentsUrl":"/code/yhay81/fieldbook-commit-for-three-days/comments","scriptInputUrl":"/code/yhay81/fieldbook-commit-for-three-days/input","scriptEditUrl":"/code/yhay81/fieldbook-commit-for-three-days/edit","hasDataOutputFiles":true,"dateCreated":"2026-09-01T02:22:01.244397100Z"},{"author":{"id":33436204,"displayName":"Taylor Clark","userName":"taylorclark637","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/default-thumb.png","profileUrl":"/taylorclark637","performanceTier":"CONTRIBUTOR","thumbnailName":"default-thumb.png"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"},{"reference":{"sourceType":"DATA_SOURCE_TYPE_MODEL_INSTANCE_VERSION","sourceId":820624,"modelInstanceId":623539,"modelId":635365},"name":"Echo Witness","dataSourceUrl":"/models/taylorclark637/echo/PyTorch/default/1","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/default-thumb.png","variationSlug":"default"}],"id":132673078,"scriptVersionId":346625945,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":83.3,"lastRunExecutionTimeSeconds":15,"categories":[{"id":11205,"name":"economics","fullPath":"subject \u003E people and society \u003E social science \u003E economics","description":"The economics tag contains resources for analyzing the production, consumption, and transfer of wealth.","datasetCount":5274,"competitionCount":3,"scriptCount":1098,"totalCount":6375,"tagUrl":"/tags/economics"},{"id":12001,"name":"agriculture","fullPath":"subject \u003E earth and nature \u003E environment \u003E agriculture","description":"You could be well on your way to creating the next big precision agriculture company with the resources in this tag. At the very least, you can use Weekly Corn Prices to make more informed decisions about your purchases at the store.","datasetCount":2180,"competitionCount":14,"scriptCount":810,"totalCount":3004,"tagUrl":"/tags/agriculture"}],"title":"Kaggriculture ","totalViews":54,"totalLines":1110,"currentUrlSlug":"kaggriculture","scriptVersionDateCreated":"2026-09-01T22:53:59.993Z","dateEvaluated":"2026-09-01T22:54:02.353Z","hasLinkedSubmission":true,"lastRunTime":"2026-09-01T22:54:02.353Z","scriptUrl":"/code/taylorclark637/kaggriculture","scriptCommentsUrl":"/code/taylorclark637/kaggriculture/comments","scriptInputUrl":"/code/taylorclark637/kaggriculture/input","scriptEditUrl":"/code/taylorclark637/kaggriculture/edit","hasDataOutputFiles":true,"dateCreated":"2026-08-31T13:34:28.468796400Z"},{"author":{"id":7212220,"displayName":"Jocelyn Dumlao","userName":"jocelyndumlao","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/7212220-kg.png","profileUrl":"/jocelyndumlao","performanceTier":"GRANDMASTER","thumbnailName":"7212220-kg.png"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":129224128,"scriptVersionId":346399222,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":195.9,"forumTopicId":736745,"lastRunExecutionTimeSeconds":35,"medal":"BRONZE","title":"\uD83C\uDF3EKaggriculture AI Agent","totalComments":7,"totalViews":633,"totalVotes":19,"totalLines":2160,"currentUrlSlug":"kaggriculture-ai-agent","scriptVersionDateCreated":"2026-09-01T02:35:03.110Z","dateEvaluated":"2026-09-01T02:35:04.920Z","hasLinkedSubmission":true,"cardImageUrl":"https://www.kaggleusercontent.com/kf/346399222/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..0-1liUK71gfmf3OQtxPciQ.mOLEJ2A5RwQ7LRGUoN3_G9kSboUeLEOrRapLx9CdJ2odLsamkCXFf4AHifA6MH26P391iNS75eks2TjBsNsoyVYjQ6CkY_LUrPduShdPmbc-AltTGHO6SJ68HX0cKsdsalO7PmOXCF3qucXljuXogWBJsTyW8aplv37Ji1xMGeXUOae2bcgjspYlMgWshq0jELXSTghM4C5zFKqpeQTv8tS_74_MGyZv9cpn_jMphM6fh3cafOLsbS3d5jMl2JACtCO5yFCVKyMr9nhjDcsjrdROewg7aahlTQTgbdFP57WwXBTI8LvGAXaxjVP9mC2jr2kkfkGcMH4cQoZbIPiGBlnEw5wsFaURVQDiWAWUTXpJFWlEfnBFCFaOBN37p43nCxooq0FqNCNTIGld2rO5sP0cENkrN7hqdF5MrT3AUt6iOxR9tilqPPbt7oYzcA6YIa9Z213yMOmPlIv2baMs_BtvzS5k8Q6EQ6-QxBY5e3UhI0O9xPAyERWoF60CYWMYB6DRiOqDFfcvNbAkE6dTqhHie34y3FswQ2HGjtrV2hfD2hyb2LyKC79FyugWhU4uWChJfJO9iAkAI6-_bdowwWnk9Lm4Desnr5jCTW9jx9qobcebOTUINy4IIzPJNyRJ.0ElteF38Wa6TLrbSZ6Nvfw/__results___files/__results___13_0.png","lastRunTime":"2026-09-01T02:35:04.920Z","scriptUrl":"/code/jocelyndumlao/kaggriculture-ai-agent","scriptCommentsUrl":"/code/jocelyndumlao/kaggriculture-ai-agent/comments","scriptInputUrl":"/code/jocelyndumlao/kaggriculture-ai-agent/input","scriptEditUrl":"/code/jocelyndumlao/kaggriculture-ai-agent/edit","hasDataOutputFiles":true,"dateCreated":"2026-07-31T00:45:08.232883600Z"},{"author":{"id":35366071,"displayName":"destbreso","userName":"destbreso","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/35366071-kg.png?t=2026-08-09-19-10-01","profileUrl":"/destbreso","performanceTier":"EXPERT","thumbnailName":"35366071-kg.png?t=2026-08-09-19-10-01"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":131868520,"scriptVersionId":346531657,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"lastRunExecutionTimeSeconds":80,"title":"kagsim | The engine at 2000 episodes per second","totalViews":179,"totalVotes":4,"totalLines":1592,"currentUrlSlug":"kagsim-the-engine-at-2000-episodes-per-second","scriptVersionDateCreated":"2026-09-01T14:36:58.097Z","dateEvaluated":"2026-09-01T14:36:59.530Z","cardImageUrl":"https://www.kaggleusercontent.com/kf/346531657/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..f7naX_ga-I0b37ygdg8DgQ.zw5YelXEOZiFhXfIfr4OiftpCjo8ZEoZDIEnvuIPgT8fB8V5M9IJSB89Tkr_4sWc8Kdw4vdFh8hJmWd1q-uIOSiyzELm2DZhm-0uUmW_CEkbTj0bnq69_nNM-559oagqdIadid6wLHFPOPMjQqgpBO1ERlphVZrW4IWSwLD6GzrVQv9ey9MtPwINJKPbLPl-i3XehnUiiYPQLxS8xHineUYjqoEo1PBFeSvip4IfpGXHbUO0_UpRAlI2p1pZeuNx92OSseOUuSYhvWYemq5eJddJYms1SaxOuZHei-iA0jeZ_MYg-1fscELiyZn7MOCJ0k2t0GEmQ4Vu5LtuKYEJDYTcQ_xAl5TGNtcF4450W-Nm2NIqq5yY1cM2gEeWhTQit55aEJAU31pcbFxBfld_M-yE-AMLadM-cm61RtH1PugSyAKLfNfc8pD4MQR55U7OrrXtUkEX50naqxcWyGajLnGqAphj6xIlBFHqmBL3Cw4h0dm4vG-Rt0u_xSZVOkMxNOp-cFRpFXvgUwgI7VrpU5sFiAgncOMBQhAXcPkY8aR0rjvQenqrXNmUqPg799dDMzMLd2MNOvgsVUuHAc9wsDXK6RlSXg6pttGPs8jQN1ygl_Fe3HaZCUI5ueUM9sGMgl_3SjJtBzIJ9d2U5zftHQ.UHEfbBxj6AV5CIsnG3vFiw/__results___files/__results___17_0.png","lastRunTime":"2026-09-01T14:36:59.530Z","scriptUrl":"/code/destbreso/kagsim-the-engine-at-2000-episodes-per-second","scriptCommentsUrl":"/code/destbreso/kagsim-the-engine-at-2000-episodes-per-second/comments","scriptInputUrl":"/code/destbreso/kagsim-the-engine-at-2000-episodes-per-second/input","scriptEditUrl":"/code/destbreso/kagsim-the-engine-at-2000-episodes-per-second/edit","hasDataOutputFiles":true,"dateCreated":"2026-08-24T23:34:04.578608300Z"},{"author":{"id":18749304,"displayName":"KOUSHIK KUMAR DINDA","userName":"koushikkumardinda","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/18749304-gr.jpg","profileUrl":"/koushikkumardinda","performanceTier":"EXPERT","thumbnailName":"18749304-gr.jpg"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"id":131324382,"scriptVersionId":345741068,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":150.1,"lastRunExecutionTimeSeconds":102,"medal":"BRONZE","categories":[{"id":16151,"name":"simulations","fullPath":"subject \u003E culture and humanities \u003E games \u003E video games \u003E simulations","datasetCount":903,"competitionCount":92,"scriptCount":323,"totalCount":1318,"tagUrl":"/tags/simulation-games"}],"title":"Kaggriculture Starter","totalViews":696,"totalVotes":29,"totalLines":173,"currentUrlSlug":"kaggriculture-starter","scriptVersionDateCreated":"2026-08-29T01:53:40.333Z","dateEvaluated":"2026-08-29T01:53:41.577Z","hasLinkedSubmission":true,"lastRunTime":"2026-08-29T01:53:41.577Z","scriptUrl":"/code/koushikkumardinda/kaggriculture-starter","scriptCommentsUrl":"/code/koushikkumardinda/kaggriculture-starter/comments","scriptInputUrl":"/code/koushikkumardinda/kaggriculture-starter/input","scriptEditUrl":"/code/koushikkumardinda/kaggriculture-starter/edit","hasDataOutputFiles":true,"dateCreated":"2026-08-20T01:01:11.509454900Z"}],"pinnedKernels":[{"author":{"id":50767,"displayName":"Bovard Doerschuk-Tiberi","userName":"bovard","thumbnailUrl":"https://storage.googleapis.com/kaggle-avatars/thumbnails/50767-kg.jpg","profileUrl":"/bovard","performanceTier":"STAFF","thumbnailName":"50767-kg.jpg"},"dataSources":[{"reference":{"sourceId":147734},"name":"Kaggriculture","dataSourceUrl":"/competitions/kaggriculture","thumbnailUrl":"https://storage.googleapis.com/kaggle-competitions/kaggle/147734/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com\u0026Expires=1788385081\u0026Signature=PNpC6%2FOzgoiT1J30aQ4owSJ8Y1tqeQwexQuitutG4XXlvanhYy7lMq4o0eepWnGzv1eu7YBpvT7XaqaGBRdCw%2Ftx3e4%2BWEa6ik3vL0DIAOAFWVAUMf7ZibOsP160jwXwwK35h%2Bd96Dm2S21UYfo%2B%2FkHZ%2BLza2vOz%2BbBpWw7UqddrcW%2BL1hknYPj5SJgTVWUtjxoN9GHxtpgLgu3OnvuD%2FtxfGtcP2hQEwIZt4UNh%2ByQpAareNULzRvkYMe4%2FeXdLzIu8YpV32XWsANw0y48W95EiJHc%2B4PaURjLg68qg5NVUWw%2BF84iof4jsDEn5JfAGdIwqYnBGBGpjF2rIojF4DQ%3D%3D\u0026t=2026-06-09-23-19-07"}],"forkDiffLinesDeleted":3,"forkDiffLinesInserted":3,"hasCollaborators":true,"id":129194650,"scriptVersionId":339145588,"isFork":true,"languageName":"Python","aceLanguageName":"python","isNotebook":true,"bestPublicScore":273.6,"forumTopicId":731154,"lastRunExecutionTimeSeconds":81,"medal":"GOLD","title":"Kaggriculture: Getting Started","totalComments":4,"totalViews":21052,"totalVotes":917,"totalLines":308,"currentUrlSlug":"kaggriculture-getting-started","scriptVersionDateCreated":"2026-07-30T21:04:36.810Z","dateEvaluated":"2026-07-30T21:04:39.087Z","hasLinkedSubmission":true,"forkParentInfo":{"kernelId":128141852},"lastRunTime":"2026-07-30T21:04:39.087Z","scriptUrl":"/code/bovard/kaggriculture-getting-started","scriptCommentsUrl":"/code/bovard/kaggriculture-getting-started/comments","scriptInputUrl":"/code/bovard/kaggriculture-getting-started/input","scriptEditUrl":"/code/bovard/kaggriculture-getting-started/edit","hasDataOutputFiles":true,"dateCreated":"2026-07-30T16:50:41.196319800Z"}]}


  use this curl to fetch all the public notebooks for starter