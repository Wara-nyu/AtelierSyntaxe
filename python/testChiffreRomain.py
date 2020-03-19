import unittest
from ASyn import *

class test_Romain(unittest.TestCase):
    def test_renvoie_I(self):
        self.assertEqual("I", romain(1))

    def test_renvoie_II(self):
        self.assertEqual("II", romain(2))

    def test_renvoie_V(self):
       self.assertEqual("V", romain(5))

    def test_renvoie_X(self):
       self.assertEqual("X", romain(10))

    def test_renvoie_L(self):
       self.assertEqual("L", romain(50))

    def test_renvoie_C(self):
       self.assertEqual("C", romain(100))

    def test_renvoie_D(self):
       self.assertEqual("D", romain(500))

    def test_renvoie_M(self):
       self.assertEqual("M", romain(1000))

    def test_renvoie_IV(self):
       self.assertEqual("IV", romain(4))

unittest.main()
