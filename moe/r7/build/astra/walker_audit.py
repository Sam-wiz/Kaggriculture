import collections, json, time
from pathlib import Path
start=time.monotonic()
byep=collections.defaultdict(collections.Counter)
for line in open('mine/rawkeep/tilerows_DSM.jsonl'):
    r=json.loads(line)
    if 'label' not in r: continue
    c=byep[r['ep']]; c['rows']+=1
    lab=r['label']; matches=[x for x in r['cands'] if x['ty']==lab['ty'] and [x['x'],x['y']]==lab['xy']]
    if not matches:
        c['target_absent']+=1
        continue
    ty=lab['ty']; inv=r['inv']
    feasible=(ty!='feed' or inv.get('WHEAT',0)>0) and (ty!='fert' or inv.get('FERTILIZER',0)>0) and (ty!='struct_free' or sum(inv.get(k,0) for k in ['COW','SHEEP','GOOSE'])>0) and (ty!='plant' or r.get('seeds_tot',0)>0)
    if not feasible: c['target_masked']+=1
split={}
eps=sorted(byep)
for name, group in [('train',eps[:-10]),('test',eps[-10:])]:
    total=collections.Counter()
    for ep in group: total.update(byep[ep])
    split[name]={'episodes':group,**total}
raw=collections.Counter(); beps=set()
for line in open('moe/r7/build/opus/bc2s_DSM.jsonl'):
    r=json.loads(line); raw[r['y']]+=1; beps.add(r['ep'])
report={'tile_split':split,'bc_rows':sum(raw.values()),'bc_episodes':len(beps),'bc_raw_action_counts':raw,'bc_fields':sorted(r),'elapsed_seconds':round(time.monotonic()-start,2),'inspection':'tilefit.py computes oktr but trains all rows; missing and masked targets contribute invalid softmax gradients. BC y has op/item but omits pickup/place quantity; local neighborhoods require raw replay extraction.'}
Path('moe/r7/build/astra/walker_audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
