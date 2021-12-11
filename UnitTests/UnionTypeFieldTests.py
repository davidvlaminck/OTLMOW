import unittest
from ModelGenerator.BaseClasses.UnionTypeField import UnionTypeField
from OTLClasses.Verification.Aftakking import Aftakking
from OTLClasses.Verification.DtcAdres import DtcAdres
from OTLClasses.Verification.KlAlgGemeente import KlAlgGemeente


class UnionTestClass(Aftakking):
    unionveld = UnionTypeField(naam="testAdres", label="atestAdres",
                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#testAdres",
                                  definition="testAdres definitie"
                                  , usagenote="", deprecated_version="",fieldsTuple=(DtcAdres, KlAlgGemeente))


class KeuzelijstFieldTests(unittest.TestCase):
    def test_InitField(self):
        c = UnionTestClass()

        adresveld = DtcAdres()
        adresveld.bus.waarde = "BUS"
        c.unionveld.waarde = adresveld

        self.assertTrue(c.unionveld.waarde.bus.waarde == "BUS")

        gemeenteveld = KlAlgGemeente()
        gemeenteveld.set_value_by_label('aalst')
        c.unionveld.waarde = gemeenteveld

        self.assertTrue(c.unionveld.waarde.waarde.invulwaarde == "aalst")

        with self.assertRaises(TypeError):
            c.unionveld.waarde = "2"
