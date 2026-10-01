"""Generate the Kaggle notebook: four instruments that lied, and how to catch them.

Deliberately scoped to measurement methodology. The agent-side findings that are currently our edge
stay out; everything here is either a property of the public engine, a statistical argument, or a
mistake I made and can prove.

Every code cell is runnable on Kaggle with only `kaggle_environments` installed.
"""
import json
import os

CELLS = []


def md(text):
    CELLS.append({"cell_type": "markdown", "metadata": {}, "source": text.strip("\n").splitlines(True)})


def code(text):
    CELLS.append({"cell_type": "code", "execution_count": None, "metadata": {},
                  "outputs": [], "source": text.strip("\n").splitlines(True)})


md(r"""
# Four instruments that lied to me

I spent two weeks improving a Kaggriculture agent. Every change I shipped measured positive
offline. The leaderboard did not move.

The changes were not the problem. **The instruments were.** This notebook is the four ways my
measurements lied, each with the check that catches it. Three of the four are specific to how this
competition is scored, and I have not seen them written down.

Nothing here is about which crops to plant. It is about how to know whether the thing you just
built is better than the thing you had.
""")

md(r"""
## 0. First, the number that made me start over

Two of my submissions scored **2609.9** and **2202.9** on the leaderboard.

They were the same file. Identical bytes, same md5 — I had submitted one as an "A/B control" and
forgotten I already had it live.

```
$ md5 sub_hover.py sub_ab_control.py
0b37a0fc22a449f0531beb9bc724a1f5  sub_hover.py
0b37a0fc22a449f0531beb9bc724a1f5  sub_ab_control.py
```

A second identical pair scored 2314.0 and 2020.6.

Much of that gap is convergence — the lower scorer in each pair had played fewer games (51 vs 129,
and 35 vs 144). That is exactly the point: **the leaderboard number is a function of how long an
agent has played, not only of how good it is**, and I had been comparing agents at different ages
as though the number were a property of the agent.

Every improvement I had shipped was worth less than that gap.
""")

md(r"""
## 1. The power problem: how many games does a real improvement need?

Per-game margin against a fixed opponent has a huge spread. In my games the standard deviation of
`our_bank - their_bank` is around **6,000**, while the improvements I could actually build were
worth **+68 to +374** of mean margin.

That ratio decides everything. Before running a benchmark, ask how many games it needs.
""")

code(r"""
import math

SIGMA = 6000        # per-game margin spread, measured on ~600 real games
EFFECTS = [68, 117, 277, 374, 1000, 3000]

def games_needed(effect, sigma=SIGMA, power=0.8, alpha=0.05):
    # two-sided z-test on a paired mean difference
    z_a, z_b = 1.959964, 0.8416212
    return math.ceil(2 * ((z_a + z_b) * sigma / effect) ** 2)

print(f"per-game sigma = {SIGMA:,}\n")
print(f"{'effect (margin)':>16}{'games for 80% power':>22}")
for e in EFFECTS:
    print(f"{e:>16,}{games_needed(e):>22,}")
""")

md(r"""
A +277 improvement needs about **3,000 paired games** to establish at 80% power. On the ladder, at
~150 games per submission, that is not happening — the leaderboard *cannot* see it. Offline, at
under a second per episode, it is twenty minutes.

**So: use the ladder to detect large changes, and an offline pool for everything smaller.** If you
are reading a 50-point leaderboard move as signal, this table is the reason you should not.
""")

md(r"""
## 2. Ladder win rate is not strength — it is a measure of your opponents

This one inverted my rankings completely.

| my build | ladder rating | win rate over its games |
|---|---|---|
| A | 2304 | **79%** |
| B | 2573 | **35%** |

Build B is rated 269 points higher and wins less than half as often. Nothing is broken: matchmaking
pairs you by rating, so **win rate equilibrates toward 50% no matter how strong you are**, and what
actually varies is the strength of the field you are drawn against.

I ranked four builds by their ladder win rate and got the reverse of the truth. If you compare
agents by win rate over ladder games, you are mostly measuring where they happened to sit while
they played.

**The fix:** compare win rate *within opponent rating bands*, so you are holding the field fixed.
""")

