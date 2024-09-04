def montantAff()-> int:
    tarif = 0
    poids = 0 

    poidsMaxVerte = 3000
    poidsMaxPrioritaire = 3000
    poidsMaxEcopli = 30000
    typeLettre = input('Entrez le type de la lettre (verte, prioritaire, ecopli)')

    if typeLettre == 'verte' or typeLettre == 'prioritaire' or typeLettre == 'ecopli':
        poids = int(input('Entrez le poids :'))
    else: 
        print('Type non valide, veuillez réessayer.')
        print('type = ', typeLettre)
        montantAff()

    # Lettre verte

    if typeLettre == 'verte':
        count=0
        # Poids et tarifs du type
        listePoids = [20,100,250,500,1000,3000]
        listeTarifs = [116,232,400,600,750,1050]
        if poids > poidsMaxVerte:
            print('Poids maximal atteint pour ce type de lettre!')
        if poids < listePoids[0]:
            return print('Tarif : ' , listeTarifs[0] / 100 , ' euros')
        for e in listePoids :
            if poids < listePoids[count]:
                return print('Tarif : ' , listeTarifs[count] / 100 , ' euros')
            count += 1
        return print('Tarif : ', listeTarifs[count - 1] / 100 , ' euros')
    
    # Lettre prioritaire

    elif typeLettre == 'prioritaire':
        count=0
        # Poids et tarifs du type
        listePoids = [20,100,250,500,3000]
        listeTarifs = [143,286,526,789,1144]
        if poids > poidsMaxPrioritaire:
            print('Poids maximal atteint pour ce type de lettre!')
        if poids < listePoids[0]:
            return print('Tarif : ' , listeTarifs[0] / 100 , ' euros')
        for e in listePoids :
            if poids < listePoids[count]:
                return print('Tarif : ' , listeTarifs[count] / 100 , ' euros')
            count += 1
        return print('Tarif : ', listeTarifs[count - 1] / 100 , ' euros')

    # Lettre éco-pli
    elif typeLettre == 'ecopli':
        count=0
        # Poids et tarifs du type
        listePoids = [20,100,250]
        listeTarifs = [114,228,392]
        if poids > poidsMaxEcopli:
            print('Poids maximal atteint pour ce type de lettre!')
        if poids < listePoids[0]:
            return print('Tarif : ' , listeTarifs[0] / 100 , ' euros')
        for e in listePoids :
            if poids < listePoids[count]:
                return print('Tarif : ' , listeTarifs[count] / 100 , ' euros')
            count += 1
        return print('Tarif : ', listeTarifs[count - 1] / 100 , ' euros')




montantAff()


""""
    # Lettre verte
    if typeLettre == 'verte':
        poidsMax = 3000
        listePoids = [20,100,250,500,1000,3000]
        listeTarifs = [116,232,400,600,750,1050]
        int_tarif = int(''.join(map(str, listeTarifs)))
        if poids > poidsMax:
            print('Poids maximal atteint pour ce type de lettre!')
        for e in listePoids :
            if poids < e:
                tarif += int_tarif
                break
        prixEuros = tarif / 100
        print('INT TARIF ', int_tarif)
        print('TARIF : ', tarif)
        print('PRIX EUROS : ', prixEuros)
        rounded = round(prixEuros, 2)
        print(rounded)
        print('ROUNDED : ', "{:.2f}".format(prixEuros))
        print('REST')
        print('%.2f' % prixEuros)
"""