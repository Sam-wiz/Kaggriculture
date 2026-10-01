import sys, os, json, gzip
sys.argv=[sys.argv[0]]
exec(open('/tmp/opus_r3/exact.py').read().split('if __name__')[0])
opps=json.load(open('/tmp/opus_r3/opps_c.json'))
def selfrep(o, path, tag):
    d=json.load(gzip.open(o['path'],'rt')); acts=d['actions']; me=o['seat']; op=1-me
    ag=load(path, tag); g=kagsim.Game(seed=int(d['seed']))
    for t in range(719):
        theirs = acts[t+1][op] if isinstance(acts[t+1][op],dict) else PASS
        a=ag(g.observe(me))
        if norm(a)!=norm(acts[t+1][me]): return t, json.dumps(a)[:200], json.dumps(acts[t+1][me])[:200]
        g.step(*((a,theirs) if me==0 else (theirs,a)))
    return 719, [g.reward(0), g.reward(1)], d['rewards']
for name in ('Konstantin Zorin','ouga','Max Fofanov','Yin Li'):
    o=[x for x in opps if x['opp']==name][0]
    path={'hyb2965':'subX_hyb2965.py','shepherd':'subW_shepherd.py'}[o['build']]
    print(name, o['build'], 'seat', o['seat'], selfrep(o, path, 'sr'+str(o['ep'])))
