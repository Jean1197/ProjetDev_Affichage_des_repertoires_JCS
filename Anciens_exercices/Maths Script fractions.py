'''
Nom    : Maths Script fractions.py
Auteur : Jean-Christophe Serrano
Date   : 24.09.2024
'''

from fractions import Fraction

f1 = Fraction(3, 4)

f2 = Fraction(5)

f3 = Fraction('7/8')

print("f1 = ", f1)
print("f2 = ", f2)
print("f3 = ", f3)

resultat_addition = f1 + f2
print("f1 + f2 = ", resultat_addition)

resultat_soustraction = f1 - f2
print("f1 - f2 = ", resultat_soustraction)

resultat_multiplication = f1 * f2
print("f1 * f2 = ", resultat_multiplication)

resultat_division = f1 / f2
