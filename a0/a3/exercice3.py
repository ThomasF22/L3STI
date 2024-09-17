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
    output = ''
    count = 0
    # for char in mot:
    #     if char == lpos[count]:
    #         output += char
    #     else:
    #         output += ''


    listeChars= []
    for lettre in mot:
        while lettre != lpos[count]:
            output += '-'
        else:
            output += lettre
        count += 1

    return output


# placesLettre('b','bonjour')-> [0]
# placesLettre('m','maman')-> [0,2]

# outputStr('bonjour',[])-> '_ _ _ _ _ _ _'
# outputStr('bonjour',[0,1,4])-> 'b o _ _ o _ _'

def main():
    assert places_lettre('b' , 'bonjour') == [0]
    assert places_lettre('a' , 'bonjour') == []
    assert places_lettre('m' , 'maman') == [0, 2]

    print(places_lettre('b' , 'bonjour'))

    print(outputStr('bonjour', [0,2,3]))

if __name__ == "__main__":
    print("Le script est exécuté directement.")
    main()
else:
    print("Le script est importé comme un module.")



