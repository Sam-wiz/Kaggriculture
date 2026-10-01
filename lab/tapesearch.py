"""Hill-climbing search over the action tape itself.

Every hand-designed change is exhausted: the overlay is squeezed, and no crop substitution works
because the tape's watering/harvest schedule is co-tuned to what it planted. The top players' edge is
purely crop mix (keiz: 119 wheat / 42 carrot / 9 tomato vs our 194/9/0), and carrot only pays if the
tile is ALSO recycled faster (it yields 4 vs wheat's 6 but matures a day sooner). That is a schedule
change, so it has to be searched, not reasoned out.

So: mutate the tape directly and let the mirror benchmark judge. A candidate is the current best tape
plus one mutation, played against the current best over the same seeds, both seats, scored by mean
margin (per MISTAKES C9 -- never win-rate, which is degenerate against a tie).

Cheap screen first, then confirm on a larger seed set, so most bad mutations cost almost nothing.

Usage:  .venv/bin/python tapesearch.py [hours] [workers]
Writes accepted patches to tape_patches.json (resumable).
"""
import sys, os, json, time, random, statistics, importlib.util
from concurrent.futures import ProcessPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
BASE = os.path.join(ROOT, "port3/newtape_impact.py")
PATCHES = os.path.join(ROOT, "tape_patches.json")

SCREEN_SEEDS = list(range(30000, 30006))     # 6 seeds x 2 seats = 12 games
CONFIRM_SEEDS = list(range(31000, 31024))    # 24 seeds x 2 seats = 48 games
ACCEPT = 150.0                                # margin needed to keep a mutation

_UNIT_OPS = ('PASS','NORTH','SOUTH','EAST','WEST','PICKUP','DROP','PLACE','PLANT','WATER',
             'HARVEST','FERTILIZE','DIG','BUILD_COOP','BUILD_PASTURE','FEED',
             'COLLECT_FERTILIZER','CARE')
OP = {n: i for i, n in enumerate(_UNIT_OPS)}
CROP_ARG = {'WHEAT': 0, 'CARROT': 1, 'TOMATO': 2, 'STRAWBERRY': 3, 'MELON': 4}


def load(patches, tag):
    """Load the agent and apply tape patches: (route, step, unit_index, op, arg)."""
    name = "ts_" + tag
    spec = importlib.util.spec_from_file_location(name, BASE)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    for (r, s, u, op, arg) in patches:
        nu, units, no, orders = m._TAPES[r][s]
        if u >= len(units):
            continue
        units = list(units)
        old = units[u]
        units[u] = (op, arg, old[2])
        m._TAPES[r][s] = (nu, units, no, orders)
    fn = [v for v in vars(m).values() if callable(v)][-1]
    return lambda o, c=None: fn(o, c)


def _game(args):
    patches, base_patches, seed, swap = args
    from harness import run_episode
    cand = load(patches, f"c{seed}{swap}")
    ref = load(base_patches, f"r{seed}{swap}")
    x, y = (cand, ref) if not swap else (ref, cand)
    r = run_episode(x, y, seed=seed)["reward"]
    us, them = (r[0], r[1]) if not swap else (r[1], r[0])
    return us - them


def evaluate(ex, patches, base_patches, seeds):
    jobs = [(patches, base_patches, s, sw) for s in seeds for sw in (False, True)]
    d = list(ex.map(_game, jobs))
    return statistics.mean(d)


def sample_mutation(rng, tapes_meta):
    """Propose one edit, weighted toward the action types that plausibly matter."""
    r = rng.randrange(2)
    kind = rng.random()
    plants, idles, harvests = tapes_meta
    if kind < 0.45 and plants:
        s, u, arg = rng.choice(plants[r])
        new = rng.choice([v for k, v in CROP_ARG.items() if v != arg])
        return (r, s, u, OP['PLANT'], new)
    if kind < 0.75 and idles:
        s, u = rng.choice(idles[r])
        op = rng.choice([OP['WATER'], OP['HARVEST'], OP['CARE'], OP['COLLECT_FERTILIZER']])
        return (r, s, u, op, 0)
    if harvests:
        s, u = rng.choice(harvests[r])
        op = rng.choice([OP['WATER'], OP['CARE'], OP['HARVEST'], OP['PASS']])
        return (r, s, u, op, 0)
    return None


def build_meta():
    m = load([], "meta")
    mod = sys.modules["ts_meta"]
    plants, idles, harvests = ([[], []] for _ in range(3))
    for r in range(len(mod._TAPES)):
        for s, (nu, units, no, orders) in enumerate(mod._TAPES[r]):
            for u in range(min(nu, len(units))):
                op, arg, q = units[u]
                if op == OP['PLANT']:
                    plants[r].append((s, u, arg))
                elif op == OP['PASS']:
                    idles[r].append((s, u))
                elif op in (OP['HARVEST'], OP['WATER'], OP['CARE']):
                    harvests[r].append((s, u))
    return plants, idles, harvests


def main():
    hours = float(sys.argv[1]) if len(sys.argv) > 1 else 6.0
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    rng = random.Random(12345)
    meta = build_meta()
    print(f"editable: {len(meta[0][0])} PLANT, {len(meta[1][0])} PASS, "
          f"{len(meta[2][0])} tend actions (route 0)", flush=True)

    best = json.load(open(PATCHES)) if os.path.exists(PATCHES) else []
    best = [tuple(p) for p in best]
    print(f"resuming with {len(best)} accepted patches", flush=True)

    t0 = time.time(); tried = 0; accepted = 0
    with ProcessPoolExecutor(max_workers=workers) as ex:
        null = evaluate(ex, best, best, SCREEN_SEEDS)
        print(f"null control (must be 0.0): {null:+.1f}", flush=True)
        while time.time() - t0 < hours * 3600:
            mut = sample_mutation(rng, meta)
            if mut is None or mut in best:
                continue
            cand = best + [mut]
            tried += 1
            sc = evaluate(ex, cand, best, SCREEN_SEEDS)
            if sc <= 20:
                continue
            cf = evaluate(ex, cand, best, CONFIRM_SEEDS)
            el = (time.time() - t0) / 60
            print(f"  [{el:6.1f}m] tried {tried:4d}  screen {sc:>+8,.0f}  confirm {cf:>+8,.0f}  "
                  f"{mut}", flush=True)
            if cf >= ACCEPT:
                best = cand; accepted += 1
                json.dump([list(p) for p in best], open(PATCHES, "w"))
                print(f"  ==> ACCEPTED #{accepted} (total {len(best)} patches)", flush=True)
    print(f"\ndone: {tried} mutations tried, {accepted} accepted in {(time.time()-t0)/3600:.1f}h",
          flush=True)


if __name__ == "__main__":
    main()
