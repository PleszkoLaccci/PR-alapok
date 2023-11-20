import random
szam = int(input(f"Adj meg egy számot 1 és 3 között: "))
generalt_szam = random.randint(1,3)

if szam == generalt_szam:
    print(f"A tipped helyes! {szam} ")
else:
    print("Szar vagy")
