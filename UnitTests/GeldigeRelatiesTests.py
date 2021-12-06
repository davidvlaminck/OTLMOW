import unittest

from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from OTLClasses.Verification.Aftakking import Aftakking
from OTLClasses.Verification.EnergiemeterAWV import EnergiemeterAWV
from OTLClasses.Verification.Voedt import Voedt


class GeldigeRelatiesTests(unittest.TestCase):
    def test_GeldigeRelatieAttrOk(self):
        instance = GeldigeRelatie(EnergiemeterAWV, Aftakking, Voedt)
        self.assertTrue(instance is not None)

    def test_GeldigeRelatieAttr2Fout(self):
        with self.assertRaises(TypeError):
            instance = GeldigeRelatie(EnergiemeterAWV, Voedt, Voedt)

    def test_GeldigeRelatieAttr3Fout(self):
        with self.assertRaises(TypeError):
            instance = GeldigeRelatie(EnergiemeterAWV, Aftakking, Aftakking)

    def test_GeldigeRelatieAttr1Fout(self):
        with self.assertRaises(TypeError):
            instance = GeldigeRelatie(Voedt, Aftakking, Voedt)


