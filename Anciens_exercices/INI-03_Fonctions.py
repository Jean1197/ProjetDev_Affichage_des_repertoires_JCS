'''
Nom    : INI-03_C1a_Dictionnaires.py
Auteur : Jean-Christophe Serrano
Date   : 02.10.2024
'''

liste_de_prenoms = ["Emel", "Yuri", "Alex"]

def fonction_prenoms(prenoms):
    print("Bonjour,", liste_de_prenoms[0])
    print("Bonjour,", liste_de_prenoms[1])
    print("Bonjour,", liste_de_prenoms[2])

def fonction_addition(nombre1, nombre2):
    #print("L'addition de", nombre1, "et", nombre2, "donne :", nombre1 + nombre2)
    return nombre1 + nombre2

def fonction_soustraction(nombre1, nombre2):
    print("La soustraction de", nombre1, "et", nombre2, "donne :", nombre1 - nombre2)

def fonction_division(nombre1, nombre2):
    print("La division de", nombre1, "et", nombre2, "donne :", nombre1 / nombre2)


nb1 = int(input("Entrez nombre1 : "))
nb2 = int(input("Entrez nombre2 : "))

fonction_addition(nb1, nb2)
fonction_soustraction(nb1, nb2)
fonction_division(nb1, nb2)
fonction_prenoms(liste_de_prenoms)