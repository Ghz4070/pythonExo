# TP Exceptions : Créer un programme qui permet de saisir 2 nombres : Pour chaque nombre saisi
# on contrôle si il s'agit d'un type entier, pour le 2ieme nombre saisi on contrôle en plus si il est différent de 0.
# Pour le premier nombre saisi, on contrôle en plus si il est un nombre pair. Si tout est bon on fait
# la division du premier par le deuxième

a = input("Veuillez saisir votre premier entier : ")
b = input("Veuillez saisir votre deuxieme entier : ")
error = 0
try:
    a = int(a)
    b = int(b)
except:
    error = error + 1
    print("Les deux entrées ddoivent etre des entiers")
try:
    assert a % 2 == 0
except:
    error = error + 1
    print("Votre premier entier doit etre paire")
try:
    assert a != 0
except:
    error = error + 1
    print("Votre premier entier doit etre superieur a 0")
try:
    assert b != 0
except:
    error = error + 1
    print("Votre deuxieme entier doit etre superieur a 0")
if (error == 0):
    print("La division : {} / {} = {}".format(a, b, a / b))
