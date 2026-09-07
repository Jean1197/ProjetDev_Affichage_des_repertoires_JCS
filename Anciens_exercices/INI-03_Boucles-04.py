#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Boucles-04.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Utilisation de for.
          Programme qui écrit le texte entré par l'utilisateur à la
          verticale.

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

# Demande un texte à l'utilisateur
texte = input("Entrez un texte : ")

# Affiche le texte à la verticale
for char in texte :
    print(char)
