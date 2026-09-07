#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------1---------2---------3---------4---------5---------6---------7---------8
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Dictionnaire-01c.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Utilisation d'un dictionnaire avec une liste de valeurs.
          Programme qu'affiche les mots des chiffres dans différentes
          langues.

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
    "langues": ["FR", "EN", "DE"],
    1: ["un", "one", "eins"],
    2: ["deux", "two", "zwei"],
    3: ["trois", "three", "drei"]
}

# Demande à l'utilisateur de choisir un chiffre parmis ceux existants
# dans le dictionnaire
chiffre = int(input("Choisissez un chiffre "
                + str(list(dictionnaire.keys())[1:]) + " : "))

# Demande à l'utilisateur de choisir la langue dans laquelle il veut
# que le chiffre soit affiché
langue = input("Choisissez la langue " + str(dictionnaire["langues"]) + " : ")

# Determine la position de la langue dans la liste
pos_langue = dictionnaire["langues"].index(langue)

# Affiche le mot en fonction du chiffre et de la langue
print(dictionnaire[chiffre][pos_langue])
