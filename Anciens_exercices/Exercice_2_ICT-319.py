'''
Nom    : Exercice_2_ICT-319.py
Auteur : Jean-Christophe Serrano
Date   : 13.11.2024
'''
from tkinter import *

nombre_boutton = 0

def boutton_plus_local():
    plus = int(txt_nb_points.get())
    lbl_points_local.config(text=f"points : {nombre_boutton+1}")

def boutton_plus_invite():
    plus = int(txt_nb_points.get())
    lbl_points_invite.config(text=f"points : {nombre_boutton}")

window = Tk()

window.title("Score")

window_width = 500
window_height = 200

window.geometry(f"{window_width}x{window_height}")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_left = int(screen_width /2 - window_width/2)
y_top = int(screen_height /2 - window_height/2)

window.geometry("+{}+{}".format(x_left, y_top))

frame_top = LabelFrame(window)
frame_top.pack(fill=X)

frame_center = LabelFrame(window)
frame_center.pack(fill=X)

frame_bottom_left = LabelFrame(window)
frame_bottom_left.pack(side=LEFT, expand=True, fill=BOTH)

frame_bottom_right = LabelFrame(window)
frame_bottom_right.pack(side=RIGHT, expand=True, fill=BOTH)

frame_bottom_left_button = LabelFrame(frame_bottom_left)
frame_bottom_left_button.pack(side=BOTTOM, expand=True)

frame_bottom_right_button = LabelFrame(frame_bottom_right)
frame_bottom_right_button.pack(side=BOTTOM, expand=True)


lbl_nb_sets = Label(frame_top, text="Nombre de sets")
lbl_nb_sets.pack(side=LEFT)

txt_nb_sets = Entry(frame_top)
txt_nb_sets.pack(side=LEFT)

lbl_nb_points = Label(frame_center, text="Nombre de points")
lbl_nb_points.pack(side=LEFT)

txt_nb_points = Entry(frame_center)
txt_nb_points.pack(side=LEFT)


lbl_local = Label(frame_bottom_left, text="Local :")
lbl_local.pack(side=TOP)

lbl_sets_local = Label(frame_bottom_left, text="sets : 0")
lbl_sets_local.pack(side=TOP)

lbl_points_local = Label(frame_bottom_left, text="points : 0")
lbl_points_local.pack(side=TOP)

bt_plus_local = Button(frame_bottom_left_button, text="+", command=boutton_plus_local)
bt_plus_local.pack(side=LEFT, padx=10)

bt_moins_local = Button(frame_bottom_left_button, text="-")
bt_moins_local.pack(side=RIGHT, padx=10)


lbl_invite = Label(frame_bottom_right, text="Invité :")
lbl_invite.pack(side=TOP)

lbl_sets_invite = Label(frame_bottom_right, text="sets : 0")
lbl_sets_invite.pack(side=TOP)

lbl_points_invite = Label(frame_bottom_right, text="points : 0")
lbl_points_invite.pack(side=TOP)

bt_plus_invite = Button(frame_bottom_right_button, text="+", command=boutton_plus_invite)
bt_plus_invite.pack(side=LEFT, padx=10)

bt_moins_invite = Button(frame_bottom_right_button, text="-")
bt_moins_invite.pack(side=RIGHT, padx=10)



window.mainloop()