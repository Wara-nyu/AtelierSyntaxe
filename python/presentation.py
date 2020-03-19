def presentation(age, nom, genre):
    genre = "une femme" if genre == "F" else "un homme"
    return "Bonjour, je suis {}, je m'appelle {} et j'ai {} ans.".format(genre, nom, age)
