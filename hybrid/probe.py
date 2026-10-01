import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness

BL = "rivals/boatlee_v29-r1-adaptive-market-hysteresis/main.py"

def probe(a, b, seed=1):
    rec = []
    def on_step(step, state, env):
        obs0 = state[0].observation
        rec.append(dict(step=step,
                        shed=[dict(s.observation.private["shed"]) for s in state],
                        money=[float(f["money"]) for f in obs0.farms],
                        inv=dict(obs0.market["inventory"]),
                        px=dict(obs0.market["prices"]),
                        act=[ (s.action or {}).get("market") for s in state]))
    r = harness.run_episode(a, b, seed=seed, on_step=on_step)
    return r, rec

if __name__ == "__main__":
    r, rec = probe(BL, BL, seed=1)
    print("final", r["reward"], r["status"])
    for st in (0, 120, 240, 360, 456, 528, 600, 660, 700, 719):
        d = rec[st]
        sh = d["shed"][0]
        tot = sum(sh.values())
        print(f"step {st:3d} money={d['money'][0]:9.0f} shedtot={tot:3d} "
              f"shed={{{', '.join(f'{k}:{v}' for k,v in sh.items() if v)}}}")
    print("PRICES end:", {k: v for k, v in rec[-1]["px"].items()})
    print("INV end:", rec[-1]["inv"])

def prices():
    r, rec = probe(BL, BL, seed=1)
    items = ["WHEAT","STRAWBERRY","MILK","WOOL","MELON","FERTILIZER","CARROT","TOMATO","EGG"]
    print("step " + " ".join(f"{i[:5]:>6}" for i in items) + "   sold0")
    for st in range(0, len(rec), 24):
        d = rec[st]
        print(f"{st:4d} " + " ".join(f"{d['px'][i]:6d}" for i in items))
    print("INV")
    for st in range(0, len(rec), 48):
        d = rec[st]
        print(f"{st:4d} " + " ".join(f"{d['inv'][i]:6d}" for i in items))
