honapok = ['január', 'február','március', 'április', 'május', 'június'] 
  
for honap in honapok:
    honap = honap.upper()
    print(honap)



for index in range(len(honapok)):
    honapok[index] = honapok[index].upper()

print(honapok)

for index in range(0,len(honapok),2):
    honapok[index] = honapok[index].lower()

print(honapok)
