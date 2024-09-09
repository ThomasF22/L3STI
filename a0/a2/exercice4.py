# from exercice1 import val_max
# (importer la fonction val_max)

# import matplotlib.pyplot as plot

def valeur_max(listL:list)->int:
    """Renvoie l'entier maximum d'une liste"""
    if listL == []:
        return -1
    max = 0
    for elmt in listL:
        if max <= elmt:
            max = elmt
    return max

listFonction=[6,5,6,8,4,2,1,5]
listFonctionInj=[5,2,9,6]
listFonctionSurj=[1,2,3,0]
listFonctionBij=[1,2,3,4,0]


def genHisto(lstFonction:list)->list:
    """Compte le nombre d'occurence de chaque nombre (de 0 à la valeur maximale de la liste entrée 
    et renvoie le résultat en liste

    Args:
        lstFonction (list): La liste à entrer

    Returns:
        list: Liste allant de 0 à la valeur maximale de la liste entrée. Chaque indice correspond au nombre d'occurence de cet indice dans la liste.
    """

    # Compter le nombre d'occurence des nombres de 0 à maxValue et l'insérer dans l'histogramme
    maxValue = valeur_max(lstFonction)
    histoList = [0] * maxValue
    for elt in lstFonction:
        if 0 <= elt <= maxValue -1 :
            histoList[elt] += 1
    return histoList



def est_injective(lstFonction:list)->bool:
    histoList = genHisto(lstFonction)
    for elt in histoList:
        if elt > 1:
            return False
    return True

def est_surjective(lstFonction:list)->bool:
    histoList = genHisto(lstFonction)
    for elt in histoList:
        if elt < 1:
            return False
    return True

def est_bijective(lstFonction:list)->bool:
    if est_injective(lstFonction) and est_surjective(lstFonction):
        return True
    else:
        return False

print(genHisto(listFonction))

print(est_injective(listFonctionInj))


print(est_surjective(listFonctionSurj))

print(est_bijective(listFonctionBij))
