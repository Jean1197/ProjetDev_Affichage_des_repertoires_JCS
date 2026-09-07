#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Fonctions-03a.py
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


# Traduit des lettres en morse
def fonction_traduit_en_morse(mot) :
    mot_majuscules = mot.upper()  # Met tous les caractères en
                                  # majuscules, étant donné que
                                  # les clés dans le dictionnaire
                                  # sont en majuscule
    # Traduit le mot en morse
    mot_morse = ""
    for char_key in mot_majuscules :
        mot_morse += dictionnaire_morse[char_key] + ' '

    return mot_morse[:-1]  # Enlève le dernier espace


def fonction_traduit_en_texte(mot_morse):
    # Comme le mot morse contient plusieurs symbols morse séparées par
    # des espaces (pour pouvoir les identifier), on isole les symbols
    # dans une liste
    liste_symbols_morse = mot_morse.split(' ')

    # Traduit tous les symbols morse
    mot = ''
    for char in liste_symbols_morse:
        # Demande la position du symbol morse dans le dictionnaire
        pos_char = list(dictionnaire_morse.values()).index(char)
        # Prends la clé (caractère) correspondante (à la même position)
        char_key = list(dictionnaire_morse.keys())[pos_char]
        # Crée le mot avec le caractère trouvé
        mot += char_key

    return mot


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
texte_morse = fonction_traduit_en_morse ("Vitor")

# Affiche le mot 'Vitor' en morse
print ("Vitor en morse donne : ", texte_morse)

# Traduit le mot 'Vitor' de morse en texte
texte = fonction_traduit_en_texte(texte_morse)

# Affiche le texte traduit
print ("Le texte morse traduit donne : ", texte)
