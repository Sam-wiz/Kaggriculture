"""In-company evaluation: candidate blueprint vs a live opponent agent.

kagsim steps both seats; each gets the trimmed seat-N observation.
Returns (candidate_bank, opp_bank).
"""
import importlib.util
import json
import sys

for _p in ("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture",
           "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/"
           "kaggriculture-island-ga"):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import kagsim
import exec3

PASS = {"farmer": ["PASS"], "hands": [], "market": []}
V48_PATH = ("rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue"
            "/v48_agent/main.py")
PIPE7 = "subI_pipe7.py"


def load_agent(path):
    spec = importlib.util.spec_from_file_location("opp", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.agent


def _seat_obs(game, seat):
    return game.observe(seat)


def match(agent_a, agent_b, seed):
    """agent_a in seat 0, agent_b in seat 1. Returns (bank0, bank1)."""
    game = kagsim.Game(seed=int(seed))
    for _ in range(720):
        try:
            a0 = agent_a(_seat_obs(game, 0))
        except Exception:
            a0 = dict(PASS)
        try:
            a1 = agent_b(_seat_obs(game, 1))
        except Exception:
            a1 = dict(PASS)
        game.step(a0, a1)
    return float(game.reward(0)), float(game.reward(1))


def series(bp, opp_agent, seeds):
    """Candidate vs opp on seeds, both seat orders. Returns list of
    (seed, cand_bank, opp_bank, cand_won)."""
    cand = exec3.make_agent(bp)
    out = []
    for s in seeds:
        b0, b1 = match(cand, opp_agent, s)          # cand seat 0
        out.append((s, b0, b1, b0 > b1))
        b0, b1 = match(opp_agent, cand, s)          # cand seat 1
        out.append((s, b1, b0, b1 > b0))
    return out


if __name__ == "__main__":
    bp = json.loads(open(sys.argv[1]).read()) if len(sys.argv) > 1 else None
    seeds = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 \
        else [11, 23, 47]
    opp_path = sys.argv[3] if len(sys.argv) > 3 else PIPE7
    opp = load_agent(opp_path)
    rows = series(bp, opp, seeds)
    w = sum(1 for r in rows if r[3])
    margin = sum(r[1] - r[2] for r in rows) / len(rows)
    print(f"candidate vs {opp_path}: W{w}-L{len(rows)-w}  margin {margin:+.0f}")
    for r in rows:
        print(f"  seed{r[0]:>4}  cand {r[1]:>8.0f}  opp {r[2]:>8.0f}  "
              f"{'WIN' if r[3] else 'loss'}")
