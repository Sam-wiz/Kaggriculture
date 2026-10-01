"""Stage-1 screen (Claude Code): each candidate vs C1 closed-loop in kagsim on the RR seeds 9100001..20,
sw=0 only (seat-swap is a bit-identical duplicate in kagsim, opusb 07:34). Uses opus's rr.job.
Output moe/r4/screen1.jsonl rows in rr format (a=cand, b='C1')."""
import json, os, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r4/build/opus"); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
import rr
from concurrent.futures import ProcessPoolExecutor
SKIP = ()
if __name__ == "__main__":
    cands = [(n, p) for n, p in json.load(open("moe/r6/screen_candsGH.json")) if not any(s in n for s in SKIP)]
    out = "moe/r6/screenGH5.jsonl"; done = set()
    if os.path.exists(out):
        for l in open(out): r = json.loads(l); done.add((r["a"], r["seed"]))
    jobs = [((n, p), ("C1", "subY_C1_predict2.py"), s, 0) for n, p in cands for s in range(9100001, 9100006) if (n, s) not in done]
    print(len(cands), "candidates,", len(jobs), "games", flush=True)
    with ProcessPoolExecutor(max_workers=int(sys.argv[1]) if len(sys.argv) > 1 else 4) as ex, open(out, "a") as f:
        for i, r in enumerate(ex.map(rr.job, jobs, chunksize=1), 1):
            f.write(json.dumps(r) + "\n"); f.flush()
            if i % 40 == 0: print(i, flush=True)
    rows = [json.loads(l) for l in open(out)]
    print(f"\n{'candidate':<42}{'W-L-T vs C1':>12}{'mean margin':>13}{'err':>5}")
    res = []
    for n, _ in cands:
        rs = [r for r in rows if r["a"] == n]; ok = [r for r in rs if "err" not in r]
        w = sum(r["ra"] > r["rb"] for r in ok); l = sum(r["ra"] < r["rb"] for r in ok); t = len(ok) - w - l
        m = sum(r["ra"] - r["rb"] for r in ok) / max(1, len(ok))
        res.append(((w + .5 * t) / max(1, len(ok)), n, w, l, t, m, len(rs) - len(ok)))
    for wr, n, w, l, t, m, e in sorted(res, reverse=True):
        print(f"{n:<42}{f'{w}-{l}-{t}':>12}{m:>+13.0f}{e:>5}{'   <== stage 2' if wr >= 0.5 and len(rows) else ''}")
