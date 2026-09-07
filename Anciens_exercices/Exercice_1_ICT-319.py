'''
Nom    : Exercice_1_ICT-319.py
Auteur : Jean-Christophe Serrano
Date   : 06.11.2024
'''
from pickle import FRAME
from posixpath import expanduser
from tkinter import *

window_width = 400
window_height = 400

window = Tk()
window.title("Fenêtre")

window.geometry(f"{window_width}x{window_height}")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_left = int(screen_width /2 - window_width/2)
y_top = int(screen_height /2 - window_height/2)

window.geometry("+{}+{}".format(x_left, y_top))

def window_haut_gauche():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_left = int(screen_width /5.5 - window_width /1.1)
    y_top = int(screen_height /5.5 - window_height /2)
    window.geometry("+{}+{}".format(x_left, y_top))

def window_haut_droite():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_left = int(screen_width /1.1 - window_width /1.7 )
    y_top = int(screen_height /2 - window_height *1.35 )
    window.geometry("+{}+{}".format(x_left, y_top))

def window_bas_gauche():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_left = int(screen_width /5.5 - window_width /1.1 )
    y_top = int(screen_height - window_height *1.18 )
    window.geometry("+{}+{}".format(x_left, y_top))

def window_bas_droite():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_left = int(screen_width /1.1 - window_width /1.7 )
    y_top = int(screen_height *1.15 - window_height *1.6 )
    window.geometry("+{}+{}".format(x_left, y_top))

def fond_bleu():
    frame_top.configure(bg="blue")
    frame_center.configure(bg="blue")
    frame_bottom.configure(bg="blue")

def fond_rouge():
    frame_top.configure(bg="red")
    frame_center.configure(bg="red")
    frame_bottom.configure(bg="red")

def quitter():
    quit()

frame_top = LabelFrame(window)
frame_top.pack(fill=X)

frame_center = LabelFrame(window)
frame_center.pack(expand=True, fill=BOTH)

frame_bottom = LabelFrame(window)
frame_bottom.pack(fill=X)

bt_haut_gauche = Button(frame_top, text="Haut/Gauche", command=window_haut_gauche)
bt_haut_gauche.pack(side=LEFT, ipadx=10, ipady=5)

bt_haut_droite = Button(frame_top, text="Haut/Droite", command=window_haut_droite)
bt_haut_droite.pack(side=RIGHT, ipadx=10, ipady=5)

bt_centre_bleu = Button(frame_center, text="Bleu", command=fond_bleu)
bt_centre_bleu.pack(ipadx=10, ipady=5)

bt_centre_rouge = Button(frame_center, text="Rouge", command=fond_rouge)
bt_centre_rouge.pack(expand=True, ipadx=10, ipady=5)

bt_centre_stats = Button(frame_center, text="Stats", )
bt_centre_stats.pack(expand=True, ipadx=10, ipady=5)

bt_centre_quitter = Button(frame_center, text="Quitter", command=quitter)
bt_centre_quitter.pack(ipadx=10, ipady=5)

bt_bas_gauche = Button(frame_bottom, text="Bas/Gauche", command=window_bas_gauche)
bt_bas_gauche.pack(side=LEFT, ipadx=10, ipady=5)

bt_bas_droite = Button(frame_bottom, text="Bas/Droite", command=window_bas_droite)
bt_bas_droite.pack(side=RIGHT, ipadx=10, ipady=5)

window.mainloop()