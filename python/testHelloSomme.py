import unittest
from helloSomme import *


class testhello(unittest.TestCase):

    def test_renvoie_helloworld(self):
        self.assertEqual("Hello World!", helloworld())

    def test_renvoie_somme(self):
        self.assertEqual(3, somme(1,2))

unittest.main()
