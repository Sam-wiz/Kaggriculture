import sys, os, json, gzip
sys.argv=[sys.argv[0]]
exec(open('/tmp/opus_r3/exact.py').read().split('if __name__')[0])
lib=json.load(open('/tmp/opus_r3/libopen.json'))
opps=json.load(open('/tmp/opus_r3/opps_c.json'))
def show(o, cname, upto=6):
    d=json.load(gzip.open(o['path'],'rt')); acts=d['actions']; opp=1-o['seat']; me=o['seat']
    ag=load(lib[cname][0], "dv%d"%o['ep'])
    g=kagsim.Game(seed=int(d['seed'])); n=0; steps=[]
    for t in range(719):
        ours = acts[t+1][me] if isinstance(acts[t+1][me],dict) else PASS
        a=ag(g.observe(opp)); r=acts[t+1][opp]
        if norm(a)!=norm(r):
            steps.append(t)
            if n<upto: print(f"  {o['opp'][:14]} t={t}\n    lib={json.dumps(a)[:200]}\n    rec={json.dumps(r)[:200]}")
            n+=1
            a=r
        g.step(*((ours,a) if opp==1 else (a,ours)))
    print('  total divergent steps', n, 'first 20:', steps[:20])
for o in opps:
    if o['opp']=='J.Moriuchi': show(o,'ours/subM_pipe16clamp.py',3)
    if o['opp']=='ouga': show(o,'rivals4/kaggriculture-yummers',0)
