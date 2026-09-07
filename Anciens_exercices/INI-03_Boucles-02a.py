#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Boucles-02a.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Utilisation du mot-clé break.
          Le programme affiche les nombres depuis 1 jusqu'au chiffre
          entré par l'utilisateur, mais pas 10 et les suivants.

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

# Demande un entier à l'utilisateur
chiffre = int(input("Entrez un chiffre entier : "))

i = 0  # Utilisation de la variable i comme compteur (souvent
       # utilisée comme cela)

# Affiche les nombres jusqu'au chiffre entré par l'utilisateur
while i < chiffre:
    i += 1
    if i == 10 :
        break  # Instruction qui interrompt la boucle while (sort de la
               # boucle)
    print(i)
