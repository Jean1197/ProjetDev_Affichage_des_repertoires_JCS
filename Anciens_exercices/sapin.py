'''
Nom    : sapin.py
Auteur : Jean-Christophe Serrano
Date   : 26.09.2024
'''

hauteur = int(input("Donner la hauteur"))
largeur = int(input("Donner la largeur"))

for i in range(1,hauteur+1) :
        print(" " * (largeur-i) + "*" * (i*2-1))
for o in range(2):
        print(' ' * (hauteur - 2) + '***')