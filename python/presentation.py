def presentation(age, nom, genre):
    if genre == "H":
        genre = "un homme"
    elif genre == "F":
        genre = "une femme"
    return "Bonjour, je suis {}, je m'appelle {} et j'ai {} ans.".format(genre, nom, age)
