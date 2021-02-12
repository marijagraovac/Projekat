import json

path = './datoteke/akcije.json'

def load():
    with open(path) as f:
        return json.load(f)

def save(akcije):
    with open(path, "w") as f:
        json.dump(akcije, f, indent=4)