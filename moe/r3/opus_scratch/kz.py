import sys, os, json, gzip
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0,ROOT)
import harness, importlib.util, signal
exec(open('/tmp/opus_r3/exact.py').read().split('if __name__')[0].split('import kagsim')[1])
o=[x for x in json.load(open('/tmp/opus_r3/opps_c.json')) if x['opp']=='Konstantin Zorin'][0]
d=json.load(gzip.open(o['path'],'rt')); acts=d['actions']; me=o['seat']
def tape(seat):
    def ag(obs):
        t=obs['step']+1; a=acts[t][seat] if t<len(acts) else None
        return a if isinstance(a,dict) else PASS
    return ag
for trial in range(2):
    ag=load('subX_hyb2965.py','kz%d'%trial); first=[None]
    def wrap(obs):
        a=ag(obs); t=obs['step']
        if first[0] is None and norm(a)!=norm(acts[t+1][me]): first[0]=(t, json.dumps(a)[:260], json.dumps(acts[t+1][me])[:260])
        return a
    pair=(wrap,tape(1-me)) if me==0 else (tape(1-me),wrap)
    r=harness.run_episode(pair[0],pair[1],seed=d['seed'])
    print('trial',trial,'seat',me,'first divergence:',first[0],'rewards',r['reward'],'recorded',d['rewards'])
