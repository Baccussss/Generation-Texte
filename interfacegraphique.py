from tkinter import *
from generation_aléatoire_plusieursmot import *


#
# Création de l'application tkinter
#

root = Tk()
root.title("Géneration de texte")

#
# Données du formulaire affiché
#

onevar = BooleanVar(value=False)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=False)
fourvar = BooleanVar(value=False)
fivevar = BooleanVar(value=False)
sixvar = BooleanVar(value=False)
nbrmotvar = IntVar(value=50)


#
# Selection des donnees sources
#

# ligne 1
namelbl = Label(root, text="Choisissez un ou pluieurs auteurs !")
namelbl.grid(column=0, row=0, columnspan=3, pady=(5, 10))

# ligne 2
one = Checkbutton(root, text="Jules Vernes", variable=onevar, onvalue=True)
one.grid(column=0, row=1, padx=(50, 0), sticky='w')

two = Checkbutton(root, text="Stendhal", variable=twovar, onvalue=True)
two.grid(column=1, row=1, padx=(50, 0), sticky='w')

three = Checkbutton(root, text="Zola", variable=threevar, onvalue=True)
three.grid(column=2, row=1, padx=(50, 0), sticky='w')

# ligne 3
four = Checkbutton(root, text="Maupassant", variable=fourvar, onvalue=True)
four.grid(column=0, row=2, padx=(50, 0), sticky='w')

five = Checkbutton(root, text="Camus", variable=fivevar, onvalue=True)
five.grid(column=1, row=2, padx=(50, 0), sticky='w')

six = Checkbutton(root, text="Victor Hugo", variable=sixvar, onvalue=True)
six.grid(column=2, row=2, padx=(50, 0), sticky='w')

#
# Selection de la taille du texte resultat
#

# ligne 4
namelbl2 = Label(root, text="Choisissez un nombre de mot !")
namelbl2.grid(column=0, row=4, columnspan=3, pady=10)

# ligne 5
compt_nbrmot = Spinbox(root, from_=0, to=1000)
compt_nbrmot.grid(column=0, row=5, columnspan=3)

#
# Texte resultat
#

# ligne 6
textm = Text(root, height=15, width=70)
textm.grid(column=0, row=6, columnspan=3, pady=20, padx=20)

#
# Actions du programme

# fonction pour générer le texte


def creation():
    textm.delete("1.0", "end")
    texte = []
    if int(compt_nbrmot.get()) == 0:
        pass
    # si aucun auteur
    if onevar.get() == False and twovar.get() == False and threevar.get() == False:
        textm.insert(INSERT, "Il faut selectionner un auteur. ")
    # si premier auteur coché !
    if onevar.get() == True:
        with open("Jules_verne.txt", "r", encoding="utf-8") as fichier:
            chaine = fichier.read()
            texte = texte + chaine.split()

    # si deuxieme auteur coché
    if twovar.get() == True:
        with open("leRougeEtLeNoir.txt", "r", encoding="utf-8") as fichier:
            chaine = fichier.read()
            texte = texte + chaine.split()
    if threevar.get() == True:
        with open("zola.txt", "r", encoding="utf-8") as fichier:
            chaine = fichier.read()
            texte = texte + chaine.split()

    textm.insert(INSERT, creation_texte(texte, int(compt_nbrmot.get())))


def effacer():
    textm.delete("1.0", "end")


# fonction pour finir la phrase

def finir_la_phrase():
    textm.insert(INSERT, finir_phrase(textm.get("1.0", "end")))


# ligne 7
generer = Button(root, text="Générer", command=creation)
generer.grid(column=0, row=7, pady=(0, 10))

finir = Button(root, text="Finir la phrase", command=finir_la_phrase)
finir.grid(column=1, row=7, pady=(0, 10))

annule = Button(root, text="Supprimer", command=effacer)
annule.grid(column=2, row=7, pady=(0, 10))

#
# Lancement de l'application
#

root.mainloop()
