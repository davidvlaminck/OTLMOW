import unittest

from OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLModel.Verification.AIMDBStatus import AIMDBStatus
from OTLModel.Verification.AIMObject import AIMObject
from OTLModel.Verification.AIMToestand import AIMToestand


class AIMObjectTestInstance(AIMObject):
    def __init__(self):
        super().__init__()


class AIMNObjectTests(unittest.TestCase):
    def test_useOTLClassAIMObject(self):
        instance = AIMObjectTestInstance()

        instance.notitie.waarde = "TEST"
        self.assertEqual("TEST", instance.notitie.waarde)
        self.assertTrue(instance.typeURI == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject")
        self.assertTrue(isinstance(instance, AIMObject))
        self.assertTrue(isinstance(instance, OTLAsset))
        self.assertTrue(isinstance(instance, AIMToestand))
        self.assertTrue(isinstance(instance, AIMDBStatus))

        with self.assertRaises(ValueError):
            instance.notitie.waarde = 9

        with self.assertRaises(TypeError):
            AIMObject()

        instance2 = AIMObjectTestInstance()
        instance2.notitie.waarde = "TEST2"

        self.assertEqual("TEST", instance.notitie.waarde)
        self.assertEqual("TEST2", instance2.notitie.waarde)
