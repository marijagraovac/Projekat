from korisnici.korisnik import prijava
from knjige.knjiga import prikazi_knjige


def meni_administrator(ulogovani_korisnik):
    while True:
        print()
        print("-"*20)
        print("1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("10. Kraj")
        print("-" * 20)

        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            print("PRETRAGA KNJIGA")
        elif stavka == 10:
            return
        else:
            print("Pogresan izbor!")



def main():
    ulogovani_korisnik = prijava()

    if ulogovani_korisnik is not None:
        if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
            meni_administrator(ulogovani_korisnik)
        elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
            pass
        elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
            pass
        else:
            print("Greska! Nepostojeca uloga!")


main()