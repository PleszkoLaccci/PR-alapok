
kor = int(input(f"Hány éves vagy? "))

if kor == 0:
    print(f"Még nem születtél meg!")
elif 1<= kor <=5:
    print(f"Éves vagy, még nem jársz iskolába!")
elif 6<= kor <=14:
    print(f"Éves vagy, még általános iskolába jársz!")
elif 15  <= kor <=64:
    print(f"Éves vagy, tanulsz vagy dolgozol!")
elif kor >= 65:
    print(f"Éves vagy több vagy, nyugdíjas vagy!")
elif kor < 0:
    print(f"Tervbe se vagy tag")


