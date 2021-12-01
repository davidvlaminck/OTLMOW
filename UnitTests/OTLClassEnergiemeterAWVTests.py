import unittest

from OTLClasses.Verification.AIMDBStatus import AIMDBStatus
from OTLClasses.Verification.AIMNaamObject import AIMNaamObject
from OTLClasses.Verification.AIMObject import AIMObject
from OTLClasses.Verification.EnergiemeterAWV import EnergiemeterAWV
from OTLClasses.Verification.NaampadObject import NaampadObject


class EnergiemeterAWVTests(unittest.TestCase):
    def test_useOTLClassEnergiemeterAWV(self):
        instance = EnergiemeterAWV()
        instance2 = EnergiemeterAWV()
        instance3 = EnergiemeterAWV()
        instance.isActief = True

        self.assertTrue(instance.isActief)
        self.assertTrue(instance.uri == "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterAWV")
        self.assertTrue(isinstance(instance, EnergiemeterAWV))

        instance.aantalTelwerken = 1
        instance2.aantalTelwerken = 2
        instance2.meternummer = "123"
        self.assertTrue(instance.aantalTelwerken == 1)
        self.assertTrue(instance2.aantalTelwerken == 2)
        self.assertTrue(instance3.aantalTelwerken is None)
