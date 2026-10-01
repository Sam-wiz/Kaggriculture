import ast, collections, gzip, hashlib, json, pathlib, runpy
ROOT = pathlib.Path(__file__).resolve().parents[4]
counts = collections.Counter()
eps = set()
examples = []
with (ROOT/'mine/rawkeep/bc2_DSM.jsonl').open() as f:
    for line in f:
        r = json.loads(line); eps.add(r['ep']); counts['rows'] += 1
        y, on = r['y'], r['on']
        if y in ('WATER','FEED','CARE','COLLECT_FERTILIZER'):
            counts[y] += 1
            key = {'WATER':'watered','FEED':'fed','CARE':'cared','COLLECT_FERTILIZER':'fert_av'}[y]
            if bool(on.get(key)) == (y != 'COLLECT_FERTILIZER'):
                counts[y+'_postcondition'] += 1
        if r['ep'] == 109709272 and r['ui'] == 0 and len(examples)<3 and y in ('WATER','PLANT:MELON','BUILD_PASTURE'):
            examples.append(r)
raw = ROOT/'mine/rawkeep/109709272.json.gz'
x = json.load(gzip.open(raw,'rt')); pi = x['info']['TeamNames'].index('DSM')
transitions = []
for r in examples:
    t = r['t']; pos = r['xy']; xx,yy=pos
    transitions.append({'t':t,'action':x['steps'][t][pi]['action']['farmer'],
        'before':x['steps'][t-1][pi]['observation']['farms'][pi]['tiles'][yy][xx],
        'after':x['steps'][t][pi]['observation']['farms'][pi]['tiles'][yy][xx],
        'dataset_on':r['on']})
rank = runpy.run_path(str(ROOT/'moe/r7/build/devin/clone_dsm_bc.py'))
obs = x['steps'][0][pi]['observation']; me=obs['farms'][pi]; masks=rank['_masks_of'](me['tiles']); px,py=me['farmer']
d,sd=rank['_nears'](me['tiles'],masks,px,py)
v=rank['_feats_of'](obs['day'],obs['hour'],me['money'],me['hires_today'],len(me['unlocked_quadrants']),{}, {},0,px,py,{k:len(s) for k,s in masks.items()},d,sd,me['tiles'][py][px])
try:
    rank['_fwd'](v); err=None
except Exception as e: err=repr(e)
agent_errors = []
for t in range(24):
    ob = dict(x['steps'][t][pi]['observation']); ob['player']=pi
    try: rank['agent'](ob)
    except Exception as e: agent_errors.append({'t':t,'error':repr(e)})
files=['mine/rawkeep/bc_extract2.py','mine/rawkeep/bc_train2.py','moe/r7/build/devin/clone_bc.py','moe/r7/build/devin/clone_dsm_bc.py']
result={'dataset_counts':dict(counts),'episodes':len(eps),'raw_episode':x['info'], 'transitions':transitions,
        'ranker':{'features':len(v),'expected':rank['_D'],'forward_error':err,'shed_distance':sd,'true_shed_distance':0,'agent_probe_states':24,'agent_errors':agent_errors},
        'sha256':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files}}
print(json.dumps(result,indent=2))
(ROOT/'moe/r7/build/astra/bc_audit.json').write_text(json.dumps(result,indent=2)+'\n')
