

lst_mot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",
"finir", "aimer"]

def motsNlettres(lstMotInput:list, numLettres:int)->list:
    lstMotNum = []
    for mot in lstMotInput:
        if len(mot) == numLettres:
            lstMotNum.append(mot)
    return lstMotNum

print(motsNlettres(lst_mot, 5))

def commence_par(motInput:str, prefixInput:str)->bool:
    if motInput[0] == prefixInput:
        return True
    else:
        return False
    
def finit_par(motInput:str, suffixInput:str)->bool:
    if motInput[-1] == suffixInput:
        return True
    else:
        return False
    
def finit_par(lstMotInput:str, suffixInput:str)->bool:
    for mot in lstMotInput:
        if mot[-1] == suffixInput:
            return True
        else:
            return False
        
def commencent_par(lstMotInput:list, prefixInput:str)->list:
    for mot in lstMotInput:
        if mot[0] == prefixInput:
            return True
        else:
            return False
        

def liste_mots(lstMotInput:list, prefixInput:str, suffixInput:str, numLettres:int):
    return motsNlettres(commence_par(finit_par(lstMotInput, suffixInput), prefixInput), numLettres)

print(liste_mots(lst_mot, 'j', 'r', 5))