code(r"""
# Sketch of the band comparison. Each row is one of your games: the opponent's leaderboard
# rating, and whether you won. Bucketing by opponent strength removes the matchmaking confound.
import collections, statistics

def bands(games, edges=(0, 2100, 2250, 2400, 2550, 9999)):
    "games: list of (opponent_rating, result) with result in {1.0, 0.5, 0.0}"
    out = []
    for lo, hi in zip(edges, edges[1:]):
        g = [r for R, r in games if lo <= R < hi]
        out.append((f"{lo}-{hi}", len(g), statistics.mean(g) if g else None))
    return out

# Illustrative: a strong agent drawn against weak opposition and a weak agent drawn against strong.
strong = [(2200, 1.0)] * 40 + [(2600, 0.0)] * 10
weak   = [(2600, 1.0)] * 10 + [(2600, 0.0)] * 40
print("overall win rate  strong-but-sheltered:",
      round(statistics.mean([r for _, r in strong]), 3),
      "  weak-but-tested:", round(statistics.mean([r for _, r in weak]), 3))
print("\nby band, strong-but-sheltered:")
for b, n, wr in bands(strong):
    if n: print(f"   {b:>10}  n={n:<4} wr={wr:.2f}")
print("by band, weak-but-tested:")
for b, n, wr in bands(weak):
    if n: print(f"   {b:>10}  n={n:<4} wr={wr:.2f}")
""")

md(r"""
## 3. The mirror trap: "beats my previous build" is not "beats the field"

Most of my tuning was scored by playing a candidate against my own current build and taking the
mean margin. It is a natural choice — it is paired, low variance, and it feels like a controlled
experiment.

It selects for **beating a copy of yourself**, which is a different objective.

Four builds that the mirror ranked clearly apart, scored against a pool of published agents:

| build | margin vs pool | win rate |
|---|---|---|
| tuned | +15,242 | 0.943 |
| slot | +15,594 | 0.946 |
| impact | +15,626 | 0.946 |
| final | +15,839 | 0.946 |

They are the same agent. Everything the mirror had ranked was worth ~$200-700 against myself and
approximately nothing against anyone else.

There is a specific failure inside this. When two agents are nearly identical, they **tie exactly**,
so any perturbation at all "wins" the mirror by a few dollars at a ~50% rate. I nearly shipped one
such change on a reported 94.5% win rate that was entirely a tie-break artifact.

**The check:** whatever you tune against, validate against something else — and be suspicious of any
mirror result whose win rate is high but whose margin is tiny.
""")

md(r"""
## 4. The weak-pool trap, and the zero that is not a loss

So I built an opponent pool from published notebooks. That has its own failure: **if every opponent
loses badly, the pool cannot rank anything.**

Worse, mine actively misled me. It rated one build best by a wide margin (+27,382, winning 100%).
That build scores **exactly 0** against any opponent that competes for the early market.

Not an error. Not a timeout. Status `DONE`, final bank `0.0`.
""")

code(r"""
from kaggle_environments.envs.kaggriculture import kaggriculture as K
import inspect

# The engine hands out labour only if you can pay for it, and says nothing when you cannot.
src = inspect.getsource(K)
i = src.find("def _do_hire")
print(src[i:i+600])
""")

md(r"""
The opening of a strong tape runs on a cash floor of a few dollars. If an opponent's trading moves
the price of what you buy on day 0 by even a little, the morning hire silently does not happen — and
an agent with no hands grows weeds for two days and never recovers.

That is why a final bank of `0`, or of exactly the starting cash, is a **bug report about your
comparison**, not a win for the other side. I once accepted a whole change of direction on a result
of "100 wins to 0, mean 151,985 vs 0". The zero was the other agent dying, not losing.

**Two checks:**
- Your pool must contain opponents that beat you sometimes. If everything loses by 15-27k, it ranks
  nothing.
- Treat any final bank of 0 or `startingMoney` as invalid until you have explained it.
""")

md(r"""
## 5. The silent-exception trap

Every serious agent wraps its policy so a crash degrades to a legal action rather than forfeiting:

```python
def agent(obs):
    try:
        return my_policy(obs)
    except Exception:
        return {"farmer": ["PASS"], "hands": [], "market": []}
```

Correct for a submission. **Lethal for a benchmark**, because a layer that raises on every turn is
indistinguishable from a layer that ran and chose to do nothing.

I ported a component between two agents. It imported cleanly, ran, and produced small positive
deltas, so I nearly benchmarked it. Instrumented, it had raised **`NameError` on 714 of 719 turns** —
two lookup tables sat outside the block I had copied. The deltas were other layers underneath it.

Had I measured it as-is I would have concluded "this component does not transfer". The fixed version
reaches the same conclusion — for a completely different reason. I would have believed the right
answer on the strength of a broken experiment.
""")

