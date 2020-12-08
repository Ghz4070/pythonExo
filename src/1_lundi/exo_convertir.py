# Écrire le script convertir.py, qui effectue une conversion euros en dollars. — Le programme commencera par demander
# à l’utilisateur d’indiquer par un caractère ’€’ ou ’$’ la devise du montant qu’il va entrer
# coding:utf-8

EUR = 1.2113
USD = 0.8256


def currencyConverter():
    chosenCurrency = input("Do you wish to convert your euros into \n1)USD \n2)EUR \n\n")
    print(("=" * 36))

    # USD
    if (chosenCurrency) == "1":
        eurAmount = round(float(input("How many euros do you wish to convert into USD ? ")))
        print(("=" * 36))
        print(eurAmount, "€ is", round((eurAmount) * USD, 2), "$." + ("=" * 36))
    # EUR
    if (chosenCurrency) == "2":
        usdAmount = round(float(input("How many dollars do you wish to convert into EUR ? ")))
        print(("=" * 36))
        print(usdAmount, "$ is", round((usdAmount) * USD, 2), "€.\n" + ("=" * 36))

    # Fail
    else:
        print("Error, please try again. \nEnter 1 for USD or 2 for EUR.")


currencyConverter()
