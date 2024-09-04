import random 
import math

# Exercice 1

IMC = {'0': 'Rien',
    '16.5': 'Dénutrition ou famine',
       '18.5': 'maigreur',
       '25': 'corpulence normale',
       '30': 'surpoids',
       '35': 'obésité modéré',
       '40': 'obésité sévère',
       math.inf: 'obésité morbide'}


def message_imc(imcUtilisateur:float)->str:
    """Prend en paramètre un imc et renvoie son interprétation"""
    listeDesImc=list(IMC.keys())
    count = 0
    message = ''
    while imcUtilisateur > float(listeDesImc[count]):
        count +=1
    message = IMC.get(listeDesImc[count])

    return message

def test_imc():
    """Génère aléatoirement 10 IMC pour tester la fonction message_imc"""
    for i in range(0,10):
        imcRandom = random.randrange(0,100)
        print('Pour une IMC de : ', imcRandom , ' Vous êtes en : ', message_imc(imcRandom))

#test_imc()



# Exercice 2

def est_bissextile(annee:int)-> bool:
    """Vérifie si l'année entrée est bissextile"""
    if annee % 4 == 0 and annee % 100 != 0:
        return True
    elif annee % 400 == 0:
        return True
    else:
        return False

def test_bissextile():
    """Test la fonction est_bissextile()"""
    print(est_bissextile(2000))
    print(est_bissextile(2100))
    print(est_bissextile(2024))
# test_bissextile()

# Exercice 3

def discriminant(a:float,b:float,c:float)->float:
    """Calcule le discriminant d'une équation du second degré ax²+bx+c=0"""
    delta=b*b - 4*a*c
    return delta

def racine_unique(a:float,b:float)->float:
    """Calcule la racine unique d'une équation du second degré"""
    x = -b / (2*a)
    return x

def racine_double(a:float,b:float,delta:float,num:int)-> float:
    """Calcule la racine double d'une équation du second degré"""
    if num == 1:
        resultat = (- b + math.sqrt(delta)) / (2*a)
    elif num == 2:
        resultat = (- b - math.sqrt(delta)) / (2*a)
    else:
        print('Veuillez entrer un numéro de racine entre 1 et 2')
    return resultat

def str_equation(a:float,b:float,c:float)-> str:
    """Renvoie l'équation du second degré en chaîne de caractères"""
    return '{}x² + {}x + {} =   0'.format(a,b,c)


def solution_equation(a:float,b:float,c:float)-> str:
    """Résoud une équation du second degré"""
    message = ''
    delta=discriminant(a,b,c)
    if delta < 0:
        message = 'Solution de l\'équation {} \n Pas de racine réelle'.format(str_equation(a,b,c))
    elif delta == 0:
        message = 'Solution de l\'équation {} \n Racine unique : x = {}'.format(str_equation(a,b,c),racine_unique(a,b))
    else: 
        message = '"Solution de l\'équation {} \n Deux racines : \n x1 = {} \n x2 = {}'.format(str_equation(a,b,c),racine_double(a,b,delta,1)
        ,racine_double(a,b,delta,2))
    return message

#print(solution_equation(2,1,0))

#def equation(a:int,b:int,c:int):
