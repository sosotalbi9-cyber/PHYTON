#code pin 
'''ce programme vérifie si un code pin est correct ou non ''' 
'''
pin = int(input("Entrez le code pin : "))
if pin == 4567 :
    print("code correct !")
else : 
    print("code incorrect !")
'''

#Signe d'un nombre 
'''Écrire un programme qui demande à un utilisateur un nombre entier puis qui affiche “Positif” 
si ce nombre est supérieur à 0, “Négatif” si ce nombre est inférieur à 0 ou “Nul” si ce nombre vaut 0.'''

'''nbr_entier = int(input("entrer un nombre entier : "))
if nbr_entier > 0 : 
    print("Positif")
elif nbr_entier < 0 :
    print("Negatif")
else :
    print("nul")
'''

#Parité
'''on doit verifié si un nombre estpair ou impaire'''

'''nbr_entier = int(input("saisir un nombre entier : "))
if (nbr_entier % 2) == 0 : 
    print(nbr_entier, "est un nombre pair")
else : 
    print(nbr_entier, "est un nombre impair")'''

#Age

'''on doit ecrire un programme qui verifie si l'utilisateur 
est un enfant un adolescent ou un adulte'''

'''age = int(input("Entrer votre âge : "))
if age <= 12 :
    print(f"A {age}ans, vous êtes un enfant.")
elif age >=12 and age < 18 :
    print(f"A {age}ans, vous êtes un adolescent.")
else : 
    print(f"A {age}ans, vous êtes un adulte.") '''

#Perte ou profit

'''je dois ecrire un programme qui evalue si une vente est un profit ou une perte '''
'''prix_fabrication = float(input("Entrer le prix de fabrication : "))
prix_vente = float(input("Entrer le prix de vente : "))
if prix_vente > prix_fabrication :
    print("Profit")
else : 
    print("perte")'''

#Maximum
'''
Le programme permet d'afficher le maximum entre 3 nombres
'''

'''nbr1 = float(input("Entrer le premier nombre : "))
nbr2 = float(input("Entrer le second nombre : "))
nbr3 = float(input("Entrer le troisième nombre : "))
if nbr3 < nbr1 > nbr2 :
    print(f"le maximum est le premier nombre{nbr1} ")
elif nbr1 < nbr2 > nbr3 :
    print(f" le maximum est le second nombre {nbr2}")
else :
    print(f"le maximum est le troisième nombre {nbr3} ")'''

#Triangle rectangle 
'''
Le but est de verifié si un triangle est rectangle ou non
'''

'''cote1 = float(input("Entrer la longueur du cote le plus petit : "))
cote2 = float(input("Entrer la longueur du coté deuxième plus petit : "))
cote3 = float(input("entrer le cote le plus grand : "))
if cote2 > cote3 or cote2 > cote1 :
    print("Les longueurs des côtés n’ont pas été saisies dans l’ordre croissant.")
elif cote3 **2 == cote1 **2 + cote2 **2 :
    print("c'est un triangle rectangle ")
else :
    print("Le triangle n'est pas rectangle")

'''

#Année bissextile

'''
On doit vérifié si une année est bissextile ou non 
'''
'''annee = int(input("Saisir une année : "))
if annee %4 ==0 and annee % 100 !=0 or annee %400 ==0 :
    print("Année bissextile")
else :
    print("Année non bissextile")
'''

#Société de transport

'''
On ecrit un programme qui fait varier les prix en fonction de l'age
'''

age = int(input("Saisir votr âge : "))
if 51 > age > 21 :
    print("Le prix de transport est de 10€")
elif age >= 51 :
    print("Le prix de transport est 9€")
if age  < 21 :