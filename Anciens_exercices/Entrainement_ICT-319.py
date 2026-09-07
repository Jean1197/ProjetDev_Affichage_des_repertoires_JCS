'''
Nom    : Tkinter.py
Auteur : Jean-Christophe Serrano
Date   : 26.11.2024
'''

from tkinter import *

def produit():
    try:
        txt_val1.config(bg="white")
        txt_val2.config(bg="white")
        txt_val3.config(bg="white")
        txt_val4.config(bg="white")

        val1 = int(txt_val1.get())
        val2 = int(txt_val2.get())
        val3 = int(txt_val3.get())
        val4 = int(txt_val4.get())

        totale = val1 * val2 * val3 * val4

        lbl_produit.config(text=f"Résultat : {totale}")
    except:
        txt_val1.config(bg="red")
        txt_val2.config(bg="red")
        txt_val3.config(bg="red")
        txt_val4.config(bg="red")

        val1 = (txt_val1.get())
        val2 = (txt_val2.get())
        val3 = (txt_val3.get())
        val4 = (txt_val4.get())

        lbl_produit.config(text="Erreur : Entrez un nombre entier.")


window = Tk()
window.geometry("300x300")


frame_val1 = LabelFrame(window)
frame_val1.pack(fill=X)

frame_val2 = LabelFrame(window)
frame_val2.pack(fill=X)

frame_val3 = LabelFrame(window)
frame_val3.pack(fill=X)

frame_val4 = LabelFrame(window)
frame_val4.pack(fill=X)

frame_bottom = LabelFrame(window)
frame_bottom.pack(fill=BOTH, expand=True)


lbl_val1 = Label(frame_val1, text="Entrez un nombre : ")
lbl_val1.pack(side=LEFT)

txt_val1 = Entry(frame_val1)
txt_val1.pack(side=RIGHT)

lbl_val2 = Label(frame_val2, text="Entrez un deuxième nombre : ")
lbl_val2.pack(side=LEFT)

txt_val2 = Entry(frame_val2)
txt_val2.pack(side=RIGHT)

lbl_val3 = Label(frame_val3, text="Entrez un troisième nombre : ")
lbl_val3.pack(side=LEFT)

txt_val3 = Entry(frame_val3)
txt_val3.pack(side=RIGHT)

lbl_val4 = Label(frame_val4, text="Entrez un dernier nombre : ")
lbl_val4.pack(side=LEFT)

txt_val4 = Entry(frame_val4)
txt_val4.pack(side=RIGHT)


bt_produit = Button(frame_bottom, text="Calculer le produit", command=produit)
bt_produit.pack(pady=10)

lbl_produit = Label(frame_bottom, text="Résultat : ")
lbl_produit.pack()


window.mainloop()
