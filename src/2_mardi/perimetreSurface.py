def perimetre(a, b):
    print(("=" * 36))
    print("votre perimetre est de {}".format(round(float(a * b / 2))))


def surface(a, b):
    print(("=" * 36))
    print("votre surface est de {}".format(round(float(a * b))))


a = int(input("saisir la longueur: "))
b = int(input("saisir la largeur: "))

perimetre(a, b)
surface(a, b)
