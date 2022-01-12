import unittest

from OTLModel.Classes.BitumineuzeLaag import BitumineuzeLaag
from OTLModel.Classes.Lichtmast import Lichtmast
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# TODO testen nakijken
class UnionTypeFieldTests(unittest.TestCase):
    def test_InitClassWithField(self):
        c = Lichtmast()
        self.assertIsNotNone(c)

    def test_GebruikVeldInvalidFieldName(self):
        c = Lichtmast()
        with self.assertRaises(ValueError):
            c.masthoogte.gebruik_veld('badFieldName')

    def test_GebruikVeld1(self):
        c = Lichtmast()
        c.masthoogte.gebruik_veld('afwijkendeHoogte')
        self.assertEqual('afwijkendeHoogte', c.masthoogte.actiefVeld.naam)

    def test_AssignBeforGebruikVeld(self):
        c = Lichtmast()
        with self.assertRaises(RuntimeError):
            c.masthoogte.waarde = KwantWrdInMeter(7.5)

    def test_AssignField1BadValue(self):
        c = Lichtmast()
        c.masthoogte.gebruik_veld('afwijkendeHoogte')

        with self.assertRaises(ValueError):
            c.masthoogte.actiefVeld.waarde = "2"

    def test_AssignField1(self):
        c = Lichtmast()
        c.masthoogte.gebruik_veld('afwijkendeHoogte')
        c.masthoogte.actiefVeld.waarde = 7.5
        self.assertEqual(7.5, c.masthoogte.actiefVeld.waarde)
        self.assertEqual(7.5, c.masthoogte.waarde)

    def test_AssignField2(self):
        c = Lichtmast()
        c.masthoogte.gebruik_veld('standaardHoogte')
        c.masthoogte.actiefVeld.set_value_by_invulwaarde('10.00')
        self.assertEqual("10.00", c.masthoogte.actiefVeld.waarde.invulwaarde)
        self.assertEqual("10.00", c.masthoogte.waarde.invulwaarde)

    def test_AssignField2BadValue(self):
        c = Lichtmast()
        c.masthoogte.gebruik_veld('standaardHoogte')
        with self.assertRaises(ValueError):
            c.masthoogte.actiefVeld.set_value_by_invulwaarde("2")

    def test_AssignField_BitumineuzeLaag(self):
        b = BitumineuzeLaag()
        b.laagtype.gebruik_veld('profileerlaag')
        b.laagtype.actiefVeld.waarde.gewicht = 500
        self.assertEqual(500, b.laagtype.waarde.gewicht)

        b.laagtype.gebruik_veld('laagtype')
        b.laagtype.actiefVeld.set_value_by_invulwaarde('onderlaag')
        self.assertEqual('onderlaag', b.laagtype.waarde.invulwaarde)

