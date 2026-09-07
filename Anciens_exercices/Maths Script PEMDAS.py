'''
Nom    : Maths Script PEMDAS.py
Auteur : Jean-Christophe Serrano
Date   : 10.09.2024
'''

expression = input("Entrez une expression mathématique : ")

try:
    resultat = eval(expression)
    print(f"Le résultat de l'expression '{expression}' est : {resultat}")
    print("Félicitations.")
except Exception as e:
    print(f"Il y a eu une erreur dans le calcul de l'expression : {e}")
    print("Désolé, ce n'est pas correct.")
