"""Remaining Fable gate-(d) matchups on the rebuilt candidates: C2 vs shepherd, C2 vs hyb2965, C1 vs C2 (and C2 vs shepR),
closed-loop, seedindex [1380:1404] (20 seeds) x both seats -> c2gate.jsonl."""
import sys, json
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/run.py").read().split('\nif __name__ == "__main__":')[0])
if __name__ == "__main__":
    idx = [r["seed"] for r in json.load(open(ROOT + "/data/seedindex_900000_1400.json"))][1380:1404]
    C1 = "moe/r3/build/opus/cand_C1_rebuilt.py"; C2 = "moe/r3/build/opus/cand_C2_rebuilt.py"
    M = [("C2", C2, "shep", "subW_shepherd.py"), ("C2", C2, "hyb2965", "subX_hyb2965.py"), ("C1", C1, "C2", C2), ("C2", C2, "shepR", "moe/r3/build/opus/shepR.py")]
    jobs = [(xn, xp, on, op, s, us) for xn, xp, on, op in M for s in idx for us in (0, 1)]
    out = ROOT + "/moe/r3/build/opus/c2gate.jsonl"; open(out, "w").close(); pool(closed, jobs, out)