code(r"""
# Instrument the layer, do not trust the score. Count turns entered, turns that changed the
# action, and exceptions raised -- and require all three to match what you intended.
import collections

def instrument(layer):
    stats = collections.Counter()
    def wrapped(action, obs, *a, **kw):
        stats["turns"] += 1
        try:
            out = layer(action, obs, *a, **kw)
        except Exception as e:
            stats["exceptions"] += 1
            stats["exc_" + type(e).__name__] += 1
            raise                      # re-raise: the benchmark must see it
        if out != action:
            stats["modified"] += 1
        return out
    return wrapped, stats

# A layer that is broken in exactly the way mine was.
def broken(action, obs):
    return MISSING_TABLE[obs["step"]]          # NameError, every turn

w, stats = instrument(broken)
for step in range(100):
    try:
        w({"market": []}, {"step": step})
    except Exception:
        pass
print(dict(stats))
print("\nturns entered:", stats['turns'], " modified:", stats['modified'],
      " exceptions:", stats['exceptions'])
print("A layer with modified==0 and exceptions==turns is NOT a null result.")
""")

md(r"""
## 6. The data most people are throwing away

Replays are large, so the usual move is to reduce them to the two action tapes and delete the rest.
I did that for weeks, and it cost me: to get a bank curve I had to re-simulate from the tapes, and
**re-simulation does not reproduce the episode** — small divergences compound and the final banks
come out wrong.

The raw replay already contains the full observation at **every step, for both seats**: money,
tiles, the shed, the shared market, the town. Reading it is exact and needs no simulation.
""")

code(r"""
# Structure of a replay. Point `path` at any episode you have downloaded
# (kaggle competitions replay <episode_id> -p <dir>).
import json, gzip, os

def per_turn(path, me_team):
    with open(path) as f:
        d = json.load(f)
    teams = d["info"]["TeamNames"]
    me = teams.index(me_team)
    rows = []
    for t, pair in enumerate(d["steps"]):
        o0 = pair[0].get("observation") or {}
        farms = o0.get("farms")
        if not farms:
            continue
        priv = [(pair[0].get("observation") or {}).get("private") or {},
                (pair[1].get("observation") or {}).get("private") or {}]
        rows.append(dict(
            t=t,
            money=[farms[me]["money"], farms[1-me]["money"]],
            shed=[sum((priv[me].get("shed") or {}).values()),
                  sum((priv[1-me].get("shed") or {}).values())],
            prices=dict(o0["market"]["prices"]),
            shops=sorted((o0.get("town") or {}).get("unlocked_shops") or []),
        ))
    return rows

print(per_turn.__doc__ or "reduce a replay to a per-turn trace of BOTH farms")
print("\nEach player's own `private` block (shed, seeds, inventories) is only in that player's")
print("observation -- take shed[0] from steps[t][0] and shed[1] from steps[t][1].")
""")

md(r"""
With that in hand, the useful question about a loss stops being "what did they plant" and becomes
**"on which day did the margin turn, and what was different on either side of it"** — which you can
ask across every game you have ever lost, at once.

Sorting my losses that way put roughly half of them in a category I had not known existed, and the
day the margin turned was nowhere near where I had assumed.
""")

md(r"""
## The checklist

1. **Score the same agent twice** and treat the gap as your noise floor. Any claimed gain smaller
   than it is not a result.
2. **Compute how many games your effect needs** before you run the benchmark. Most useful effects in
   this game need thousands.
3. **Never rank by ladder win rate.** Matchmaking equalises it. Band by opponent rating instead.
4. **Do not tune against your own build.** It optimises "beats a copy of me".
5. **Your pool must beat you sometimes**, or it ranks nothing.
6. **A final bank of 0, or of `startingMoney`, invalidates the comparison.** It is not a win.
7. **Instrument any layer wrapped in `except Exception`** — count turns, modifications and
   exceptions — before you believe any number it produces.
8. **Keep the full replay**, not just the action tapes.

None of this tells you what to build. It tells you whether what you built worked, which turned out
to be the harder half.
""")

nb = {
    "cells": CELLS,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.11"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

if __name__ == "__main__":
    out = "notebook/four-instruments-that-lied.ipynb"
    os.makedirs("notebook", exist_ok=True)
    with open(out, "w") as f:
        json.dump(nb, f, indent=1)
    print("wrote %s  (%d cells, %d code)"
          % (out, len(CELLS), sum(1 for c in CELLS if c["cell_type"] == "code")))
