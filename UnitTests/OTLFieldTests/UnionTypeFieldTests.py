import unittest

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.Classes.Lichtmast import Lichtmast


class UnionTypeFieldTests(unittest.TestCase):
    def test_InitClassWithField(self):
        c = Lichtmast()
        self.assertIsNotNone(c)

    def test_bad_value(self):
        c = Lichtmast()

        with self.assertRaises(ValueError):
            c.masthoogte.standaardHoogte = "10.2"

        with self.assertRaises(CouldNotConvertToCorrectType):
            c.masthoogte.afwijkendeHoogte.waarde = "a"

    # TODO setting complex datatype in unionfield skips the clear_props method :-/
    def test_correct_values(self):
        c = Lichtmast()
        c.masthoogte.afwijkendeHoogte.waarde = 7.5
        self.assertEqual(7.5, c.masthoogte.afwijkendeHoogte.waarde)
        c.masthoogte.standaardHoogte = '10.00'
        self.assertEqual('10.00', c.masthoogte.standaardHoogte)
        self.assertEqual(None, c.masthoogte.afwijkendeHoogte.waarde)
        c.masthoogte.afwijkendeHoogte.waarde = 7.5
        self.assertEqual(7.5, c.masthoogte.afwijkendeHoogte.waarde)
        self.assertEqual(None, c.masthoogte.standaardHoogte)
