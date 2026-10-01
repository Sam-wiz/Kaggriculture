"""O1 = C1 + 4th quadrant (SE), cash-timed, as a switchable option.

C1 already owns a mature SE executor: V233 (+ VE/SL/VT refinements), which buys SE + 6 sheep at the d11/d12 dawn when
cash covers land + animals + the tape's d11-12 spend + $3k reserve, and runs them with 2 hired hands/day. Natively it is
world-gated (>=2 YARN_STORE, WOOL >= 220). O1 removes that world gate when armed, so SE is bought on cash alone.
  variant 'S': sheep (C1's executor verbatim, gate removed when armed)
  variant 'C': cows  (same executor, 'SHEEP'->'COW', 'WOOL'->'MILK' inside the V233-family blocks only)
Unarmed, variant 'S' is C1 exactly (checked bank-identical by o1_smoke.py). Arm per seat: ns['_O1_ARM'][player] = True.
"""
import contextlib, io

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
C1 = ROOT + "/subY_C1_predict2.py"
GATE = ("    if obs['town']['unlocked_shops'].count('YARN_STORE')<2 or prices['WOOL']<220 or "
        "prices['WHEAT']>45:return False")
GATE_O1 = ("    if (not _O1_ARM.get(int(obs['player'])) and (obs['town']['unlocked_shops'].count('YARN_STORE')<2 or "
           "prices['WOOL']<220)) or prices['WHEAT']>45:return False")
REGIONS = (("V233: bounded, financed six-sheep", "EXP182: finite-harvest wheat/carrot"),
           ("One-worker non-harvest service for the inherited six-sheep", "Claude CARROT2 layer"))
_SRC = {}


def source(variant):
    if variant in _SRC:
        return _SRC[variant]
    src = open(C1).read()
    if variant == "C1":
        _SRC[variant] = src
        return src
    assert src.count(GATE) == 1
    src = src.replace(GATE, GATE_O1)
    if variant in ("C", "G"):
        sp, pr = {"C": ("COW", "MILK"), "G": ("GOOSE", "EGG")}[variant]
        out, inside, n = [], False, 0
        for ln in src.split("\n"):
            if any(a in ln for a, _ in REGIONS):
                inside = True
            if any(b in ln for _, b in REGIONS):
                inside = False
            if inside:
                new = ln.replace("'SHEEP'", "'%s'" % sp).replace("'WOOL'", "'%s'" % pr).replace("SHEEP=0", sp + "=0")
                if variant == "G":
                    new = new.replace("'BUILD_PASTURE'", "'BUILD_COOP'").replace("'PASTURE'", "'COOP'")
                n += new != ln
                ln = new
            out.append(ln)
        assert n >= 25, n
        src = "\n".join(out)
    _SRC[variant] = src
    return src


def load(variant, tag=""):
    """Fresh C1 namespace. variant: 'C1' pristine, 'S' sheep O1, 'C' cow O1, 'G' goose O1 (coops)."""
    ns = {"__name__": "o1_%s_%s" % (variant, tag), "_O1_ARM": {}}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(source(variant), C1, "exec"), ns)
    return ns


def telemetry(ns, farm):
    rep = dict(ns.get("_V233_REPORT", {}))
    se = [farm["tiles"][y][x] for y in range(5, 10) for x in range(5, 10)]
    rep["se_unlocked"] = "SE" in farm["unlocked_quadrants"]
    rep["se_animals"] = sum(isinstance(t, dict) and bool(t.get("animal")) for t in se)
    rep["se_kinds"] = sorted({t.get("animal") for t in se if isinstance(t, dict) and t.get("animal")})
    rep["committed"] = any(s.get("committed") for s in ns.get("_V233_STATES", {}).values())
    return rep
