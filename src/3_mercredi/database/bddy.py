# BASES DE DONNEES
from sqlite3 import *

# CRUD : create, read, update, delete

# Connexion
connection = connect("database/base.db")
cursor = connection.cursor()

# POST
# new_etudiant = (cursor.lastrowid, "Toto", "Tata", 25)
# cursor.execute('INSERT INTO etudiant VALUES(?, ?, ?, ?)', new_etudiant)
# connection.commit()
# print("le nouvel utilisateur a ete ajouté en BDD")

# GET
etudiantID = (1,)
cursor.execute('SELECT * FROM etudiant WHERE id=?', etudiantID)
print(cursor.fetchone())

# UPDATE
modif_etudiant = ('ZEC', 'UNION', 20, 1)
cursor.execute('UPDATE etudiant SET firstname=?, lastname=?, age=? WHERE id=?', modif_etudiant)
connection.commit()
print('le nouvel utilisateur a ete mis a jours')

# GET
etudiantID = (1,)
cursor.execute('SELECT * FROM etudiant WHERE id=?', etudiantID)
print(cursor.fetchone())

# DELTE
# del_etudiant = 2,
# cursor.execute('DELETE from etudiant WHERE id=?', del_etudiant)
# connection.commit()
# print("l'etudiant a bien ete supprimer")

# GET ALL
cursor.execute('SELECT * FROM etudiant')
print(cursor.fetchall())

# Fermeture de SQLite
cursor.close()
connection.close()
