'''
Nom    : INI-03_Exercice_5.py
Auteur : Jean-Christophe Serrano
Date   : 11.09.2024
'''

chaine = "apcpedagogie"

find = chaine.find("p")
find1 = chaine.find("p", find+1)

print("Le caractère 'p' se trouve à la position :" ,find ,"dans la chaine")
print("Le caractère 'p' se trouve à la position :" ,find1 ,"dans la chaine")
