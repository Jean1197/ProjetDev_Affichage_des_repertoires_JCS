'''
Nom    : Password.py
Auteur : Jean-Christophe Serrano
Date   : 06.11.2024
'''

from tkinter import *

root = Tk()
root.title("Login")
root.configure(bg="white")
root.geometry("350x220")

password_label = Label(text="Password :")
password_label.pack()
password = Entry(show="*")
password.pack(anchor="w", padx=10, pady=5, fill=X)

password_button = Button(text="Enter")
password_button.pack()

root.mainloop()