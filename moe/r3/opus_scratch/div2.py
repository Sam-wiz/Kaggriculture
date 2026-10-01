import sys, os, json, gzip
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0,ROOT)
import harness, importlib.util, signal
exec(open('/tmp/opus_r3/exact.py').read().split('if __name__')[0].split('import kagsim')[1])
lib=json.load(open('/tmp/opus_r3/libopen.json'))
opps=json.load(open('/tmp/opus_r3/opps_c.json'))
o=[x for x in opps if x['opp']=='ouga'][0]
d=json.load(gzip.open(o['path'],'rt')); acts=d['actions']; opp=1-o['seat']; me=o['seat']
def tape(seat):
    def ag(obs):
        t=obs['step']+1; a=acts[t][seat] if t<len(acts) else None
        return a if isinstance(a,dict) else PASS
    return ag
for cname, seat, label in [('rivals/a-wonderful-life',opp,'lib-in-opp-seat'),('ours/subW_shepherd.py',me,'shepherd-in-our-seat')]:
    ag=load(lib[cname][0],'pe'+label.replace('-','_'))
    first=[None]
    def wrap(obs):
        a=ag(obs); t=obs['step']
        if first[0] is None and norm(a)!=norm(acts[t+1][seat]): first[0]=(t, json.dumps(a)[:150], json.dumps(acts[t+1][seat])[:150])
        return a
    pair=(wrap,tape(1-seat)) if seat==0 else (tape(1-seat),wrap)
    r=harness.run_episode(pair[0],pair[1],seed=d['seed'])
    print(label,'first divergence:',first[0],'rewards',r['reward'],'recorded',d['rewards'])
