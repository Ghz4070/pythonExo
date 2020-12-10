# Exercice BDD:

# Dans une base de données GestionFormation, créer les tables suivantes:
# Matiere(idMatiere, nomMatiere) exemple : java, python, c#, html, css
# Cursus(idCursus, nomCursus) exemple de cursus : Devops, Developpeur Java, Developpeur C#, Developpeur php
# Etudiant(idEtudiant, nomEtudiant, PrenomEtudiant, age)

# Un cursus regroupe plusieurs etudiants, un étudiant peut s'inscrire a un seul cursus
# Un Cursus peut contenir plusieurs Matiere et une Matiere peut se retrouver dans plusieurs Cursus

# 1- Créer un module (modulebdd.py) qui regroupera les fonctions suivantes
# ajouterMatiere
# ajouterCursus
# ajouterEtudiant

# listerMatiere
# listerCursus
# listerEtudiant

# modifierMatiere
# modifierCursus
# modifierEtudiant

# supprimerMatiere
# supprimerCursus
# supprimerEtudiant

# afficherEtudiantDeCursus (qui affiche les étudiants d'un cursus donné)
# afficherMatiereCursus (qui affiche les matieres d'un cursus donné)
# afficherCursurs (qui affiche les cursus ou on dispense une matiere donnée)

# 2- créer un fichier qui appelle ces méthodes (main.py)
import sys

sys.path.append('..')
from sqlite3 import *
import src.TP_UN.database.config as config
import src.TP_UN.database.modulebdd as module

database = connect("database/gestionFormation.db")

print('Connexion : OK')
config.init(database)

module.add(database, 'JavaScript')

database.close()
