"""Push each of the router's decisions as late as prefix-safety allows.

The shipped model decides tape 0-vs-1 at step 144 and 2-vs-3 at step 648. A switch is only sound
while the candidate tapes are still byte-identical, and the measured divergence points are:

    tape0 vs tape1  ->  168        tape0 vs tape2  ->  649
    tape0 vs tape3  ->  672        tape2 vs tape3  ->  649

So the first decision is safe up to turn 167 and the second up to 648 (tape 2 forces it), while a
decision that only chooses tape 3 is safe to 671. The shipped steps leave 23 turns of shop and
market information unused on the first call -- nearly a full day, during which another shop can
unlock -- for no gain in safety.

Only `model.json` changes; the agent code is untouched.

Usage:  python mklate.py <outdir> <step1> <step2>
"""
import json
import os
import shutil
import sys

SRC = "rivals/yhay81_shop-router-0908/pkg"
FILES = ("main.py", "observation.py", "model.json", "actions.json")


def build(outdir, step1, step2):
    if os.path.isdir(outdir):
        shutil.rmtree(outdir)
    os.makedirs(outdir)
    for f in FILES:
        shutil.copy(os.path.join(SRC, f), os.path.join(outdir, f))
    model = json.load(open(os.path.join(SRC, "model.json")))
    stages = sorted(model["stages"], key=lambda s: s["step"])
    assert len(stages) == 2, "expected the shipped two-stage model"
    stages[0]["step"] = step1
    stages[1]["step"] = step2
    model["stages"] = stages
    json.dump(model, open(os.path.join(outdir, "model.json"), "w"))
    print("wrote %s  decisions at steps %d and %d (was 144 and 648)"
          % (outdir, step1, step2))
    return os.path.join(outdir, "main.py")


if __name__ == "__main__":
    out = sys.argv[1]
    s1 = int(sys.argv[2]) if len(sys.argv) > 2 else 167
    s2 = int(sys.argv[3]) if len(sys.argv) > 3 else 648
    build(out, s1, s2)
