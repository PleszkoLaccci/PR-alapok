#listak bejarasa indexxel

honapok = ['január', 'február','március', 'április', 'május', 'június'] 
  
index = 0
for honap in honapok:
      print(index, honap)
      index = index + 1
print("2. futás")
for honap in honapok:
      print(f"A honapok lista indexe: {index},  honap")
      index = index + 1