'''
Nom    : INI-03_GestionErreurs.py
Auteur : Jean-Christophe Serrano
Date   : 30.10.2024
'''
'''
try:
    # Code pouvant générer une erreur
    nombre = float(input("Entrez un nombre : "))
    resultat = 100 / nombre
except ValueError:
    print("Erreur : Vous devez entrer un nombre valide.")
except ZeroDivisionError:
    print("Erreur : Division par zéro impossible.")
else:
    print("Résultat : ", resultat)
finally:
    print("Bloc finally exécuté, que l'erreur ait eu lieu ou non.")
'''

def is_float(myfloat):
    try:
        floatvalue = float(myfloat)
    except:
        return True
    return False

my_value= input("Entrez un digit : ")
while not is_float(my_value):
    my_value = input("Ce n'est pas un float !")
print("C'est un float")