'''
Nom    : carré_vide.py
Auteur : Jean-Christophe Serrano
Date   : 26.09.2024
'''

hauteur = int(input("Donner la hauteur")) #demander la hauteuer
largeur = int(input("Donner la largeur")) #demander la largeur

for i in range(1,hauteur+1) :
    if  i == 1 or i == hauteur :
        print("*" * largeur)
    else :
        print("*" + " " * (largeur-2) + "*")
