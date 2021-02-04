from korisnici.korisnikIO import load, save
import re, getpass

users = load()
n = len(users)
username = ''


def login():
    korisnicko_ime = input('Korisničko ime:')
    if korisnicko_ime == 'exit()':
        exit()
    lozinka = getpass.getpass('Lozinka:')
    for user in users:
        if(['korisnicko_ime'] == korisnicko_ime) and (user['lozinka'] == lozinka):
            korisnicko_ime = user['korisnicko_ime']
            return user
        return False


def get_korisnicko_ime():
    return users


length = [1, 1, 1, 1, 1]

key = ['korisnicko_ime', 'lozinka', 'ime', 'prezime', 'tip_korisnika']


def length_list():
    max = '1'
    for i in range(5):
        max = len(str(users[0][key[i]]))
        for j in range(n-1):
            if max < len(str(users[j+1][key[i]])):
                max = len(str(users[j+1][key[i]]))
        length[i] = max


def list(users):
    length_list()
    print('\Korisničko ime', end="")
    for i in range(length[0]+1):
        print(' ', end="")
    print('Lozinka', end="")
    for i in range(length[1] + 1):
        print(' ', end="")
    print('Ime', end="")
    for i in range(length[2] + 1):
        print(' ', end="")
    print('Prezime', end="")
    for i in range(length[3] + 1):
        print(' ', end="")
    print('Tip korisnika', end="")
    for i in range(length[4] + 1):
        print(' ', end="")
    print('\n')
    for user in users:
        print(user['korisnicko_ime'], end="")
        for i in range(length[0]+9-len(str(user['korisnicko_ime']))):
            print(' ', end="")
        print('*****', end="")
        for i in range(length[1]+4):
            print(' ', end="")
        print(user['Ime'], end="")
        for i in range(length[2]+5-len(str(user['Ime']))):
            print(' ', end="")
        print(user['Prezime'], end="")
        for i in range(length[3]+9-len(str(user['Prezime']))):
            print(' ', end="")
        print(user['Tip korisnika'], end="\n")
        i += 1


def sort():
    while True:
        print('\nSortirati po:')
        print('1. Ime')
        print('2. Prezime')
        print('3. Tip korisnika')
        print('4. Nazad')
        option = input('Izaberite opciju:')
        if option == '1':
            sorter = 'Ime'
            break
        elif option == '2':
            sorter = 'Prezime'
            break
        elif option == '3':
            sorter = 'Tip korisnika'
            break
        elif option == '4':
            return False
        else: print('Nepostojeća opcija, pokušajte ponovo')
        list(users)


def admin_register():
    while True:
        korisnicko_ime = input("\nKorisničko ime (input 'Nazad' to return to main menu):")
        result = re.search(' ', korisnicko_ime)
        if result != None: print('Greška, pokušajte ponovo')
        elif username == ' ': print('Korisničko ime ne može biti prazno, pokušajte ponovo')
        else: break
    for user in users:
        if(user['korisnicko_ime'] == korisnicko_ime):
            print('Korisničko ime je zauzeto, pokušajte ponovo')
            if(admin_register() == False):
                return False
        if (korisnicko_ime == 'Nazad'):
            return False
    while True:
        lozinka = getpass.getpass('Lozinka:')
        result = re.search(' ', lozinka)
        if (result !=None): print('Greška, pokušajte ponovo')
        elif (lozinka == ''):
            print('Lozinka ne može biti prazna, pokušajte opet')
        else: break
    ime = input('Ime:')
    prezime = input('Prezime:')
    while True:
        type = input('Menadžer ili prodavac (m/s):')
        if(type != 'm' and type != 's'): print('Greška, pokušajte ponovo')
        else:
            break

    novi_korisnik = {
        "korisnicko_ime": "",
        "lozinka": "",
        "ime": "",
        "prezime": ""
    }
    novi_korisnik['korisnicko_ime'] = korisnicko_ime
    novi_korisnik['lozinka'] = lozinka
    novi_korisnik['ime'] = ime
    novi_korisnik['prezime'] = prezime
    if(type == 'm'): novi_korisnik['tip korisnika'] = 'Menadžer'
    else:
        novi_korisnik['tip korisnika'] = 'Prodavac'
    print('\nKorisnik će biti dodan u bazu podataka:')
    novi_korisnik = [novi_korisnik]
    list(novi_korisnik)
    while True:
        print('\nŽelite li nastaviti?\n1. Da\n2. Ne')
        option = input('Input:')
        if (option == '1'):
            users.append(novi_korisnik)
            break
        elif (option == '2'):
            return False
        else:
            print('Nepostojeća opcija, pokušajte ponovo')
        save(users)
        print('\n%s je dodan u bazu podataka. Tip=[%s]'%(novi_korisnik['korisnicko_ime'], novi_korisnik['tip_korisnika']))
        return False

def manager_register():
    while True:
        korisnicko_ime = input("\nKorisničko ime (input 'Nazad' za povratak):")
        result = re.search(' ', korisnicko_ime)
        if (result != None):
            print('Greška, pokušajte ponovo')
        elif (korisnicko_ime == ''):
            print('Korisničko ime ne može biti prazno, pokušajte ponovo')
        else:
            break
    for user in users:
        if(user['korisnicko_ime'] == korisnicko_ime):
            print('Korisničko ime je zauzeto, pokušajte ponovo')
            if(manager_register() == False):
                return False
        if(korisnicko_ime == 'Nazad'):
            return False
    while True:
        lozinka = getpass.getpass('Lozinka:')
        result = re.search(' ', lozinka)
        if (result != None):
            print('Greška, pokušajte ponovo')
        elif (lozinka == ''):
            print('Lozinka ne može biti prazna, pokušajte ponovo')
        else:
            break
    ime = input('Ime:')
    prezime = input('Prezime:')

    novi_korisnik = {
        "korisnicko_ime": "",
        "lozinka": "",
        "ime": "",
        "prezime": ""
    }
    novi_korisnik['korisnicko_ime'] = korisnicko_ime
    novi_korisnik['lozinka'] = lozinka
    novi_korisnik['ime'] = ime
    novi_korisnik['prezime'] = prezime
    novi_korisnik ['tip korisnika'] = 'Prodavac'
    print('\nDa li želite da nastavite?\n1. Da\n2. Ne')
    option = input('Input:')
    if (option == '1'):
        users.append(novi_korisnik)

    elif (option == '2'):
        return False
    else:
        print('Nepostojeća opcija, pokušajte ponovo')
    save(users)
    print('\n%s je dodan u bazu podataka. Tip=[%s]' % (novi_korisnik['korisnicko_ime'], novi_korisnik['tip korisnika']))
    return False