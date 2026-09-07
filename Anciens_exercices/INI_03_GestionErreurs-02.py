#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_GestionErreurs-02.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Utilisation des exceptions.
          Programme qui demande un float à l'utilisateur et valide la
          valeur entrée.

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-10-30 02 VCL
  - Ajout de commentaires
  - Revue du code pour qu'il soit en conformité avec la convention de
    codage Python
# 2024-10-10 01 VCL
  - Version initiale
"""


# Définition d'une fonction qui vérifie si une string peut être castée
# en un float.
def is_float(float_string):
    """Renvoie True si une chaîne de caractères peut être castée en
     float, sinon renvoie False
    """
    try:
        my_float = float(float_string)
    except:
        return False
    return True


# ------------
# --- Main ---
# ------------

# Demande un float à l'utilisateur, avec vérification
while not is_float(input("Entrez un Float svp : ")):
    print("On vous a demandé un float")

print("Ahhh enfin !")
