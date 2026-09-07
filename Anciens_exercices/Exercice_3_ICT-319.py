'''
Nom    : Exercice_3_ICT-319.py
Auteur : Jean-Christophe Serrano
Date   : 04.12.2024
'''

import tkinter.messagebox
from tkinter import *
from tkinter import messagebox

def calcule():
    try:
        val_revenu_brut = float(txt_revenu_brut.get())
        val_coeff = float(txt_coefficient.get())
        val_jeune = float(txt_jeune.get())
        val_transport = float(txt_transport.get())
        val_rabais = float(txt_rabais.get())

        if check_jeune.get():
            val_jeune = int(txt_jeune.get())
        else:
            val_jeune = 0

        if check_transport.get():
            val_transport = int(txt_transport.get())
        else:
            val_transport = 0

        if check_rabais.get():
            val_rabais = int(txt_rabais.get())
        else:
            val_rabais = 0

        resultat_total = val_revenu_brut / val_coeff - (val_revenu_brut / val_coeff * val_rabais / 100) - val_jeune - val_transport

        lbl_texte.config(text=f"Revenu imposable : fr. {resultat_total}")
    except:
        if len(txt_revenu_brut.get()) == 0:
            messagebox.showerror("Erreur", "Le champ doit etre rempli!")

        if len(txt_coefficient.get()) == 0:
            messagebox.showerror("Erreur", "Le champ doit etre rempli!")

window = Tk()
window.title("Déductions")
window.geometry("300x350")

check_jeune = IntVar()
check_transport = IntVar()
check_rabais = IntVar()


frame_revenu_brut = Frame(window)
frame_revenu_brut.pack(fill=X)

frame_coefficient = Frame(window)
frame_coefficient.pack(fill=X)

frame_case_jeune = Frame(window)
frame_case_jeune.pack(fill=X)

frame_case_transport = Frame(window)
frame_case_transport.pack()

frame_case_rabais = Frame(window)
frame_case_rabais.pack(fill=X)

frame_boutton = Frame(window)
frame_boutton.pack(fill=X)

frame_texte = Frame(window)
frame_texte.pack(fill=X)


lbl_revenu_brut = Label(frame_revenu_brut, text="Revenu annuel brut")
lbl_revenu_brut.pack(side=LEFT, pady=10)

lbl_coefficient = Label(frame_coefficient, text="Coefficient familial")
lbl_coefficient.pack(side=LEFT, pady=10)

txt_revenu_brut = Entry(frame_revenu_brut)
txt_revenu_brut.pack(side=RIGHT, expand=True)

txt_coefficient = Entry(frame_coefficient)
txt_coefficient.pack(side=RIGHT, padx=30, expand=True)

checkbox_jeune = Checkbutton(frame_case_jeune, text="Déduction jeune", variable=check_jeune)
checkbox_jeune.pack(side=LEFT, padx=30)

txt_jeune = Entry(frame_case_jeune)
txt_jeune.pack(padx=30, expand=True)

txt_jeune.insert(0, "900")

checkbox_transport = Checkbutton(frame_case_transport, text="Déduction transport", variable=check_transport)
checkbox_transport.pack(side=LEFT, padx=30)

txt_transport = Entry(frame_case_transport)
txt_transport.pack(padx=30, expand=True)

txt_transport.insert(0, "650")

checkbox_rabais = Checkbutton(frame_case_rabais, text="Rabais fidélité (%)", variable=check_rabais)
checkbox_rabais.pack(side=LEFT, padx=30)

txt_rabais = Entry(frame_case_rabais)
txt_rabais.pack(padx=30, expand=True)

txt_rabais.insert(0, "0")

bt_calcul = Button(frame_boutton, text="Calcul", command=calcule)
bt_calcul.pack(pady=10)

lbl_texte = Label(frame_texte)
lbl_texte.pack(side=RIGHT)
lbl_texte.config(font=("Helvetica bold", 13))

window.mainloop()