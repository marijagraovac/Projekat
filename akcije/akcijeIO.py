import json

path = './datoteke/akcije.json'


def load():
    with open(path) as f:
        return json.load(f)


def save(nove_akcije):
    with open(path, "w") as f:
        json.dump(nove_akcije, f)
