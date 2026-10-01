import sys,importlib.util,concurrent.futures as cf
sys.path.insert(0,'.venv/lib/python3.14/site-packages')
from kaggle_environments import make

def loadm(p):
    spec=importlib.util.spec_from_file_location(p.replace('.','_'),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def pair(args):
    ap,bp,seed=args
    ma=loadm(ap);mb=loadm(bp)
    out=[]
    for order in ((ma.agent,mb.agent),(mb.agent,ma.agent)):
        env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
        env.run(list(order))
        r=[s.reward for s in env.steps[-1]]
        # candidate seat
        cseat=0 if order[0] is ma.agent else 1
        cand=ma
        # signature: shops at end of day 9 (step 239 obs of next turn)
        obs=env.steps[240][cseat].observation if len(env.steps)>240 else env.steps[-1][cseat].observation
        shops=tuple(sorted((obs.get('town') or {}).get('unlocked_shops') or []))
        fired=cand._V231_STATES.get(cseat,{}).get('confirmed',0)
        diff=(r[0]-r[1]) if cseat==0 else (r[1]-r[0])
        out.append((seed,cseat,diff,shops,fired))
    return out

if __name__=='__main__':
    cand=sys.argv[1];opp=sys.argv[2]
    seeds=[int(x) for x in sys.argv[3].split(',')]
    with cf.ProcessPoolExecutor(6) as ex:
        for res in ex.map(pair,[(cand,opp,s) for s in seeds]):
            for seed,cseat,diff,shops,fired in res:
                print(f"{seed} seat{cseat} diff={diff:+.0f} fired={fired} shops={shops}",flush=True)
