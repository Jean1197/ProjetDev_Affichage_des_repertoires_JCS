#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_GestionErreurs-01a.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Utilisation des exceptions.
          Programme qui utilise une fonction de division pour créer une
          erreur de division par zéro et gérer l'exception.

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


# Fonction qui permet de diviser le chiffre passé en premier argument
# par le chiffre passé en deuxième argument avec gestion de la division
# par zéro
def division(chiffre1, chiffre2):
    try:
        result = chiffre1/chiffre2
    except:
        return None
    finally:
        print("try ... except fait !")
    return result


# ------------
# --- Main ---
# ------------

# Teste la fonction avec une division normale
print("Division normale 6/2 :", division(6, 2))

# Génére une erreur en faisant une division par zéro
print("Division par 0 :", division(6, 0))
