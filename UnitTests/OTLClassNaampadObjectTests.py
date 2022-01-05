import unittest

from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Classes.NaampadObject import NaampadObject


class NaampadObjectTestInstance(NaampadObject):
    def __init__(self):
        pass


class OSLOCollectorTests(unittest.TestCase):
    def test_useOTLClassNaampadObject(self):
        instance = NaampadObjectTestInstance()

        instance.naam.waarde = "TEST"
        instance.naampad.waarde = "TEST/TEST"
        self.assertTrue(instance.naam.waarde == "TEST")
        self.assertTrue(instance.naampad.waarde == "TEST/TEST")
        self.assertTrue(instance.typeURI == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject")
        self.assertTrue(isinstance(instance, NaampadObject))
        self.assertTrue(isinstance(instance, AIMNaamObject))

        with self.assertRaises(ValueError):
            instance.naampad.waarde = 9

    # TODO waarde gebruiken in tests