from unittest import TestCase

from Facility.DavieDecoder import DavieDecoder
from OTLModel.Classes.HeeftBetrokkene import HeeftBetrokkene
from OTLModel.Classes.Netwerkpoort import Netwerkpoort
from OTLModel.Classes.Verkeersregelaar import Verkeersregelaar
from OTLModel.Classes.Wegberm import Wegberm
from OTLModel.Classes.Wegkantkast import Wegkantkast
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.StringField import StringField


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

    def test_invalid_typeURI(self):
        davie_decoder = DavieDecoder()
        with self.assertRaises(ValueError):
            davie_decoder.decode('[{"typeURI": "https://invalid.uri.com"}]')

    def test_decode_invalid_attribute(self):
        davie_decoder = DavieDecoder()
        with self.assertRaises(NotImplementedError):
            davie_decoder.decode('[{"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort", "invalid attribute": "some value"}]')

    def test_decode_empty_value(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode('[{"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort", "naam": ""}]')
        self.assertTrue(isinstance(lijstObjecten[0], Netwerkpoort))
        self.assertIsNone(lijstObjecten[0].naam.waarde)

    def test_decode_geometry(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode('[{"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast", "geometry": "POINT Z(157696.6 219065.5 0)"}]')
        self.assertTrue(isinstance(lijstObjecten[0], Wegkantkast))
        self.assertEqual("POINT Z(157696.6 219065.5 0)", lijstObjecten[0].geometry.waarde)

    def test_decode_Davie_json_case_1_and_assert_fields(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(self.jsonDataCase1)
        self.assertEqual(1, len(lijstObjecten))
        self.assertTrue(isinstance(lijstObjecten[0], Netwerkpoort))

        with self.subTest("Assert IntField"):
            self.assertTrue(isinstance(lijstObjecten[0].nNILANCapaciteit, IntegerField))
            self.assertEqual(155, lijstObjecten[0].nNILANCapaciteit.waarde)

        with self.subTest("Assert StringField"):
            self.assertTrue(isinstance(lijstObjecten[0].naam, StringField))
            self.assertEqual('Poort_2625', lijstObjecten[0].naam.waarde)

        with self.subTest("Assert KeuzelijstField"):
            self.assertTrue(isinstance(lijstObjecten[0].toestand, KeuzelijstField))
            self.assertEqual('in-ontwerp', lijstObjecten[0].toestand.waarde.invulwaarde)

        with self.subTest("Assert ComplexField"):
            self.assertTrue(isinstance(lijstObjecten[0].assetId, ComplexField))
            self.assertEqual('000a35d5-c4a5-4a36-8620-62c99e053ba0-b25kZXJkZWVsI05ldHdlcmtwb29ydA', lijstObjecten[0].assetId.
                             identificator.waarde)
            self.assertEqual('AWV', lijstObjecten[0].assetId.toegekendDoor.waarde)

    def test_decode_Davie_json_case_2_and_assert_fields(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(self.jsonDataCase2)
        self.assertEqual(1, len(lijstObjecten))
        self.assertTrue(isinstance(lijstObjecten[0], HeeftBetrokkene))

        self.assertEqual("4be83a8f-ab97-44c7-8dc6-1666c8dfb68e-b25kZXJkZWVsI0hlZWZ0QmV0cm9ra2VuZQ",
                         lijstObjecten[0].assetId.identificator.waarde)
        self.assertEqual("000a35d5-c4a5-4a36-8620-62c99e053ba0-b25kZXJkZWVsI05ldHdlcmtwb29ydA",
                         lijstObjecten[0].bronAssetId.identificator.waarde)
        self.assertEqual("5434ffca-8bdc-445a-a4ba-b395c87dec30-cHVybDpBZ2VudA",
                         lijstObjecten[0].doelAssetId.identificator.waarde)
        self.assertEqual("toezichter", lijstObjecten[0].rol.waarde.invulwaarde)
        self.assertEqual(True, lijstObjecten[0].isActief.waarde)
        self.assertListEqual([], lijstObjecten[0].specifiekeContactinfo.waarde)

    def test_decode_Davie_json_case_3_and_assert_fields(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(self.jsonDataCase3)
        self.assertEqual(1, len(lijstObjecten))
        self.assertTrue(isinstance(lijstObjecten[0], Wegberm))

        with self.subTest("Assert DecimalFloatField"):
            self.assertTrue(isinstance(lijstObjecten[0].niveau, DecimalFloatField))
            self.assertEqual(1.1, lijstObjecten[0].niveau.waarde)

        with self.subTest("Assert KwantWrdInMeter"):
            self.assertTrue(isinstance(lijstObjecten[0].breedte, KwantWrdInMeter))
            self.assertEqual(2.0, lijstObjecten[0].breedte.waarde)

    def test_decode_Davie_json_case_4_and_assert_fields(self):
        davie_decoder = DavieDecoder()
        lijstObjecten = davie_decoder.decode(self.jsonDataCase4) # TODO fails tests
        self.assertEqual(1, len(lijstObjecten))
        self.assertTrue(isinstance(lijstObjecten[0], Verkeersregelaar))

        with self.subTest("Assert KardinaliteitField met KeuzelijstField"):
            self.assertTrue(isinstance(lijstObjecten[0].coordinatiewijze, KardinaliteitField))
            self.assertTrue(isinstance(lijstObjecten[0].coordinatiewijze.waarde, list))
            self.assertEqual("centraal", lijstObjecten[0].coordinatiewijze.waarde[0].waarde.invulwaarde)
            self.assertEqual("pulsen", lijstObjecten[0].coordinatiewijze.waarde[1].waarde.invulwaarde)

        with self.subTest("Assert KardinaliteitField met ComplexField"):
            self.assertTrue(isinstance(lijstObjecten[0].externeReferentie, KardinaliteitField))
            self.assertTrue(isinstance(lijstObjecten[0].externeReferentie.waarde, list))
            self.assertEqual("bij externe partij 2", lijstObjecten[0].externeReferentie.waarde[0].externePartij.waarde)
            self.assertEqual("externe referentie 2", lijstObjecten[0].externeReferentie.waarde[0].externReferentienummer.waarde)
            self.assertEqual("bij externe partij 1", lijstObjecten[0].externeReferentie.waarde[1].externePartij.waarde)
            self.assertEqual("externe referentie 1", lijstObjecten[0].externeReferentie.waarde[1].externReferentienummer.waarde)