"""Same-seed decomposition of the top-10 gap, on the dump episodes (recorded seed; opponent seat = recorded tape open-loop).
modes:
  a   our agent (C1) full closed-loop in seat X                      -> farm+market gap (open-loop-flattered)
  b   top team's units + tape buys/hires, product SELLs from C1     -> what our sell policy makes on THEIR farm
  c   top team's units + tape buys/hires, sell-all product policy   -> what a trivial sell policy makes on THEIR farm
  d   pure tape both seats (exactness control)
usage: decomp.py OUT.jsonl MODES(comma) [AGENT=subY_C1_predict2.py] [LIMIT]
"""
import sys, json, os
sys.argv[1] = os.path.abspath(sys.argv[1])
from common import *

def job(args):
    path, X, mode, agent_path = args
    d = load_ep(path); acts = d["actions"]; Y = 1 - X
    opp = tape_agent(acts, Y)
    if mode == "d": me = tape_agent(acts, X)
    elif mode == "a": me = load_agent(agent_path, "a")[0]
    elif mode == "b": me = hybrid_agent(acts, X, agent_market_fn(load_agent(agent_path, "b")[0]))
    elif mode == "c": me = hybrid_agent(acts, X, sell_all_orders)
    pair = (me, opp) if X == 0 else (opp, me)
    g = run_game(pair[0], pair[1], d["seed"], trace_days=True)
    rec = d["rewards"]
    return dict(ep=d["episode_id"], X=X, team=d["teams"][X], opp=d["teams"][Y], mode=mode, rec_me=rec[X], rec_opp=rec[Y],
                me=g["r"][X], oppb=g["r"][Y], shopok=g["shops"] == d.get("shops"), money=g["money"][X],
                tele=g["tele"][X])

if __name__ == "__main__":
    out = sys.argv[1]; modes = sys.argv[2].split(",")
    agent_path = sys.argv[3] if len(sys.argv) > 3 else C1
    lim = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    files = top10_files(); files = files[:lim] if lim else files
    jobs = [(p, X, m, agent_path) for p in files for X in (0, 1) for m in modes]
    pool(job, jobs, out)
    rows = [json.loads(l) for l in open(out)]
    for m in modes:
        R = [r for r in rows if r["mode"] == m]
        if not R: continue
        dm = [r["me"] - r["rec_me"] for r in R]; mg = [r["me"] - r["oppb"] for r in R]; rmg = [r["rec_me"] - r["rec_opp"] for r in R]
        print(f"mode {m} n={len(R)} bank-vs-recorded mean {sum(dm)/len(dm):+.0f} (min {min(dm):+.0f} max {max(dm):+.0f}) | "
              f"margin mean {sum(mg)/len(mg):+.0f} W {sum(x>0 for x in mg)} | recorded margin mean {sum(rmg)/len(rmg):+.0f} | shopok {sum(r['shopok'] for r in R)}/{len(R)}")
