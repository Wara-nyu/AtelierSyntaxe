import unittest
from ASyn import *


class testAsyn(unittest.TestCase):
    def test_renvoie_helloworld(self):
        self.assertEqual("Hello World!", helloworld())
    
    def test_renvoie_somme(self):
        self.assertEqual(3, somme(1,2))

    def test_renvoie_presentation(self):
        self.assertEqual("Bonjour, je suis un homme, je m'appelle Jean et j'ai 20 ans.", presentation("20","Jean","H"))
    
class test_Romain(unittest.TestCase):
    def test_renvoie_1(self):
        self.assertEqual("I", romain(1))

    #def
unittest.main()
