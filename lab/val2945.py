import sys; sys.path.insert(0,'kaggriculture-island-ga'); sys.path.insert(0,'.')
import inco, kagsim, json
from multiprocessing import Pool
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
    return (a_path,b_path,seed,swapped,g.reward(0) if not swapped else g.reward(1),
            g.reward(1) if not swapped else g.reward(0))
if __name__=='__main__':
    A='rivals/the-2945-farm-96-vs-the-top-10-public-bots/main.py'
    tasks=[]
    for opp in ('subI_pipe7.py','subH_v48.py'):
        for s in range(8100,8110):
            tasks.append((A,opp,s,False)); tasks.append((A,opp,s,True))
    from collections import defaultdict
    agg=defaultdict(lambda:[0,0,0])
    with Pool(6) as p:
        for r in p.imap_unordered(game,tasks):
            a,b,s,sw,ra,rb=r
            k=b
            agg[k][0]+=ra-rb; agg[k][1]+=ra>rb; agg[k][2]+=1
            print(f'{s} {"seat1" if sw else "seat0"}: {ra:.0f} vs {rb:.0f} margin {ra-rb:+.0f}',flush=True)
    for k,(mg,w,n) in agg.items():
        print(f'== 2945 vs {k}: W{w}-L{n-w} mean margin {mg/n:+.0f} over {n}')
