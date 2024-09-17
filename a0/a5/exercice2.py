# Exercice 2
from random import *

lst_test=[1,2,3,9,5,100,5,4,8,9]

def mix_list(list_to_mix:list)->list:
    lstResult=[]
    lstIndex=[]
    while len(lstIndex) != len(list_to_mix) :
        nbRandom = randint(0,len(list_to_mix) - 1)
        if nbRandom not in lstIndex:
            lstIndex.append(nbRandom)
    # in range plutôt ?
    for i in range (len(lstIndex)):
        lstResult.append(lstIndex[i])

    return lstResult

print('Liste mixée : ', mix_list(lst_test))