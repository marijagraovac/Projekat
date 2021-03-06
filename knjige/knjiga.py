from knjige.knjigaIO import load, save
from akcije import akcije
from datetime import date, datetime
from korisnici import korisnik
from racuni import lista_racuna
from racuni import racuni as mracun
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
        Kategorija = input('Kategorija:')
        Broj_strana = input('Broj strana:')
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

    def edit(nova_knjiga=''):
        validator = 0
        ID = input("\nID (input 'Nazad' to return to the main menu):")
        i = 0
        for knjiga in knjige:
            if knjiga['ID'] == ID:
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

        Naslov = input('\nPromenite naslov:')
        if Naslov == '':
            Naslov = knjige[i]['Naslov']
        Autor = input('Promenite autora:')
        if Autor == '':
            Autor = knjige[i]['Autor']
        ISBN = input('Promenite ISBN')
        if ISBN == '':
            ISBN = knjige[i]['ISBN']
        Izdavač = input('Promenite izdavača')
        if Izdavač == '':
            Izdavač = knjige[i]['Izdavač']
        try:
            Godina = int(input('Promenite godinu'))
        except ValueError:
            Godina = knjige[i]['Godina']
        try:
            Cena = float(input('Promenite cenu'))
        except ValueError:
            Cena = knjige[i]['Cena']
        Kategorija = input('Promenite kategoriju')
        if Kategorija == '':
            Kategorija = knjige[i]['Kategorija']
        try:
            Broj_strana = int(input('Promenite broj strana'))
        except ValueError:
            Broj_strana = knjige[i]['Broj strana']

        stare_knjige = [knjige[z], nova_knjiga]
        list(stare_knjige)
        while True:
            print('\nDa li želite da nastavite?\n1. Da\n2. Ne')
            option = input('Input:')
            if option == '1':
                knjige[z] = nova_knjiga
                break
            elif option == '2':
                return False
            else:
                print('Greška, pokušajte ponovo')

        save(knjige)
        print('%s je dodano u bazu podataka.')
        return False

    def erase():
        z = -1
        i = 0
        while True:
            ID = input("\nID (input 'Nazad' to return to the main menu):")
            if ID == 'Nazad':
                return False
            elif ID != '':
                result = re.search(' ', ID)
                if result == None:
                    break
                else:
                    print("ID ne može imati prazna mesta, pokušajte ponovo")
                    if erase() == False:
                        return False
            else:
                print("ID ne može biti prazan, pokušajte ponovo")
                if erase () == False:
                    return False
        for knjiga in knjige:
            if knjiga['ID'] == ID:
                print('Knjiga je pronađena')
                z = i
                break
            i += 1
        if z == -1:
            print('Knjiga nije pronađena, pokušajte ponovo')
            if erase () == False:
                return False
        obrisane_knjige = [knjige[z]]
        print('\nKnjiga će biti obrisana')
        list(obrisane_knjige)
        while True:
            print('\nDa li želite da nastavite?\n1. Da\n2. Ne')
            option = input('Input:')
            if option == '1':
                obrisati_knjigu = knjige[z]
                obrisati_knjigu['Obrisano'] = True
                break
            elif option == '2':
                return False
            else:
                print('Greška, pokušajte ponovo')

        save(knjige)
        print('%s je obrisano iz baze podataka')
        return False

    def prodati_knjigu():
        global cart
        z = -1
        i = 0
        while True:
            ID = input("\nID (input 'Nazad' to return to the main menu):")
            if ID == 'Nazad':
                return False
            elif ID != '':
                result = re.search(' ', ID)
                if result == None:
                    break
                else:
                    print("Greška, pokušajte ponovo")
                    if prodati_knjigu() == False:
                        return False
            else:
                print("Greška, pokušajte ponovo")
                if prodati_knjigu() == False:
                    return False
                else:
                    return True
        for knjiga in knjige:
            if knjiga['ID'] == ID and knjiga['Obrisano'] == False:
                print('Knjiga je pronađena')
                z = i
                break
            i += 1
        if z == -1:
            print('Knjiga nije pronađena, pokušajte ponovo')
            if prodati_knjigu() == False:
                return False
            else:
                return True
        cart_item = []
        while True:
            q = -1
            try:
                q = int(input('Broj:'))
            except ValueError:
                pass
            if q>0:
                break
            else:
                print('Greška, pokušajte ponovo')
        print('Biće dodani u korpu')
        for i in range(q):
            cart_item += [knjige[z]]
        list(cart_item)
        while True:
            print('\nDa li želite da nastavite?\n1. Da\n2. Ne')
            option = input('Input:')
            if option == '1':
                cart[0]["Artikli"] += cart_item
                return True
            elif option == '2':
                return False
            else:
                print ('Greška, pokušajte ponovo')

    def prodati_akciju():
        global cart
        z = -1
        i = 0
        while True:
            ID = input("\nID (input 'Nazad' to return to the shopping menu):")
            if ID == 'Nazad':
                return False
            elif ID != '':
                result = re.search(' ', ID)
                i = 0
                for akcija in akcije:
                    if (str(akcija['ID']) == ID and akcija['Datum isteka'] > str(date.today())):
                        print('Akcija pronađena')
                        z = i
                        break
                    i += 1
            if z == -1:
                print('Akcija nije pronađena ili je istekla')
            if z != -1:
                break
        cart_item = []
        print('Artikli će biti dodani u korpu')
        n = len(akcije[z]['Artikli'])
        for i in range(n):
            cart_item += [akcije[z]['Artikli'][i]]
        list(cart_item)
        while True:
            print('\nDa li želite da nastavite?\n1. Da\n2. Ne')
            option = input('Input:')
            if option == '1':
                cart[0]["akcija_knjige"] += cart_item
                return True
            elif option == '2':
                return False
            else:
                print('Greška, pokušajte ponovo')

    def napraviti_racun():
        global total
        racun = {
            "ID": 0,
            "Prodavac": "S",
            "Datum i vreme": "2021-02-07T19:24:34",
            "Artikli": [
                {
                    "ID": "N/A",
                    "Naslov": "N/A",
                    "Autor": "N/A",
                    "ISBN": "N/A",
                    "Izdavač": "N/A",
                    "Godina": 2021,
                    "Cena": 0.0,
                    "Kategorija": "N/A",
                    "Broj strana": 0
                }
            ],
            "akcija_knjige": [
                {
                    "ID": "N/A",
                    "Naslov": "N/A",
                    "Autor": "N/A",
                    "ISBN": "N/A",
                    "Izdavač": "N/A",
                    "Godina": 2021,
                    "Cena": 0.0,
                    "Kategorija": "N/A",
                    "Broj strana": 0
                }
            ],
            "Ukupno": 0.0
        }
        stari_racuni = lista_racuna.load()
        z = 0
        for racun in stari_racuni:
            z += 1
        racun['ID'] = z
        racun['Prodavac'] = korisnik.get_korisnicko_ime()
        racun['date_time'] = date.time.now().isoformat()
        racun['Artikli'] = cart[0]['Artikli']
        racun['Akcije'] = cart[0]['Akcije_knjige']
        racun['Ukupno'] = total
        return racun

    def sell_complete():
        racuni = lista_racuna.load()
        racun = napraviti_racun()
        try:
            print('\nSledeće knjige će biti prodane:')
            list(cart[0]["Artikli"])
        except IndexError:
            pass
        try:
            print('\nSledeće akcije će biti prodane:')
            list(cart[0]["Akcija_knjige"])
        except IndexError:
            pass
        while True:
            print('\nDa li želite da nastavite?\n1. Da\n2. Ne')
            option = input('Input:')
            if option == '1':
                if total != 0:
                    racuni.append(racun)
                break
            elif option == '2':
                return True
            else:
                print('Greška, pokušajte ponovo')
        lista_racuna.save(racuni)
        if total != 0:
            print('Knjige su prodate.')
            mracun.print_table(racun)
        else:
            print('Korpa je bila prazna')
            return False

    def sell_menu():
        global cart
        global total
        while True:
            total = 0.0
            for item in cart[0]["Artikli"]:
                total += item["Cena"]
            for item in cart[0]["Akcija knjige"]:
                total += item["Cena"]
            print('\nProdati:')
            print('1. Knjige')
            print('2. Akcije')
            print('3. Prikazati korpu')
            print('4. Završiti')
            print('5. Povratak na glavni meni')
            option = input('Izaberite opciju:')
            if option == '1':
                if prodati_knjigu() == True:
                    print('Dodano u korpu:')
                else:
                    print('Nije dodano u korpu.')
                    if sell_menu() == False:
                        return False
            elif option == '2':
                if prodati_akciju() == True:
                    print('Dodano u korpu:')
                else:
                    print('Nije dodano u korpu')
                    if sell_menu() == False:
                        return False
            elif option == '3':
                try:
                    list(cart[0]["Artikli"])
                except IndexError:
                    pass
                try:
                    list(cart[0]["Akcija knjige"])
                except IndexError:
                    pass
                print('\nUkupno:', total)
            elif option == '4':
                if sell_complete() == True:
                    pass
                else:
                    return False
            elif option == '5':
                return False
            else:
                print('Greška, pokušajte ponovo')

    def sell():
        global cart
        cart_keys = {
            "Artikli": [],
            "Akcija_knjige": []
        }
        cart = [cart_keys]
        if sell_menu() == False:
            return False











