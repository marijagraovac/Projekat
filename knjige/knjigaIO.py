import json

path = './datoteke/knjige.json'

def load ():
    with open(path) as f:
        return json.load(f)

def save(nove_knjige):
    with open(path, "w") as f:
        json.dump(nove_knjige, f)
