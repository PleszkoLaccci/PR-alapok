##szamonkeres01
print("Pleszkó László, PL")
jegy = int(input(f"Kérek egy jegyet 1-5-ig: "))

if jegy == 5:
    print("A jegyed 5, jeles")
elif jegy == 4:
    print("A jegyed 4, jó")
elif jegy == 3:
    print("A jegyed 3, közepes")
elif jegy == 2:
    print("A jegyed 1, elégséges")
elif jegy == 1:
    print("A jegyed 1, elégtelen")
else: 
    print("A jegyed nem megfelelő!")