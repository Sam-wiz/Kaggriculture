import sys, os
sys.path.insert(0, '.')
from multiprocessing import Pool
import harness

def job(t):
    a, b, seed = t
    ra, rb, r = harness.play(a, b, seed=seed)
    return {'a': a, 'b': b, 'seed': seed, 'ra': ra, 'rb': rb,
            'status': r['status'], 'err': r['errors']}

def match(agent_a, agent_b, seeds, workers=4):
    jobs = []
    for s in seeds:
        jobs.append((agent_a, agent_b, s))
        jobs.append((agent_b, agent_a, s))
    with Pool(workers) as p:
        recs = p.map(job, jobs)
    wa = wb = t = 0
    margin_a = []
    for r in recs:
        # normalize back to agent_a's perspective
        if r['a'] == agent_a:
            sa, sb = r['ra'], r['rb']
        else:
            sa, sb = r['rb'], r['ra']
        margin_a.append(sa - sb)
        if r['status'][0] == 'ERROR' and r['a'] == agent_a or r['status'][1] == 'ERROR' and r['b'] == agent_a:
            pass
        if sa > sb: wa += 1
        elif sb > sa: wb += 1
        else: t += 1
        print(f"seed {r['seed']:5d} {os.path.basename(r['a']):>22} {r['ra']:8.0f}  vs  {r['rb']:8.0f} {os.path.basename(r['b']):<22} status={r['status']} err={[e for e in r['err'] if e]}")
    avg = sum(margin_a) / len(margin_a)
    print(f"\n{os.path.basename(agent_a)} vs {os.path.basename(agent_b)}: W{wa}-L{wb}-T{t}  avg margin {avg:+.0f}")
    return wa, wb, t, margin_a

if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]
    s0 = int(sys.argv[3]); s1 = int(sys.argv[4])
    match(a, b, range(s0, s1 + 1))
