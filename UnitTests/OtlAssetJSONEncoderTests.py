import unittest
from datetime import datetime

from src.OTLMOW.ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from src.OTLMOW.OTLModel.Classes.Aftakking import Aftakking
from src.OTLMOW.OTLModel.Classes.Exoten import Exoten
from src.OTLMOW.OTLModel.Classes.Laagspanningsbord import Laagspanningsbord
from src.OTLMOW.OTLModel.Classes.Verkeersregelaar import Verkeersregelaar
from src.OTLMOW.OTLModel.Classes.WVLichtmast import WVLichtmast
from src.OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from src.OTLMOW.OTLModel.Datatypes.DtuWvLichtmastBevsToestelMethode import DtuWvLichtmastBevsToestelMethode


class OtlAssetJSONEncoderTests(unittest.TestCase):
    def test_JsonEncode(self):
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

    def test_JsonEncode_Deprecated(self):
        e = Exoten()
        e.isActief = True

        json = OtlAssetJSONEncoder().encode(e)
        expected = '{"isActief": true, "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Exoten"}'

        self.assertEqual(expected, json)

    def test_JsonEncode_Boolean(self):
        a = Aftakking()
        a.isActief = True

        json = OtlAssetJSONEncoder().encode(a)
        expected = '{"isActief": true, "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}'

        self.assertEqual(expected, json)

    def test_JsonEncode_KwantWrd_Decimal(self):
        l = Laagspanningsbord()
        l.vermogen.waarde = float(25)

        json = OtlAssetJSONEncoder().encode(l)
        expected = '{"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord", "vermogen": 25.0}'

        self.assertEqual(expected, json)

    def test_JsonEncode_ComplexType_DtcIdentificator(self):
        a = Aftakking()
        a.assetId.identificator = 'eigen_id'
        a.assetId.toegekendDoor = 'Python'

        json = OtlAssetJSONEncoder().encode(a)
        expected = '{"assetId": {"identificator": "eigen_id", "toegekendDoor": "Python"}, "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}'

        self.assertEqual(expected, json)

    def test_JsonEncode_KeuzelijstType_KlAIMToestand(self):
        a = Aftakking()
        a.toestand = 'in-gebruik'

        json = OtlAssetJSONEncoder().encode(a)
        expected = '{"toestand": "in-gebruik", "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}'

        self.assertEqual(expected, json)

    def test_JsonEncode_Date_DatumOprichtingObject(self):
        a = Aftakking()
        a.datumOprichtingObject = datetime(2022, 1, 20)

        json = OtlAssetJSONEncoder().encode(a)
        expected = '{"datumOprichtingObject": "2022-01-20", "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"}'

        self.assertEqual(expected, json)

    def test_JsonEncode_Keuzelijst_Kardinaliteit_Coordinatiewijze(self):
        v = Verkeersregelaar()
        v.coordinatiewijze = ["centraal", "pulsen"]

        json = OtlAssetJSONEncoder().encode(v)
        expected = '{"coordinatiewijze": ["centraal", "pulsen"], "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar"}'

        self.assertEqual(expected, json)

    def test_JsonEncode_Complex_Kardinaliteit_ExterneReferentie(self):
        v = Verkeersregelaar()
        v.externeReferentie = []

        v.externeReferentie.append(DtcExterneReferentie.waardeObject())
        v.externeReferentie[0].externReferentienummer = "externe referentie 2"
        v.externeReferentie[0].externePartij = "bij externe partij 2"

        v.externeReferentie.append(DtcExterneReferentie.waardeObject())
        v.externeReferentie[1].externReferentienummer = "externe referentie 1"
        v.externeReferentie[1].externePartij = "bij externe partij 1"

        json = OtlAssetJSONEncoder().encode(v)
        expected = '{"externeReferentie": [{"externReferentienummer": "externe referentie 2", "externePartij": "bij externe partij 2"}, {"externReferentienummer": "externe referentie 1", "externePartij": "bij externe partij 1"}], "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar"}'

        self.assertEqual(expected, json)

    def test_JsonEncode_Union_DtuLichtmasthoogte(self):
        w = WVLichtmast()
        w.masthoogte.afwijkendeHoogte.waarde = 7.8

        json = OtlAssetJSONEncoder().encode(w)
        expected = '{"masthoogte": {"afwijkendeHoogte": 7.8}, "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast"}'

        self.assertEqual(expected, json)

        w.masthoogte.standaardHoogte = '10.00'

        json = OtlAssetJSONEncoder().encode(w)
        expected = '{"masthoogte": {"standaardHoogte": "10.00"}, "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast"}'

        self.assertEqual(expected, json)

    def test_JsonEncode_Union_Kardinaliteit_DtuWvLichtmastBevsToestelMethode(self):
        w = WVLichtmast()
        w.bevestigingToestellen = []
        w.bevestigingToestellen.append(DtuWvLichtmastBevsToestelMethode.waardeObject())
        w.bevestigingToestellen[0].standaardMethode = "mediaanbalk-H"

        json = OtlAssetJSONEncoder().encode(w)
        expected = '{"bevestigingToestellen": [{"standaardMethode": "mediaanbalk-H"}], "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast"}'

        self.assertEqual(expected, json)


# union type
# list of complex
# list of KWantWrd?