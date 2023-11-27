#Pleszkó László 10/b 8
import random
dobas = random.randint(1,3)

tipp = int(input("Fej(1) vagy írás(2)"))
if tipp == dobas:
    print("Eltaláltad")
else:
    print("Nem találtad el!")