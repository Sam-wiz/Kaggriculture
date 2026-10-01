"""Independent expert-state probes for duplicate idempotent service operations."""
import collections, copy, gzip, hashlib, json, pathlib, runpy, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
p = ROOT / 'moe/r7/build/devin/clone_bc.py'
source = p.read_bytes()
ns = runpy.run_path(str(p))
raw = json.load(gzip.open(ROOT / 'mine/rawkeep/109709272.json.gz', 'rt'))
pi = raw['info']['TeamNames'].index('DSM')
counts = collections.Counter()
examples = []
for t in range(144):
    ob = copy.deepcopy(raw['steps'][t][pi]['observation'])
    ob.update(player=pi, step=t)
    ns['_ST'].update(assign={}, step=-1)
    try:
        action = ns['agent'](ob)
    except Exception as e:
        counts['exceptions'] += 1
        continue
    counts['states'] += 1
    me = ob['farms'][pi]
    units = [me['farmer']] + me['hands']
    ops = [action['farmer']] + action['hands']
    grouped = collections.defaultdict(list)
    for ui, (pos, op) in enumerate(zip(units, ops)):
        if op[0] in ('FEED', 'WATER', 'CARE'):
            grouped[(tuple(pos), op[0])].append(ui)
    dupes = [(pos, op, ids) for (pos, op), ids in grouped.items() if len(ids)>1]
    if dupes:
        counts['states_duplicate_service'] += 1
        for pos, op, ids in dupes:
            counts['redundant_' + op] += len(ids)-1
            if len(examples)<8:
                examples.append({'t':t, 'pos':pos, 'op':op, 'units':ids,
                                 'tile':me['tiles'][pos[1]][pos[0]],
                                 'inventories':[ob['private']['inventories'][i] for i in ids]})
report = {'source_sha256':hashlib.sha256(source).hexdigest(),
          'source_unchanged':source==p.read_bytes(),
          'scope':'144 independent expert-state probes, intentions reset; actual embedded weights; no games or held-out win-rate claim',
          'episode':raw['info'], 'counts':dict(counts), 'examples':examples}
out=ROOT/'moe/r7/build/astra/bc_claim_audit.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
