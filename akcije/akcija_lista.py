import json

path = './datoteke/akcije.json'

def load():
    with open(path) as f:
        return json.load(f)

def save(bundles_new):
    with open(path, "w") as f:
        json.dump(bundles_new, f, ensure_ascii=False)