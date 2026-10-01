import collections,gzip,glob,json
from pathlib import Path
out={'episodes':[],'counts':collections.Counter(),'sell_quantities':collections.Counter(),'milk_cases':[]}
for f in sorted(glob.glob('mine/rawkeep/*.json.gz')):
    x=json.load(gzip.open(f,'rt')); teams=x.get('info',{}).get('TeamNames',[])
    if 'DSM' not in teams: continue
    seat=teams.index('DSM'); steps=x['steps']
    out['episodes'].append({'ep':x['info']['EpisodeId'],'seed':x['info']['seed'],'seat':seat,'opponent':teams[1-seat]})
    for t in range(1,len(steps)):
        obs=steps[t-1][seat].get('observation') or {}; act=steps[t][seat].get('action')
        if not obs or not isinstance(act,dict): continue
        orders=act.get('market') or []; c=out['counts']; c['turns']+=1
        c['full_order_list']+=len(orders)>=10
        c['private_present']+='private' in obs
        shed=obs['private']['shed']; milk=[o for o in orders if o and o[0]=='SELL' and o[1]=='MILK']
        stock=shed.get('MILK',0)>0
        c['milk_stock_'+str(stock)+'_fire_'+str(bool(milk))]+=1
        for o in orders:
            if o and o[0]=='SELL':
                out['sell_quantities'][str(o[2])]+=1
                c['sell_orders']+=1
                c['sell_zero_pre_shed']+=shed.get(o[1],0)==0
        if stock and not milk and len(out['milk_cases'])<12:
            out['milk_cases'].append({'ep':x['info']['EpisodeId'],'t':t,'day':obs['day'],'hour':obs['hour'],'milk':shed['MILK'],'price':obs['market']['prices']['MILK'],'orders':orders})
Path('moe/r7/build/astra/boundary_probe.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'episodes':len(out['episodes']),'counts':out['counts'],'sell_quantities':out['sell_quantities'],'milk_cases':out['milk_cases'][:3]},indent=2))
