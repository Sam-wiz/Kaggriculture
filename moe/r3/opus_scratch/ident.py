import sys, json
sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture")
import harness
for name, path in [("shepherd","subW_shepherd.py"),("hyb2965","subX_hyb2965.py")]:
    ag = harness.load_agent(path, name="id_"+name)
    acts=[]
    def wrap(obs, ag=ag):
        a = ag(obs); acts.append(a); return a
    harness.run_episode(wrap, "pass", seed=12345, configuration={"episodeSteps": 4})
    print(name, json.dumps([a.get("market") for a in acts[:3]])[:200])
