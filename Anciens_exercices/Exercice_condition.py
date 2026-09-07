'''
Nom    : Exercice_condition.py
Auteur : Jean-Christophe Serrano
Date   : 13.09.2024
'''

clavier = input("a : ")
a = int(clavier)

print("Le reste est :", (a%2))
if a<5 :
    print("a < 5")
elif a % 2 :
    print("a >= 5 et est impair")
else :
    print("a >= 5 et est pair")

print("Fin de condition")

