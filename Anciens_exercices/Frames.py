'''
Nom    : Frames.py
Auteur : Jean-Christophe Serrano
Date   : 06.11.2024
'''
from pickle import FRAME
from posixpath import expanduser
from tkinter import *

frame = Tk()
frame.geometry("500x500")

frame_label1 = LabelFrame(frame)
frame_label1.pack(fill=X)

frame_label2 = LabelFrame(frame)
frame_label2.pack(expand=True, fill=BOTH)

frame_label3 = LabelFrame(frame)
frame_label3.pack(fill=X)

frame_button1 = Button(frame_label1, text="Haut/Gauche")
frame_button1.pack(side=LEFT, ipadx=10, ipady=5)

frame_button2 = Button(frame_label1, text="Haut/Droite")
frame_button2.pack(side=RIGHT, ipadx=10, ipady=5)

frame_button3 = Button(frame_label2, text="Bleu")
frame_button3.pack(ipadx=10, ipady=5)

frame_button4 = Button(frame_label2, text="Rouge")
frame_button4.pack(expand=True, ipadx=10, ipady=5)

frame_button5 = Button(frame_label2, text="Stats")
frame_button5.pack(expand=True, ipadx=10, ipady=5)

frame_button6 = Button(frame_label2, text="Quitter")
frame_button6.pack(ipadx=10, ipady=5)

frame_button7 = Button(frame_label3, text="Bas/Gauche")
frame_button7.pack(side=LEFT, ipadx=10, ipady=5)

frame_button8 = Button(frame_label3, text="Bas/Droite")
frame_button8.pack(side=RIGHT, ipadx=10, ipady=5)

frame.mainloop()