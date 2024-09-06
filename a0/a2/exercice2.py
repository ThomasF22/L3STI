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
    """Renvoie le nombre d'occurence de e dans une liste lst"""
    occurenceCount = 0
    for elt in lst:
        if elt == e:
            occurenceCount += 1
    return occurenceCount 

def est_trieeFor(lst:list)->bool:
    """Renvoie False si lst est triée par ordre croissant, False sinon (avec boucle for in range)"""
    for i in range(0, len(lst) -1):
        if lst[i] < lst[i+1]:
            i += 1
        else:
            return False
    return True


def est_trieeWhile(lst:list)->bool:
    """Renvoie False si lst est triée par ordre croissant, False sinon (avec boucle while)"""
    count = 0
    while lst[count] != None and count < len(lst)- 1:
        if lst[count] < lst[count+1]:
            count += 1
        else:
            return False
    return True

def position_tri(lst:list,num:int)-> int:
    """Renvoie l'index de l'entier num s'il est dans la liste entrée, -1 sinon"""
    start = 0
    stop = len(lst)
    middle = 0
    while start <= stop:
        middle = (start + stop) // 2
        if lst[middle] == num:
            return middle
        elif lst[middle] < num:
            start = middle + 1
        else:
            stop = middle - 1
    return -1

def a_repetitions(lst:list)->bool:
    """Renvoie True si la liste entrée contient une répétition, False sinon"""
    repetitionList = []
    count = 0
    while count <= len(lst):
        if lst[count] not in repetitionList:
            repetitionList.append(lst[count])
        else:
            return True
        count += 1
    return False


# à tester les assert
# def testFunctions()->bool:
#     assert positionFor([1,4,10,25,0,7,4],25) == 3, ' positionFor OK'

print('Test position for 3 : ', positionFor([1,4,10,25,0,7,4],25))
print('Test position while 2 : ' , positionWhile([1,4,10,25,0,7,4],10))
print('Test occurence 2 : ', nb_occurence([1,4,10,25,0,7,4],4))

print('Test est triée For True : ', est_trieeFor([1,2,3,6,9,15]))
print('Test est triée For False : ', est_trieeFor([1,2,3,2,5,8,10]))

print('Test est triée While True : ', est_trieeWhile([1,2,3,6,9,15]))
print('Test est triée While False : ', est_trieeWhile([1,2,3,2,5,8,10]))

print('Test position tri : ', position_tri([1,2,3,6,9,15],3))
print('Test a repetition True :  ', a_repetitions([1,2,3,2,5,8,10]))
