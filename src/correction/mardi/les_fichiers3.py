#Ecriture dans un fichier
try:
	with open("donnees2.txt",'w') as fic:
		fic.write("Bonjour, je suis la première phrase\n")
		fic.write("Bonjour, je suis la deuxième phrase\n")
		fic.write("Bonjour, je suis la troisième phrase\n")
# Gestion de l'erreur
except FileNotFoundError:
	print("fichier introuvable")