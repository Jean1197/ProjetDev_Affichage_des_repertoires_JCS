#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Boucles-07.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Utilisation de la fonction de 'string'.isdigit().
          Programme qui affiche toutes les valeurs entre deux nombres entiers
          avec vérification de l'entrée et que le deuxième nombre soit plus
          grand que le premier

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-10-30 02 VCL
  - Ajout de commentaires
  - Revue du code pour qu'il soit en conformité avec la convention de
    codage Python
# 2024-09-26 01 VCL
  - Version initiale
"""

# Demande un nombre entier à l'utilisateur et valide le nombre entré,
# avec utilisation de break pour sortir de la boucle
while True:
    nombre1 = input("Entrez un nombre entier : ")
    if nombre1.isdigit():
        break

nombre1 = int(nombre1)

# Demande un deuxième nombre entier à l'utilisateur et valide le nombre
# entré, ainsi qu'il soit plus grand que le premier, avec utilisation
# d'une variable pour sortir de la boucle
pas_entier = True
while pas_entier:
    nombre2 = input("Entrez un deuxième nombre entier : ")
    if nombre2.isdigit():
        if int(nombre2) > nombre1:
            pas_entier = False
        else:
            print("Le nombre doit être plus grand que", nombre1)

# Affiche tous les chiffres entre les deux nombres entiers
for chiffre in range(nombre1, int(nombre2)+1):
    print (chiffre)
