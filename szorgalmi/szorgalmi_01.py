#szorgalmi_01

"""
Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
legkisebb értéket ezek közül!
"""
"""
szam1 = input(f"Add meg az első számot: ")
szam2 = input(f"Add meg a második számot: ")
szam3 = input(f"Add meg a harmadik számot: ")
legkisebb_szam = min(szam1, szam2, szam3)

print(f"A legkisebb szám: {legkisebb_szam}")
"""
#szorgalmi_02

"""
Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.
"""

jegy = int(input(f"Add meg a dolgozatod pontszámát: "))

if jegy < 50:
    print(f"Eleg szar lett majd legkozelebb!")
elif 50<=jegy<60:
    print(f"A dolgozatod kettes lett!")
elif 60<=jegy<70:
    print(f"A dolgozatod hármas lett!")
elif 70<=jegy<85:
    print(f"A dolgozatod négyes lett!")
elif jegy>=85:
    print(f"A dolgozatod ötös lett!")
else:
    print(f"Nem adtál jó mnennyiséget")