# feladat 001
"""
Kérjünk be a billentyűzetről a nevünket és írassuk ki a képernyőre! 
Írassuk ki a két szám összegét a képernyőre!
"""



szam_1 = input("Kérek egy számot: ")
szam_1 = int(szam_1 )
szam_3 = float(szam_1)
szam_2 = int(input("Kérek egy másik számot:"))
osszeg = szam_1 + szam_2
print(f"A megadott két szám összege: {osszeg}")
print(f"A szam_1 változó típusa: {type(szam_1)}")
print(f"A szam_2 változó típusa: {type(szam_2)}")
print(f"A osszeg változó típusa: {type(osszeg)}")
print(f"A szam_3 változó típusa: {type(szam_3)}")
print(f"A szam_3 változó értéke: {szam_3}")




