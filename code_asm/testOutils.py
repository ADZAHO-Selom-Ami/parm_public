import unittest
from outils import *

class testOutils(unittest.TestCase):

    def test_traduire_registre(self):
        self.assertEqual(traduireRegistre("  R7  "), "111")
        self.assertEqual(traduireRegistre("  R1  "), "001")
        with self.assertRaises(ValueError):
            traduireRegistre("  #1  ")
        
    
    def test_est_un_registre(self):
        self.assertTrue(estUnRegistre("  R0  "))
        self.assertTrue(estUnRegistre("R7"))
        self.assertFalse(estUnRegistre("#7"))


    def test_traduire_immediat(self):
        self.assertEqual(traduireImmediat("  #1  ", 8), "00000001")
        self.assertEqual(traduireImmediat("  #127  ", 7), "1111111")
        self.assertEqual(traduireImmediat("  #1  ", 7, 4), "0000000")
        self.assertEqual(traduireImmediat("  #127  ", 7, 4), "0011111")
        with self.assertRaises(ValueError):
            traduireImmediat("  R127  ", 4)
        
    
    def test_est_un_immediat(self):
        self.assertTrue(estUnImmediat("  #0  "))
        self.assertTrue(estUnImmediat("#127"))
        self.assertFalse(estUnImmediat("R7"))


    def test_traduire_en_hexadecimal(self):
        self.assertEqual(traduireEnHexadecimal("0000000000000000"), "0000")
        self.assertEqual(traduireEnHexadecimal("1111111111111111"), "ffff")
        self.assertEqual(traduireEnHexadecimal("0100100000101100"), "482c")
        with self.assertRaises(ValueError):
            traduireEnHexadecimal("0000")
            traduireEnHexadecimal("00001111111111111111111111")


    def test_traduire_entier_en_binaire_complement_2(self):
        self.assertEqual(traduireEntierEnBinaireComplement2(15), "00001111")
        self.assertEqual(traduireEntierEnBinaireComplement2(-64), "11000000")
        self.assertEqual(traduireEntierEnBinaireComplement2(-2, 4), "1110")


    def test_traduire_entier_en_binaire_complement_2(self):
        self.assertEqual(traduireEntierEnBinaireComplement2(15), "00001111")
        self.assertEqual(traduireEntierEnBinaireComplement2(-64), "11000000")
        self.assertEqual(traduireEntierEnBinaireComplement2(-2, 4), "1110")

 
    def test_traduire_symbole_egalite(self):
        self.assertEqual(traduireSymboleEgalite("EQ"), "0000")
        self.assertEqual(traduireSymboleEgalite("CS"), "0010")
        self.assertEqual(traduireSymboleEgalite(":("), None)
