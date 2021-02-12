import json

path = './datoteke/računi.json'

def load():
    with open(path) as f:
        return json.load(f)

    def save(novi_racun):
        with open(path, "w") as f:
            json.dump(novi_racun, f, ensure_ascii = False)