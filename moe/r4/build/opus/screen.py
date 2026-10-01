"""Stage-1 necessary-condition screen: each distinct rivals7/8 payload (dedup by _entry.py md5) vs an anchor on the RR
seeds 9100001.. (sw=0: candidate seat 0; seat-swap is a kagsim duplicate per opusb 07:34). Breadth-first over seeds,
hard wall-clock deadline, <=2 workers. usage: screen.py OUT.jsonl ANCHOR=PATH NSEEDS DEADLINE_S"""
import json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0, ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
def job(arg):
    from run import load, act
    import kagsim
    cn, cp, an, ap, seed = arg; t0 = time.time()
    try:
        a, _ = load(cp, "c"); b, _ = load(ap, "o"); g = kagsim.Game(seed=int(seed))
        for t in range(719):
            o0, o1 = g.observe(0), g.observe(1); g.step(act(a, o0), act(b, o1))
        return dict(a=cn, b=an, seed=seed, sw=0, ra=float(g.reward(0)), rb=float(g.reward(1)), dt=round(time.time() - t0, 1))
    except Exception as e:
        return dict(a=cn, b=an, seed=seed, sw=0, err=repr(e)[:120])
if __name__ == "__main__":
    out, anc, ns, dl = sys.argv[1], sys.argv[2].split("=", 1), int(sys.argv[3]), float(sys.argv[4])
    seen, cands = set(), []
    for l in open("moe/r4/build/opus/rivals_entry_md5.txt"):
        md, _, d = l.split()
        if md not in seen: seen.add(md); cands.append((d.split("/")[1][:28] + "@" + md[:4], d + "/main.py"))
    done = set()
    if os.path.exists(out):
        for l in open(out): r = json.loads(l); done.add((r["a"], r["seed"]))
    jobs = [(cn, cp, anc[0], anc[1], s) for s in range(9100001, 9100001 + ns) for cn, cp in cands if (cn, s) not in done]
    print(len(cands), "cands", len(jobs), "jobs", flush=True)
    import multiprocessing as mp
    T0 = time.time(); pool = mp.Pool(2); n = 0
    with open(out, "a") as f:
        try:
            for r in pool.imap(job, jobs, chunksize=1):
                f.write(json.dumps(r) + "\n"); f.flush(); n += 1
                if time.time() - T0 > dl: print("deadline", n, flush=True); break
        finally:
            pool.terminate(); pool.join()
    print("done", n, round(time.time() - T0), "s", flush=True)
