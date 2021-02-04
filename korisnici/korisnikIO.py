import json

path = './datoteke/korisnici.json'


def load():
    with open(path) as f:
        return json.load(f)


def save(korisnici):
    with open(path, "w") as f:
        json.dump(korisnici, f)
