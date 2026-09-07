#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------1---------2---------3---------4---------5---------6---------7---------8
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Fonctions-02.py
Author  : Vitor COVAL
Date    : 2024.10.31
Version : 0.02
Purpose : Utilisation des fonctions avec une valeur en retour et du
          mot-clé pass.
          Programme qui définit plusieurs fonctions de calculation mais
          dont une seule est développée (la fonction d'addition).

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-10-31 02 VCL
  - Ajout de commentaires
  - Revue du code pour qu'il soit en conformité avec la convention de
    codage Python
# 2024-10-10 01 VCL
  - Version initiale
"""


# Fonction qui permet d'additioner deux chiffres
def fonction_addition(arg_chiffre_1, arg_chiffre_2):
    print("Total global : ", global_chiffre_1 + global_chiffre_2)
    return arg_chiffre_1 + arg_chiffre_2


# Fonction qui permet de soustraire le chiffre passé en deuxième
# argument au chiffre passé en premier argument
def fonction_soustraction(arg_chiffre_1, arg_chiffre_2):
    pass


# Fonction qui permet de multiplier deux chiffres
def fonction_multiplication(arg_chiffre_1, arg_chiffre_2):
    pass


# Fonction qui permet de diviser le chiffre passé en premier
# argument par le chiffre passé en deuxième argument
def fonction_division(arg_chiffre_1, arg_chiffre_2):
    pass


# ------------
# --- Main ---
# ------------

# Demande à l'utilisateur d'entrer deux chiffres
global_chiffre_1 = int(input("Entrez le premier chiffre :"))
global_chiffre_2 = int(input("Entrez le deuxième chiffre :"))

# Appel de la fonction d'addition
resultat = fonction_addition(global_chiffre_1, global_chiffre_2)
print("Résultat de l'addition :", resultat)

# Appel de la fonction de soustraction
resultat = fonction_soustraction(global_chiffre_1, global_chiffre_2)
print("Résultat de la soustraction :", resultat)

# Appel de la fonction de multiplication
resultat = fonction_multiplication(global_chiffre_1, global_chiffre_2)
print("Résultat de la multiplication :", resultat)

# Appel de la fonction de division
resultat = fonction_division(global_chiffre_1, global_chiffre_2)
print("Résultat de la division :", resultat)
