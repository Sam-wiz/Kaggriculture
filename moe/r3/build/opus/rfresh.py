"""R instrument characterization: X vs candidate on the 20 fresh W1 seeds (seedindex [1356:1376]), both seats."""
import sys, json
FARGS = list(sys.argv); sys.argv = [sys.argv[0]]
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/run.py").read().split('\nif __name__ == "__main__":')[0])
if __name__ == "__main__":
    S = json.load(open(ROOT + "/moe/r3/build/opus/w1_seeds.json"))
    pairs = [a.split(":") for a in FARGS[2:]]   # xname=xpath:oname=opath
    jobs = []
    for x, o in pairs:
        xn, xp = x.split("="); on, op = o.split("=")
        for s in S["fresh"]:
            for us in (0, 1): jobs.append((xn, xp, on, op, s, us))
    out = ROOT + f"/moe/r3/build/opus/rfresh_{FARGS[1]}.jsonl"; open(out, "w").close()
    pool(closed, jobs, out)
