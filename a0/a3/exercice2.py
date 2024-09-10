

lst_mot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",
"finir", "aimer"]
        


def mots_Nlettres(lst_mot:list,n:int):
    resultat = []
    for elt in lst_mot:
        if len(elt) == n:
            resultat.append(elt)
    if resultat == []:
        return " aucun mot de longeur n dans la liste"
    else: return resultat

print (mots_Nlettres(["jouer","bonjour","punir","aurevoir","revoir","pouvoir","cour","abaour","finir","aimer",],7))

def commence_par(mot:str,prefixe:str):
    long = len(prefixe)
    motPre = mot[:long]       
    if motPre == prefixe :
        return True
    else:
        return False
    
print (commence_par("regarde","reg"))

def fini_par(mot:str,suffixe:str):
    long = len(suffixe)
    motSuf = mot[-long:]       
    if motSuf == suffixe :
        return True
    else:
        return False
    
print (fini_par("barde","de"))

def commencent_par(lst_mot,prefixe):
    resultat = []
    long = len(prefixe)

    for elt in lst_mot:
        eltPre = elt[:long]       
        if eltPre == prefixe :
            resultat.append(elt)
    if resultat == []:
        return " aucun mot de longeur n dans la liste"
    else: return resultat
    
print (commencent_par(["jouer","bonjour","punir","aurevoir","revoir","pouvoir","cour","abaour","finir","aimer",],"ai"))

def finissent_par(lst_mot,suffixe):
    resultat = []
    long = len(suffixe)

    for elt in lst_mot:
        eltPre = elt[-long:]       
        if eltPre == suffixe :
            resultat.append(elt)
    if resultat == []:
        return " aucun mot de longeur n dans la liste"
    else: return resultat
    
print (finissent_par(["jouer","bonjour","punir","aurevoir","revoir","pouvoir","cour","abaour","finir","aimer",],"er"))


def liste_mots(lstMotInput:list, prefixInput:str, suffixInput:str, numLettres:int):
    return mots_Nlettres(commencent_par(finissent_par(lstMotInput, suffixInput), prefixInput), numLettres)


def dictionnaire(fileInput)->list:
    listeMots = []
    file = open(fileInput, "r")
    for line in file:
        if line != "":
            listeMots.append(line)
    return listeMots

print(dictionnaire("a0/a3/littreUTF8.txt"))

print('TEST : ' , liste_mots(lst_mot, 'j', 'r', 5))