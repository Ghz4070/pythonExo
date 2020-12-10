# Fenetre
import tkinter

"""
StringVar(): chaine de caractère
IntVar() : nombre entier
DoubleVar(): nombre à virgule
BooleanVar() : booléen
"""
#Création de la fenetre globale
root = tkinter.Tk()
#Paramétrer la fenetre globale
root.geometry("400x400")
root.title("Ma Fenetre tkinter")
 
# Initialiser les widgets à afficher (ex Label)
#Label
w = tkinter.Label(root, text = "Hello, tout le monde!")
#Zone de Saisie
var_entry = tkinter.StringVar()
entry = tkinter.Entry(root,textvariable=var_entry)

var_gender = tkinter.IntVar()
radio1 = tkinter.Radiobutton(root,text="Homme",value=1,variable=var_gender)
radio2 = tkinter.Radiobutton(root,text="Femme",value=0,variable=var_gender)

# appliquer le mode d'affichage
w.pack()
entry.pack()
radio1.pack()
radio2.pack()
# Affichage de la fenetre Globle
root.mainloop()