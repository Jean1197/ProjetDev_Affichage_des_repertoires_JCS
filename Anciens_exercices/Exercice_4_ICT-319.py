'''
Nom    : Exercice_4_ICT-319.py
Auteur : Jean-Christophe Serrano
Date   : 11.12.2024
'''

from tkinter import *




def commande():
    nb_table = int(txt_table.get())
    option_pate = radio.get()
    option_anchois = check_anchois.get()
    option_capres = check_capres.get()
    option_jambon = check_jambon.get()
    option_crevettes = check_crevettes.get()

    section = []

    if check_anchois.get():
        texte_anchois = section.append(option_anchois)
        texte_anchois
    if check_capres.get():
        texte_capres = section.append(option_capres)
        texte_capres
    if check_jambon.get():
        texte_jambon = section.append(option_jambon)
        texte_jambon
    if check_crevettes.get():
        texte_crevettes = section.append(option_crevettes)
        texte_crevettes



    lbl_message.config(text=f"Pour la {nb_table}: pâte {option_pate} avec \n {section[0]}, {section[1]}, {section[2]}, {section[3]}")




window = Tk()
window.geometry("400x250")
window.title("Pizza")

radio = StringVar(value=NO)
check_anchois = StringVar(value=NO)
check_capres = StringVar(value=NO)
check_jambon = StringVar(value=NO)
check_crevettes = StringVar(value=NO)

frame_table = Frame(window)
frame_table.pack(fill=X, padx=10)

frame_pate_graniture = Frame(window)
frame_pate_graniture.pack(fill=BOTH, expand=True)

frame_pate = LabelFrame(frame_pate_graniture, text="Pâte")
frame_pate.pack(side=LEFT, padx=15)

frame_graniture = Frame(frame_pate_graniture)
frame_graniture.pack(side=RIGHT, padx=50)

frame_bt_commande = Frame(window)
frame_bt_commande.pack(fill=X)

frame_message = LabelFrame(window, borderwidth=1, relief="solid")
frame_message.pack()


lbl_table = Label(frame_table, text="Table")
lbl_table.pack(side=LEFT)

txt_table = Entry(frame_table, width=5)
txt_table.pack(side=LEFT, padx=10)

btr_extra_fine = Radiobutton(frame_pate, text="Extra-fine", variable=radio, value="extra_fine")
btr_extra_fine.pack()

btr_fine = Radiobutton(frame_pate, text="Fine          ", variable=radio, value="fine")
btr_fine.pack()

btr_normale = Radiobutton(frame_pate, text="Normale  ", variable=radio, value="normale")
btr_normale.pack()

btr_epaisse = Radiobutton(frame_pate, text="Epaisse     ", variable=radio, value="epaisse")
btr_epaisse.pack()

box_anchois = Checkbutton(frame_graniture, text="Anchois  ", variable=check_anchois, onvalue="anchois")
box_anchois.pack()

box_capres = Checkbutton(frame_graniture, text="Câpres    ", variable=check_capres, onvalue="capres")
box_capres.pack()

box_jambon = Checkbutton(frame_graniture, text="Jambon  ", variable=check_jambon, onvalue="jambon")
box_jambon.pack()

box_crevettes = Checkbutton(frame_graniture, text="Crevettes", variable=check_crevettes, onvalue="crevettes")
box_crevettes.pack()

lbl_commande = Label(frame_bt_commande, text="Commande")
lbl_commande.pack(side=LEFT, padx=15)

bt_commander = Button(frame_bt_commande, text="Commander", command=commande)
bt_commander.pack(side=RIGHT)

lbl_message = Label(frame_message, background="yellow", font=("bold", 15))
lbl_message.pack()

window.mainloop()