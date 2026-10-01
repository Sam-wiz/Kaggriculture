# Does the BC ranker graft actually change clone_dsm's choice? Solo vs pass, seeds 1/2.
import sys,os,importlib.util
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0,ROOT+"/moe/r3/build/opus")
import kagsim
from run import act
NOP={"farmer":["PASS"],"hands":[],"market":[]}
for seed in (1,2):
    sp=importlib.util.spec_from_file_location("m%d"%seed,ROOT+"/moe/r7/build/opus/clone_dsm_bc_fire.py"); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    g=kagsim.Game(seed=seed)
    for t in range(719): g.step(act(m.agent,g.observe(0)),NOP)
    S=m._S; print(seed, round(g.reward(0)), S, "diff_frac",round(S['diff']/S['n'],3),"difftype_frac",round(S['difftype']/S['n'],3))
