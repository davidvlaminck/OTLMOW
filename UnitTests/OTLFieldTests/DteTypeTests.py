import decimal
import unittest
from abc import ABC

from OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Classes.AIMObject import AIMObject


class DteTestClass(AIMObject, ABC):
    RALKleur = DteKleurRAL()


class RelatiesTests(unittest.TestCase):
    def test_DteTestClass(self):
        instance = DteTestClass

        self.assertTrue(isinstance(instance.RALKleur, DteKleurRAL))
        self.assertIsNone(instance.RALKleur.eenheidVeld)
        self.assertEqual(None, instance.RALKleur.waarde)

        instance.RALKleur.waarde = "1111"
        self.assertEqual("1111", instance.RALKleur.waarde)

        with self.assertRaises(ValueError):
            instance.RALKleur.waarde = 2.0

        self.assertTrue(isinstance(instance.RALKleur.waardeVeld, StringField))
