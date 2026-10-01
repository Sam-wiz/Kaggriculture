"""Distill v2: foreign tape + arbitrage cash overlay.

Same as distill.py but appends an overlay layer that:
- days 0..ARB_BUY_DAYS: adds BUY_PRODUCT WHEAT in free market slots while
  cash > ARB_MIN_CASH (fixed buy price; feeds the arbitrage float + feed)
- all days: adds SELL WHEAT / SELL FERTILIZER of shed surplus (above
  FEED_BUFFER) in free slots — monetizes the float at market prices
"""
import gzip
import json
import re
import sys
import zlib
import base64

BASE = "subV_a.py"

OVERLAY = '''
_ARB_MIN_CASH = %(mincash)d
_ARB_BUY_END = %(buyend)d
_ARB_FEED = %(feed)d
_ARB_REPORT = {"errors":0,"bought":0,"sold_w":0,"sold_f":0}
_arb_base = agent

def _arb_agent(observation, configuration=None):
    a=_arb_base(observation, configuration)
    try:
        step=int(observation.get("step") or 0)
        day=step//24
        me=observation["farms"][int(observation["player"])]
        cash=float(me["money"])
        shed=(observation["private"] or {}).get("shed") or {}
        m=list((a or {}).get("market") or [])
        if len(m)>=10: return a
        add=[]
        havew=int(shed.get("WHEAT",0) or 0)
        havef=int(shed.get("FERTILIZER",0) or 0)
        prices=(observation.get("market") or {}).get("prices") or {}
        # sell surplus wheat (keep feed buffer) and fertilizer
        if havew>_ARB_FEED and "WHEAT" not in {o[1] for o in m if o and o[0]=="SELL"}:
            add.append(["SELL","WHEAT",havew-_ARB_FEED])
        if havef>2 and "FERTILIZER" not in {o[1] for o in m if o and o[0]=="SELL"}:
            add.append(["SELL","FERTILIZER",havef])
        # buy arbitrage wheat while young and liquid
        if day<=_ARB_BUY_END and cash>_ARB_MIN_CASH:
            room=min(10-len(m)-len(add),3)
            for _ in range(room):
                q=int(min(60,(cash-_ARB_MIN_CASH)/12))
                if q<=0: break
                add.append(["BUY_PRODUCT","WHEAT",q])
                cash-=q*12; _ARB_REPORT["bought"]+=q
        if add:
            for o in add:
                if len(m)<10: m.append(o)
            _ARB_REPORT["sold_w"]+=sum(o[2] for o in add if o[0]=="SELL" and o[1]=="WHEAT")
            _ARB_REPORT["sold_f"]+=sum(o[2] for o in add if o[0]=="SELL" and o[1]=="FERTILIZER")
            a=dict(a); a["market"]=m
    except Exception:
        _ARB_REPORT["errors"]+=1
    return a

_arb_agent.telemetry=_ARB_REPORT
globals().pop("agent",None)
agent=_arb_agent
'''


def main():
    replay_path, winner_idx, out_path = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    route_id = int(sys.argv[4]) if len(sys.argv) > 4 else 200
    mincash = int(sys.argv[5]) if len(sys.argv) > 5 else 1200
    buyend = int(sys.argv[6]) if len(sys.argv) > 6 else 5
    feed = int(sys.argv[7]) if len(sys.argv) > 7 else 25
    d = json.load(gzip.open(replay_path))
    stream = [a[winner_idx] for a in d["actions"]]
    tape = []
    for a in stream:
        if not isinstance(a, dict):
            a = {}
        tape.append({
            "farmer": a.get("farmer") or ["PASS"],
            "hands": [h for h in (a.get("hands") or [])],
            "market": [list(o) for o in (a.get("market") or [])],
        })
    while len(tape) < 719:
        tape.append({"farmer": ["PASS"], "hands": [], "market": []})

    blob = base64.b85encode(zlib.compress(
        json.dumps(tape, separators=(",", ":")).encode())).decode()
    src = open(BASE).read()
    src = src.replace(
        "_SETTINGS={'hand_align':",
        f"\n_ROUTES[{route_id}]=json.loads(zlib.decompress(base64.b85decode('{blob}')))\n_SETTINGS={{'hand_align':",
        1)
    src = re.sub(
        r"def _router\(observation,step,state\):.*?\n    return state\.get\('route',0\)",
        "def _router(observation,step,state):\n    return %d" % route_id,
        src, count=1, flags=re.S)
    src += OVERLAY % {"mincash": mincash, "buyend": buyend, "feed": feed}
    open(out_path, "w").write(src)
    print("wrote", out_path, "| team:", d["teams"][winner_idx],
          "| bank:", d["rewards"][winner_idx])


if __name__ == "__main__":
    main()
