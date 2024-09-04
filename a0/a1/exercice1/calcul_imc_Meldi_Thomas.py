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

test_imc()



# Exercice 2

def est_bissextile(annee:int)-> bool:
    if annee % 4 == 0 and annee % 100 != 0:
        return True
    elif annee % 400 == 0:
        return True
    else:
        return False

def test_bissextile():
    print(est_bissextile(2000))
    print(est_bissextile(2100))
    print(est_bissextile(2024))
# test_bissextile()