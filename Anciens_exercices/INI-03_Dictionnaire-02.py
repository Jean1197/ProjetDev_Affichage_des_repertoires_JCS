#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Dictionnaire-02.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Utilisation d'un dictionnaire.
          Programme qu'affiche les lettres en morse.

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-10-30 02 VCL
  - Ajout de commentaires
  - Revue du code pour qu'il soit en conformité avec la convention de
    codage Python
# 2024-10-03 01 VCL
  - Version initiale
"""

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

# Affiche le prénom VITOR en morse
print (dictionnaire_morse["V"], end=" ")
print (dictionnaire_morse["I"], end=" ")
print (dictionnaire_morse["T"], end=" ")
print (dictionnaire_morse["O"], end=" ")
print (dictionnaire_morse["R"], end=" ")