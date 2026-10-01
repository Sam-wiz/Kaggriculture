"""Genome policy plumbing for the GRPO-style search.

The "policy" is a distribution over season-spec genomes anchored on a
center genome. islandga.mutate() is the sampling kernel; the update is
an advantage-weighted per-block vote (see train.py).

Two bounded patches to islandga's search space, applied at import:

* ANIMALS[].max_held is the compiler's per-species herd cap (4/6/6),
  which makes DSM-scale herds (C11/S8/G6) inexpressible. The engine's
  real max_held is a per-TILE product cap, not a species count cap, so
  lifting it here only widens what a genome may ask for; the engine
  still enforces tile-level rules.
* BOUNDS gets a wider plateau range (8-18 hands/day) — a paid hand is
  ~$fib/day and at scale extra hands are affordable.
"""
import copy
import json

from islandga.genome import BOUNDS, gid_of, mutate, crossover, make_species  # noqa: F401
from islandga.compiler import compile_spec
import islandga.engine_facts as ef
import islandga.genome as gmod

# ---- widen the search space (compile-time caps only; engine unchanged) ----
ef.ANIMALS["COW"]["max_held"] = 14
ef.ANIMALS["SHEEP"]["max_held"] = 10
ef.ANIMALS["GOOSE"]["max_held"] = 8
gmod.BOUNDS["plateau"] = (6, 18)
gmod.BOUNDS["ramp_full"] = (3, 12)
gmod.BOUNDS["ne"] = (3, 9)
gmod.BOUNDS["sw"] = (7, 13)
gmod.BOUNDS["se"] = (10, 16)
gmod.BOUNDS["tomato_day"] = (6, 20)


def normalize(g):
    """Deep-copied, schema-coerced genome."""
    g = copy.deepcopy(g)
    g.pop("gid", None)   # bookkeeping key must not enter gid_of's hash
    g["ne"] = int(g.get("ne") or 6)
    g["sw"] = int(g.get("sw") or 10)
    se = g.get("se")
    g["se"] = None if se in (None, 0, 99) else int(se)
    g["plateau"] = int(g.get("plateau") or 12)
    g["ramp_full"] = int(g.get("ramp_full") or 8)
    g["tomato_day"] = int(g.get("tomato_day") or 8)
    g["melon2"] = int(bool(g.get("melon2", 1)))
    g["sellpol"] = g.get("sellpol") if g.get("sellpol") in (
        "daily", "sweep", "hybrid") else "hybrid"
    g["herd"] = [[int(w[0]), str(w[1]), int(w[2])]
                 for w in (g.get("herd") or []) if len(w) >= 3]
    g["prog"] = {q: {c: int(n) for c, n in (alloc or {}).items()
                     if int(n) > 0}
                 for q, alloc in (g.get("prog") or {}).items()}
    for q in ("NW", "NE", "SW", "SE"):
        g["prog"].setdefault(q, {})
    return g


def compile_genome(g):
    """Validity check + compile. Returns blueprint or raises."""
    return compile_spec(normalize(g))


def is_valid(g):
    try:
        bp = compile_genome(g)
        return isinstance(bp, dict) and isinstance(bp.get("market"), dict) \
            and isinstance(bp.get("days"), dict)
    except Exception:
        return False


# ---------------------------------------------------------------- blocks
# Coherent subsystems (same decomposition as islandga.crossover: crops,
# labour and cash are co-adapted through shared hands and the shared
# pocket, so blocks travel together).
BLOCKS = [
    ("land",   (("ne",), ("sw",), ("se",))),
    ("labor",  (("plateau",), ("ramp_full",))),
    ("herd",   (("herd",),)),
    ("market", (("tomato_day",), ("melon2",), ("sellpol",))),
    ("progNW", (("prog", "NW"),)),
    ("progNE", (("prog", "NE"),)),
    ("progSW", (("prog", "SW"),)),
    ("progSE", (("prog", "SE"),)),
]


_MISSING = object()


def _get(g, path):
    v = g
    for k in path:
        if not isinstance(v, dict) or k not in v:
            return _MISSING
        v = v[k]
    return v


def _set(g, path, val):
    if len(path) == 1:
        g[path[0]] = copy.deepcopy(val)
    else:
        g.setdefault(path[0], {})
        g[path[0]][path[1]] = copy.deepcopy(val)


def block_vote(anchor, members, weights, rng):
    """Build the next anchor: for each coherent block, copy the block of
    member i with probability proportional to weights[i]. members[0] must
    be the anchor (its blocks are the status quo)."""
    child = normalize(anchor)
    for _name, paths in BLOCKS:
        i = rng.choices(range(len(members)), weights=weights, k=1)[0]
        src = members[i]
        for p in paths:
            v = _get(src, p)
            if v is not _MISSING:
                _set(child, p, v)   # copies se=None too (a real choice)
    return child
