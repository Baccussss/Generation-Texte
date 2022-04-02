from encodings import utf_8
from random import *

alphabet = [None for i in range(26)]
for i in range(26):
    alphabet[i] = chr(65 + i)

with open("discours.txt", "r", encoding="utf-8") as fichier:
    chaine = fichier.read()


def transi_markov1lettre(chaine):
    # permet de creer un dictionaire avec les caractères et le nombre d'occurences des carctères suivants
    dico = {}
    n = len(chaine)
    for i in range(n-1):
        if chaine[i] not in dico:

            dico[chaine[i]] = {}
            dico[chaine[i]][chaine[i+1]] = 1
        else:
            if chaine[i+1] not in dico[chaine[i]]:
                dico[chaine[i]][chaine[i+1]] = 1
            else:
                dico[chaine[i]][chaine[i+1]] += 1
    return dico


def suitelettre(car, dico):
    D = dico[car]
    somme = 0
    for cle in D:
        somme = somme + D[cle]
    somme = randint(1, somme)

    for cle in D:
        if somme > 0:
            prochain_caractere = cle
        somme = somme - D[cle]

    return prochain_caractere


def creation_texte(chaine, nbr):
    # creation d'un texte de n caractères en preant en compte les probas du dictionnaire des transiions
    texte = ""
    d = transi_markov1lettre(chaine)
    # premier caractère choisi aleatoirement
    premiere_lettre = alphabet[randint(1, 26)]
    premiere_lettre_mini = premiere_lettre.lower()

    print(premiere_lettre_mini)

    texte = texte + premiere_lettre_mini

    # reste des letres du texte
    for i in range(nbr-1):
        if i == 0:
            # suite de la premiere lettre
            car = suitelettre(premiere_lettre_mini, d)
        else:
            car = suitelettre(texte[i], d)  # autre caractères
        texte = texte + car
    return texte


print(transi_markov1lettre(chaine))
print(creation_texte(chaine, 1000))
