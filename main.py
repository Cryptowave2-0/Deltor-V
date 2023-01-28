# coding: utf-8

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


fenetre = Tk()

# menu barre
def alert():
    showinfo("alerte", "Bravo!")

def edit():
    filename = askopenfilename(title="Ouvrir votre document", filetypes=[('txt files', '.txt'), ('all files', '.*')])
    fichier = open(filename, "r")
    content = fichier.read()
    fichier.close()

    Label(fenetre, text=content).pack(padx=10, pady=10)

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=edit)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

print(dir(Button()))

# INPUT
def recupere():
    showinfo("Alerte", entree.get())
    print(entree.get())

value = StringVar()
value.set("Valeur")
entree = Entry(fenetre, textvariable=value, width=40)
entree.pack(side=RIGHT, padx=10, pady=5)

bouton = Button(fenetre, text="Valider", command=recupere, cursor="target")
bouton.pack(side=TOP, padx=10, pady=5)

Button(fenetre, text ="retour", cursor="target").pack(side=TOP, padx=10, pady=5)



# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack(side=BOTTOM, padx=10, pady=10)

fenetre.mainloop()