'''
Nom    : INI-03_SI-C1a_Evaluation_SerranoJean-Christophe.py
Auteur : Jean-Christophe Serrano
Date   : 27.09.2024
'''
from turtledemo.penrose import start

min = int(input("Bonjour, j'attends un premier nombre entre 5 et 30 : ")) #demande à l'utilisateur un nombre entre 5 et 30
max = int(input("Bonjour, j'attends un second nombre entre 5 et 30, différent du premier : ")) #demande à l'utilisateur un second nombre entre 5 et 30

print("Donc j'ai compris, je vais travailler avec min=", min, "et max=", max) #affiche le min et le max
print("Le produit de", min,"par", max,"donne", min * max) #affiche le produit du min et max
print("Et on peut l'illustrer par le rectangle suivant de", min,"lignes de", max,"etoiles:") #affiche les caractères

for i in range(1,min+1) : #boucle fort, affiche la hauteur du rectangle
        print("*" * max) #affiche la largeur du rectangle

print("Voici les nombres entre", min," et", max,":") #affiche les caractères

for s in range(min,max+1) : #boucle fort
    print(s, end=" ") #affiche les nombres entre min et max

print(" ") #retour à la ligne
print("Leur somme est :", s-1 + min + max,", on peut l'illustrer par la figure suivante de",s-1 + min + max,"etoiles;") #affiche la somme des nombres entre min et max

for d in range(min,max+1) : #boucle fort
    print(d, ":", end=" ") #affiche les nombres entre min et max avec un " : " pour chaque nombre et retour à la ligne
    print(d * "*") #affiche le produit de 1 et de chaque nombre entre min et max en étoiles