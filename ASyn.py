def helloworld():
    return "Hello World!"

def somme(a,b):
    return a+b

def presentation(age,prenom,genre):
    if genre == "H":
        genre = "un homme"
    elif genre == "F" :
        genre = "une femme"
    return "Bonjour, je suis {}, je m'appelle {} et j'ai {} ans.".format(genre, prenom, age)

def romain (chiffre):
    resultat = "" 
    while chiffre > 0 :
        
        if chiffre >= 1000 :
            chiffre -= 1000
            resultat += "M"
        elif chiffre >= 500 :
            chiffre -= 500
            resultat += "D"
        elif chiffre >= 100 :
            chiffre -= 100
            resultat += "C"
        elif chiffre >= 50 :
            chiffre -= 50
            resultat += "L"
        elif chiffre >= 10 :
            chiffre -= 10
            resultat += "X"
        elif chiffre >= 5 :
            chiffre -= 5
            resultat += "V"
        else :
            chiffre -= 1
            resultat += "I" 
    return resultat 
