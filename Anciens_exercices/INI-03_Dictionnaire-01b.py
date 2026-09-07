#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------1---------2---------3---------4---------5---------6---------7---------8
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Dictionnaire-01b.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Lister le contenu d'un dictionnaire.
          Programme qu'affiche toutes les clés et les valeurs contenues
          dans le dictionnaire.

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-10-30 02 VCL
  - Ajout de commentaires
  - Revue du code pour qu'il soit en conformité avec la convention de
    codage Python
# 2024-10-09 01 VCL
  - Version initiale
"""

# Initialisation du dictionnaire
dictionnaire = {
    1: "un",
    2: "deux",
    3: "trois",
    6: "six",
    4: "quatre",
    5: "cinq",
}

# Lit toutes les clés et valeurs d'un dictionnaire
for dict_key in dictionnaire.keys():
    print ("La valeur de la clé '", dict_key, "' est '",
           dictionnaire[dict_key], "'")
