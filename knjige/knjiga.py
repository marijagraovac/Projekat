from knjige.knjigaIO import ucitaj_knjige
from util import bubble_sort


def prikazi_knjige():
    print("-"*20)
    print("1. Sortiranje po naslovu")
    print("2. Sortiranje po autoru")
    print("3. Sortiranje po kategoriji")
    print("4. Sortiranje po izdavacu")
    print("5. Sortiranje po ceni")
    print("-" * 20)

    stavka = int(input("Izaberite stavku: "))
    knjige = ucitaj_knjige()

    if stavka == 1:
        bubble_sort(knjige, "naslov")
    elif stavka == 2:
        bubble_sort(knjige, "autor")
    elif stavka == 3:
        bubble_sort(knjige, "kategorija")
    elif stavka == 4:
        bubble_sort(knjige, "izdavac")
    elif stavka == 5:
        bubble_sort(knjige, "cena")

    ispisi_knjige(knjige)


def ispisi_knjige(knjige):
    zaglavlje = f"{'sifra':<10}" \
               f"{'naslov':<20}" \
               f"{'autor':<20}" \
               f"{'isbn':^20}" \
               f"{'izdavac':^20}" \
               f"{'godina izdanja':^20}" \
               f"{'broj strana':^20}" \
               f"{'cena':^20}" \
               f"{'kategorija':^20}"

    print(zaglavlje)
    print("-"*len(zaglavlje))

    for knjiga in knjige:
        za_ispis = f"{knjiga['sifra']:<10}" \
                   f"{knjiga['naslov']:<20}" \
                   f"{knjiga['autor']:<20}" \
                   f"{knjiga['isbn']:^20}" \
                   f"{knjiga['izdavac']:^20}" \
                   f"{knjiga['godina_izdanja']:^20}" \
                   f"{knjiga['broj_strana']:^20}" \
                   f"{knjiga['cena']:^20}" \
                   f"{knjiga['kategorija']:^20}"
        print(za_ispis)