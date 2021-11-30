import unittest

from OTLClasses.Verification.NaampadObject import NaampadObject


class NaampadObjectTestInstance(NaampadObject):
    def __init__(self):
        pass


class OSLOCollectorTests(unittest.TestCase):
    def test_useOTLClassNaampadObject(self):
        instance = NaampadObjectTestInstance()

        instance.naampad = "TEST/TEST"
        self.assertTrue(instance.naampad == "TEST/TEST")
        self.assertTrue(instance.uri == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject")
        self.assertTrue(isinstance(instance, NaampadObject))
