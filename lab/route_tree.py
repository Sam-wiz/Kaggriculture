"""Build the route prefix tree: which routes remain reachable at each step."""
import ast, json, zlib, base64, collections
src = open('subV_sirxL96.py').read()
tree = ast.parse(src)
blob = None
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id == '_R108_DATA':
                for n in ast.walk(node.value):
                    if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 10000:
                        blob = n.value
b = json.loads(zlib.decompress(base64.b85decode(blob)))
routes = {int(k): [b["actions"][i] for i in ids] for k, ids in b["routes"].items()}
rids = sorted(r for r in routes if r != 1)
steps = [144, 168, 192, 216, 240, 288, 312, 360, 432, 480, 648]
for s in steps:
    classes = collections.defaultdict(list)
    for r in rids:
        key = json.dumps(routes[r][:s], sort_keys=True)
        classes[key].append(r)
    groups = sorted(len(v) for v in classes.values() if len(v) > 1)
    print(f"step {s} (day {s//24}): {len(classes)} classes, multi-route groups: {groups}")
