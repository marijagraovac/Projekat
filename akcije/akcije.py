import sys
sys.path.insert(0, '')

from akcijeIO import load, save
from datetime import date
from knjige import knjiga
import re

akcije = load()
n = len(akcije)

key = ['naslov', 'autor', 'kategorija']


def print_knjige(akcije):
    string = ''
    i = 0
    for knjige in akcije["akcije"]:
        string += knjige["naslov"]
        try:
            if akcije["knjige"][i+1] != None:
                string += '\n'
        except IndexError:
            break
        i += 1
    return string


def print_cene(akcije):
    string = ''
    i = 0
    for knjige in akcije['akcije']:
        string += str(knjige['cena'])
        try:
            if akcije['knjige'][i+1] != None:
                string += '\n'
        except IndexError:
            break
        i += 1
    return string

def table_create(akcije, show_valid, table=None):
    table.maxwidth=300
    for akcija in akcije:
        if(akcija['datum isteka']>str(date.today()) or show_valid == False):
            table.rows.append([akcija["id"], akcija["datum isteka"], print_knjige(akcije), print_cene(akcije)])
    table.columns.header = ["ID", "Važi do \n(inclusive)", "Knjige", "Nove cene"]
    return table

def sort():
    show_valid = True
    table = table_create(akcije, show_valid)
    while True:
        print('\nSortirati po:')
        print('1. ID')
        print('2. Datum isteka')
        print('3. Nazad')
        option = input('Izaberite opciju:')
        if (option == '1'):
            table.rows.sort("ID")
            break
        elif (option == '2'):
            table.rows.sort("Važi do\n(inclusive)")
            break
        elif (option == '3'):
            return False
        else:
            print('Nepostojeća opcija, pokušajte ponovo')
    print (table)

def search():
    show_valid = False
    print('\nPretražiti po:')
    print('1. ID')
    print('2. Naslov')
    print('3. Autor')
    print('4. Kategorija')
    print('5. Nazad')
    option = input('Izaberite opciju:')
    if (option == '2' or option == '3' or option == '4'):
        term = input('Pretražiti:')
        notes = []
        for akcija in akcije:
            if (option == '2'):
                i = 0
            elif (option == '3'):
                i = 1
            elif (option == '4'):
                i = 2
            for knjiga in akcije['knjige']:
                result = re.search(term.lower(), str(knjiga[key[i]]).lower())
                if (result != None):
                    notes.append(akcije)
                    break
        table = table_create(notes, show_valid)
        print(table)
        search()

    elif (option == '1'):
        notes = []
        while True:
            try:
                term = int(input('\nPretraži:'))
                break
            except ValueError:
                print('Ukucajte samo cele brojeve')
        for akcija in akcije:
            result = re.search(str(term).lower(), str(akcije['id']).lower())
            if (result != None):
                notes.append(akcija)
        table = table_create(notes,show_valid)
        print(table)
        search()

    elif (option == '5'):
        return False
    else:
        print('Pokušajte ponovo')
        if (search() == False):
            return False

def register():
    nove_akcije = {
        "id": "320384",
        "knjige": [{
            "šifra": "978867",
            "naslov": "Alijenista",
            "isbn": "978-86-7436-067-5",
            "autor": "Kejleb Kar",
            "izdavač": "Laguna",
            "broj strana": 587,
            "godina": 1994,
            "cena": 799.20,
            "kategorija": "Triler"
        }],
        "datum isteka": "2021-02-19"
    }
    for akcija in akcije:
        id = akcija['id']
    id += 1
    nove_akcije = []
    while True:
        prompt = 0
        breaker = 0
        id = input("ID Knjige (input 'nazad' za povratak):")
        if(knjiga.find(id) != None and id != ''):
            knjiga1 = knjiga.find(id)
            print('Knjiga pronađena')
            prompt = 1
            print('Knjige će biti dodana u akciju.')
            knjige = [knjiga1]
            knjiga.permissions('a')
            knjiga.list(knjige)
            knjiga.permissions('m')
            while True:
                print('\nŽelite li da nastavite?\1. Da\n2. Ne')
                option = input('Input:')
                if (option == '1'):
                    while True:
                        try:
                            cena = float(input('Nova cene knjige:'))
                            knjiga1['cena'] = cena
                            break
                        except ValueError:
                            print('Greška, pokušajte ponovo')
                    nove_akcije.append(knjiga1)
                    break
                elif (option == '2'):
                    prompt = 0
                    id = 'a'
                    break
                else:
                    print('Greška, pokušajte ponovo')
        elif(id == 'nazad'):
            return False
        else:
            print('Pogrešan ID, pokušajte ponovo')
        if (prompt == 1):
            while True:
                print('\nDa li želite da dodate još jednu knjigu u akciju?\n1. Da\n2. Ne')
                option = input('Input:')
                if (option == '1'):
                    break
                elif (option == '2'):
                    breaker = 1
                    break
                else:
                    print('Greška, pokušajte ponovo')
            if(breaker == 1 and nove_akcije != []):
                break
    nove_akcije['knjige'] = nove_akcije
    
    while True:
        try:
            godina = int(input('Ističe godine:'))
            datum_isteka = date(godina, 1, 1)
            break
        except ValueError:
            print('Greška, pokušajte ponovo')
    while True:
        try:
            mesec = int(input('Mesec:'))
            datum_isteka = date(godina, mesec, 1)
            break
        except ValueError:
            print('Greška, pokušajte ponovo')
    nove_akcije['datum_isteka'] = str(datum_isteka)
    print('\nAkcija će biti dodana u bazu podataka:')
    nove_akcije = [nove_akcije]
    show_valid = False
    table = table_create(nove_akcije, show_valid)
    print(table)
    while True:
        print('\nDa li želite da nastavite?\n1. Da\n2. Ne')
        option = input('Input:')
        if (option == '1'):
            akcije.append(nove_akcije)
            break
        elif (option == '2'):
            return False
        else:
            print('Greška, pokušajte ponovo')
    save(akcije)
    print('Akcije je dodana u bazu podataka. Akcija ID=[%s]'%(nove_akcije['id']))
    return False

