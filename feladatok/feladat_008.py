#feladat_008

'''
Kérjünk be egy jegyet 1-5, és irassuk ki a megadott jegy értékét számmal és szöveggel
'''

jegy = int(input("Kérek egy jegyet 1-5-ig: "))
if jegy == 5:
    print(f"A jegyed: {jegy} jeles.")
elif jegy == 4:
    print(f"A jegyed: {jegy} jó.")
elif jegy == 3:
    print(f"A jegyed: {jegy} középszerű.")
elif jegy == 2:
    print(f"A jegyed: {jegy} elégséges.")
elif jegy == 1:
    print(f"A jegyed: {jegy}, anyu büszke.")