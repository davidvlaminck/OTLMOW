import unittest

from OTLModel.Classes.Lichtmast import Lichtmast


class UnionTypeFieldTests(unittest.TestCase):
    def test_InitClassWithField(self):
        c = Lichtmast()
        self.assertIsNotNone(c)

    def test_bad_value(self):
        c = Lichtmast()

        with self.assertRaises(ValueError):
            c.masthoogte = "2"
        with self.assertRaises(ValueError):
            c.masthoogte = "10.0"

    def test_correct_values(self):
        c = Lichtmast()
        c.masthoogte = 7.5
        self.assertEqual(7.5, c.masthoogte)
        c.masthoogte = '10.00'
        self.assertEqual('10.00', c.masthoogte)
