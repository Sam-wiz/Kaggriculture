"""r6 opusb stage-1 lineage screen: each candidate's step-1 action (seat 0 and 1) on a fresh game vs lane openings.
usage: fp1step.py START END  -> fp1step_START.jsonl"""
import json, sys, signal, os
sys.path.insert(0, "moe/r3/build/opus"); sys.path.insert(0, "kaggriculture-cppsim")
from run import load, act
import kagsim
C = json.load(open("moe/r6/build/opusb/cands.json"))
class TO(Exception): pass
def al(*_): raise TO()
signal.signal(signal.SIGALRM, al)
def canon(a): return json.dumps(dict(farmer=a.get("farmer"), hands=list(a.get("hands") or []), market=a.get("market") or []), sort_keys=True) if isinstance(a, dict) else None
out = open(f"moe/r6/build/opusb/fp1step_{sys.argv[1]}.jsonl", "w")
for p in C[int(sys.argv[1]):int(sys.argv[2])]:
    r = dict(cand=p)
    for seat in (0, 1):
        signal.alarm(20)
        try:
            fn, m = load(p, "s1"); g = kagsim.Game(seed=12345)
            r[f"a{seat}"] = canon(act(fn, g.observe(seat)))
        except TO: r[f"a{seat}"] = "TO"
        except Exception as e: r[f"a{seat}"] = "ERR " + repr(e)[:40]
        signal.alarm(0)
    out.write(json.dumps(r) + "\n"); out.flush()
