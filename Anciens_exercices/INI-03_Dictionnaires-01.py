'''
Nom    : INI-03_C1a_Dictionnaires.py
Auteur : Jean-Christophe Serrano
Date   : 02.10.2024
'''

dictionnaire = {
    "langue" : ["FR", "EN", "DE"],
    1 : ["un", "one", "eins"],
    2 : ["deux", "two", "zwei"],
    3 : ["trois", "three", "drei"]
}

dict_keys = dictionnaire.keys()
langue = input("Choisissez une langue : ")

for dictKey in dict_keys :

    if langue == (dictionnaire["langue"][0]):
        print("La valeur de la clé", dictKey, "est", dictionnaire[dictKey][0])
    elif langue == (dictionnaire["langue"][1]):
        print("La valeur de la clé", dictKey, "est", dictionnaire[dictKey][1])
    elif langue == (dictionnaire["langue"][2]):
        print("La valeur de la clé", dictKey, "est", dictionnaire[dictKey][2])
