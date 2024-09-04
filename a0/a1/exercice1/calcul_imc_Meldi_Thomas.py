import random 

IMC = {'0': 'Rien',
    '16.5': 'Dénutrition ou famine',
       '18.5': 'maigreur',
       '25': 'corpulence normale',
       '30': 'surpoids',
       '35': 'obésité modéré',
       '40': 'obésité sévère',
       '100': 'obésité morbide'}


def message_imc(imcUtilisateur:float)->str:
    """Prend en paramètre un imc et renvoie son interprétation"""
    listeDesImc=list(IMC.keys())
    count = 1
    start = True
    message = ''
    # On parcours la liste des IMC pour déterminer l'interpretation correspondante
    for e in IMC:
        if float(listeDesImc[count - 1]) <= imcUtilisateur < float(listeDesImc[count]) and start == True:
            start = False
            message = IMC.get(listeDesImc[count])
        count += 1
    return message
#print(message_imc(14))

def test_imc():
    """Génère aléatoirement 10 IMC pour tester la fonction message_imc"""
    for i in range(0,10):
        imcRandom = random.randrange(0,100)
        print('Pour une IMC de : ', imcRandom , ' Vous êtes en : ', message_imc(imcRandom))

test_imc()