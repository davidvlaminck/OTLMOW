from unittest import TestCase

from OTLMOW.Facility.DavieDecoder import DavieDecoder
from OTLMOW.OTLModel.Classes.ExterneDetectie import ExterneDetectie
from OTLMOW.OTLModel.Classes.HeeftBetrokkene import HeeftBetrokkene
from OTLMOW.OTLModel.Classes.Netwerkpoort import Netwerkpoort
from OTLMOW.OTLModel.Classes.Verkeersregelaar import Verkeersregelaar
from OTLMOW.OTLModel.Classes.Wegberm import Wegberm
from OTLMOW.OTLModel.Classes.Wegkantkast import Wegkantkast


class DavieDecoderTests(TestCase):
    jsonDataCase1 = """[{
    "assetId": {
      "identificator": "000a35d5-c4a5-4a36-8620-62c99e053ba0-b25kZXJkZWVsI05ldHdlcmtwb29ydA",
      "toegekendDoor": "AWV"
    },
    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
    "isActief": true,
    "naam": "Poort_2625",
    "toestand": "in-ontwerp",
    "beschrijvingFabrikant": "test",
    "nNILANCapaciteit": 155
  }]"""
    jsonDataCase2 = """[{
    "assetId": {
      "identificator": "4be83a8f-ab97-44c7-8dc6-1666c8dfb68e-b25kZXJkZWVsI0hlZWZ0QmV0cm9ra2VuZQ"
    },
    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene",
    "bronAssetId": {
      "identificator": "000a35d5-c4a5-4a36-8620-62c99e053ba0-b25kZXJkZWVsI05ldHdlcmtwb29ydA"
    },
    "doelAssetId": {
      "identificator": "5434ffca-8bdc-445a-a4ba-b395c87dec30-cHVybDpBZ2VudA"
    },
    "bron": {
      "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort"
    },
    "doel": {
      "typeURI": "http://purl.org/dc/terms/Agent"
    },
    "rol": "toezichter",
    "specifiekeContactinfo": [],
    "isActief": true
  }]"""
    jsonDataCase3 = """[{
  "assetId" : {
    "identificator" : "842cc8b2-3117-4757-a11a-1f0344b159e4-aW5zdGFsbGF0aWUjV2VnYmVybQ",
    "toegekendDoor" : "AWV"
  },
  "typeURI" : "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wegberm",
  "niveau" : 1.1,
  "breedte" : 2,
  "toestand" : "in-ontwerp",
  "oppervlakte" : 50.2,
  "isActief" : true
}]"""
    jsonDataCase4 = """[{
  "assetId" : {
    "identificator" : "f184a415-10c3-465a-85d0-5e3495e7c57f-b25kZXJkZWVsI1ZlcmtlZXJzcmVnZWxhYXI",
    "toegekendDoor" : "AWV"
  },
  "typeURI" : "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar",
  "vplanNummer" : "V015254v11",
  "coordinatiewijze" : [ "centraal", "pulsen" ],
  "toestand" : "in-gebruik",
  "kabelaansluitschema" : {
    "uri" : "/eminfra/core/api/otl/assets/f184a415-10c3-465a-85d0-5e3495e7c57f-b25kZXJkZWVsI1ZlcmtlZXJzcmVnZWxhYXI/documenten/e4457b0f-5e08-4157-a01a-b955e6a4186f",
    "bestandsnaam" : "00_input.json"
  },
  "isActief" : true,
  "voltageLampen" : "230",
  "vplanDatum" : "2020-04-22",
  "datumOprichtingObject" : "2020-03-14",
  "technischeDocumentatie" : {
    "uri" : "/eminfra/core/api/otl/assets/f184a415-10c3-465a-85d0-5e3495e7c57f-b25kZXJkZWVsI1ZlcmtlZXJzcmVnZWxhYXI/documenten/3771787b-889d-4c81-8cfa-99718f81db4a",
    "bestandsnaam" : "Cooper.jpg"
  },
  "programmeertool" : "fwispbnxlo",
  "externeReferentie" : [ {    "externePartij" : "bij externe partij 2",    "externReferentienummer" : "externe referentie 2"  }, {    "externePartij" : "bij externe partij 1",    "externReferentienummer" : "externe referentie 1"  } ],
  "regelaartype" : "type-1",
  "notitie" : "test 123",
  "naam" : "Gevondenproficiat",
  "geometry" : "POINT Z (155377.8 211520.7 0)"
}]"""
    jsonDataCase5 = """{
  "assetId" : {
    "identificator" : "ae6c5f35-930d-47a3-b67f-a5ff40c6e0fe-b25kZXJkZWVsI1NsYWdib29ta29sb20",
    "toegekendDoor" : "AWV"
  },
  "typeURI" : "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom",
  "toestand" : "in-gebruik",
  "isActief" : true,
  "geometry" : "POINT Z (61716.3 209331.2 0)"
}"""
    jsonDataCase6 = """[{
  "assetId" : {
    "identificator" : "7102cbba-4391-4d7c-a2d1-8873eac3eee8-b25kZXJkZWVsI0V4dGVybmVEZXRlY3RpZQ",
    "toegekendDoor" : "AWV"
  },
  "typeURI" : "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie",
  "isActief" : true,
  "contactpersoon" : {
    "adres" : [ {
      "gemeente" : "aalter",
      "straatnaam" : "teststraat"
    } ],
    "voornaam" : "test_voornaam",
    "achternaam" : "test_achternaam"
  },
  "toestand" : "in-ontwerp",
  "naam" : "test_ExterneDetectie"
}]"""

    def test_invalid_typeURI(self):
        davie_decoder = DavieDecoder()
        with self.assertRaises(ValueError):
            davie_decoder.decode('[{"typeURI": "https://invalid.uri.com"}]')

    def test_decode_invalid_attribute(self):
        davie_decoder = DavieDecoder()
        with self.assertRaises(AttributeError):
            davie_decoder.decode(
                '[{"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort", "invalid_attribute": "some value"}]')

    def test_decode_empty_value(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(
            '[{"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort", "naam": ""}]')
        self.assertTrue(isinstance(lijstObjecten[0], Netwerkpoort))
        self.assertIsNone(lijstObjecten[0].naam)

    def test_decode_geometry(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(
            '[{"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast", "geometry": "POINT Z (157696.6 219065.5 0)"}]')
        self.assertTrue(isinstance(lijstObjecten[0], Wegkantkast))
        self.assertEqual("POINT Z (157696.6 219065.5 0)", lijstObjecten[0].geometry)

    def test_decode_Davie_json_case_1_and_assert_fields(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(self.jsonDataCase1)
        self.assertEqual(1, len(lijstObjecten))
        self.assertTrue(isinstance(lijstObjecten[0], Netwerkpoort))

        with self.subTest("Assert IntField"):
            self.assertEqual(155, lijstObjecten[0].nNILANCapaciteit)

        with self.subTest("Assert StringField"):
            self.assertEqual('Poort_2625', lijstObjecten[0].naam)

        with self.subTest("Assert KeuzelijstField"):
            self.assertEqual('in-ontwerp', lijstObjecten[0].toestand)

        with self.subTest("Assert ComplexField"):
            self.assertEqual('000a35d5-c4a5-4a36-8620-62c99e053ba0-b25kZXJkZWVsI05ldHdlcmtwb29ydA',
                             lijstObjecten[0].assetId.identificator)
            self.assertEqual('AWV', lijstObjecten[0].assetId.toegekendDoor)

    def test_decode_Davie_json_case_2_and_assert_fields(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(self.jsonDataCase2)
        self.assertEqual(1, len(lijstObjecten))
        self.assertTrue(isinstance(lijstObjecten[0], HeeftBetrokkene))

        self.assertEqual("4be83a8f-ab97-44c7-8dc6-1666c8dfb68e-b25kZXJkZWVsI0hlZWZ0QmV0cm9ra2VuZQ",
                         lijstObjecten[0].assetId.identificator)
        self.assertEqual("000a35d5-c4a5-4a36-8620-62c99e053ba0-b25kZXJkZWVsI05ldHdlcmtwb29ydA",
                         lijstObjecten[0].bronAssetId.identificator)
        self.assertEqual("5434ffca-8bdc-445a-a4ba-b395c87dec30-cHVybDpBZ2VudA",
                         lijstObjecten[0].doelAssetId.identificator)
        self.assertEqual("toezichter", lijstObjecten[0].rol)
        self.assertEqual(True, lijstObjecten[0].isActief)

    def test_decode_Davie_json_case_3_and_assert_fields(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(self.jsonDataCase3)
        self.assertEqual(1, len(lijstObjecten))
        self.assertTrue(isinstance(lijstObjecten[0], Wegberm))

        with self.subTest("Assert DecimalFloatField"):
            self.assertEqual(1.1, lijstObjecten[0].niveau)

        with self.subTest("Assert KwantWrdInMeter"):
            self.assertEqual(2.0, lijstObjecten[0].breedte.waarde)

    def test_decode_Davie_json_case_4_and_assert_fields(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(self.jsonDataCase4)
        self.assertEqual(1, len(lijstObjecten))
        self.assertTrue(isinstance(lijstObjecten[0], Verkeersregelaar))

        with self.subTest("Assert KardinaliteitField met KeuzelijstField"):
            self.assertTrue(isinstance(lijstObjecten[0].coordinatiewijze, list))
            self.assertEqual("centraal", lijstObjecten[0].coordinatiewijze[0])
            self.assertEqual("pulsen", lijstObjecten[0].coordinatiewijze[1])

        with self.subTest("Assert KardinaliteitField met ComplexField"):
            self.assertTrue(isinstance(lijstObjecten[0].externeReferentie, list))
            self.assertEqual("bij externe partij 2", lijstObjecten[0].externeReferentie[0].externePartij)
            self.assertEqual("externe referentie 2", lijstObjecten[0].externeReferentie[0].externReferentienummer)
            self.assertEqual("bij externe partij 1", lijstObjecten[0].externeReferentie[1].externePartij)
            self.assertEqual("externe referentie 1", lijstObjecten[0].externeReferentie[1].externReferentienummer)

    def test_decode_Davie_json_case_6_and_assert_fields_kard_complex_in_complex(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(self.jsonDataCase6)
        self.assertEqual(1, len(lijstObjecten))
        self.assertTrue(isinstance(lijstObjecten[0], ExterneDetectie))
        self.assertEqual('test_voornaam', lijstObjecten[0].contactpersoon.voornaam)
        self.assertEqual('test_achternaam', lijstObjecten[0].contactpersoon.achternaam)

        self.assertEqual('aalter', lijstObjecten[0].contactpersoon.adres[0].gemeente)
        self.assertEqual('teststraat', lijstObjecten[0].contactpersoon.adres[0].straatnaam)
