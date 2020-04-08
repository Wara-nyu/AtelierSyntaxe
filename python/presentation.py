def presentation(age, nom, genre):
    genre = "une femme" if genre == "F" else "un homme"
    return "Bonjour, je suis {}, je m'appelle {} et j'ai {} ans.".format(genre, nom, age)

#def presentation2(age,nom,genre):
#    genre = ['F','H']
#    literale = ["une femme", "une homme"]
#    for g,l  in zip(genre, literale):
#        return "Bonjour, je suis {1}, je m'appelle {} et j'ai {} ans.".format(genre, nom, age)
