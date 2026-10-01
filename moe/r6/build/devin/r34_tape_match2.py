# Tape-match v2: (1) replay the fish episode verbatim -> check banks reproduce.
# (2) Shadow-run agents_v8 on the episode trajectory: at each step feed recorded actions
#     to the sim, but log what OUR agent emits; compare to rec[t] and rec[t+1] (offset).
import gzip, json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act
import kagsim

EP = "mine/top10/112239186.json.gz"
d = json.load(gzip.open(EP))
seat = 1
rec = [a[seat] for a in d["actions"]]
opp = [a[1 - seat] for a in d["actions"]]

# (1) verbatim replay
g = kagsim.Game(seed=int(d["seed"]))
N0 = min(720, len(rec))
for t in range(N0 - 1):
    g.step(rec[t] if seat == 0 else opp[t], rec[t] if seat == 1 else opp[t])
    # careful: step(a0, a1) - seat0 action first
print("replay banks:", g.reward(0), g.reward(1), "episode rewards:", d["rewards"])

# (2) shadow run: feed recorded tape, log our agent's outputs
a, _ = load("rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py", "a")
g = kagsim.Game(seed=int(d["seed"]))
mine_log = []
N = min(120, len(rec) - 1)
for t in range(N):
    mine_log.append(act(a, g.observe(seat)))
    if seat == 1:
        g.step(opp[t], rec[t])
    else:
        g.step(rec[t], opp[t])

def same(x, y):
    return json.dumps(x, sort_keys=True) == json.dumps(y, sort_keys=True)

m_same = sum(same(mine_log[t], rec[t]) for t in range(N))
m_shift = sum(same(mine_log[t], rec[t + 1]) for t in range(N - 1))
m_back = sum(same(mine_log[t + 1], rec[t]) for t in range(N - 1))
print(f"identical full-action dicts: rec[t]=mine[t] {m_same}/{N}; rec[t+1]=mine[t] {m_shift}/{N-1}; rec[t]=mine[t+1] {m_back}/{N-1}")
for t in range(2, 8):
    print("t", t, "mine:", json.dumps(mine_log[t])[:150])
    print("   rec:", json.dumps(rec[t])[:150])
