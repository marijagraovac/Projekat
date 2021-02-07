from knjige.knjigaIO import load, save
from akcije import akcije
from datetime import date, datetime
from korisnici import korisnik
from racuni import lista_racuna
from racuni import racun as mracun
import re

type = 'neutral'


def permissions(rights):
    global type
    type = rights


akcije = akcije.load()
knjige = load()
n = len(knjige)

length = [1, 1, 1, 1, 1, 1, 1, 1, 1]
cart = []
total = 0.0
key = ['id', 'naslov', 'autor', 'isbn', 'izdavač', 'godina', 'cena', 'kategorija', 'broj strana']


def length_list(knjige):
    max = '1'
    n = len(knjige)
    for i in range(9):
        max = len(str(knjige[0][key[i]]))
        for j in range(n-1):
            if max < len(str(knjige[j+1][key[i]])):
                max = len(str(knjige[j+1][key[i]]))
        length[i] = max
    return length


def list(knjigaIO):
    length = length_list(knjigaIO)
    print('\nID', end="")
    for i in range(length[0]+1):
        print(' ', end="")
    print('Naslov', end="")
    for i in range(length[1]+1):
        print(' ', end="")
    print('Autor', end="")
    for i in range(length[2]+1):
        print(' ', end="")
    print('ISBN', end="")
    for i in range(length[3] + 1):
        print(' ', end="")
    print('Izdavač', end="")
    for i in range(length[4] + 1):
        print(' ', end="")
    print('Godina', end="")
    for i in range(length[5] + 1):
        print(' ', end="")
    print('Cena', end="")
    for i in range(length[6] + 1):
        print(' ', end="")
    print('Kategorija', end="")
    for i in range(length[7] + 1):
        print(' ', end="")
    print('Broj strana', end="\n")
    print(' ')
    for knjiga in knjigaIO:
        if type == 'a' or knjiga['Obrisana'] == False:
            print(knjiga['ID'], end="")
            for i in range(length[0]+3-len(str(knjiga['ID']))):
                print(' ', end="")
            print(knjiga['Naslov'], end="")
            for i in range(length[1]+6-len(str(knjiga['Naslov']))):
                print(' ', end="")
            print(knjiga['Autor'], end="")
            for i in range(length[2]+7-len(str(knjiga['Autor']))):
                print(' ', end="")
            print(knjiga['ISBN'], end="")
            for i in range(length[3]+5-len(str(knjiga['ISBN']))):
                print(' ', end="")
            print(knjiga['Izdavač'], end="")
            for i in range(length[4]+10-len(str(knjiga['Izdavač']))):
                print(' ', end="")
            print(knjiga['Godina'], end="")
            for i in range(length[5]+5-len(str(knjiga['Godina']))):
                print(' ', end="")
            print(knjiga['Cena'], end="")
            for i in range(length[6]+6-len(str(knjiga['Cena']))):
                print(' ', end="")
            print(knjiga['Kategorija'], end="")
            for i in range(length[7]+6-len(str(knjiga['Kategorija']))):
                print(' ', end="")
            print(knjiga['Broj strana'], end="\n")
        else:
            pass


