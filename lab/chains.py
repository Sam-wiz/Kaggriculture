"""Extract the tape's animal chains: BUY -> PICKUP(unit) -> PLACE(unit).

Livestock reaches a pasture through three species-bound actions. `BUY_ANIMAL X` puts X in the shed;
`PICKUP X` by unit u moves it into that unit's inventory (and takes it from the shed by name); and
`PLACE X` by the same unit puts it on a tile, but only if the unit is standing on an unoccupied
structure of the right kind. FEED and CARE take no argument at all -- they act on whatever animal
occupies the tile -- so they need no changes.

COW and SHEEP share the PASTURE structure, so a pasture tile accepts either. That makes a
cow->sheep conversion a rename of exactly three actions, provided all three are renamed together.
Renaming only the purchase (what I did the first time) leaves the tape running `PICKUP COW` against
a shed holding SHEEP: the pickup finds nothing, the place has nothing to put down, and the farm ends
with one fewer animal and no replacement.
"""
import collections
import importlib.util
import sys

SPECIES = ("COW", "SHEEP", "GOOSE")


def load_router(path="sub_router.py", name="_chainrouter"):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def events(route):
    """Every animal-related action in a route, as (turn, op, species, unit_index)."""
    out = []
    for t, a in enumerate(route):
        for o in (a.get("market") or []):
            if o and o[0] == "BUY_ANIMAL" and len(o) > 1 and o[1] in SPECIES:
                out.append((t, "BUY", o[1], int(o[2]) if len(o) > 2 else 1))
        units = [a.get("farmer")] + list(a.get("hands") or [])
        for i, u in enumerate(units):
            if u and u[0] in ("PICKUP", "PLACE") and len(u) > 1 and u[1] in SPECIES:
                out.append((t, u[0], u[1], i))
    return out


def chains(route):
    """Match each PLACE to the PICKUP by the same unit, and to a preceding BUY of that species.

    Returns a list of dicts, in PLACE order, each naming the three (turn, unit) sites to rewrite.
    """
    ev = events(route)
    picks = collections.defaultdict(list)   # (species, unit) -> [turn]
    buys = collections.defaultdict(list)    # species -> [(turn, qty)]
    out = []
    for t, op, sp, arg in ev:
        if op == "BUY":
            buys[sp].append([t, arg])
        elif op == "PICKUP":
            picks[(sp, arg)].append(t)
        elif op == "PLACE":
            pk = picks.get((sp, arg))
            if not pk:
                out.append(dict(species=sp, unit=arg, place=t, pickup=None, buy=None))
                continue
            p = pk.pop(0)
            b = None
            for rec in buys[sp]:
                if rec[0] <= p and rec[1] > 0:
                    rec[1] -= 1
                    b = rec[0]
                    break
            out.append(dict(species=sp, unit=arg, place=t, pickup=p, buy=b))
    return out


if __name__ == "__main__":
    m = load_router()
    R = m.routes()
    names = {getattr(m, n): n for n in ("MAIN", "YARN", "YARN_CARROT", "MILK_GLUT")}
    for key, route in R.items():
        cs = chains(route)
        done = [c for c in cs if c["pickup"] is not None and c["buy"] is not None]
        print(f"\n=== {names.get(key, key)} : {len(cs)} placements, "
              f"{len(done)} fully matched ===")
        by = collections.Counter(c["species"] for c in cs)
        print("   ", dict(by))
        print(f"    {'species':<8}{'buy':>6}{'pickup':>8}{'place':>7}{'unit':>6}{'buyDay':>8}")
        for c in cs:
            if c["species"] != "COW":
                continue
            b = c["buy"]
            print(f"    {c['species']:<8}{(b if b is not None else -1):>6}"
                  f"{(c['pickup'] if c['pickup'] is not None else -1):>8}"
                  f"{c['place']:>7}{c['unit']:>6}"
                  f"{(b // 24 if b is not None else -1):>8}")
