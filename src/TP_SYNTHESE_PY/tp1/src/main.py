from sqlite3 import *
import sys

sys.path.append('..')
import src.TP_SYNTHESE_PY.tp1.database.config as config
import src.TP_UN.database.modulebdd as module

init = ""
while init == "":
    init = input('Do you want init database ? y/N'.lower())

if (init) == "y":
    database = connect("database/banque.db")
    config.init(database)
    print('Connexion : OK')
elif (init) == "n":
    print('Aucune action.')

# module.add(database, 'JavaScript')

database.close()
