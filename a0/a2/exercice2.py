def positionFor(lst:list,elt:int):
    """Renvoie l'indice d'un élément dans une liste (ou -1 si il n'existe pas dans cette liste)"""
    indice = -1
    for e in lst:
        indice += 1
        if e == elt:
            return indice
    return -1

def positionWhile(lst:list,elt:int):
    """Renvoie l'indice d'un élément dans une liste (ou -1 si il n'existe pas dans cette liste)"""
    indice = 0
    while indice <= len(lst) - 1:
        if elt == lst[indice]:
            return indice
        else:
            indice += 1
    return -1

def nb_occurence(lst:list,e:int)->int:
    occurenceCount = 0
    for elt in lst:
        if elt == e:
            occurenceCount += 1
    return occurenceCount 

def est_triee(lst:list)->bool:
    for i in range(0, len(lst) -1):
        if lst[i] < lst[i+1]:
            i += 1
        else:
            return False
    return True

# def est_trieeWhile(lst:list)->bool:
#     while 


# à tester les assert
print('Test position for 3 : ', positionFor([1,4,10,25,0,7,4],25))
print('Test position while 2 : ' , positionWhile([1,4,10,25,0,7,4],10))
print('Test occurence 2 : ', nb_occurence([1,4,10,25,0,7,4],4))

print('Test est triée True : ', est_triee([1,2,3,6,9,15]))
print('Test est triée False : ', est_triee([1,2,3,2,5,8,10]))

