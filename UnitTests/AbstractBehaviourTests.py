import unittest

from OTLModel.Verification.AIMDBStatus import AIMDBStatus
from OTLModel.Verification.AIMObject import AIMObject
from OTLModel.Verification.AIMToestand import AIMToestand
from OTLModel.Verification.Contactor import Contactor


class AbstractBehaviour(unittest.TestCase):
    def test_ErrorsOnInstantiateAbstractClasses(self):
        with self.assertRaises(TypeError):
            AIMDBStatus()
        with self.assertRaises(TypeError):
            AIMToestand()
        with self.assertRaises(TypeError):
            AIMObject()

    def test_TestAssignmentsOnSameClasses(self):
        contactor = Contactor()
        self.assertTrue(contactor.uri == "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor")
        self.assertTrue(isinstance(contactor, Contactor))
        self.assertTrue(isinstance(contactor, AIMObject))
        contactor2 = Contactor()

        contactor.notitie.waarde = "notitie1"
        contactor2.notitie.waarde = "notitie2"
        self.assertTrue(contactor.notitie.waarde == "notitie1")
        self.assertTrue(contactor2.notitie.waarde == "notitie2")

        contactor3 = Contactor()
        self.assertTrue(contactor3.notitie.waarde is None)

        contactor3.notitie.waarde = "notitie3"
        self.assertTrue(contactor.notitie.waarde == "notitie1")
        self.assertTrue(contactor2.notitie.waarde == "notitie2")
        self.assertTrue(contactor3.notitie.waarde == "notitie3")
