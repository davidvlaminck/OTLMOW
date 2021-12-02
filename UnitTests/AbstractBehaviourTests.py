import unittest

from OTLClasses.Verification.AIMDBStatus import AIMDBStatus
from OTLClasses.Verification.AIMObject import AIMObject
from OTLClasses.Verification.AIMToestand import AIMToestand
from OTLClasses.Verification.Contactor import Contactor


class AbstractBehaviour(unittest.TestCase):
    def test_ErrorsOnInstantiateAbstractClasses(self):
        with self.assertRaises(TypeError):
            instanceOfAbstractClass = AIMDBStatus()
        with self.assertRaises(TypeError):
            instanceOfAbstractClass2 = AIMToestand()
        with self.assertRaises(TypeError):
            instanceOfAbstractClass3 = AIMObject()
        contactor = Contactor()
        self.assertTrue(contactor.uri == "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor")
        self.assertTrue(isinstance(contactor, Contactor))
        self.assertTrue(isinstance(contactor, AIMObject))
        contactor2 = Contactor()

        contactor.notitie = "notitie1"
        contactor2.notitie = "notitie2"
        self.assertTrue(contactor.notitie == "notitie1")
        self.assertTrue(contactor2.notitie == "notitie2")

        contactor3 = Contactor()
        self.assertTrue(contactor3.notitie is None)

        contactor3.notitie = "notitie3"
        self.assertTrue(contactor.notitie == "notitie1")
        self.assertTrue(contactor2.notitie == "notitie2")
        self.assertTrue(contactor3.notitie == "notitie3")





