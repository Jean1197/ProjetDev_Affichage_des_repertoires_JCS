#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_List-01b.py
Author  : Vitor COVAL
Date    : 2024.10.31
Version : 0.02
Purpose : Utilisation des Lists.
          Programme qu'affiche la position d'un élément dans la liste.

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-10-31 02 VCL
  - Ajout de commentaires
  - Revue du code pour qu'il soit en conformité avec la convention de
    codage Python
# 2024-10-03 01 VCL
  - Version initiale
"""

# Initialisation de ma variable de type List
liste = [2, 4, 6, 8]

# Affichage de la position de ma valeur
print (liste.index(6))

# Affichage de la position d'une valeur qui n'est pas dans la liste
# (!!! Doit provoquer une erreur !!!)
print (liste.index(5))
