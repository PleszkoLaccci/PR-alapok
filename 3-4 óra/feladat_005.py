#feladat_005
#dk 106-oldal

'''
Amikor karakterlánccá alakítunk, az str utasításra van szükség. Programunk 
utolsó két sora ezt a formát ölti
'''
felhasználó_kora = 16
print(f"A felhasználó_kora típusa: {type(felhasználó_kora)}")
felhasználó_kora = str(felhasználó_kora)
print(f"A felhasználó_kora típusa: {type(felhasználó_kora)}")
ilyen = input('És milyen ' + felhasználó_kora + ' évesnek lenni? ')