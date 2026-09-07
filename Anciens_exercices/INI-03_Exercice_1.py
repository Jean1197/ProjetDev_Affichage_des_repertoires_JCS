'''
Nom : INI-03_Exercice_1.py
Auteur : Jean-Christophe Serrano
Date : 04.09.2024
'''

anneeActuelle = 2024
anneeNaissance = input("Mettez votre année de naissance :")
ageAnnee = anneeActuelle - int(anneeNaissance) # int() cast string en entier
print("Cette année (" , anneeActuelle, "), vous aurez" ,ageAnnee * 12 ,"mois ")
print("Cette année (" , anneeActuelle, "), vous aurez" ,ageAnnee * 52 ,"semaine ")
print("Cette année (" , anneeActuelle, "), vous aurez" ,ageAnnee * 365 ,"jours ")
print("Cette année (" , anneeActuelle, "), vous aurez" ,ageAnnee * 8760 ,"heures ")
print("Cette année (" , anneeActuelle, "), vous aurez" ,ageAnnee * 525600 ,"minutes ")
print("Cette année (" , anneeActuelle, "), vous aurez" ,ageAnnee * 31536000 ,"secondes ")



