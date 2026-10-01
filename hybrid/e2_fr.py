"""boatlee v29 tape with its dormant front-run overlay switched on (per-item)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _base
_M = _base.load("boatlee29", "e2")
P = dict(fr_items=["STRAWBERRY", "MILK", "WOOL", "FERTILIZER", "MELON", "CARROT", "TOMATO", "EGG"])
def agent(obs):
    _M._FR_ITEMS = tuple(P["fr_items"])
    return _M.agent(obs)
