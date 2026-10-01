"""One descriptive event-signature test. Future endpoint is outcome ONLY.
First 20 episode IDs in existing bc2s DSM; no tuning or predictive fit.
Contiguous moves ending in successful service before dawn; distance>=3.
Compare dawn-ready, rarest-type and quadrant-backlog hypotheses on identical trips.
"""
import json,gzip,time,collections,pathlib
START=time.time(); ROOT=pathlib.Path('mine/rawkeep'); OUT=pathlib.Path('moe/r7/build/astra')
MOVE={'NORTH':(0,-1),'SOUTH':(0,1),'EAST':(1,0),'WEST':(-1,0)}
MAP={'WATER':'water','FEED':'feed','CARE':'care','COLLECT_FERTILIZER':'cfert','HARVEST':'harvest','DIG':'dig'}
DAILY={'water','feed','care','cfert'}
def jobs(obs,pi):
    ans={k:set() for k in MAP.values()}
    for yy,row in enumerate(obs['farms'][pi]['tiles']):
        for xx,t in enumerate(row):
            if not isinstance(t,dict):continue
            p=(xx,yy); kind=t.get('kind')
            if kind=='WEED':ans['dig'].add(p)
            if kind=='PLANT':
                if not t.get('watered_today'):ans['water'].add(p)
                if t.get('yield_units',0)>0:ans['harvest'].add(p)
            if kind in ('COOP','PASTURE') and t.get('animal'):
                if not t.get('fed_today'):ans['feed'].add(p)
                if not t.get('cared_today'):ans['care'].add(p)
                if t.get('fertilizer_available'):ans['cfert'].add(p)
                if t.get('yield_units',0)>0:ans['harvest'].add(p)
    return ans

def pos(o,pi,u):
    m=o['farms'][pi]; p=[m['farmer']]+m.get('hands',[])
    return tuple(p[u]) if u<len(p) else None

def op(s,pi,u):
    a=s[pi].get('action') or {}; ops=[a.get('farmer')]+(a.get('hands') or [])
    return ops[u][0] if u<len(ops) and ops[u] else 'ABSENT'

def quad(p):return (p[0]//5,p[1]//5)
def dist(a,b):return abs(a[0]-b[0])+abs(a[1]-b[1])
ids=[]
with open('moe/r7/build/opus/bc2s_DSM.jsonl') as f:
    for l in f:
        ep=json.loads(l)['ep']
        if ep not in ids:ids.append(ep)
        if len(ids)==20:break
S=collections.defaultdict(collections.Counter); rows=[]
for ep in ids:
    data=json.load(gzip.open(ROOT/f'{ep}.json.gz','rt')); pi=data['info']['TeamNames'].index('DSM'); ss=data['steps']
    obs=[s[pi].get('observation') or {} for s in ss]
    jj=[jobs(o,pi) if o else {} for o in obs]
    dawn={}
    for t in range(1,len(ss)):
        o=obs[t-1]
        if not o:continue
        day=o['day']; hour=o['hour']; J=jj[t-1]
        if hour==0:dawn[day]=J
        if day not in dawn:continue
        DJ=dawn[day]
        units=[o['farms'][pi]['farmer']]+o['farms'][pi].get('hands',[])
        for u,p0 in enumerate(units):
            p0=tuple(p0); a=op(ss[t],pi,u)
            if a not in MOVE:continue
            invs=(o.get('private') or {}).get('inventories') or []
            inv=invs[u] if u<len(invs) else {}
            F={k:ps for k,ps in J.items() if k!='feed' or inv.get('WHEAT',0)>0}
            allp=set().union(*F.values())
            # Audit metric on every move with work, including equal-distance alternatives.
            away=allp-{p0}
            if away:
                md=min(dist(p0,p) for p in away); near={p for p in away if dist(p0,p)==md}
                dx,dy=MOVE[a]; p1=(p0[0]+dx,p0[1]+dy)
                S['all_moves']['n']+=1
                S['all_moves']['toward_any_nearest']+=any(dist(p1,p)<md for p in near)
            if t>1 and obs[t-2].get('day')==day and op(ss[t-1],pi,u) in MOVE:continue
            S['starts']['n']+=1
            end=t
            while end<len(ss) and obs[end-1].get('day')==day and op(ss[end],pi,u) in MOVE:end+=1
            if end>=len(ss) or obs[end-1].get('day')!=day:
                S['starts']['censored_dawn_or_end']+=1;continue
            k=MAP.get(op(ss[end],pi,u)); target=pos(obs[end-1],pi,u)
            if not k or target is None:
                S['starts']['other_endpoint']+=1;continue
            # Diagnostic endpoint must be feasible just before service AND at departure.
            if target not in jj[end-1].get(k,set()):
                S['starts']['invalid_endpoint']+=1;continue
            if target not in F.get(k,set()):
                S['starts']['not_ready_departure']+=1;continue
            if p0 not in allp:continue
            d=dist(p0,target); group='distant' if d>=3 else 'short'
            C=S[group];C['n']+=1
            C['ready_dawn']+=target in DJ[k]
            counts={a:len(ps) for a,ps in F.items() if ps}
            rare={a for a,n in counts.items() if n==min(counts.values())}
            near_type=min(dist(p0,p) for p in F[k])
            C['rarest_type']+=k in rare; C['nearest_of_type']+=d==near_type
            C['rarest_and_nearest']+=k in rare and d==near_type
            # Backfill proxy: fraction of dawn daily jobs still undone by quadrant.
            rem={}; initial={}
            for q in [(0,0),(0,1),(1,0),(1,1)]:
                initial[q]=sum(quad(p)==q for a in DAILY for p in DJ[a])
                rem[q]=sum(quad(p)==q for a in DAILY for p in (DJ[a]&J[a]))
            fractions={q:rem[q]/n for q,n in initial.items() if n}
            q0=quad(p0); qt=quad(target)
            rec=dict(ep=ep,t=t,ui=u,hour=hour,kind=k,d=d,group=group,ready_dawn=target in DJ[k],rarest=k in rare,nearest_type=d==near_type)
            if k in DAILY and qt in fractions and q0 in fractions:
                C['daily_quad_n']+=1
                C['source_quadrant_clear']+=rem[q0]==0
                C['cross_quadrant']+=q0!=qt
                C['target_most_behind']+=fractions[qt]==max(fractions.values())
                C['target_strictly_more_behind']+=fractions[qt]>fractions[q0]
                rec.update(src_remaining=rem[q0],src_fraction=fractions[q0],dst_fraction=fractions[qt])
            rows.append(rec)
    print(ep,dict(S['distant']),flush=True)
res={'episodes':ids,'seconds':round(time.time()-START,2),'counts':{k:dict(v) for k,v in S.items()},'notes':'Descriptive reused episodes, no seed holdout. Six service types, cargo FEED mask; quadrants only a zone proxy; future endpoints outcomes only. Literal rarest=minimum positive feasible job count; frozen queue=ready at dawn, excluding future scheduled jobs.'}
(OUT/'round_c_probe.json').write_text(json.dumps(res,indent=2))
with open(OUT/'round_c_trips.jsonl','w') as f:
    for r in rows:f.write(json.dumps(r)+'\n')
print(json.dumps(res,indent=2))
