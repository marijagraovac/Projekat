from korisnici import korisnik
from knjige import knjiga
from akcije import akcije
from racuni import racuni

def menu_administrator():
    while True:
        type = 'a'
        knjiga.permissions(type)
        print('\n1. Prikazati sve knjige')
        print('2. Pretražiti knjige')
        print('3. Prikazati sve akcije')
        print('4. Pretražiti akcije')
        print('5. Prijaviti korisnika')
        print('6. Prikazati sve korisnike')
        print('7. Dodati knjigu')
        print('8. Izmeniti knjigu')
        print('9. Izbrisati knjigu')
        print('10. Odjava')
        print('11. Nazad')
        option = input('Izaberite opciju:')
        if option == '1':
            if knjiga.sort() == False:
                menu_administrator()
        elif option == '2':
            if knjiga.search() == False:
                menu_administrator()
        elif option == '3':
            if akcije.sort() == False:
                menu_administrator()
        elif option == '4':
            if akcije.search() == False:
                menu_administrator()
        elif option == '5':
            if korisnik.admin_register() == False:
                menu_administrator()
        elif option == '6':
            if korisnik.sort() == False:
                menu_administrator()
        elif option == '7':
            if knjiga.register() == False:
                menu_administrator()
        elif option == '8':
            if knjiga.edit() == False:
                menu_administrator()
            menu_administrator()
        elif option == '9':
            if knjiga.erase() == False:
                menu_administrator()
        elif option == '10':
            main()
        elif option == '11':
            exit()
        else:
            print('Greška, pokušajte ponovo')

def menu_manager():
    while True:
        type = 'm'
        knjiga.permissions(type)
        print('\n1. Prikaz svih knjiga')
        print('2. Pretraga knjiga')
        print('3. Prikaz svih akcija')
        print('4. Pretraga akcija')
        print('5. Prijava korisnika')
        print('6. Prikaz svih korisnika')
        print('7. Dodati akciju')
        print('8. Nalog')
        print('9. Odjava')
        print('10. Nazad')
        option = input('Izaberite opciju')
        if option == '1':
            if knjiga.sort() == False:
                menu_manager()
        elif option == '2':
            if knjiga.search() == False:
                menu_manager()
        elif option == '3':
            if akcije.sort() == False:
                menu_manager()
        elif option == '4':
            if akcije.search() == False:
                menu_manager()
        elif option == '5':
            if korisnik.manager_register() == False:
                menu_manager()
        elif option == '6':
            if korisnik.sort() == False:
                menu_manager()
        elif option == '7':
            if akcije.register() == False:
                menu_manager()
        elif option == '8':
            if racuni.account() == False:
                menu_manager()
            menu_manager()
        elif option == '9':
            main()
        elif option == '10':
            exit()
        else:
            print('Greška, pokušajte ponovo')

def menu_seller():
    while True:
        type = 's'
        knjiga.permissions(type)
        print('\n1. Prikaz svih knjiga')
        print('2. Pretraga knjiga')
        print('3. Prikaz svih akcija')
        print('4. Pretraga akcija')
        print('5. Prodaja knjiga')
        print('6. Dodati knjigu')
        print('7. Izmena knjige')
        print('8. Obrisati knjigu')
        print('9. Odjava')
        print('10. Nazad')
        option = input('Izaberite opciju:')
        if option == '1':
            if knjiga.sort() == False:
                menu_seller()
        elif option == '2':
            if knjiga.search() == False:
                menu_seller()
        elif option == '3':
            if akcije.sort() == False:
                menu_seller()
        elif option == '4':
            if akcije.search() == False:
                menu_seller()
        elif option == '5':
            if knjiga.sell() == False:
                menu_seller()
        elif option == '6':
            if knjiga.register() == False:
                menu_seller()
        elif option == '7':
            if knjiga.edit() == False:
                menu_seller()
        elif option == '8':
            if knjiga.erase() == False:
                menu_seller()
        elif option == '9':
            main()
        elif option == '10':
            exit()
        else:
            print('Greška, pokušajte ponovo')

def main():
    for i in range(4):
        if i == 3:
            print('Previše neuspešnih pokušaja. Program se gasi sada')
            exit()
        korisnik1 = korisnik.login()
        if korisnik1 != False:
            print('Uspešno. Tip naloga:', korisnik1['Tip'])
            if korisnik1['Tip'] == 'Administrator':
                menu_administrator()
            if korisnik1['Tip'] == 'Menadžer':
                menu_manager()
            if korisnik1['Tip'] == 'Prodavac':
                menu_seller()
        elif korisnik1 == False and i<2:
            print('Neuspešno, pokušajte ponovo')

main()