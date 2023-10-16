def menut_kiiir(tipus):
    if tipus == 2:
        print("Új adat bevitele")
        print("Kilépés a programból")
    elif tipus == 3:
        print("Új adat bevitele")
        print("Adatok módosítása / törlése")
        print("Kilépés a programból")
    else:
        print("A megadott menüszám érvénytelen")

menuszam = int(input("Kérek egy menüszámot: "))
menut_kiiir(menuszam)