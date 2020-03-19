import unittest
from Presentation import *

class testPresentation(unittest.TestCase):

    def test_renvoie_presentationF(self):
        self.assertEqual("Bonjour, je suis une femme, je m'appelle Jeanne et j'ai 23 ans.", presentation("23","Jeanne","F"))

    def test_renvoie_presentationiH(self):
        self.assertEqual("Bonjour, je suis un homme, je m'appelle Jean et j'ai 23 ans.", presentation("23","Jean","H"))


unittest.main()
