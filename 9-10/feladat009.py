

szam = int(input("Írj be egyszámot: "))
print(f"A megadott számod: {szam}")


"""
if szam <= 10:
    print(f"A szám kisebb vagy egyenlő mint 10! ")
else:
    print(f"A szám nagyobb mint 10!")
"""


if szam <= 10 or szam == 100:
    print(f"A szám kisebb vagy egyenlő mint 10 vagy a szám egyenlő 100-zal! ")
else:
    print(f"A szám nem kisebb vagy egyenlő mint 10 vagy a szám egyenlő 100-zal! ")