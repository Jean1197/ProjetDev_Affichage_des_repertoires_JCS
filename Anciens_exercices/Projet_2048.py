'''
Nom    : Projet_2048.py
Auteur : Jean-Christophe Serrano
Date   : 20.01.2025
'''

import random
from tkinter import *

def pack_4():
    moves = 0

    # Récupérer la première ligne de la grille
    a, b, c, d = nombre[0]

    # Créer une liste avec les valeurs non None
    ligne = [x for x in [a, b, c, d] if x is not None]

    # Compléter avec None à la fin
    while len(ligne) < 4:
        ligne.append(None)

    # Mettre à jour la grille principale
    nombre[0] = ligne

    # Mettre à jour l'affichage
    display_game()

    return a, b, c, d, moves

# Fonction du mise à jour de l'affichage du tableau
def display_game():
    for line in range(len(nombre)):
        for col in range(len(nombre[line])):
            valeur = nombre[line][col]
            couleur = colors.get(int(valeur)) if valeur is not None else "#CCC0B5" # Couleur des cases vides

            labels[line][col] = Label(frame_tableau, text=valeur if valeur is not None else "",
                                      width=12, height=5, borderwidth=1, relief="solid",
                                      bg=couleur)

            labels[line][col].grid(row=line, column=col, padx=5, pady=5)

    return

# Etat du jeu des nombres entre 2 et 2048 (lignes 10-18)
'''
nombre = [
    ["2", "4", "8", "16"],
    ["32", "64", "128", "256"],
    ["512", "1024", "2048", None],
    [None, None, None, None],
]

''' 
# Etat du jeu qui affiche deux "2" aléatoirement sur la grille (lignes 20-31)
nombre = [
    ["2", None, "2", None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]
'''

positions = random.sample([(x, y) for x in range(len(nombre)) for y in range(len(nombre))], 2) # Affichage aléatoire sur la grille (avec ChatGPT)

for x, y in positions:
    nombre[x][y] = "2" # Placer un "2" sur la grille
'''

# Cases vides
labels = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]

# Dictionnaire des codes couleurs
colors = {2 : "#FFFFFF", 4 : "#EDE0C8", 8 : "#F2B179", 16 : "#F59563",
          32 : "#F67C5F", 64 : "#F65E3B", 128 : "#EDCF72", 256 : "#EDCC61",
          512 : "#EDC850", 1024 : "#EDC53F", 2048 : "#EDC22E"}


window = Tk()
window.geometry("500x570")
window.title("2048")

frame_titre_score_top = Frame(window, pady=30)
frame_titre_score_top.pack(fill=X)

frame_titre = Frame(frame_titre_score_top)
frame_titre.pack(side=LEFT)

frame_score = LabelFrame(frame_titre_score_top, borderwidth=3, bg="#006400")
frame_score.pack(side=LEFT, padx=80)

frame_top = LabelFrame(frame_titre_score_top, borderwidth=3, bg="#006400")
frame_top.pack(side=RIGHT, padx=20)

frame_consigne_bouton = Frame(window)
frame_consigne_bouton.pack(fill=X)

frame_tableau = LabelFrame(window, bg="#BBADA0")
frame_tableau.pack(pady=30)

lbl_titre = Label(frame_titre, text="2048", font=('Helvetica', 30))
lbl_titre.pack(padx=20)

lbl_score = Label(frame_score, text="Score \n 0", bg="#006400", fg="#FFFFFF")
lbl_score.pack(padx=20)

lbl_top = Label(frame_top, text="Top \n 0", bg="#006400", fg="#FFFFFF")
lbl_top.pack(padx=24)

lbl_consigne = Label(frame_consigne_bouton, text="Glissez les chiffres et obtenez la tuile 2048.")
lbl_consigne.pack(side=LEFT, padx=20)

bt_nouveau = Button(frame_consigne_bouton, text="Nouveau", bg="#3E3A32", fg="#FFFFFF")
bt_nouveau.pack()

# Boucle qui permet d'afficher le tableau
for line in range(len(nombre)):
    for col in range(len(nombre[line])):
        valeur = nombre[line][col]
        couleur = colors.get(int(valeur)) if valeur is not None else "#CCC0B5" # Couleur des cases vides

        labels[line][col] = Label(frame_tableau, text=valeur if valeur is not None else "",
                                  width=12, height=5, borderwidth=1, relief="solid",
                                  bg=couleur)

        labels[line][col].grid(row=line, column=col, padx=5, pady=5)

window.bind("<Left>", lambda event: pack_4())  # Associer la touche flèche gauche au déplacement

window.mainloop()
