"""Gate (d): closed-loop sanity. Candidate vs subW_shepherd.py and vs subX_hyb2965.py (both sides live and reacting),
24 fresh seeds (seed-index slice [1380:1404]) x both seats. Pass = WR >= 0.45 vs each. Also C1 vs C2 (reference).
usage: python gate_d.py [matchups comma list, default C1-shep,C1-hyb,C2-shep,C2-hyb,C1-C2]"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common
common.setup()
from concurrent.futures import ProcessPoolExecutor

AG = {"C1": os.path.join(common.HERE, "cand_C1.py"), "C2": os.path.join(common.HERE, "cand_C2.py"),
      "shep": "subW_shepherd.py", "hyb": "subX_hyb2965.py"}


def job(args):
    a, b, seed, swap = args
    import harness
    t0 = time.time()
    x, y = (b, a) if swap else (a, b)
    fx, mx = common.load_module_agent(AG[x], f"d_{x}_{seed}_{swap}_0")
    fy, my = common.load_module_agent(AG[y], f"d_{y}_{seed}_{swap}_1")
    r = harness.run_episode(fx, fy, seed=seed, copy_obs=True)
    rw = r["reward"]
    ma, mb = (rw[1], rw[0]) if swap else (rw[0], rw[1])
    tel = {x: dict(q=dict(getattr(mx, "_V92_Q_REPORT", {})), p=dict(getattr(mx, "_V92_P_REPORT", {}))),
           y: dict(q=dict(getattr(my, "_V92_Q_REPORT", {})), p=dict(getattr(my, "_V92_P_REPORT", {})))}
    for n in (f"d_{x}_{seed}_{swap}_0", f"d_{y}_{seed}_{swap}_1"):
        sys.modules.pop(n, None)
    return dict(a=a, b=b, seed=seed, swap=swap, a_bank=ma, b_bank=mb, margin=ma - mb, status=r["status"], errors=r["errors"],
                tel=tel, secs=round(time.time() - t0, 1))


if __name__ == "__main__":
    ms = (sys.argv[1] if len(sys.argv) > 1 else "C1-shep,C1-hyb,C2-shep,C2-hyb,C1-C2").split(",")
    idx = json.load(open("data/seedindex_900000_1400.json"))
    seeds = [r["seed"] for r in idx][1380:1404]
    jobs = [(a, b, s, sw) for m in ms for a, b in [m.split("-")] for s in seeds for sw in (False, True)]
    out = open(os.path.join(common.HERE, "gate_d.jsonl"), "a")
    print(len(jobs), "games; seeds", seeds[0], "..", seeds[-1], flush=True)
    with ProcessPoolExecutor(max_workers=2) as ex:
        for i, res in enumerate(ex.map(job, jobs, chunksize=1)):
            out.write(json.dumps(res) + "\n"); out.flush()
            print(i, res["a"], "vs", res["b"], res["seed"], "swap" if res["swap"] else "    ", f"m={res['margin']:+.0f}",
                  "telA", res["tel"][res["a"]]["q"], "telB", res["tel"][res["b"]]["q"], f"{res['secs']}s", res["errors"], flush=True)
