import json, time, sys, os, signal
sys.path.insert(0, "moe/r3/build/opus")
from run import load
C = json.load(open("moe/r6/build/opusb/cands.json"))
class TO(Exception): pass
def al(*_): raise TO()
signal.signal(signal.SIGALRM, al)
out = {}
for p in C[int(sys.argv[1]):int(sys.argv[2])]:
    t = time.time(); signal.alarm(20)
    try: load(p, "lt"); e = None
    except TO: e = "TO"
    except Exception as ex: e = repr(ex)[:40]
    signal.alarm(0)
    out[p] = (round(time.time() - t, 2), e)
    print(out[p], p, flush=True)
json.dump(out, open(f"moe/r6/build/opusb/loadtime_{sys.argv[1]}.json", "w"))
