from __future__ import print_function
from encodings import utf_8
from itertools import chain
from random import *
from this import d


with open("Zemmourdiscours", "r", encoding="utf-8") as fichier:
    chaine = fichier.read()
    listMots = chaine.split()

n = ["je" for i in range(10)]


def transi_markovmots(listMots):
    dico = {}
    n = len(listMots)
    for i in range(1, n-2):
        # si 2 mots d'affilés pas dans le dico
        t = listMots[i-1] + " " + listMots[i]
        if listMots[i-1] + " " + listMots[i] not in dico:
            # on les ajoute
            dico[t] = {}
            dico[t][listMots[i+1]+" " + listMots[i+2]] = 1
        else:
            k = listMots[i+1]+" " + listMots[i+2]
            if k not in dico[t]:

                dico[t][listMots[i+1]+" " + listMots[i+2]] = 1
            else:
                dico[t][listMots[i+1] + " " + listMots[i+2]] += 1
    return dico


def suitemot(mot, dico):
    # permet de choisir aleatoirement le mot suivant
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


def moyenneoccurence(dico):
    # nombre moyen de cle par dictionnaire
    somme = 0
    for cle in dico:
        for elt in cle:
            somme = somme + 1
    print(somme)
    print(len(dico))
    moyenne = somme/len(dico)
    return moyenne


def creation_texte(liste_mots, nbr):
    # creation d'un texte de n mots en preant en compte les probas du dictionnaire des transiions
    texte = ""
    d = transi_markovmots(liste_mots)
    # premier mot choisi aleatoirement
    n = len(liste_mots)
    lettre = randint(0, 25)
    lettre = chr(65 + lettre)  # majuscule
    mots_potentiels = []
    for cle in d:
        if cle[0] == lettre:
            mots_potentiels.append(cle)

    longueur = len(mots_potentiels)
    indice = randint(0, longueur-1)

    mot = mots_potentiels[indice]

    texte = texte + mot + " "

    # reste des mots du texte
    for i in range(nbr//2):
        if i == 0:
            # suite du premier mot
            car = suitemot(mot, d)
        else:
            car = suitemot(car, d)  # autre mot
        texte = texte + car + " "
    return texte


print(creation_texte(listMots, 100))


# def finir_phrase(chaine):
#     t = ""
#     if chaine[-1] == "!" or "?" or ".":
#         pass
#     else:
#         while t[-1] != "!" or "?" or ".":
#             car = suitemot(deux_derniers_mots, d)
#             t = t + car
#     print(t)
