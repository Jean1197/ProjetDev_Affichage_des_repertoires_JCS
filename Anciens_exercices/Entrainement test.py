hauteur = int(input("Donner la hauteur"))#demander la hauteur
largeur = int(input("Donner la largeur"))#demander la largeur

for i in range(1, hauteur+1) :
    if i == 1 or i == hauteur :
        print("*" * largeur)