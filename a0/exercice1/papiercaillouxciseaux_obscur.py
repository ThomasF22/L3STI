import random

cpo = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )
if cpo != 'O' :
    if cpo != 'N' :
        print("Je n'ai pas compris votre réponse")
if cpo == 'O':
    nomJoueur1 = input("Quel est votre nom ? ")
    print("Bienvenu ",nomJoueur1, " nous allons jouer ensemble \n")
    nomJoueur2 = 'Machine'
scoreJoueur1 = 0
np = 0 # nombre parties ?
if cpo == 'N':
    nomJoueur1 = input("Quel est votre nom ? ")
    print("Bienvenu ",nomJoueur1, " nous allons jouer ensemble")
    nomJoueur2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ",nomJoueur2, " nous allons jouer ensemble \n")

c = True
scoreJoueur2 = 0
while c == True:
    np += 1 
    choixJoueur1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ".format(nom=nomJoueur1))
    if choixJoueur1 != 'pierre':
        if choixJoueur1 != 'papier':
            if choixJoueur1 != 'ciseaux':
                if choixJoueur1 != 'puit' :

                    c1ok = False
                    print("Je n'ai pas compris votre réponse")
                    while c1ok == False :
                        print("Joueur ", nomJoueur1)
                        choixJoueur1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
                        c1ok = True
                        if choixJoueur1 != 'pierre': 
                            if choixJoueur1 != 'papier':
                                if choixJoueur1 != 'ciseaux':
                                    c1ok = False

    if cpo == 'O': 
        #il y a un problème si le joueur 2 s'appelle Machine !
        choixJoueur2 = ['papier','pierre','ciseaux','puit'][random.randint(0, 3)]


    if nomJoueur2 != 'Machine':
        print("Joueur", nomJoueur2)
        choixJoueur2 = input("faîtes votre choix parmi (pierre, papier, ciseaux): ")
        if choixJoueur2 != 'pierre':
            if choixJoueur2 != 'papier':
                if choixJoueur2 != 'ciseaux':
                    if choixJoueur2!= 'puit' :
                        j2bon = False #à remplacer avec j2ok 
                        print("Je n'ai pas compris votre réponse")
                        while not j2bon :
                            print("Joueur ", nomJoueur2)
                            choixJoueur2 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
                            j2bon = True
                            if choixJoueur2 != 'pierre': 
                                if choixJoueur2 != 'papier':
                                    if choixJoueur2 != 'ciseaux':
                                        if choixJoueur2 != 'puit' :
                                            j2bon = False

    #On affiche les choix de chacun
    print("Si on récapitule :",nomJoueur1, choixJoueur1, "et", nomJoueur2, choixJoueur2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat

    # egalité
    if choixJoueur1 == choixJoueur2 :
        gagnantRound = "aucun de vous, vous être ex æquo"
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnantRound)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")


    if choixJoueur1 == 'pierre' and choixJoueur2 == 'papier' :
        gagnantRound = nomJoueur2
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 1
        print("le gagnant est",gagnantRound)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")


    if choixJoueur1 == 'pierre' and choixJoueur2 == 'ciseaux' :
        gagnantRound = nomJoueur1
        scoreJoueur1 = scoreJoueur1 + 1
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnantRound)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'papier' and choixJoueur2 == 'ciseaux' :
        gagnantRound = nomJoueur2
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 1
        print("le gagnant est",gagnantRound)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'papier' and choixJoueur2 == 'pierre' :
        gagnantRound = nomJoueur1
        scoreJoueur1 = scoreJoueur1 + 1
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnantRound)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'ciseaux' and choixJoueur2 == 'pierre' :
        gagnantRound = nomJoueur2
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 1
        print("le gagnant est",gagnantRound)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'ciseaux' and choixJoueur2 == 'papier' :
        gagnantRound = nomJoueur1
        scoreJoueur1 = scoreJoueur1 + 1
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnantRound)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    # Le puit

    if choixJoueur1 == 'puit' and choixJoueur2 == 'pierre' :
        gagnantRound = nomJoueur1
        scoreJoueur1 = scoreJoueur1 + 1
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnantRound)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'puit' and choixJoueur2 == 'ciseaux' :
        gagnantRound = nomJoueur1
        scoreJoueur1 = scoreJoueur1 + 1
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnantRound)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'puit' and choixJoueur2 == 'papier' :
        gagnantRound = nomJoueur2
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 1
        print("le gagnant est",gagnantRound)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")    

    if np >= 5:
        c = False
        
    if np <= 5:
        #On propose de c ou de s'arrêter 
        go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nomJoueur1,nomJoueur2))
        if go == 'O':
            c = True
        if go == 'N':
            c = False
        if go != 'O' and go != 'N':
            c = True
            print("Vous ne répondez pas à la question, on continue ")
  
        
if c == False :
    if scoreJoueur1 == scoreJoueur2:
        print('Egalité!')

    else:
        if scoreJoueur1 > scoreJoueur2 : 
            gagnantPartie=nomJoueur1
        else : 
            gagnantPartie=nomJoueur2
        print('Le gagnant est :', gagnantPartie)
    print("Merci d'avoir joué ! A bientôt")