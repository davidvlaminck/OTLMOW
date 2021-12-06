import unittest

from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField
from ModelGenerator.BaseClasses.Keuzelijst import Keuzelijst


# class TestKeuzeLijst(Keuzelijst):
#     def __init__(self):
#         super(TestKeuzeLijst, self).__init__('TestKeuzeLijst', 'Test KeuzeLijst',
#                                             "https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/TestKeuzeLijst")
#         self.addOption('optie1', 'optie 1', 'definitie 1', 'uri 1')
#         self.addOption('optie2', 'optie 2', 'definitie 2', 'uri 2')
from ModelGenerator.BaseClasses.UnionTypeField import UnionTypeField
from OTLClasses.Verification.Aftakking import Aftakking
from OTLClasses.Verification.DtcAdres import DtcAdres
from OTLClasses.Verification.KlAlgGemeente import KlAlgGemeente


class UnionTestClass(Aftakking):
    unionveld = UnionTypeField(DtcAdres, KlAlgGemeente)


class KeuzelijstFieldTests(unittest.TestCase):
    def test_InitField(self):
        c = UnionTestClass()
        with self.assertRaises(TypeError):
            c.unionveld = "2"

        adresveld = DtcAdres()
        adresveld.bus = "BUS"
        c.unionveld = adresveld

        gemeenteveld = KeuzelijstField(KlAlgGemeente())
        gemeenteveld.set_value_by_label('aalst')
        c.unionveld = gemeenteveld






