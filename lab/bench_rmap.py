"""Holdout gate: rmap variant vs plain L96 on the REAL engine, both seats."""
import os, sys
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

def kload(path):
    env = {}
    exec(compile(open(path).read(), path, 'exec'), env)
    return env['agent']

def job(args):
    s, sw = args
    a = kload(sys.argv[1]); b = kload(sys.argv[2])
    x, y = (b, a) if sw else (a, b)
    r = harness.run_episode(x, y, seed=s, catch_errors=True)
    p, q = r['reward'][::-1] if sw else r['reward']
    return p, q, r['status']

if __name__ == '__main__':
    start, n = int(sys.argv[3]), int(sys.argv[4])
    jobs = [(s, sw) for s in range(start, start + n) for sw in (0, 1)]
    w = l = t = 0; margins = []; errs = 0
    with ProcessPoolExecutor(max_workers=10) as ex:
        for p, q, st in ex.map(job, jobs):
            if st != ['DONE', 'DONE']: errs += 1
            margins.append(p - q)
            if p > q: w += 1
            elif p < q: l += 1
            else: t += 1
    import statistics
    print(f"{sys.argv[1]} vs {sys.argv[2]}: W{w}-L{l}-T{t} margin={statistics.mean(margins):+.0f} worst={min(margins):+.0f} errs={errs}")
