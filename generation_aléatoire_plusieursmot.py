from __future__ import print_function
from encodings import utf_8
from itertools import chain
from random import *


with open("zola.txt", "r", encoding="utf-8") as fichier:
    chaine = fichier.read()
    listMots = chaine.split()


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
    moyenne = somme/len(dico)
    return moyenne


def creation_texte(liste_mots, nbr):
    if nbr == 0:
        return "Vous n'avez pas séléctionné le nombre de mots."
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


#print(creation_texte(listMots, 100))


def finir_phrase(chaine):
    # split pour recuperer les deux derniers mots de la chaine
    tab_chaine = chaine.split()
    # chaine pour terminer le mot avec 1 pour que la condition puisse exister
    t = "1 1"
    t_split = t.split()

    # si la chaine fini deja par un point alors Rien
    if chaine[-1] == "!" or chaine[-1] == "?" or chaine[-1] == ".":
        pass
    else:
        # tant que le dernier caractere n'est pas un point
        while t_split[-1][-1] != "." and t_split[-2][-1] != ".":
            t = t + " "
            # premier rajout de caracteres
            if t == "1 1 ":
                t = ""
                car = suitemot(tab_chaine[-2] + " " +
                               tab_chaine[-1], transi_markovmots(listMots))
                t = t + car
            # pour les autres on prend les deux derniers mots de t et chaine de markov
            else:
                tab_t = t.split()
                car = suitemot(tab_t[-2] + " " +
                               tab_t[-1], transi_markovmots(listMots))
                t = t + car
            t_split = t.split()
    if t[-1] == ".":
        return t
    else:  # il faudrait enlever le dernier mot
        n = len(t_split[-1])
        for i in range(n):
            t = t[:-1]
        return t
