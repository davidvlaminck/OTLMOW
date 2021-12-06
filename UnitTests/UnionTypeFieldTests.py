import unittest
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

        gemeenteveld = KlAlgGemeente()
        gemeenteveld.set_value_by_label('aalst')
        c.unionveld = gemeenteveld
