from tkinter import *
from generation_aléatoire_plusieursmot import *

fenetre = Tk()
fenetre.title("Mon application")
fenetre.geometry("640x480")

var_nbrMots = IntVar()

label_auteur = Label(fenetre, text="Choisissez un ou pluieurs auteurs !")

label_auteur.pack()


auteur1 = Checkbutton(fenetre, text="choix 1")
auteur2 = Checkbutton(fenetre, text="choix 2")
auteur3 = Checkbutton(fenetre, text="choix 3")
auteur1.pack()
auteur2.pack()
auteur3.pack()

label_nbrmot = Label(fenetre, text="Choisissez un nombre de mot !")
compt_nbrmot = Spinbox(fenetre, from_=0, to=1000000, textvariable=var_nbrMots)
label_nbrmot.pack()
compt_nbrmot.pack()


def creation():

    textm.insert(INSERT, creation_texte(listMots, int(compt_nbrmot.get())))


generer = Button(fenetre, text="GENERER", command=creation)
generer.pack()

textm = Text(fenetre, height=15, width=70)
textm.pack()

fin_phrase = Checkbutton(fenetre, text="finir la phrase")
fin_phrase.pack()
fenetre.mainloop()


def pp():
    pass
