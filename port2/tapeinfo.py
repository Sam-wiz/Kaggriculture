"""Decode the port's two tapes: SELL schedule, order-slot pressure, PICKUP usage."""
import importlib.util
import os
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


M = load(os.path.join(ROOT, "port/main.py"), "portmain_info")

for route in range(2):
    tape = M._TAPES[route]
    sells = Counter()
    sell_orders = 0
    nslots = Counter()
    first = {}
    pickups = Counter()
    diff = 0
    for s, (nu, units, no, orders) in enumerate(tape):
        nslots[no] += 1
        for i in range(no):
            op, item, n = orders[i]
            if op == M.M_SELL:
                sells[M._ITEMS[item]] += n
                sell_orders += 1
                first.setdefault(M._ITEMS[item], s)
        for i in range(nu):
            op, arg, n = units[i]
            if op == 5:  # PICKUP
                pickups[M._ITEMS[arg]] += max(1, n)
        if route == 1 and tape[s] != M._TAPES[0][s]:
            diff += 1
    print(f"--- route {route}: sell orders={sell_orders}")
    print("   sells:", dict(sells.most_common()))
    print("   first sale step:", first)
    print("   pickups:", dict(pickups.most_common()))
    print("   n_orders histogram:", dict(sorted(nslots.items())))
    if route == 1:
        print(f"   steps differing from route 0: {diff}")
        firstdiff = next(s for s in range(719) if M._TAPES[1][s] != M._TAPES[0][s])
        print(f"   first differing step: {firstdiff}")
