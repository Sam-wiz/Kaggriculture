import sys,os,json; sys.path.insert(0,'.')
import inco, kagsim
from multiprocessing import Pool
ROOT='/Users/samrudh/Documents/Projects/kaggle/Kaggriculture'
OPPS={'v2945':'subJ_2945.py','v48':'subH_v48.py'}
def load(path):
    d=os.path.dirname(os.path.abspath(path))
    if d not in sys.path: sys.path.insert(0,d)
    return inco.load_agent(path)
def game(args):
    c,oppname,seed,sw=args
    sys.path.insert(0,ROOT)
    import inco, kagsim
    ag=load(f'{ROOT}/rivals/{c}/main.py'); op=load(f'{ROOT}/{OPPS[oppname]}')
    g=kagsim.Game(seed=seed)
    for t in range(720):
        o0,o1=g.observe(0),g.observe(1)
        if sw: g.step(op(o0),ag(o1))
        else: g.step(ag(o0),op(o1))
    return (c,oppname,seed,sw,g.reward(1) if sw else g.reward(0),g.reward(0) if sw else g.reward(1))
if __name__=='__main__':
    cands=[d for d in os.listdir(ROOT+'/rivals4') if os.path.exists(f'{ROOT}/rivals/{d}/main.py')]
    print(len(cands),'cands:',cands)
    tasks=[]
    for c in cands:
        for o in OPPS:
            for s in (9001,9002):
                tasks.append((c,o,s,False)); tasks.append((c,o,s,True))
    from collections import defaultdict
    agg=defaultdict(lambda:[0,0,0])
    out=open(ROOT+'/screen4.jsonl','w')
    with Pool(6) as p:
        for r in p.imap_unordered(game,tasks):
            c,o,s,sw,ra,rb=r
            agg[(c,o)][0]+=ra-rb; agg[(c,o)][1]+=ra>rb; agg[(c,o)][2]+=1
            out.write(json.dumps(r)+'\n'); out.flush()
    for (c,o),(mg,w,n) in sorted(agg.items(),key=lambda x:-x[1][0]/x[1][2]):
        print(f'{c[:55]:57s} vs {o}: W{w}-L{n-w} {mg/n:+7.0f}')
