import sys; sys.path.insert(0,'kaggriculture-island-ga'); sys.path.insert(0,'.')
import inco, kagsim, json
from multiprocessing import Pool
from collections import defaultdict
ROOT='/Users/samrudh/Documents/Projects/kaggle/Kaggriculture'
def game(args):
    a_path,b_path,seed,swapped=args
    sys.path.insert(0,ROOT+'/kaggriculture-island-ga'); sys.path.insert(0,ROOT)
    import inco, kagsim
    ag=inco.load_agent(ROOT+'/'+a_path); op=inco.load_agent(ROOT+'/'+b_path)
    g=kagsim.Game(seed=seed)
    for t in range(720):
        o0,o1=g.observe(0),g.observe(1)
        if swapped: g.step(op(o1),ag(o0))
        else: g.step(ag(o0),op(o1))
    return (a_path,b_path,seed,swapped,
            g.reward(1) if swapped else g.reward(0),
            g.reward(0) if swapped else g.reward(1))
if __name__=='__main__':
    cands=['rivals/aurax7_kaggriculture-shop-router-reactive-v7/main.py',
           'rivals/jaxa623_2802/main.py']
    tasks=[]
    for A in cands:
        for opp in ('subI_pipe7.py','subH_v48.py'):
            for s in range(8200,8208):
                tasks.append((A,opp,s,False)); tasks.append((A,opp,s,True))
    agg=defaultdict(lambda:[0,0,0])
    with Pool(6) as p:
        for r in p.imap_unordered(game,tasks):
            a,b,s,sw,ra,rb=r
            agg[(a,b)][0]+=ra-rb; agg[(a,b)][1]+=ra>rb; agg[(a,b)][2]+=1
    for (a,b),(mg,w,n) in sorted(agg.items()):
        print(f'{a.split("/")[1][:45]} vs {b[:14]}: W{w}-L{n-w} margin {mg/n:+.0f} n={n}')
