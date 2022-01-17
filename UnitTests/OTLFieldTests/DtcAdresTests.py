import unittest

from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcAdres import DtcAdres


class TestClass(AIMObject):
    def __init__(self):
        AIMObject.__init__(self)
        self.testAdres = DtcAdres()


class DtcAdresTests(unittest.TestCase):
    def test_UseTestClassToTestDtcAdres(self):
        instance = TestClass()
        self.assertTrue(isinstance(instance.testAdres, DtcAdres))
        self.assertTrue(isinstance(instance.testAdres, ComplexField))

        instance.testAdres.bus = "A"
        self.assertFalse(instance.testAdres is None)
        self.assertEqual(instance.testAdres.bus, "A")


        instance.testAdres.postcode.waarde = "2880"
        self.assertEqual(instance.testAdres.postcode, "2880")
        with self.assertRaises(ValueError):
            instance.testAdres.postcode = 2880

        instance.testAdres.gemeente = "de Haan"
        self.assertTrue(instance.testAdres.gemeente == "de-Haan")

        self.assertTrue(instance.testAdres.default() is not None)
        self.assertEqual(instance.testAdres.default()["bus"], "A")
        self.assertEqual(instance.testAdres.default()["postcode"], "2880")
        self.assertEqual(instance.testAdres.default()["gemeente"], "de-Haan")
