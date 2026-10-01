"""Paired bench: carrot-boost V48 vs stock V48, split by draw demand."""
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
import carrot_relabel2 as cr


def kload(path):
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


def job(a):
    s, sw, n, lo, hi = a
    m = cr.load_module()
    mod, _ = cr.build_agent(n, lo, hi)
    base = [v for v in vars(m).values() if callable(v)][-1]
    x, y = (base, mod) if sw else (mod, base)
    r = harness.run_episode(x, y, seed=s, catch_errors=True)
    p, q = r["reward"][::-1] if sw else r["reward"]
    # detect first-2-shops: probe obs during a short stock game is overkill;
    # reuse r? just return margin; classify via a cheap second run vs pass
    obs_shops = []
    def spy(step, state, env):
        if step == 144:
            obs_shops.extend(state[0].observation["town"]["unlocked_shops"][:2])
    harness.run_episode(base, "pass", seed=s, catch_errors=True, on_step=spy)
    return s, p - q, tuple(obs_shops)


if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 6100
    nseeds = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 14
    lo = int(sys.argv[4]) if len(sys.argv) > 4 else 10
    hi = int(sys.argv[5]) if len(sys.argv) > 5 else 17
    jobs = [(s, sw, n, lo, hi) for s in range(start, start + nseeds) for sw in (0, 1)]
    rows = []
    with ProcessPoolExecutor(7) as ex:
        for s, d, shops in ex.map(job, jobs, chunksize=2):
            rows.append((s, d, shops))
    gate = [d for s, d, sh in rows if "PET_CAFE" in sh or "FARMERS_MARKET" in sh]
    other = [d for s, d, sh in rows if not ("PET_CAFE" in sh or "FARMERS_MARKET" in sh)]
    def stat(ms, tag):
        w = sum(1 for m in ms if m > 0)
        l = sum(1 for m in ms if m < 0)
        print("%-10s n=%d W%d-L%d margin=%+.0f" % (tag, len(ms), w, l,
              sum(ms) / len(ms) if ms else 0))
    stat(gate, "pet/FM")
    stat(other, "other")
    stat([d for _, d, _ in rows], "ALL")
    for s, d, sh in sorted(rows):
        print("  seed", s, sh, "%+.0f" % d)
