
def koszont_nevvel(vnev, knev):
    print(f"Szia " + vnev + knev + ", üdv a fedélzeten")

koszont_nevvel("Kiss " ,"Ádám")


print("-------------------------")

#függvény - érték
def koszont_nevvel(nev1):
    uzenet = "Szia" + nev1 + "üdv a fedélzeten!"
    if nev1 == "Ádám1":
        return uzenet
    else:
        return "Hiba!"
print(koszont_nevvel("Ádám"))


print("------------------------")
