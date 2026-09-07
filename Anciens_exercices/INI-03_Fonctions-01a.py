#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------1---------2---------3---------4---------5---------6---------7---------8
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Fonctions-01a.py
Author  : Vitor COVAL
Date    : 2024.10.31
Version : 0.02
Purpose : Utilisation des fonctions, avec des paramètres.
          Programme qui affiche bonjour avec le nom de la personne.

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


# Définition d'une fonction qui dit bonjour à une personne dont le nom
# est le premier argument
def fonction_dit_bonjour(arg_nom):
    print("Bonjour", arg_nom)


# ------------
# --- Main ---
# ------------

# Appel (demande à la fonction de s'exécuter) de la fonction qui dit
# bonjour avec le nom de la personne passé en paramètre.
fonction_dit_bonjour("Mouldi")
fonction_dit_bonjour("Pang")
fonction_dit_bonjour("Ahmet")

# Appel de la fonction qui dit bonjour avec le nom de la personne passé
# en paramètre avec une variable.
nom = input ("Quel est votre nom ? ")
fonction_dit_bonjour(nom)