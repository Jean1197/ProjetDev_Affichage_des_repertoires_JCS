#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Boucles-07a.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Programme qui affiche toutes les valeurs entre deux nombres entiers
          avec vérification de l'entrée et que le deuxième nombre soit
          différent du premier

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

# Demande un nombre entier à l'utilisateur et valide le nombre entré
while True:
    nombre1 = input("Entrez un nombre entier : ")
    if nombre1.isdigit():
        break

# Demande un deuxième nombre entier à l'utilisateur et valide le nombre
# entré, il faut qu'il soit différent du premier nombre
pasEntier = True
while pasEntier:
    nombre2 = input("Entrez un deuxième nombre entier : ")
    if nombre2.isdigit():
        if int(nombre2) != int(nombre1):
            pasEntier = False
        else:
            print("Le nombre doit être différent de "+nombre1)

# Affiche tous les chiffres entre les deux nombres entiers
# indépendament duquel est le plus grand
if nombre1 < nombre2:
    for chiffre in range(int(nombre1), int(nombre2)+1):
        print (chiffre)
else:
    for chiffre in range(int(nombre2), int(nombre1)+1):
        print (chiffre)
