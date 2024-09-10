"""
Nom du fichier : exercice3.py
Description : Exercice 3 de l'atelier 3
Auteur : Thomas
Date : 10 septembre 2024
"""


def places_lettre(charInput:str, wordInput:str)->list:

    listeIndexLettres = []
    index = 0
    # On parcours le mot et ajoute à la liste des index l'index où se trouve le caractère 
    for char in wordInput:
        if char == charInput :
            listeIndexLettres.append(index)
        index += 1
    return listeIndexLettres

def outputStr(mot:str , lpos:list)->str:
    


def main():
    assert places_lettre('b' , 'bonjour') == [0]
    assert places_lettre('a' , 'bonjour') == []
    assert places_lettre('m' , 'maman') == [0, 2]

    print(places_lettre('b' , 'bonjour'))

if __name__ == "__main__":
    print("Le script est exécuté directement.")
    main()
else:
    print("Le script est importé comme un module.")
