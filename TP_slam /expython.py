'''voyage scolaire, vinci location, natation facture et salaire net'''

eleves = int(input("Nombre d'élèves : "))
duree = int(input("Durée du voyage en jours : "))

# Transport par élève
if eleves > 25:
    transport = 100
else:
    transport = 110

# Hébergement par élève
if eleves < 20:
    hebergement = 4.20 * duree
elif eleves <= 35:
    hebergement = 3.80 * duree
else:
    hebergement = 4.00 * duree

# Nourriture par élève
nourriture = 3.50 * duree

totale = hebergement + nourriture + transport

print("Le prix du voyage revient à ", totale, " euros à par élève.")