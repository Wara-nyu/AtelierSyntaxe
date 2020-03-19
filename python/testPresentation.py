import unittest
from presentation import *

class testPresentation(unittest.TestCase):

    def test_renvoie_presentation(self):
        self.assertEqual("Bonjour, je suis un homme, je m'appelle Jean et j'ai 20 ans.", presentation("20","Jean","H"))

unittest.main()
