

liste1=[1.0, 2.0, 3.0, 4.0, 5.0]
liste2=[]
def somme_recursive(lstInput:list)->float:
    # Si liste vide :
    if not lstInput:
        raise ValueError('La liste est vide')
    elif len(lstInput) == 1:
        return lstInput[0]
    else:
        # Appel de la fonction en excluant le premier élément
        return lstInput[0] + somme_recursive(lstInput[1:])
resultat1 = somme_recursive(liste1)
print("La somme de la liste est :", resultat1)
resultat2 = somme_recursive(liste2)
print("La somme de la liste est :", resultat2)


def factorielle_recursive(numInput:int)->int:
    # Cas : Factoriel de 0 est 1
    if numInput == 0:
        return 1
    else:
        return numInput * factorielle_recursive(numInput - 1)
# Test de la fonction
nombre = 5
resultat = factorielle_recursive(nombre)
print("Le factoriel de", nombre, "est :", resultat)

def longueur(lstInput):
    # Cas liste vide
    if not lstInput:
        return 0
    else:
        return 1 + longueur(lstInput[1:])


def minimum(lstInput):
    # Cas liste à un élément
    if len(lstInput) == 1:
        return lstInput[0]
    else:
        min_rest = minimum(lstInput[1:])
        # Compare le premier élément avec le reste de la liste
        return min(lstInput[0], min_rest)
    
listeMin= [10, 5, 8, 12, 7]
print('Element minimum de la liste : ' , minimum(listeMin))


def listPairs(lstInput:list)->list:
    # Cas de liste vide 
    if not lstInput:
        return []
    else:
        premier_element = lstInput[0]
        reste = lstInput[1:]
        if premier_element % 2==0:
            return [premier_element] + listPairs(reste)
        else:
            return listPairs(reste)

listePairs= [1,5,2,3,10,720,24,33,109,204]
print('Liste pairs :' , listPairs(listePairs))


listeDeListe=[[0,1],[2,3],[4],[6,7]]
def concat_list(lstList:list)->list:
    lstConcat=[]
    if lstList == []:
        return []
    else:
        
print(concat_list(listeDeListe))




def incluse(liste1: list, liste2: list) -> bool:
    #si liste1 est vide alors la liste est incluse
    if  liste1 == [] :
        return True
    # si liste 2 est vide elle ne l'est pas 
    if  liste2 ==  []:
        return False
    
    if liste1[0] == liste2[0]:
        return incluse(liste1[1:], liste2[1:])
    else:
        #vérifie si tout les éléments de la liste1 sont dans la liste2 
        return incluse(liste1, liste2[1:])

print(incluse([], [4, 3]))         
print(incluse([], []))            
print(incluse([1, 2, 6], [1, 2, 3, 5, 6]))  
print(incluse([1, 2, 3], [1, 2]))  