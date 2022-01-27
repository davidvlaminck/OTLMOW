import unittest

from OTLMOW.OTLModel.Classes.AIMDBStatus import AIMDBStatus
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Classes.AIMToestand import AIMToestand
from OTLMOW.OTLModel.Classes.Contactor import Contactor


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
        self.assertTrue(contactor.typeURI == "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor")
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
