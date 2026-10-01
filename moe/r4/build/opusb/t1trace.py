"""Trace one T1 'own' run vs 'rec': per-step money, hires, dead-action counter of the tape seat; first divergence."""
import sys, json, gzip
sys.path.insert(0, "moe/r4/build/opusb")
from t1 import *
g_path, k = sys.argv[1], int(sys.argv[2]); live = sys.argv[3] if len(sys.argv) > 3 else "subY_C1_predict2.py"
G = ep(g_path); X = tape(G["actions"], k)
fn, m = load(live, "lv")
def run(O):
    g = kagsim.Game(seed=int(G["seed"])); tr = []
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        f = (o0 if k == 0 else o1)
        te = g.telemetry(k)
        tr.append((t, f["farms"][k]["money"], len(f["farms"][k]["hands"]), te["dead_actions"], te["refused_hire"], te["refused_buy_animal"], te["refused_buy_seed"], te["refused_buy_land"], tuple(o0["town"]["unlocked_shops"]), farmsig(f["farms"][k])))
        A, B = (X, O) if k == 0 else (O, X)
        g.step(A(o0), B(o1))
    return tr
rec = run(tape(G["actions"], 1 - k)); own = run(lambda o: act(fn, o))
fd = None
for a, b in zip(rec, own):
    if a[1:] != b[1:]:
        print("first diff t=%d rec money %s hands %s dead %s refH %s refA %s refS %s refL %s | own money %s hands %s dead %s refH %s refA %s refS %s refL %s" % ((a[0],) + a[1:8] + b[1:8]))
        fd = a[0]; break
for t in list(range(fd, fd + 6)) + list(range(0, 720, 48)):
    a, b = rec[t], own[t]
    print(t, "rec $%d h%d dead%d rH%d rA%d rS%d rL%d" % a[1:8], "| own $%d h%d dead%d rH%d rA%d rS%d rL%d" % b[1:8], "shops", a[8] == b[8], "tilesdiff", sum(x != y for x, y in zip(a[9], b[9])))
print("tape market t=%d.." % fd, [G["actions"][t + 1][k]["market"] for t in range(fd, fd + 3)])
