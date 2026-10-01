"""Instrument C1-D: one game vs shepherd, report _DC_REPORT and PREDICT counters; also C1 on the same seed."""
import sys, os
sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus")
from run import load, act, kagsim, tele
for path in sys.argv[1:]:
    a, ma = load(path, "x"); b, mb = load("subW_shepherd.py", "o")
    g = kagsim.Game(seed=9300001)
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1); g.step(act(a, o0), act(b, o1))
    print(path.split('/')[-1], [g.reward(0), g.reward(1)], getattr(ma, "_DC_REPORT", None), tele(ma))
