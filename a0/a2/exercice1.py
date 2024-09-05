def sommeRange(listL:list)->int:
    """Renvoie la somme de la liste entrée (avec for in range)"""
    result = 0
    for i in range(0, len(listL)):
        result += listL[i]
    return result
# print(somme1([3,2,2]))

# Cette fonction est pour moi la meilleure à utiliser
def sommeForIn(listL:list)->int:
    """Renvoie la somme de la liste entrée (avec for in)"""
    result = 0
    for e in listL:
        result += e
    return result
# print(somme2([5,0,3]))

def sommeWhile(listL:list)->int:
    """Renvoie la somme de la liste entrée (avec while et count)"""
    result = 0
    count = 0
    while count < len(listL):
        result += listL[count]
        count += 1
    return result 
# print(somme3([1,1,7]))

def moyenne(listL:list)->int:
    """Renvoie la moyenne des entiers d'une liste"""
    resultat = 0
    if len(listL) != 0:
        resultat = sommeForIn(listL) / len(listL)
    return resultat

def nb_supRange(listL,e)->int:
    """Renvoie le nombre d'éléments d'une liste supérieur à e (avec for in range)"""
    count = 0
    nbSup=0
    for i in range(0, len(listL)):
        if listL[count] > e:
            nbSup += 1
            count += 1
    return nbSup

def nb_supForIn(listL,e)->int:
    """Renvoie le nombre d'éléments d'une liste supérieur à e (avec for in)"""
    nbSup = 0
    for elmt in listL:
        if elmt > e:
            nbSup += 1
    return nbSup

def moy_sup(listL,e)->int:
    """Renvoie la moyenne des éléments d'une liste qui sont supérieur à e"""
    if listL == []:
        print('Liste vide!')
    listSup = []
    for elmt in listL:
        if elmt > e:
            listSup.append(elmt)
    moyenneSup = moyenne(listSup)
    return moyenneSup

def val_max(listL:list)->int:
    """Renvoie l'entier maximum d'une liste"""
    max = 0
    for elmt in listL:
        if max <= elmt:
            max = elmt
    return max

def ind_max(listL:list)->int:
    valMax = val_max(listL)
    return listL.index(valMax)

def test_exercice1()->str:
    """Renvoie des test de chaque fonctions avec une ou plusieurs listes pertinantes."""
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", sommeRange([]))
    #test somme 11111
    lst2test1=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", sommeRange(lst2test1))

    print("Test moyenne : ", moyenne([3,5,1]))
    print("Test moyenne avec négatif : ", moyenne([-5, 10, 15]))

    print("Test nombre sup avec Range : ", nb_supRange([1,2,6,9,4],4))

    print("Test moyenne sup : ", moy_sup([1,3,10,5],4))

    print("Test valeur max : ", val_max([1,0,20,36,9]))

    print("Test indice max : ", ind_max([1,0,20,36,9]))

test_exercice1()
    
