"""Price-gate v2: dynamic percentile floors + drip reissue.

For each premium item we track the rolling price distribution seen this game
(deque, ~3 days). The effective floor = max(abs_floor, p60 of window).

Each turn:
  1. suppress emitted SELL orders on premium items priced below floor
     (skipped entirely when cash is short / shed near cap / endgame dump)
  2. drip-feed: append SELL for premium shed stock in free market slots,
     only when price >= floor. Lot size scales with stock so piles drain.

All decisions are additive/reordering-safe: buys are never touched, staple
sells pass through, and any suppression only happens when cash comfortably
covers this turn's buys.
"""
import re
import sys

LAYER = '''
from collections import deque as _dq

_G_ABS=%(abs_floors)s
_G_PCT=%(pct)d          # percentile of recent window used as floor
_G_WIN=%(win)d          # window size in steps
_G_DUMP_DAY=%(dump)d
_G_MARGIN=%(margin)d
_G_SHEDCAP=%(shedcap)d
_G_LOTMAX=%(lotmax)d
_G_PREM=tuple(_G_ABS)
_G_HIST={}
_G_REPORT={"errors":0,"suppressed":0,"dripped":0}

def _g_floor(it):
    h=_G_HIST.get(it)
    if not h: return _G_ABS[it]
    s=sorted(h)
    return max(_G_ABS[it], s[min(len(s)-1,(len(s)*_G_PCT)//100)])

_g_base=agent
def _g_agent(observation,configuration=None):
    a=_g_base(observation,configuration)
    try:
        step=int(observation.get("step") or 0)
        day=step//24
        me=observation["farms"][int(observation["player"])]
        cash=float(me["money"])
        shed=(observation.get("private") or {}).get("shed") or {}
        shed_tot=sum(int(v) for v in shed.values())
        prices=(observation.get("market") or {}).get("prices") or {}
        for it in _G_PREM:
            p=float(prices.get(it,0) or 0)
            if p>0:
                dq=_G_HIST.get(it)
                if dq is None: dq=_G_HIST[it]=_dq(maxlen=_G_WIN)
                dq.append(p)
        m=list((a or {}).get("market") or [])
        # cost of this turn's non-sell orders
        turn_buys=0
        for o in m:
            if o and o[0]!="SELL":
                if o[0]=="BUY_SEED": turn_buys+=80*max(1,int(o[2]) if len(o)>2 else 1)
                elif o[0]=="BUY_ANIMAL": turn_buys+=500*max(1,int(o[2]) if len(o)>2 else 1)
                elif o[0]=="BUY_PRODUCT": turn_buys+=45*max(1,int(o[2]) if len(o)>2 else 1)
                elif o[0]=="BUY_LAND": turn_buys+=4000
                elif o[0]=="HIRE": turn_buys+=150
        liquidate = day>=_G_DUMP_DAY or shed_tot>=_G_SHEDCAP or cash < turn_buys+_G_MARGIN
        kept=[]
        for o in m:
            if (o and o[0]=="SELL" and len(o)>1 and o[1] in _G_ABS
                    and not liquidate
                    and float(prices.get(o[1],0) or 0) < _g_floor(o[1])):
                _G_REPORT["suppressed"]+=1
                continue
            kept.append(o)
        m=kept
        selling={o[1] for o in m if o and o[0]=="SELL" and len(o)>1}
        for it in _G_PREM:
            if len(m)>=10: break
            if it in selling: continue
            have=int(shed.get(it,0) or 0)
            if have<=0: continue
            p=float(prices.get(it,0) or 0)
            ok = p>1 if (liquidate or day>=_G_DUMP_DAY) else p>=_g_floor(it)
            if not ok: continue
            q=min(have,_G_LOTMAX,max(2,have//8))
            m.append(["SELL",it,q]); _G_REPORT["dripped"]+=q
        a=dict(a); a["market"]=m[:10]
    except Exception:
        _G_REPORT["errors"]+=1
    return a
_g_agent.telemetry=_G_REPORT
globals().pop("agent",None)
agent=_g_agent
'''


def main():
    base, out = sys.argv[1], sys.argv[2]
    abs_floors = sys.argv[3] if len(sys.argv) > 3 else \
        '{"MILK":40,"WOOL":90,"STRAWBERRY":110,"MELON":90,"EGG":30}'
    pct = int(sys.argv[4]) if len(sys.argv) > 4 else 60
    win = int(sys.argv[5]) if len(sys.argv) > 5 else 72
    dump = int(sys.argv[6]) if len(sys.argv) > 6 else 27
    margin = int(sys.argv[7]) if len(sys.argv) > 7 else 400
    shedcap = int(sys.argv[8]) if len(sys.argv) > 8 else 85
    lotmax = int(sys.argv[9]) if len(sys.argv) > 9 else 10
    src = open(base).read()
    src += LAYER % {"abs_floors": abs_floors, "pct": pct, "win": win,
                    "dump": dump, "margin": margin, "shedcap": shedcap,
                    "lotmax": lotmax}
    open(out, "w").write(src)
    print("wrote", out)


if __name__ == "__main__":
    main()
