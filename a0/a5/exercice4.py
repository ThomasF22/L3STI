# Exercice 4
from random import *

lst_test=[1,2,3,9,5,100,5,4,8,9]


def extract_elements_list(list_in_which_to_choose:list, int_nbr_of_element_to_extract:int)->list:
    lstResult=[]
    lstIndex=[]
    # cas si nbr > len list
    if int_nbr_of_element_to_extract > len(lstIndex):
        return 0
    while len(lstIndex) <= int_nbr_of_element_to_extract:
        nbRandom = randint(0, len(list_in_which_to_choose) - 1)
        if nbRandom not in lstIndex:
            lstIndex.append(nbRandom)
    for i in range (len(lstIndex) - 1):
        lstResult.append(list_in_which_to_choose[lstIndex[i]])
    return lstResult

print('Echantillions : ' , extract_elements_list(lst_test, 3))