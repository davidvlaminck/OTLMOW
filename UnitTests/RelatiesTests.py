import unittest

from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from OTLClasses.Verification.Aftakking import Aftakking
from OTLClasses.Verification.EnergiemeterAWV import EnergiemeterAWV
from OTLClasses.Verification.Voedt import Voedt


class RelatiesTests(unittest.TestCase):
    def test_LegVoedtRelatieTussenEnergiemeterAWVEn(self):
        instance = EnergiemeterAWV()

    def test_GeldigeRelatieAttrOk(self):
        instance = GeldigeRelatie(Voedt(), Aftakking(), RelatieRichting.BRON_DOEL)
        self.assertTrue(instance is not None)

    def test_GeldigeRelatieAttr1Fout(self):
        with self.assertRaises(TypeError):
            instance = GeldigeRelatie(Aftakking(), Aftakking(), RelatieRichting.BRON_DOEL)

    def test_GeldigeRelatieAttr2Fout(self):
        with self.assertRaises(TypeError):
            instance = GeldigeRelatie(Voedt(), Voedt(), RelatieRichting.BRON_DOEL)

    def test_GeldigeRelatieAttr3Fout(self):
        with self.assertRaises(TypeError):
            instance = GeldigeRelatie(Voedt(), Voedt(), "BRON_DOEL")


