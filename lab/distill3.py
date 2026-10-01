"""Distill v3: foreign tape + cash-flow guard.

The tape's buys assume its original game's revenue trajectory. In a new game
sell prices differ -> buys starve -> hires fail -> cascade.

Guard: precompute the tape's upcoming fixed-cost buy schedule; each turn, if
cash < lookahead cost + margin, append SELL orders for shed surplus (keeping
a feed buffer) in free market slots to close the gap.
"""
import gzip
import json
import re
import sys
import zlib
import base64

BASE = "subV_a.py"

GUARD = '''
# ---- cash-flow guard: pre-sell shed surplus to fund upcoming tape buys ----
_CG_SEEDP={"WHEAT":10,"CARROT":20,"TOMATO":50,"STRAWBERRY":100,"MELON":80}
_CG_ANIMP={"GOOSE":300,"COW":400,"SHEEP":500}
_CG_LAND=[1000,2000,4000]
_CG_LOOKAHEAD=%(la)d
_CG_MARGIN=%(margin)d
_CG_FEED=%(feed)d
_CG_TAPE=%(tape)d
_CG_REPORT={"errors":0,"sold":0,"turns":0}

def _cg_cost(o, hires):
    op=o[0]
    try:n=max(1,int(o[2]))
    except Exception:n=1
    if op=="BUY_SEED": return _CG_SEEDP.get(o[1],50)*n
    if op=="BUY_ANIMAL": return _CG_ANIMP.get(o[1],400)*n
    if op=="BUY_PRODUCT": return 40*n
    if op=="HIRE":
        c=0
        for _ in range(n):
            a,b=1,1
            for _ in range(hires): a,b=b,a+b
            c+=a; hires+=1
        return c
    if op=="BUY_LAND": return 1000
    return 0

_CG_SCHED=None
def _cg_build():
    global _CG_SCHED
    tape=_ROUTES[_CG_TAPE]
    _CG_SCHED=[0.0]*(len(tape)+_CG_LOOKAHEAD+2)
    # suffix-sum of estimated buy costs
    for t in range(len(tape)-1,-1,-1):
        c=sum(_cg_cost(o,0) for o in (tape[t].get("market") or []) if o)
        _CG_SCHED[t]=_CG_SCHED[t+1]+c
_cg_build()

_cg_base=agent
def _cg_agent(observation,configuration=None):
    a=_cg_base(observation,configuration)
    try:
        step=int(observation.get("step") or 0)
        me=observation["farms"][int(observation["player"])]
        cash=float(me["money"])
        need=_CG_SCHED[step]-_CG_SCHED[min(step+_CG_LOOKAHEAD,len(_CG_SCHED)-1)]
        gap=need+_CG_MARGIN-cash
        if gap<=0: return a
        shed=(observation["private"] or {}).get("shed") or {}
        m=list((a or {}).get("market") or [])
        prices=(observation.get("market") or {}).get("prices") or {}
        selling={o[1] for o in m if o and o[0]=="SELL" and len(o)>1}
        add=[]
        # sell highest-price shed items first, keep feed buffer of wheat
        order=sorted([p for p in shed if p not in ("WHEAT",)],
                     key=lambda p:-float(prices.get(p,0) or 0))
        order.append("WHEAT")
        for p in order:
            if len(m)+len(add)>=10 or gap<=0: break
            if p in selling: continue
            have=int(shed.get(p,0) or 0)
            if p=="WHEAT": have-=_CG_FEED
            if have<=0: continue
            q=min(have,60)
            add.append(["SELL",p,q])
            gap-=float(prices.get(p,20) or 20)*q
            _CG_REPORT["sold"]+=q
        if add:
            for o in add:
                if len(m)<10: m.append(o)
            _CG_REPORT["turns"]+=1
            a=dict(a); a["market"]=m
    except Exception:
        _CG_REPORT["errors"]+=1
    return a
_cg_agent.telemetry=_CG_REPORT
globals().pop("agent",None)
agent=_cg_agent
'''


def main():
    replay_path, winner_idx, out_path = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    route_id = int(sys.argv[4]) if len(sys.argv) > 4 else 200
    la = int(sys.argv[5]) if len(sys.argv) > 5 else 48
    margin = int(sys.argv[6]) if len(sys.argv) > 6 else 200
    feed = int(sys.argv[7]) if len(sys.argv) > 7 else 20
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
    src += GUARD % {"la": la, "margin": margin, "feed": feed, "tape": route_id}
    open(out_path, "w").write(src)
    print("wrote", out_path, "| team:", d["teams"][winner_idx],
          "| bank:", d["rewards"][winner_idx])


if __name__ == "__main__":
    main()
