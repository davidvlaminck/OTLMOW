import unittest

from OTLClasses.Verification.AIMNaamObject import AIMNaamObject
from OTLClasses.Verification.NaampadObject import NaampadObject


class NaampadObjectTestInstance(NaampadObject):
    def __init__(self):
        pass


class OSLOCollectorTests(unittest.TestCase):
    def test_useOTLClassNaampadObject(self):
        instance = NaampadObjectTestInstance()

        instance.naam = "TEST"
        instance.naampad = "TEST/TEST"
        self.assertTrue(instance.naam == "TEST")
        self.assertTrue(instance.naampad == "TEST/TEST")
        self.assertTrue(instance.uri == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject")
        self.assertTrue(isinstance(instance, NaampadObject))
        self.assertTrue(isinstance(instance, AIMNaamObject))

        with self.assertRaises(ValueError):
            instance.naampad = 9
