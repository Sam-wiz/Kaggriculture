# Tape-flip gate: replay v8 / v8p vs the recorded opponent action stream on the real seeds.
# For each fetched live episode: put candidate on v8's seat, opponent tape on theirs.
# Open-loop caveat: opponent can't react — measures trajectory improvement only.
import sys, os, gzip, json, glob
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor

NOP = {"farmer": ["PASS"], "hands": [], "market": []}

def make_tape(actions):
    def agent(obs):
        step = obs.get("step")
        if step is None:
            step = int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        if step < 0 or step >= len(actions):
            return dict(NOP)
        a = actions[step]
        if not isinstance(a, dict):
            return dict(NOP)
        hands = a.get("hands") or []
        have = len(obs["farms"][obs["player"]].get("hands", []))
        if len(hands) > have:
            hands = hands[:have]
        elif len(hands) < have:
            hands = list(hands) + [["PASS"]] * (have - len(hands))
        return {"farmer": a.get("farmer") or ["PASS"], "hands": hands,
                "market": a.get("market") or []}
    return agent

def job(arg):
    from run import load, act
    import kagsim
    f, cand_path, tag = arg
    rec = json.load(gzip.open(f))
    seat = rec["teams"].index("Sam-wiz"); o = 1 - seat
    opp_actions = [s[o].get("action") for s in rec["steps"]]
    cand, _ = load(cand_path, "c")
    tape = make_tape(opp_actions)
    g = kagsim.Game(seed=int(rec["seed"]))
    for t in range(719):
        obs0, obs1 = g.observe(0), g.observe(1)
        a0 = act(cand, obs0) if seat == 0 else act(tape, obs0)
        a1 = act(tape, obs1) if seat == 0 else act(cand, obs1)
        g.step(a0, a1)
    rc, ro = (g.reward(0), g.reward(1)) if seat == 0 else (g.reward(1), g.reward(0))
    live_margin = rec["rewards"][seat] - rec["rewards"][o]
    return dict(ep=rec["episode_id"], tag=tag, cand=float(rc), opp=float(ro),
                live_margin=live_margin, opp_name=rec["teams"][o])

if __name__ == "__main__":
    os.nice(10)
    files = sorted(glob.glob(ROOT + "/mine/rawkeep/v8live/*.json.gz"))
    jobs = []
    for f in files:
        jobs.append((f, ROOT + "/moe/r7/build/devin/v8p.py", "v8p"))
        jobs.append((f, ROOT + "/subAC_v8.py", "v8"))
    with ProcessPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/tape_flip.json", "w"), indent=1)
    for tag in ("v8", "v8p"):
        g = [r for r in rows if r["tag"] == tag]
        w = sum(r["cand"] > r["opp"] for r in g)
        print(f"{tag}: {w}-{len(g)-w} vs tapes  mean {sum(r['cand'] for r in g)/len(g):.0f} "
              f"margin {sum(r['cand']-r['opp'] for r in g)/len(g):+.0f}")
    # flip analysis
    print("\nper-episode (loss eps only matter):")
    byep = {}
    for r in rows: byep.setdefault(r["ep"], {})[r["tag"]] = r
    for ep, d in sorted(byep.items()):
        v8, v8p = d["v8"], d["v8p"]
        print(f"ep{ep} vs {v8['opp_name'][:18]:20} live{v8['live_margin']:+7.0f} | "
              f"v8 {v8['cand']-v8['opp']:+7.0f} | v8p {v8p['cand']-v8p['opp']:+7.0f}")
