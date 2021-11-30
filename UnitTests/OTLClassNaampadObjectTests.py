import unittest

from OTLClasses.Verification.NaampadObject import NaampadObject


class NaampadObjectTestInstance(NaampadObject):
    def __init__(self):
        pass



class OSLOCollectorTests(unittest.TestCase):
    def test_useOTLClassNaampadObject(self):
        instance = NaampadObjectTestInstance()
        instance.uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'

    def test_instantiateNaampadObject(self):
        instance = NaampadObject()
        instance.uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'