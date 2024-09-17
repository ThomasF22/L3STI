from random import *

lst_test= [1,2,3,9,5,100,5,4,8,9]


# Exercice 1

def gen_list_random_int(int_nbr=10, int_binf =0, int_bsup=10)->list:
    result=[]
    for i in range (int_nbr):
        result.append(randrange(int_binf, int_bsup))
    return result

print('Liste aléatoire : ', gen_list_random_int())
