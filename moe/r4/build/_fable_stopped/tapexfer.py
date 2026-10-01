"""Cross-seed tape transfer: a top-10 team's FULL recorded tape (units + market, open-loop, hands fixed) played on
foreign seeds against our live build C1 (closed-loop). Baseline on the same seeds: C1 self-play.
usage: tapexfer.py OUT.jsonl NSEEDS [TEAMS(comma)]
"""
import sys, json, os
sys.argv[1] = os.path.abspath(sys.argv[1])
from common import *

def pick_tapes(teams):
    out = {}
    for p in top10_files():
        d = load_ep(p)
        for s in (0, 1):
            t = d["teams"][s]
            if t in teams and t not in out: out[t] = (p, s)
    return out

def job(args):
    kind, path, seat, seed, us = args
    if kind == "self":
        a, b = load_agent(C1, "s0")[0], load_agent(C1, "s1")[0]
        g = run_game(a, b, seed); return dict(kind=kind, seed=seed, r=g["r"], shops=g["shops"])
    d = load_ep(path); me = tape_agent(d["actions"], seat, fix_hands=True); opp = load_agent(C1, "o")[0]
    pair = (me, opp) if us == 0 else (opp, me)
    g = run_game(pair[0], pair[1], seed)
    return dict(kind=kind, team=d["teams"][seat], ep=d["episode_id"], rec=d["rewards"][seat], rec_shops150=d.get("shops150"),
                seed=seed, us=us, me=g["r"][us], opp=g["r"][1 - us], shops=g["shops"], tele=g["tele"][us])

if __name__ == "__main__":
    out = sys.argv[1]; n = int(sys.argv[2])
    teams = sys.argv[3].split(",") if len(sys.argv) > 3 else ["DSM", "DECEM", "Unknown Mother-Goose", "Vadim Vasilenko", "Boey", "Majkel1337"]
    tapes = pick_tapes(teams); seeds = [9100001 + i for i in range(n)]
    jobs = [("self", None, None, s, 0) for s in seeds]
    for t, (p, seat) in tapes.items():
        jobs += [("tape", p, seat, s, i % 2) for i, s in enumerate(seeds)]
    pool(job, jobs, out)
    rows = [json.loads(l) for l in open(out)]
    selfb = {r["seed"]: r["r"] for r in rows if r["kind"] == "self"}
    print("C1 self-play mean bank", sum(sum(v) / 2 for v in selfb.values()) / max(1, len(selfb)))
    for t in tapes:
        R = [r for r in rows if r.get("team") == t]
        if not R: continue
        m = [r["me"] - r["opp"] for r in R]
        print(f"{t:22s} n={len(R)} tape bank mean {sum(r['me'] for r in R)/len(R):.0f} (recorded {R[0]['rec']:.0f}) | C1 opp bank {sum(r['opp'] for r in R)/len(R):.0f} | "
              f"margin {sum(m)/len(m):+.0f} W{sum(x>0 for x in m)}-L{sum(x<0 for x in m)} | vs C1-self {sum(r['me']-sum(selfb.get(r['seed'],[0,0]))/2 for r in R)/len(R):+.0f}")
