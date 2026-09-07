'''
Nom    : Tkinter.py
Auteur : Jean-Christophe Serrano
Date   : 06.11.2024
'''

from tkinter import *

def dit_bonjour():
    global mon_label, txt_nom
    message = "Hey, " + txt_nom.get() + " bonjour !"
    mon_label.config(text=message)

window = Tk()
window.title("IntroTK")
window.configure(bg='light blue')
window.geometry("400x200")

mon_label = Label(window, text="", bg="light blue")
mon_label.pack()

lbl_nom = Label(window, text="Votre nom", bg="light blue")
lbl_nom.pack(side=LEFT)
txt_nom = Entry(window)
txt_nom.pack(side=LEFT)

mon_boutton = Button(window, text="Dire bonjour", bg="light blue",command=dit_bonjour)
mon_boutton.pack(side=LEFT)

window.mainloop()