def sort():
    while True:
        print('\nSortirati po:')
        print('1. Naslov')
        print('2. Kategorija')
        print('3. Autor')
        print('4. Izdavač')
        print('5. Cena')
        print('6. Nazad')
        option = input('Izaberite opciju:')
        if option == '1':
            sorter = 'Naslov'
            break
        elif option == '2':
            sorter = 'Kategorija'
            break
        elif option == '3':
            sorter = 'Autor'
            break
        elif option == '4':
            sorter = 'Izdavač'
            break
        elif option == '5':
            sorter = 'Cena'
            break
        elif option == '6':
            return False
        else:
            print('Pogrešna opcija, pokušajte ponovo')
        list(knjige)

    if sorter == 'Naslov':
        knjige.sort(key=lambda knjige:knjige.get('Naslov'))
    else:
        print('Greška, pokušajte ponovo')
    if sorter == 'Kategorija':
        knjige.sort(key=lambda knjige:knjige.get('Kategorija'))
    else:
        print('Greška, pokušajte ponovo')
    if sorter == 'Autor':
        knjige.sorter(key=lambda knjige:knjige.get('Autor'))
    else:
        print('Greška, pokušajte ponovo')
    if sorter == 'Izdavač':
        knjige.sort(key=lambda knjige:knjige.get('Izdavač'))
    else:
        print('Greška, pokušajte ponovo')
    if sorter == 'Cena':
        knjige.sort(key=lambda knjige:knjige.get('Cena'))
    else:
        print('Greška, pokušajte ponovo')
    list(knjige)

    def find(term):
        for knjiga in knjige:
            result = re.search(term.lower(), str(knjiga['ID']).lower())
            if result != None:
                return knjiga
        return None

    def search():
        print('\nSortirati po:')
        print('1. ID')
        print('2. Naslov')
        print('3. Autor')
        print('4. Kategorija')
        print('5. Izdavač')
        print('6. Raspon cene')
        print('7. Nazad')
        option = input('Izaberite opciju:')
        if option == '1' or option == '2' or option == '3' or option == '4' or option == '5':
            term = input('Traži:')
            notes = []
            for knjiga in knjige:
                if option == '1': i = 0
                if option == '2': i = 1
                if option == '3': i = 2
                if option == '4': i = 3
                if option == '5': i = 4
                result = re.search(term.lower(), str(knjiga[key[i]]).lower())
                if result != None:
                    notes.append(knjiga)
            if notes != []:
                list(notes)
            else:
                print('Nema rezultata pretrage.')
            search()
        elif option == '6':
            notes = []
            while True:
                try:
                    term = int(input('\nNajmanja cena:'))
                    break
                except ValueError:
                    print('Unesite samo cele brojeve')
            while True:
                try:
                    term2 = int(input('Najveća cena:'))
                    break
                except ValueError:
                    print('Unesite samo cele brojeve')
            for knjiga in knjige:
                if term <= knjiga['Cena'] and term2 >= knjiga['Cena']:
                    notes.append(knjiga)
            if notes != []:
                list(notes)
            else:
                print('Nema rezultata pretrage')
            search()
        elif option == '7':
            return False
        else:
            print('Pokušajte ponovo')
            if search() == False:
                return False

    def register():
        while True:
            ID = input("\nID (input 'Nazad' to return to the main menu):")
            if ID != '':
                result = re.search(' ', ID)
                if result == None:
                    break
                else:
                    print("ID ne može imati prazna mesta, pokušajte ponovo")
                    if register() == False:
                        return False
            else:
                print ("ID ne može biti prazan, pokušajte ponovo")
                if register() == False:
                    return False
        for knjiga in knjige:
            if knjiga['ID'] == ID:
                print('Knjiga sa istim ID već postoji, pokušajte ponovo')
                if register() == False:
                    return False
            elif ID == 'Nazad':
                return False
        Naslov = input('Naslov:')
        Autor = input('Autor:')
        ISBN = input('ISBN')
        Izdavač = input('Izdavač:')
        while True:
            try:
                Godina = int(input('Godina:'))
                break
            except ValueError:
                print('Greška, pokušajte ponovo')
        while True:
            try:
                Cena = float(input('Cena:'))
                break
            except ValueError:
                print('Greška, pokušajte ponovo')
        nova_knjiga = {
            "ID": "3318",
            "naslov": "Kralj Ožiljaka",
            "isbn": "978-86-89-56581-2",
            "autor": "Li Bardugo",
            "izdavač": "Urban Reads",
            "broj strana": 277,
            "godina": 2019,
            "cena": 1100.00,
            "kategorija": "Fantastika"
        }
        nova_knjiga['ID'] = ID
        nova_knjiga['Naslov'] = Naslov
        nova_knjiga['Autor'] = Autor
        nova_knjiga['ISBN'] = ISBN
        nova_knjiga['Izdavač'] = Izdavač
        nova_knjiga['Godina'] = Godina
        nova_knjiga['Kategorija'] = Kategorija
        nova_knjiga['Broj strana'] = Broj_strana
        nova_knjiga['Obrisano'] = False
        print('\nKnjiga će biti dodana u bazu podataka.')
        nove_knjige = [nova_knjiga]
        list(nove_knjige)
        while True:
            print('\nDa li želite da nastavite?\n1. Da\n2. Ne')
            option = input('Input:')
            if option == '1':
                knjige.append(nova_knjiga)
                break
            elif option == '2':
                return False
            else:
                print('Greška, pokušajte ponovo')
        save(knjige)
        print('%s je dodano u bazu podataka.')
        return False

    def edit():
        validator = 0
        ID = input("\nID (input 'Nazad' to return to the main menu):")
        i = 0
        for knjiga in knjige:
            if knjiga ['ID'] == ID:
                validator = 1
                print('Knjiga je pronađena.')
                break
            elif ID == 'Nazad':
                return False
            i += 1
        if validator == 0:
            print('Pogrešan ID, pokušajte ponovo')
            if edit() == False:
                return False
        stara_knjiga = {
            "ID": "3318",
            "naslov": "Kralj Ožiljaka",
            "isbn": "978-86-89-56581-2",
            "autor": "Li Bardugo",
            "izdavač": "Urban Reads",
            "broj strana": 277,
            "godina": 2019,
            "cena": 1100.00,
            "kategorija": "Fantastika"
        }
        stara_knjiga = knjige[i]
        z = i
        stare_knjige = [stara_knjiga]
        list(stare_knjige)

## 345



