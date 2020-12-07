# coding:utf-8
n = int(input("Veuillez saisir la table de multiplication : "))
print("La table de multiplication de : ", n, " est :")
for i in range(1, 11):
    print(n, "x", i, " = ", i * n)
