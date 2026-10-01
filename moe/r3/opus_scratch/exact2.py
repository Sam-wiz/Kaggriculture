import sys, os, json, gzip
_ARGV=list(sys.argv); sys.argv=[sys.argv[0]]
exec(open('/tmp/opus_r3/exact.py').read().split('if __name__')[0])
from concurrent.futures import ProcessPoolExecutor
if __name__=="__main__":
    cands=dict(a.split('=',1) for a in _ARGV[2:]); minR=float(_ARGV[1])
    opps=json.load(open('/tmp/opus_r3/opps_c.json'))
    jobs=[]
    for o in opps:
        if (o['R'] or 0)<minR or o['uid']<0.6: continue
        d=json.load(gzip.open(o['path'],'rt'))
        for c,p in cands.items(): jobs.append((o['ep'],c,p,d['seed'],1-o['seat'],d['actions']))
    print(len(jobs),'jobs',flush=True)
    res={}
    with ProcessPoolExecutor(max_workers=2) as ex:
        for ep,name,t,rw in ex.map(work, jobs, chunksize=1): res.setdefault(ep,[]).append((t,name,rw))
    for o in opps:
        if o['ep'] in res:
            b=sorted(res[o['ep']],key=lambda x:-x[0])
            print(f"R={o['R']:.0f} {o['opp'][:18]:18} {o['build'][:4]} m={o['m']:+6.0f} "+"; ".join(f"{n}@{t}" for t,n,_ in b), flush=True)
    json.dump({str(k):v for k,v in res.items()},open('/tmp/opus_r3/exact2_out.json','w'))
