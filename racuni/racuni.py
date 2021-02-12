from beautifultable import BeautifulTable
from racuni.lista_racuna import load
import re

racuni = load()

def print_articles(racun):
    string = ''
    i = 0
    for article in racun['Artikli']:
        string += article['Naslov']
        try:
            if racun['Artikli'][i+1] != None:
                string += '\n'
        except IndexError:
            break
        i += 1
    if racun['Artikli'] != []:
        string += '\n'
    i = 0
    for article in racun['Akcije']:
        string += article['Naslov']
        try:
            if racun['Akcije'][i+1] != None:
                string += '\n'
        except IndexError:
            break
        i += 1
    return string

def print_cene(racun):
    string = ''
    i = 0
    for article in racun['Artikli']:
        string += str(article['Cena'])
        try:
            if racun['Artikli'][i+1] != None:
                string += '\n'
        except IndexError:
            break
        i += 1
    if racun['Akcije'] != []:
        string += '\n'
        i = 0
    for article in racun['Akcije']:
        string += str(article['Cena'])
        try:
            if racun['Akcije'][i+1] != None:
                string += '\n'
        except IndexError:
            break
        i += 1
    return string

def print_table(racun):
    table = BeautifulTable()
    table.maxwidth = 300
    table.rows.append([racun['ID'], racun['Prodavac'], racun['date_time'], print_articles(racun), print_cene(racun), racun['total']])
    table.columns.header = ["ID", "Prodavac", "Vreme", "Artikli", "Nove cene", "Ukupno"]
    print(table)

def all_knjige():
    lista_knjiga = []
    racuni = load()
    for racun in racuni:
        if racun['Artikli'] != []:
            for article in racun['Artikli']:
                lista_knjiga.append(article)
        if racun['Akcije'] != []:
            for article in racun['Akcije']:
                lista_knjiga.append(article)
    return lista_knjiga

def all_akcije():
    lista_knjiga = []
    racuni = load()
    for racun in racuni:
        if racun['Akcije'] != []:
            for article in racun['Akcije']:
                lista_knjiga.append(article)
    return lista_knjiga

def filter_knjige(knjige, key):
    filtered_knjige = []
    term = input('Pretraži:')
    for knjiga in knjige:
        result = re.search(term.lower(), str(knjiga[key]).lower())
        if result != None:
            filtered_knjige.append(knjiga)
    print_table_account(filtered_knjige)

def print_table_account(knjige):
    table = BeautifulTable()
    table.maxwidth = 300
    current_knjige = []
    for current_knjiga in knjige:
        quantity = 0
        book_earnings = 0
        for knjiga in knjige:
            if current_knjiga['Naslov'] == knjiga['Naslov']:
                quantity += 1
                book_earnings += knjiga['Cena']
        if current_knjiga not in current_knjige:
            table.rows.append([current_knjiga['Naslov'], quantity, book_earnings])
            current_knjige.append(current_knjiga)
    table.columns.header = ["Naslov", "Prodato", "Zarada"]
    print(table)

def account():
    while True:
        knjige = all_knjige()
        akcije = all_akcije()
        print('\nPrikazati:')
        print('1. Sve transakcije')
        print('2. Sve knjige prodate preko akcija')
        print('3. Sve knjige prodate od specifičnog autora')
        print('4. Sve knjige prodate od specifičnog izdavača')
        print('5. Sve knjige prodate iz specifične kategorije')
        print('6. Nazad')
        option = input('Izaberite opciju:')
        if option == '1':
            print_table_account(knjige)
        elif option == '2':
            print_table_account(akcije)
        elif option == '3':
            filter_knjige(knjige, 'Autor')
        elif option == '4':
            filter_knjige(knjige, 'Izdavač')
        elif option == '5':
            filter_knjige(knjige, 'Kategorija')
        elif option == '6':
            return False
        else:
            print('Greška, pokušajte ponovo')