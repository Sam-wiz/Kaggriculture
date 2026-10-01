"""Screen one v8prog variant: argv = name, V8PROG json, seed list, [opp]."""
import json
import os
import sys

sys.path.insert(0, '.')
name = sys.argv[1]
os.environ["V8PROG"] = sys.argv[2]
seeds = json.loads(sys.argv[3])
opp = sys.argv[4] if len(sys.argv) > 4 else 'agents/v8x.py'

import harness  # noqa: E402

wa, wb, t, recs = harness.match('moe/r8/build/prog/v8prog.py', opp, seeds, swap=True)
marg = sum(r['a'] - r['b'] for r in recs) / len(recs)
errs = sum(1 for r in recs if r['errors'][0] or r['errors'][1])
line = "%-8s W%d-L%d-T%d margin %+7.0f errs %d  vs %s" % (
    name, wa, wb, t, marg, errs, opp)
print(line, flush=True)
with open('moe/r8/build/prog/results.log', 'a') as f:
    f.write(line + '\n')
    for r in recs:
        f.write("  seed %d swap=%d a=%.0f b=%.0f\n"
                % (r['seed'], r['swapped'], r['a'], r['b']))
