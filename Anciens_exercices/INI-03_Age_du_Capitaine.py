'''
Nom : INI-03_Age_du_Capitaine.py
Auteur : Jean-Christophe Serrano
Date : 04.09.2024
'''

prénom = input("C'est quoi ton prénom")

anneeNaissance = input("Entrez votre année de naissance :")

anneeCourante = 2024
age = anneeCourante - int(anneeNaissance)
print("Cette année (" , anneeCourante, ") vous aurez", age, "ans")