#Ecriture dans un fichier
try:
	with open("donnees2.txt",'a') as fic:
		fic.write("Bonjour, je suis la quatrième phrase\n")
		fic.write("Bonjour, je suis la cinquième phrase\n")
		fic.write("Bonjour, je suis la sixième phrase\n")
# Gestion de l'erreur
except FileNotFoundError:
	print("fichier introuvable")