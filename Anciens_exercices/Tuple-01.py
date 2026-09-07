'''
Nom    : Tuple.py
Auteur : Jean-Christophe Serrano
Date   : 04.10.2024
'''

objet1 = (2, 4, 6, 8)

print(objet1)
print(type(objet1))
print(len(objet1))
print(objet1[3])

objet2 = (6,)
print(type(objet2))
print(objet2)

objet3 = objet1 + (10, 12, 14, 16) + objet2

print(objet3)
print(len(objet3))
print(objet3.count(6))
position = objet3.index(6)
print(objet3.index(6))
print(objet3.index(6, objet3.index(6)+1))

print(objet3[2:7])


if 7 in objet3 :
    print("est dans objet3")
else:
    print("n'est pas dans objet 3")

print(objet1)

(variable1, *variable2, variable3) = objet3

print(variable1)
print(variable2)
print(variable3)



