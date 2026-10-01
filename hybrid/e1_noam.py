"""boatlee v29 tape with its adaptive-market overlay switched off."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _base
_M = _base.load("boatlee29", "e1")
_M._adaptive_market = lambda action, obs, step: action
P = {}
def agent(obs):
    return _M.agent(obs)
