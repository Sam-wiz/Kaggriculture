import sys, os, json, gzip
sys.argv=[sys.argv[0]]
exec(open('/tmp/opus_r3/closed.py').read().split('if __name__')[0])
o=[x for x in json.load(open('/tmp/opus_r3/opps_c.json')) if x['opp']=='Konstantin Zorin'][0]
d=json.load(gzip.open(o['path'],'rt')); acts=d['actions']; me=o['seat']; op=1-me
def norm(a):
    if isinstance(a, dict): return tuple((k, norm(v)) for k, v in sorted(a.items()))
    if isinstance(a, (list, tuple)): return tuple(norm(x) for x in a)
    if isinstance(a, float) and a == int(a): return int(a)
    return a
G='rivals/guruprasaathas111_kaggriculture-master-engine-v3/_entry.py'
for order in ('opp_first','ours_first'):
    if order=='opp_first': b=load(G,'g'+order); a=load('subX_hyb2965.py','h'+order)
    else: a=load('subX_hyb2965.py','h'+order); b=load(G,'g'+order)
    g=kagsim.Game(seed=int(d['seed'])); fo=fm=None
    for t in range(720):
        x=a(g.observe(me)); y=b(g.observe(op))
        if fm is None and t<719 and norm(x)!=norm(acts[t+1][me]): fm=t
        if fo is None and t<719 and norm(y)!=norm(acts[t+1][op]): fo=(t, json.dumps(y)[:150], json.dumps(acts[t+1][op])[:150])
        g.step(*((x,y) if me==0 else (y,x)))
    print(order, 'ours first div', fm, 'opp first div', fo, [g.reward(0),g.reward(1)], d['rewards'])
