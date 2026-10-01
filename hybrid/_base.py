"""Load a private copy of a rival tape module.

Each caller passes its own `tag`, so two hybrid variants running inside one
process never share the tape module's globals (_WEED_STATE, _AM_STATE, ...).
"""
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAPES = {
    "boatlee29": os.path.join(ROOT, "rivals/boatlee_v29-r1-adaptive-market-hysteresis/main.py"),
    "yhay81": os.path.join(ROOT, "rivals/yhay81_fieldbook-commit-for-three-days/main.py"),
}


def load(tape, tag):
    name = "_hybtape_%s_%s" % (tape, tag)
    mod = sys.modules.get(name)
    if mod is not None:
        return mod
    spec = importlib.util.spec_from_file_location(name, TAPES[tape])
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod
