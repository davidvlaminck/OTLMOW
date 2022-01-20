import decimal
import unittest

from ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from OTLModel.Classes.Aftakking import Aftakking
from OTLModel.Classes.Laagspanningsbord import Laagspanningsbord
from UnitTests.RelatieValidatorTests import GeldigeRelatieLijstTestInstance


class OtlAssetJSONEncoderTests(unittest.TestCase):
    def test_JsonEncode(self):
        # add _geldige_relaties on Aftakking fieldType
        geldigeRelatieLijst = GeldigeRelatieLijstTestInstance()
        validator = RelatieValidator(geldigeRelatieLijst)

        # create testable OTLAsset
        a = Aftakking()
        a.naam = "aftakking"
        a.notitie = "notitie aftakking"
        a.isActief = True
        a.toestand = "in-ontwerp"

        encoder = OtlAssetJSONEncoder()
        js = encoder.encode(a)

        self.assertEqual(
            '{"isActief": true, "naam": "aftakking", "notitie": "notitie aftakking", "toestand": "in-ontwerp", "typeURI": '
            '"https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}',
            js)

    def test_JsonEncodeDecimal(self):
        l = Laagspanningsbord()
        l.vermogen.waarde = float(25)

        encoder = OtlAssetJSONEncoder()
        js = encoder.encode(l)

        self.assertEqual(
            '{"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord", "vermogen": 25.0}',
            js)

    def test_JsonEncodeWithDtcIdentificator(self):
        # create testable OTLAsset
        a = Aftakking()
        a.assetId.identificator = "mijn eigen id"
        a.naam = "aftakking"

        encoder = OtlAssetJSONEncoder()
        js = encoder.encode(a)

        self.assertEqual('{"assetId": {"identificator": "mijn eigen id"}, '
                         '"naam": "aftakking", "typeURI": '
                         '"https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}', js)

    def test_JsonEncodeWithDtcIdentificatorAndIndent(self):
        a = Aftakking()
        a.assetId.identificator = "mijn_eigen_id_voor_deze_aftakking_asset"
        a.assetId.toegekendDoor = "python script"
        a.naam = "aftakking"
        a.notitie = "notitie aftakking"
        a.isActief = True
        a.toestand = "in-ontwerp"

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
