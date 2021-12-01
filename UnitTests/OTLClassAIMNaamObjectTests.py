import unittest

from OTLClasses.Verification.AIMNaamObject import AIMNaamObject
from OTLClasses.Verification.NaampadObject import NaampadObject


class AIMNaamObjectTestInstance(AIMNaamObject):
    def __init__(self):
        pass


class OSLOCollectorTests(unittest.TestCase):
    def test_useOTLClassAIMNaamObject(self):
        instance = AIMNaamObjectTestInstance()

        instance.naam = "TEST"
        self.assertTrue(instance.naam == "TEST")
        self.assertTrue(instance.uri == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject")
        self.assertTrue(isinstance(instance, AIMNaamObject))

        with self.assertRaises(ValueError):
            instance.naam = 9