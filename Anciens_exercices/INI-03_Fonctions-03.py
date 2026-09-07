#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Fonctions-03.py
Author  : Vitor COVAL
Date    : 2024.10.31
Version : 0.02
Purpose : Utilisation des fonctions.
          Programme qui traduit en morse (reprends l'exercice
          INI-03_Dictionnaire-02).

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


# Traduit du text en morse
def fonction_traduit_en_morse(mot_ascii) :
    mot_majuscules = mot_ascii.upper()  # Met tous les caractères en
                                        # majuscules, étant donné que
                                        # les clés dans le dictionnaire
                                        # sont en majuscule
    # Traduit le mot ASCII en morse
    mot_morse = ""
    for char_key in mot_majuscules :
        mot_morse += dictionnaire_morse[char_key] + ' '

    return mot_morse


# ------------
# --- Main ---
# ------------

# Initialisation du dictionnaire
dictionnaire_morse = {
    'A' : ".-",
    'B': "-...",
    'C': "-.-.",
    'D': "-..",
    'E': ".",
    'F': "..-.",
    'G': "--.",
    'H': "....",
    'I': "..",
    'J': ".---",
    'K': "-.-",
    'L': ".-..",
    'M': "--",
    'N': "-.",
    'O': "---",
    'P': ".--.",
    'Q': "--.-",
    'R': ".-.",
    'S': "...",
    'T': "-",
    'U': "..-",
    'V': "...-",
    'W': ".--",
    'X': "-..-",
    'Y': "-.--",
    'Z': "--..",
}

# Traduit le mot 'Vitor' en morse
texte_morse = fonction_traduit_en_morse("Vitor")

# Affiche le mot 'Vitor' en morse
print("Vitor en morse donne : ", texte_morse)
