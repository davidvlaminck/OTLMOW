import unittest

from ModelGenerator.BaseClasses.OTLAsset import OTLAsset
from OTLClasses.Verification.AIMDBStatus import AIMDBStatus
from OTLClasses.Verification.AIMObject import AIMObject
from OTLClasses.Verification.AIMToestand import AIMToestand


class AIMObjectTestInstance(AIMObject):
    def __init__(self):
        pass


class AIMNObjectTests(unittest.TestCase):
    def test_useOTLClassAIMObject(self):
        instance = AIMObjectTestInstance()

        instance.notitie = "TEST"
        self.assertTrue(instance.notitie == "TEST")
        self.assertTrue(instance.uri == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject")
        self.assertTrue(isinstance(instance, AIMObject))
        self.assertTrue(isinstance(instance, OTLAsset))
        self.assertTrue(isinstance(instance, AIMToestand))
        self.assertTrue(isinstance(instance, AIMDBStatus))

        with self.assertRaises(ValueError):
            instance.notitie = 9

        with self.assertRaises(TypeError):
            instanceOfAbstractClass = AIMObject()
