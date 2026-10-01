"""Add the price-gate layer to a submission file.

Outermost layer. For each emitted SELL on a premium item:
  - pass through if price >= floor, OR day >= DUMP_DAY, OR shed nearly full,
    OR cash cannot cover the tape's upcoming fixed buys + margin.
  - otherwise drop the order (stock stays in shed) and let the drip-feeder
    resell it in small lots when the price recovers.

The drip-feeder appends SELL orders in free market slots for premium shed
stock whenever price >= floor (same floors as the gate). Lots are capped small
because fills reprice per unit -- a 20-unit dump walks its own price down.
"""
import re
import sys

LAYER = '''
# ---- price gate + drip feeder (premium sells only) ----
_G_FLOOR=%(floors)s
_G_DUMP_DAY=%(dump)d
_G_MARGIN=%(margin)d
_G_SHEDCAP=%(shedcap)d
_G_LOT=%(lot)d
_G_SEEDP={"WHEAT":10,"CARROT":20,"TOMATO":50,"STRAWBERRY":100,"MELON":80}
_G_ANIMP={"GOOSE":300,"COW":400,"SHEEP":500}
_G_PREM=tuple(_G_FLOOR)
_G_REPORT={"errors":0,"suppressed":0,"dripped":0,"turns":0}

def _g_cost(o, hires):
    op=o[0]
    try:n=max(1,int(o[2]))
    except Exception:n=1
    if op=="BUY_SEED": return _G_SEEDP.get(o[1],50)*n
    if op=="BUY_ANIMAL": return _G_ANIMP.get(o[1],400)*n
    if op=="BUY_PRODUCT": return 40*n
    if op=="BUY_LAND": return 4000
    if op=="HIRE":
        a,b=1,1
        for _ in range(hires): a,b=b,a+b
        return a
    return 0

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
        m=list((a or {}).get("market") or [])
        hires=int(me.get("hires_today",0) or 0)
        # upcoming buy cost in next ~12 steps of THIS turn's order list only
        # (cheap proxy: sum this-turn buys; sells are what we are judging)
        turn_buys=0
        hh=hires
        for o in m:
            if o and o[0]!="SELL":
                turn_buys+=_g_cost(o,hh)
                if o[0]=="HIRE": hh+=1
        liquidate = day>=_G_DUMP_DAY or shed_tot>=_G_SHEDCAP or cash < turn_buys+_G_MARGIN
        kept=[]; suppressed=[]
        for o in m:
            if (o and o[0]=="SELL" and len(o)>1 and o[1] in _G_FLOOR
                    and not liquidate
                    and float(prices.get(o[1],0) or 0) < _G_FLOOR[o[1]]):
                suppressed.append(o); _G_REPORT["suppressed"]+=1
                continue
            kept.append(o)
        m=kept
        # drip feeder: resell premium stock at good prices in free slots
        if not liquidate or day>=_G_DUMP_DAY:
            selling={o[1] for o in m if o and o[0]=="SELL" and len(o)>1}
            for it in _G_PREM:
                if len(m)>=10: break
                if it in selling: continue
                p=float(prices.get(it,0) or 0)
                ok = p>=_G_FLOOR[it] if day<_G_DUMP_DAY else p>1
                if not ok: continue
                have=int(shed.get(it,0) or 0)
                if have<=0: continue
                q=min(have,_G_LOT)
                m.append(["SELL",it,q]); _G_REPORT["dripped"]+=q
        if m is not (a or {}).get("market"):
            _G_REPORT["turns"]+=1
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
    floors = sys.argv[3] if len(sys.argv) > 3 else \
        '{"MILK":70,"WOOL":150,"STRAWBERRY":135,"MELON":150}'
    dump = int(sys.argv[4]) if len(sys.argv) > 4 else 27
    margin = int(sys.argv[5]) if len(sys.argv) > 5 else 300
    shedcap = int(sys.argv[6]) if len(sys.argv) > 6 else 85
    lot = int(sys.argv[7]) if len(sys.argv) > 7 else 8
    src = open(base).read()
    src += LAYER % {"floors": floors, "dump": dump, "margin": margin,
                    "shedcap": shedcap, "lot": lot}
    open(out, "w").write(src)
    print("wrote", out)


if __name__ == "__main__":
    main()
