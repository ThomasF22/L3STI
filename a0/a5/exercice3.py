# Exercice 3
from random import *

lst_test=[1,2,3,9,5,100,5,4,8,9]

def choose_element_list(list_in_which_to_choose:list)->int:
    randomIndex = randint(0,len(list_in_which_to_choose) - 1)
    return list_in_which_to_choose[randomIndex]

print('Element aléatoire : ' , choose_element_list(lst_test))