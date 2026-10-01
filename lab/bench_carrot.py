"""Paired bench: carrot-relabel V48 vs stock V48, on seeds bucketed by pet count."""
import collections
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness


def kload(path):
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


def job(arg):
    seed, n_rel, sw = arg
    import carrot_relabel
    base = kload("rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py")
    mod, _ = carrot_relabel.build_agent(n_rel)
    pets = collections.Counter()
    def on_step(step, state, env):
        pets.clear(); pets.update(state[0].observation["town"]["unlocked_shops"])
    x, y = (base, mod) if sw else (mod, base)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True, on_step=on_step)
    # sw=0 -> seats (mod,base) -> reward [mod,base]; sw=1 -> seats (base,mod) -> [base,mod]
    p, q = r["reward"][::-1] if sw else r["reward"]
    return seed, pets.get("PET_CAFE", 0), p, q


if __name__ == "__main__":
    n_rel = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
    nseeds = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    args = [(s, n_rel, sw) for s in range(start, start + nseeds) for sw in (0, 1)]
    rows = list(ProcessPoolExecutor(7).map(job, args))
    bypet = {}
    tot = [0, 0, 0.0]
    for seed, pet, p, q in rows:
        bypet.setdefault(pet, []).append(p - q)
        tot[0] += p > q
        tot[1] += p < q
        tot[2] += p - q
    for pet in sorted(bypet):
        v = bypet[pet]
        print("pet=%d n=%2d  mean mod-base margin=%+8.0f  (mod wins %d)" %
              (pet, len(v), sum(v) / len(v), sum(1 for x in v if x > 0)))
    print("TOTAL: mod %dW-%dL  mean margin %+.0f over %d paired games"
          % (tot[0], tot[1], tot[2] / len(rows), len(rows)))
