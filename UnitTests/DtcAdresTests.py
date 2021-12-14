import unittest

from ModelGenerator.BaseClasses.ComplexField import ComplexAttributen, ComplexField
from OTLClasses.Verification.AIMObject import AIMObject
from OTLClasses.Verification.DtcAdres import DtcAdres


class TestClass(AIMObject):
    def __init__(self):
        AIMObject.__init__(self)
        self.testAdres = DtcAdres()


class DtcAdresTests(unittest.TestCase):
    def test_UseTestClassToTestDtcAdres(self):
        instance = TestClass()
        self.assertTrue(isinstance(instance.testAdres, DtcAdres))
        self.assertTrue(isinstance(instance.testAdres, ComplexField))
        self.assertTrue(isinstance(instance.testAdres.waarde, ComplexAttributen))

        instance.testAdres.bus.waarde = "A"
        self.assertFalse(instance.testAdres.waarde is None)
        self.assertEqual(instance.testAdres.bus.waarde, "A")
        self.assertEqual(instance.testAdres.waarde.bus.waarde, "A")

        instance.testAdres.postcode.waarde = "2880"
        self.assertEqual(instance.testAdres.postcode.waarde, "2880")
        self.assertEqual(instance.testAdres.waarde.postcode.waarde, "2880")
        with self.assertRaises(ValueError):
            instance.testAdres.postcode.waarde = 2880

        instance.testAdres.gemeente.set_value_by_label("de Haan")
        self.assertTrue(instance.testAdres.gemeente.waarde.invulwaarde == "de-Haan")

        self.assertTrue(instance.testAdres.waarde.default() is not None)
        self.assertEqual(instance.testAdres.waarde.default()["bus"], "A")
        self.assertEqual(instance.testAdres.waarde.default()["postcode"], "2880")
        self.assertEqual(instance.testAdres.waarde.default()["gemeente"], "de-Haan")