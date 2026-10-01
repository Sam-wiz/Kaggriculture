"""Index our own cached live episodes: build, seat, opponent, opponent rating, rewards, seed, path.

Full replays keep info/rewards before the bulky `steps` key (keys are alphabetical), so we parse only
the head of each file. Writes moe/opus/eps_index.json.
"""
import glob, gzip, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
own = {int(k): v for k, v in json.load(open('live_eps/own.json')).items()}
lb = json.load(open('live_eps/lb_now.json'))
ME = 'Sam-wiz'
rows = {}

for p in sorted(glob.glob('live_eps/replays/*.json')):
    with open(p, 'rb') as f:
        head = f.read(200_000).decode('utf-8', 'ignore')
    i = head.find('"specification"')
    head = head[:i] if i > 0 else head
    m_info = re.search(r'"info": (\{.*?\}), "module_version"', head)
    m_rew = re.search(r'"rewards": \[([^\]]*)\]', head)
    if not (m_info and m_rew):
        print('skip', p); continue
    info = json.loads(m_info.group(1))
    ep = info['EpisodeId']; t = info['TeamNames']
    if ep not in own or ME not in t or t[0] == t[1]:
        continue
    rew = [float(x) if x.strip() not in ('null', 'None') else None for x in m_rew.group(1).split(',')]
    me = t.index(ME)
    rows[ep] = dict(ep=ep, build=own[ep], seat=me, opp=t[1 - me], R=lb.get(t[1 - me]),
                    ours=rew[me], theirs=rew[1 - me], seed=info.get('seed'), path=p, kind='full')

for p in sorted(glob.glob('mine/opp/*.json.gz')):
    ep = int(os.path.basename(p).split('.')[0])
    if ep not in own or ep in rows:
        continue
    try:
        d = json.load(gzip.open(p, 'rt'))
    except Exception:
        continue
    t = d.get('teams') or []
    if ME not in t or t[0] == t[1] or not d.get('rewards'):
        continue
    me = t.index(ME)
    rows[ep] = dict(ep=ep, build=own[ep], seat=me, opp=t[1 - me], R=lb.get(t[1 - me]),
                    ours=d['rewards'][me], theirs=d['rewards'][1 - me], seed=d.get('seed'),
                    path=p, kind='reduced')

out = sorted(rows.values(), key=lambda r: r['ep'])
json.dump(out, open('moe/opus/eps_index.json', 'w'), indent=0)
import collections
print(len(out), 'own episodes indexed;', collections.Counter(r['kind'] for r in out))
band = [r for r in out if r['R'] and 2400 <= r['R'] < 2900 and r['ours'] is not None]
print('vs 2400-2900:', len(band))
for b in sorted(set(r['build'] for r in band)):
    g = [r for r in band if r['build'] == b]
    w = sum(1 if r['ours'] > r['theirs'] else .5 if r['ours'] == r['theirs'] else 0 for r in g)
    print(f"  {b:12s} n={len(g):3d} W={w:5.1f} wr={w/len(g):.2f}  losses={sum(r['ours']<r['theirs'] for r in g)}")
