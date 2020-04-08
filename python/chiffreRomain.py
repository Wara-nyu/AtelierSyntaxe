def romain(chiffre):
    conversion = {
            1000 : 'M',
            500  : 'D',
            100  : 'C',
            50   : 'L',
            10   : 'X',
            5    : 'V',
            1    : 'I',
            0    : None
    }
    resultat = "" 
    while chiffre > 0 :
#        if chiffre >= 1000 :
#            chiffre -= 1000
#            resultat += "M"
#        elif chiffre >= 500 :
#            chiffre -= 500
#            resultat += "D"
#        elif chiffre >= 100 :
#            chiffre -= 100
#            resultat += "C"
#        elif chiffre >= 50 :
#            chiffre -= 50
#            resultat += "L"
#        elif chiffre >= 10 :
#            chiffre -= 10
#            resultat += "X"
#        elif chiffre >= 5 :
#            chiffre -= 5
#            resultat += "V"
#        else :
#            chiffre -= 1
#            resultat += "I" 
#
        for nombre, romain in convertion.items():
            chiffre -= nombre
            resultat += romain
    return resultat 
