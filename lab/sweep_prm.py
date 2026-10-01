"""Joint sweep of prem-overlay params vs clone pool + mirror."""
import os,sys,json,importlib.util,statistics
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0,'.')
import harness

def L(p):
    spec=importlib.util.spec_from_file_location('m'+p.replace('/','_').replace('.','_'),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m.agent

def evalcand(args):
    tune,seed,oppfile,swap=args
    os.environ['PRM_TUNE']=json.dumps(tune)
    cand=L('subV_tune.py')
    opp=L(oppfile)
    if swap: a,b=opp,cand; si=1
    else: a,b=cand,opp; si=0
    r=harness.run_episode(a,b,seed=seed,copy_obs=False)
    return r['reward'][si]-r['reward'][1-si]

def main():
    floorsets={
      'f40':{"MILK":72,"WOOL":84,"STRAWBERRY":54,"MELON":36},
      'f55':{"MILK":60,"WOOL":70,"STRAWBERRY":45,"MELON":30},
      'f25':{"MILK":96,"WOOL":112,"STRAWBERRY":72,"MELON":48},
    }
    cands=[]
    for fk,fl in floorsets.items():
        for batch in (15,30,50):
            for minday in (10,14):
                cands.append({'name':f'{fk}-b{batch}-d{minday}','floors':fl,'batch':batch,'minday':minday})
    opps=['subK_pipe16.py','subV_a.py']
    seeds=list(range(9100,9106))
    for c in cands:
        jobs=[(c,s,o,sw) for s in seeds for o in opps for sw in (False,True)]
        with ProcessPoolExecutor(max_workers=8) as ex:
            res=list(ex.map(evalcand,jobs))
        w=sum(1 for d in res if d>0);n=len(res)
        print('%-16s W%2d/%d avg %+6.0f'%(c['name'],w,n,statistics.mean(res)),flush=True)

if __name__=='__main__':
    main()
