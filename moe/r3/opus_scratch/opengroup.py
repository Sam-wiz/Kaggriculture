import json, gzip, collections
lib=json.load(open('/tmp/opus_r3/libopen.json'))
opps=json.load(open('/tmp/opus_r3/opps.json'))
def norm(a):
    if isinstance(a, dict): return [[k, norm(v)] for k, v in sorted(a.items())]
    if isinstance(a, (list, tuple)): return [norm(x) for x in a]
    if isinstance(a, float) and a == int(a): return int(a)
    return a
# group library by first action (step 0 reply) only market part
def key0(sig):
    s=json.loads(sig); return json.dumps(s[0])
groups=collections.defaultdict(list)
for n,(p,sig) in lib.items():
    if sig.startswith('ERR'): continue
    groups[key0(sig)].append(n)
res=[]
for o in opps:
    d=json.load(gzip.open(o['path'],'rt')); op=1-o['seat']
    k=json.dumps(norm(d['actions'][1][op]))
    c=groups.get(k,[])
    o['cands']=c; res.append(o)
    print(f"R={o['R']:.0f} {o['opp'][:18]:18} m={o['m']:+6.0f} uid={o['uid']} ncand={len(c)} {[x.split('/')[-1][:28] for x in c[:4]]}")
json.dump(res,open('/tmp/opus_r3/opps_c.json','w'))
