# Manipulations simples

# def full_name(nomPrenomEntree:str)->str:
#     nom , prenom = nomPrenomEntree.split()
#     nom.upper()
#     prenom.replace(prenom[0], prenom[0].upper())

#     nomPrenom = nom.upper() + ' ' +  prenom[0]
#     return nomPrenom


# print(full_name('nicolai roshan'))


# (1)

def full_name(nomPrenom:str)->str:
    """Renvoie une chaîne de charactère sous forme NOM Prenom

    Args:
        nomPrenom (str): Nom et prénom 

    Returns:
        str: Une chaîne formattée
    """

    nom, prenom =  nomPrenom.split()
    nomMaj = nom.upper() # NICOLAI
    firstLetter = prenom[0] # R
    lMaj = firstLetter.upper()
    nouveauPrenom = prenom[1:] #oshan
    return   nomMaj + ' ' + lMaj + nouveauPrenom # NICOLAI + R + oshan

print (full_name("nicolai roshan"))


# (2)

str_variable2test = 'bisgambiglia_paul@univ-corse.fr'

def is_mail(mail:str)->tuple:
    code1 = 0
    code2 = 0
    codeRenvoi = (0,0)

    if '@' in mail:
        corpMail , domaineMail = mail.split('@')
        if '.' in domaineMail:
            # NON ce n'est pas juste pour univ-corse!!
            if domaineMail == 'univ-corse.fr':
                if '..' not in mail and corpMail[0] != '.' and domaineMail[0] != '.' and corpMail[-1] != '.' and domaineMail[-1] != '.' :
                    code1 = 1 # OK
                else:
                    code2 = 1 # corp invalide : 2 points consécutifs où un point au début ou à la fin du corps
            else:
                code2 = 3 # domaine invalide
        else:
            code2 = 4 # domaine invalide : pas de point dans le domaine
    else:
        code2 = 2 # corp invalide : pas de @

    codeRenvoi = (code1,code2)
    return codeRenvoi


assert is_mail(str_variable2test) == (1, 0)
assert is_mail('blabla..@univ-corse.fr') == (0, 1)
assert is_mail('bisgambiglia_pauluniv-corse.fr') == (0, 2)
assert is_mail('blabla@domaine.fr') == (0, 3)
assert is_mail('blabaaaa@univcorsefr') == (0, 4)


print(is_mail(str_variable2test))
# print(is_mail('blabla..@univ-corse.fr'))
# print(is_mail('blablaunivcorse.fr'))
# print(is_mail('blabla@domaine.fr'))
# print(is_mail('blabaaaa@univcorsefr'))