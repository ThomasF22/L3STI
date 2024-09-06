# def separate(lst:list)->list:
#     separatedList = []
#     for elt in sorted(lst):
#         separatedList.append(elt)
#     return separatedList
# print(separate([1,5,3,0,-4,-9,0,-1,10]))

def separate(lst:list)->list:
    """Renvoie la liste entrée avec ses entiers positifs et négatifs séparés"""
    separatedList= []
    for elt in lst:
        if elt < 0:
            separatedList.insert(0,elt)
        else:
            separatedList.append(elt)
    return separatedList

print(separate([1,5,3,0,-4,-9,0,-1,10]))