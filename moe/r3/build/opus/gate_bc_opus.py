"""Opus r3 copy of Fable's gate_bc.py: candidates = build/opus/cand_C*_rebuilt.py, output = build/opus/gate_bc.jsonl.
Fable's common.py and lots.json are read-only inputs."""
"""Gates (b) and (c). Our seat = live agent (vanilla base or candidate with library holdout); their seat = recorded
rival tape, open-loop (W=0) or price-reactive (W=12, delta=0.10). Tapes: the 28 >=2200 shepherd mirror games
(gate b) plus the 18 WLV games (reference). Library modes: vanilla (dormant), parity holdout (_V92_EP-equivalent:
streams whose ep has the game's parity are excluded, i.e. ~half the library incl. this game's own stream), LOO
(only this game's own stream excluded = production library size).
usage: python gate_bc.py [C1,C2] [open,react] [parity,loo]"""
import json, os, sys, time
sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/fable")
import common
common.setup()
from concurrent.futures import ProcessPoolExecutor

BASES = {"C1": ("subW_shepherd.py", "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/cand_C1_rebuilt.py"),
         "C2": ("subX_hyb2965.py", "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/cand_C2_rebuilt.py")}
W, DELTA = 12, 0.10


def job(args):
    ep, base, arm, rmode, seat, seed, acts, lots = args
    import harness
    t0 = time.time()
    vpath, cpath = BASES[base]
    name = f"g_{base}_{arm}_{rmode}_{ep}"
    if arm == "vanilla":
        me, mod = common.load_module_agent(vpath, name)
        nlib = 0
    else:
        me, mod = common.load_module_agent(cpath, name)
        streams = mod._v92_q_streams()                       # decode the embedded blob
        if arm == "parity":
            keep = [(e, ev) for e, ev in streams if e % 2 != ep % 2]
        elif arm == "loo":
            keep = [(e, ev) for e, ev in streams if e != ep]
        else:
            keep = streams
        mod._V92_Q_CACHE["streams"] = keep
        nlib = len(keep)
    them = 1 - seat
    if rmode == "open":
        rival = common.tape_agent(acts, them); rrep = None
    else:
        rival = common.ReactiveTape(acts, them, lots, W=W, delta=DELTA)
    pair = [None, None]; pair[seat] = me; pair[them] = rival
    r = harness.run_episode(pair[0], pair[1], seed=seed, copy_obs=True)
    rw = r["reward"]
    shops = list(r["state"][0].observation.town["unlocked_shops"])
    q = dict(getattr(mod, "_V92_Q_REPORT", {})); p = dict(getattr(mod, "_V92_P_REPORT", {}))
    rrep = dict(rival.report) if rmode == "react" else None
    del sys.modules[name]
    return dict(ep=ep, base=base, arm=arm, rmode=rmode, seat=seat, margin=rw[seat] - rw[them], ours=rw[seat], theirs=rw[them],
                status=r["status"], errors=r["errors"], shops=shops, q=q, p=p, nlib=nlib, rival=rrep, secs=round(time.time() - t0, 1))


if __name__ == "__main__":
    bases = (sys.argv[1] if len(sys.argv) > 1 else "C1,C2").split(",")
    rmodes = (sys.argv[2] if len(sys.argv) > 2 else "open,react").split(",")
    arms = ["vanilla"] + (sys.argv[3] if len(sys.argv) > 3 else "parity,loo").split(",")
    m28 = common.mirror28(); w18 = common.wlv18()
    tapes = {int(r["ep"]): r for r in m28}
    for r in w18:
        tapes.setdefault(int(r["ep"]), r)
    lots_all = json.load(open(os.path.join(common.HERE, "lots.json")))
    jobs = []
    for ep, r in tapes.items():
        acts, seed, rew = common.load_tape(f"mine/opp/{ep}.json.gz", "reduced")
        for base in bases:
            for rmode in rmodes:
                for arm in arms:
                    jobs.append((ep, base, arm, rmode, r["seat"], seed, acts, lots_all[str(ep)]))
    out = open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/gate_bc.jsonl", "a")
    print(len(jobs), "games over", len(tapes), "tapes", flush=True)
    with ProcessPoolExecutor(max_workers=2) as ex:
        for i, res in enumerate(ex.map(job, jobs, chunksize=1)):
            out.write(json.dumps(res) + "\n"); out.flush()
            print(i, res["ep"], res["base"], res["arm"], res["rmode"], f"m={res['margin']:+.0f}", f"ours={res['ours']:.0f}",
                  "q=", res["q"], "nlib", res["nlib"], "riv", res["rival"], f"{res['secs']}s", res["errors"], flush=True)
