#deuxième methode
#Ouverture du fichier
try:
	with open("donnees.txt",'r') as fic:
		# récupération du contenu
		content = fic.read()
		# affichage
		print(content)
# Gestion de l'erreur
except FileNotFoundError:
	print("fichier introuvable")