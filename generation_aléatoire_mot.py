from __future__ import print_function
from encodings import utf_8
from itertools import chain
from random import *


with open("discours.txt", "r", encoding="utf-8") as fichier:
    chaine = fichier.read()
    listMots = chaine.split()


def transi_markov1mot(listMots):
    dico = {}
    n = len(listMots)
    for i in range(n-1):
        if listMots[i] not in dico:
            dico[listMots[i]] = {}
            dico[listMots[i]][listMots[i+1]] = 1
        else:
            if listMots[i+1] not in dico[listMots[i]]:
                dico[listMots[i]][listMots[i+1]] = 1
            else:
                dico[listMots[i]][listMots[i+1]] += 1
    return dico


def suitemot(mot, dico):
    D = dico[mot]
    somme = 0
    for cle in D:
        somme = somme + D[cle]
    somme = randint(1, somme)

    for cle in D:
        if somme > 0:
            prochain_caractere = cle
        somme = somme - D[cle]

    return prochain_caractere


def creation_texte(liste_mots, nbr):
    # creation d'un texte de n mots en preant en compte les probas du dictionnaire des transiions
    texte = ""
    d = transi_markov1mot(liste_mots)
    # premier mot choisi aleatoirement
    mot = "je"

    # reste des mots du texte
    for i in range(nbr-1):
        if i == 0:
            # suite du premier mot
            car = suitemot(mot, d)
        else:
            car = suitemot(car, d)  # autre mot
        texte = texte + car + " "
    return texte


# print(creation_texte(listMots, 100))

print(creation_texte(listMots, 500))
