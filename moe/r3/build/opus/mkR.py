"""Arm R: build hyb2965-side WLV-rebuild candidates by named patches. usage: mkR.py OUT.py patch[,patch...]"""
import sys, re
sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus")
from lib import read_src
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
def sub1(s, a, b):
    assert s.count(a) == 1, (a, s.count(a)); return s.replace(a, b)
def open5(s):      # Fable E2: (5,0) opening -- BUY_PRODUCT WHEAT 5 then BUY_SEED WHEAT 1
    return sub1(s, 'V9_OPENING_STEP0 = (("BUY_PRODUCT", "WHEAT", 20), ("SELL", "WHEAT", 15))', 'V9_OPENING_STEP0 = (("BUY_PRODUCT", "WHEAT", 5),)')
def wllib(s):      # WL family PREDICT library (386fdddb, 1,998 streams) in place of ours
    _, blob, index = read_src(ROOT + "/rivals4/kaggriculture-yummers/_entry.py")
    s = re.sub(r"^_V92_P_BLOB = '[^']*'$", lambda m: "_V92_P_BLOB = '%s'" % blob, s, count=1, flags=re.M)
    return re.sub(r"^_V92_P_INDEX = \[.*\]$", lambda m: "_V92_P_INDEX = %r" % (index,), s, count=1, flags=re.M)
def early(s):     # Gluzdov alternative opening: EarlyCycle (BUY_PRODUCT WHEAT 5 + BUY_SEED WHEAT 1, CT_TABLE off)
    return sub1(s, "_ALT_MODE = 'HybridOpening'\n", "_ALT_MODE = 'EarlyCycle'\n")
def nopg(s):      # drop the step-91 visible-price wheat-sale guard (threshold 31); WLV sells the temp wheat at t=91
    return sub1(s, '            if price < 31:\n                orders=[list(o) for o in action.get("market",[]) if not (len(o)>=3 and o[0]=="SELL" and o[1]=="WHEAT")]',
                   '            if price < 0:\n                orders=[list(o) for o in action.get("market",[]) if not (len(o)>=3 and o[0]=="SELL" and o[1]=="WHEAT")]')
def strip(s):     # WLV wrapper: trailing empty market slots are dropped (leading/internal holes kept)
    return s + """

# ---- arm R (Opus r3): strip trailing empty market slots, as WLV's recorded stream does ----
_RSTRIP_PARENT = agent
def agent(observation, configuration=None):
    action = _RSTRIP_PARENT(observation, configuration)
    try:
        market = list(action.get("market") or [])
        n = len(market)
        while market and market[-1] == []:
            market.pop()
        if len(market) != n:
            action = dict(action, market=market)
    except Exception:
        pass
    return action
"""
def every2(s): return sub1(s, "_V92_P_EVERY = 3\n", "_V92_P_EVERY = 2\n")
def race44(s): return sub1(s, "V9_RACE_DEFAULT = 41\n", "V9_RACE_DEFAULT = 44\n")
def slot8(s):  return sub1(s, "_OR2_SLOT_MARGIN = 20.0\n", "_OR2_SLOT_MARGIN = 8.0\n")
def ca15(s):   return sub1(s, "_CA_MARGIN = -5.0\n", "_CA_MARGIN = -15.0\n")
PATCHES = {k: v for k, v in globals().items() if callable(v) and k not in ("sub1", "read_src")}
if __name__ == "__main__":
    s = open(ROOT + "/subX_hyb2965.py").read()
    for p in sys.argv[2].split(","):
        s = PATCHES[p](s)
    open(sys.argv[1], "w").write(s); print(sys.argv[1], "<-", sys.argv[2])
