a = int(input("Entrez votre premier chiffres: "))
b = int(input("Entrez votre deuxieme chiffres: "))


def add(a, b):
    print(("=" * 36))
    print("{} + {} = {}".format(a, b, round(a + b)))


def sous(a, b):
    print(("=" * 36))
    print("{} - {} = {}".format(a, b, round(a - b)))


def mult(a, b):
    print(("=" * 36))
    print("{} x {} = {}".format(a, b, round(a * b)))


def div(a, b):
    print(("=" * 36))
    print("{} / {} = {}".format(a, b, round(a / b)))


add(a, b)
sous(a, b)
mult(a, b)
div(a, b)
