#feladat_pelda
#be: szam
#ki: a szam negativ



def beker_egy_szamot():
    szam = int(input("Kérek egy egész számot: "))
    print(szam)

def beker_egy_szamot1(parameter1):
    szam1 = int(input("Kérek egy egész számot: "))
    szam1 = szam1 + parameter1
    print(szam1)

def szamok_oszege():
    return 15+9

beker_egy_szamot()
beker_egy_szamot()
beker_egy_szamot1(100)
osszeg = szamok_oszege()
print(osszeg)
szamok_oszege()




"""
szam = int(input("Adj meg egy számot! "))
if szam < 0:
    print(f"A megadott szám {szam} negatív.")
print(f">> A program vége <<")
"""

#be: szam
#ki: a szam negativ vagy nem negativ
"""
szam = int(input('Adj meg egy számot! '))
if szam < 0:
      print(f'A megadott szám {szam} negatív.')
else:
      print(f'A megadott szám nem negatív.')
print('>> A program vége! <<')
"""
#be: szam
#ki: a szam negativ vagy a szam pozitiv vagy a 0

"""
szam = int(input('Adj meg egy számot! '))
if szam < 0:
      print(f'A megadott szám {szam} negatív.')
elif szam == 0:
      print(f'A megadott szám {szam} nulla.')
else:
      print(f'A megadott szám {szam} pozitív.')
print('>> A program vége! <<')
"""
"""
szam = int(input('Adj meg egy számot! '))
if szam < 0:
      print(f'A megadott szám {szam} negatív.')
elif szam == 0:
      print(f'A megadott szám {szam} nulla.')
else:
      print(f'A megadott szám {szam} pozitív.')
print('>> A program vége! <<')
"""