#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : MA-24_pygame-base.py
Authors : Pascal Benzonana, Vitor COVAL
Date    : 2024.11.04
Version : 0.01
Purpose : Bases de de la librairie pygame

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-11-03 01 PBA & VCL
  - Version initiale
"""

# Import de la librairie pygame pour pouvoir utiliser ses fonctions
# ATTENTION !!! LE MODULE PYGAME DOIT ÊTRE INSTALLÉ !!!
import pygame

# ------------
# --- MAIN ---
# ------------

# La première instructions à faire est d'initialiser la librairie pygame
pygame.init()

# Le module display sert à contrôler la fenêtre et l'affichage. La
# fonction set_mode permet de définir la taille de la fenêtre
# graphique. Elle retourne un objet de type Surface
screen = pygame.display.set_mode((500,300))

# Pour afficher le logo de votre application (icône) il faut utiliser
# la fonction set_icon du module display.
# La fonction set_icon attends en paramètre un objet de type Surface.
# La fonction load du module image permet de charger un fichier image
# et de retourner un objet de type Surface.
# (sur le site https://www.pygame.org/docs/ref/image.html se trouve
# les différents types d'image acceptés par la fonction)
icon = pygame.image.load("pictures\\International_draughts.png")
#pygame.display.set_icon(icon)

# Pour afficher le nom de votre application, vous pouvez utiliser la
# fonction set_caption du module display.
pygame.display.set_caption("MA-24 : Bases de pygame")

# Pour changer tout ou partie de la couleur du fond (body) de votre
# application, vous pouvez utiliser la fonction fill du module Surface.
screen.fill((89, 152, 255))

# Pour dessiner des formes sur votre application, vous pouvez utiliser
# les différentes fonctions du module draw. Si après un exemple avec
# la fonction rect, utilisée pour dessiner un rectangle.
pygame.draw.rect(screen, (10,10,10),(10, 10, 30, 20),0)

# Pour redimensionner une image, vous pouvez utiliser le module
# transform de pygame.
icon = pygame.transform.scale(icon, (500, 500))

# Pour dessiner une image dans une autre image, vous pouvez utiliser
# la fonction blit du module Surface. Afin de rendre visible votre
# nouvel insert, vous pouvez utiliser la fonction flip du module
# display.
screen.blit(icon, (200, 200))
pygame.display.flip()

# Ci-après vous avez un exemple de boucle qui gére les événements
# de votre application.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        btn_presse = pygame.key.get_pressed()
        if btn_presse[pygame.K_RIGHT]:
            bouge_droite()
        elif btn_presse[pygame.K_LEFT]:
            bouge_gauche()
        elif btn_presse[pygame.K_q]:
            running = False
        pygame.display.update()

pygame.quit()
