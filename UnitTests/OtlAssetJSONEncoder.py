import unittest

from ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from OTLModel.Verification.Aftakking import Aftakking
from OTLModel.Verification.DtcIdentificator import DtcIdentificator
from UnitTests.RelatieValidatorTests import GeldigeRelatieLijstTestInstance


class OtlAssetJSONEncoderTests(unittest.TestCase):
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

        self.assertEqual(
            '{"assetId": null, "isActief": true, "naam": "aftakking", "notitie": "notitie aftakking", "toestand": "in-ontwerp", "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}',
            js)

    def test_JsonEncodeWithDtcIdentificator(self):
        # create testable OTLAsset
        a = Aftakking()
        dtcId = DtcIdentificator()
        dtcId.identificator.waarde = "mijn eigen id"
        a.assetId = dtcId
        a.naam.waarde = "aftakking"

        encoder = OtlAssetJSONEncoder()
        js = encoder.encode(a)

        self.assertEqual('{"assetId": {"identificator": "mijn eigen id", "toegekendDoor": null}, "isActief": null, '
                         '"naam": "aftakking", "notitie": null, "toestand": null, "typeURI": '
                         '"https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}', js)

    def test_JsonEncodeWithDtcIdentificatorAndIndent(self):
        a = Aftakking()
        dtcId = DtcIdentificator()
        dtcId.identificator.waarde = "mijn_eigen_id_voor_deze_aftakking_asset"
        dtcId.toegekendDoor.waarde = "python script"
        a.assetId = dtcId
        a.naam.waarde = "aftakking"
        a.notitie.waarde = "notitie aftakking"
        a.isActief.waarde = True
        a.toestand.set_value_by_label("in ontwerp")

        encoder = OtlAssetJSONEncoder(indent=4)
        js = encoder.encode(a)

        expected = ('{\n'
                    '    "assetId": {\n'
                    '        "identificator": "mijn_eigen_id_voor_deze_aftakking_asset",\n'
                    '        "toegekendDoor": "python script"\n'
                    '    },\n'
                    '    "isActief": true,\n'
                    '    "naam": "aftakking",\n'
                    '    "notitie": "notitie aftakking",\n'
                    '    "toestand": "in-ontwerp",\n'
                    '    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"\n'
                    '}')

        self.assertEqual(expected, js)
