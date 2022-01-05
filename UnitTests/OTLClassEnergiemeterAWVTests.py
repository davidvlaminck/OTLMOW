import unittest

from OTLModel.Classes.EnergiemeterAWV import EnergiemeterAWV


class EnergiemeterAWVTests(unittest.TestCase):
    def test_useOTLClassEnergiemeterAWV(self):
        instance = EnergiemeterAWV()
        instance2 = EnergiemeterAWV()
        instance3 = EnergiemeterAWV()
        instance.isActief.waarde = True
        instance.toestand.waarde = 'in gebruik'

        self.assertTrue(instance.isActief.waarde)
        self.assertTrue(instance.typeURI == "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterAWV")
        self.assertTrue(isinstance(instance, EnergiemeterAWV))

        instance.aantalTelwerken.waarde = 1
        instance2.aantalTelwerken.waarde = 2
        instance2.meternummer.waarde = "123"
        self.assertTrue(instance.aantalTelwerken.waarde == 1)
        self.assertTrue(instance2.aantalTelwerken.waarde == 2)
        self.assertTrue(instance3.aantalTelwerken.waarde is None)
