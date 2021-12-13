import unittest

from ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from OTLClasses.Verification.Aftakking import Aftakking
from UnitTests.RelatieValidatorTests import GeldigeRelatieLijstTestInstance


class JsonTests(unittest.TestCase):
    def test_JsonEncode(self):
        # add _geldige_relaties on Aftakking type
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)

        # create testable OTLAsset
        a = Aftakking()
        a.naam.waarde = "aftakking"
        a.notitie.waarde = "notitie aftakking"
        a.isActief.waarde = True
        a.toestand.set_value_by_label("in ontwerp")

        encoder = OtlAssetJSONEncoder()
        js = encoder.encode(a)

        self.assertEqual('{"isActief": true, "naam": "aftakking", "notitie": "notitie aftakking", "toestand": "in-ontwerp", "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}', js)
