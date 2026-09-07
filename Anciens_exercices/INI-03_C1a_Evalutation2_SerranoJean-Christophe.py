'''
Nom    : INI-03_C1a_Evaluation2_SerranoJean-Christophe.py
Auteur : Jean-Christophe Serrano
Date   : 01.11.2024
'''

année_de_départ = int(input("Entrez une année : "))#demande l'année de départ
population = float(input("Entrez un nombre de population en millions : "))#demande le nombre de population
pourcentage_augmentation = float(input("Entrez un pourcentage en pourcent  : "))#demande le pourcentage d'augmentation

cette_année = 2024

compteur = 0

for compteur in range (année_de_départ+1, cette_année):#affiche de l'année de départ jusqu'au cette année
    print(population, "millions en", compteur)