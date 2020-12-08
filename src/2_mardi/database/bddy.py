# BASES DE DONNEES
from sqlite3 import *

# CRUD : create, read, update, delete

# Connexion
connection = connect("database/base.db")
cursor = connection.cursor()

new_etudiant = (cursor.lastrowid, "Toto", "Tata", 25)
cursor.execute('INSERT INTO etudiant VALUES(?, ?, ?, ?)', new_etudiant)
connection.commit()
print("le nouvel utilisateur a ete ajouté en BDD")
