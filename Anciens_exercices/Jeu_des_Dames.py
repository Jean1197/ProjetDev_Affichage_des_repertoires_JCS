'''
Nom    : Jeu_des_Dames.py
Auteur : Jean-Christophe Serrano
Date   : 08.11.2024
'''

import pygame
import sys

def dessine_case(case_pos):
    global screen, case_size, cases_blanches, cases_noires, marge_gauche, marge_haut
    color = cases_blanches if case_pos % 2 else cases_noires
    pygame.draw.rect(screen, color,
                     (marge_gauche + case_pos * case_size,
                      marge_haut,
                      case_size,
                      case_size))

case_size = 50
cases_blanches = (255, 255, 255)
cases_noires = (180, 180, 180)
pions_blancs = (255, 255, 255)
pions_noirs = (0, 0, 0)

# Marges autour du damier
marge_gauche = 10
marge_droite = 10
marge_haut = 10
marge_bas = 10

pion_pos = 0

plateau = [0, 1, 0,1,0,1,0,1,0,1]

nb_colonnes = len(plateau)

def bouge_droite():
    global pion_pos, nb_colonnes, marge_haut, marge_gauche, case_size
    if pion_pos < nb_colonnes-1:
        dessine_case(pion_pos)
        pion_pos += 1
        screen.blit(pion, (marge_gauche + case_size*pion_pos, marge_haut))

def bouge_gauche():
    global pion_pos, nb_colonnes, marge_haut, marge_gauche, case_size
    if pion_pos < nb_colonnes+1:
        dessine_case(pion_pos)
        pion_pos -= 1
        screen.blit(pion, (marge_gauche + case_size*pion_pos, marge_haut))

pygame.init()

screen = pygame.display.set_mode((500,50))

pygame.display.set_caption("MA-24 : Bases de pygame")

screen.fill((20, 152, 255))

BLACK = (0,0,0)
WHITE = (255,255,255)

for i in range(10):
        color = BLACK if i % 2 == 0 else WHITE
        pygame.draw.rect(screen, color, (i * 50, 0, 50, 50))

running = True

pion = pygame.image.load("MA-24_pion.png")
pion = pygame.transform.scale(pion, (case_size, case_size))

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


    screen.blit(pion, (0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()