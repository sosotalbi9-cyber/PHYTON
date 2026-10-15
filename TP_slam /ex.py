remn = 0.0

gra = input("grade 1 ou 2 : ")
zom = input("zone 1, 2 ou 3 : ")
durm = int(input("durée en jours : "))
CA = float(input("rentrer CA : "))

if gra == "1":
    remn += 500.0
else:
    remn += 600.0

if zom == "1":
    remn += 30.0 * durm
elif zom == "2":
    remn += 25.0 * durm
elif zom == "3":
    remn += 20.0 * durm
else:
    pass

if CA >= 10000.0:
    remn += CA * (5 / 100)
else:
    remn += CA * (2 / 100)
    
print(remn)