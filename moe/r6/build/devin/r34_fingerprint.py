# Generate r34v8's action tape on a few seeds (vs 'pass') to build its fingerprint:
# market orders + unit ops for steps 0..47 (first 2 days).
import json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")

def gen(seed):
    from run import load, act
    import kagsim
    a, _ = load("rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py", "a")
    g = kagsim.Game(seed=int(seed))
    tape = []
    for t in range(48):
        aa = act(a, g.observe(0))
        tape.append(aa)
        g.step(aa, {"farmer": ["PASS"], "hands": [], "market": []})
    return tape

if __name__ == "__main__":
    out = {str(s): gen(s) for s in (9100001, 9202001, 1761340719)}
    json.dump(out, open("moe/r6/build/devin/r34_tape.json", "w"))
    t = out["9100001"]
    for i in range(6):
        print(i, json.dumps(t[i])[:220])
