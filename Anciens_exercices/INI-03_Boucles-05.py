#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Boucles-05.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Utilisation de range.
          Programme qui affiche toutes les valeurs entre deux nombres
          entiers.

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

# Demande un nombre entier à l'utilisateur
nombre1 = input("Entrez un nombre entier : ")

# Demande un deuxième nombre entier à l'utilisateur
nombre2 = input("Entrez un deuxième nombre entier : ")

# Affiche tous les chiffres entre les deux nombres entiers
for chiffre in range(int(nombre1), int(nombre2)+1):
    print(chiffre)
