import json
import unittest
from unittest import TestCase

from GeneralTests.EMInfraResponseTestDouble import ResponseTestDouble
from OTLMOW.Facility.EMInfraDecoder import EMInfraDecoder
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OTLModel.Classes.Omvormer import Omvormer


class EMInfraDecoderTests(TestCase):
    def test_decodeFirstEntry(self):
        responseString = ResponseTestDouble().response
        otl_facility = OTLFacility(None, settings_path='C:\\resources\\settings_OTLMOW.json')
        decoder = EMInfraDecoder()
        first = decoder.decodeGraph(responseString)[0]

        with self.subTest("Testing type match"):
            self.assertTrue(isinstance(first, Omvormer))
            self.assertEqual("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer", first.typeURI)

        with self.subTest("Testing keuzelijst"):
            self.assertEqual("Encoder", first.type)
            self.assertEqual("in-gebruik", first.toestand)

        with self.subTest("Testing StringField"):
            self.assertEqual("ENCA0469", first.naam)
            self.assertEqual(None, first.notitie)

        with self.subTest("Testing BooleanField"):
            self.assertEqual(True, first.isActief)

        with self.subTest("Testing Dte"):
            self.assertEqual("10.216.10.33", first.ipAdres.waarde)

        with self.subTest("Testing Dtc"):
            self.assertEqual("AWV", first.assetId.toegekendDoor)
            self.assertEqual("0005bafb-838f-47e0-a4e2-20dd120ede6b-b25kZXJkZWVsI09tdm9ybWVy", first.assetId.identificator)

    def test_decode_single_entry(self):
        responseString = ResponseTestDouble().single_response
        otl_facility = OTLFacility(None, settings_path='C:\\resources\\settings_OTLMOW.json')
        decoder = EMInfraDecoder()
        first = decoder.decodeGraph(responseString)[0]

        with self.subTest("Testing type match"):
            self.assertEqual("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring", first.typeURI)

        with self.subTest("Testing keuzelijst"):
            self.assertEqual("in-gebruik", first.toestand)

        with self.subTest("Testing StringField"):
            self.assertEqual("A10N47.4.K_stroomkring", first.naam)
            self.assertEqual(None, first.notitie)

        with self.subTest("Testing BooleanField"):
            self.assertEqual(True, first.isActief)

        with self.subTest("Testing geometry"):
            self.assertEqual("POINT Z (101489.3 190526.6 0)", first.geometry)

        with self.subTest("Testing Dtc"):
            self.assertEqual("AWV", first.assetId.toegekendDoor)
            self.assertEqual("000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n", first.assetId.identificator)

    def test_trim_jsonld_dict_single_response(self):
        responseString = ResponseTestDouble().single_response
        dict_obj = json.loads(responseString)
        obj = dict_obj["@graph"][0]
        decoder = EMInfraDecoder()

        result = decoder.trim_json_ld_dict(obj)
        expected = {
            '@id': 'https://data.awvvlaanderen.be/id/asset/000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n',
            '@type': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring',
            'assetId': {'identificator': '000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n',
                        'toegekendDoor': 'AWV'},
            'geo:log': [{'geo:bron': 'overerving',
                         'geo:gaVersie': 'GA_2.2.0',
                         'geo:geometrie': {'geo:punt': 'POINT Z(101489.3 190526.6 0)'},
                         'geo:nauwkeurigheid': '',
                         'geo:niveau': '-1',
                         'geo:overerving': [{'geo:erfgenaamId': {
                             'identificator': '000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n',
                             'toegekendDoor': 'AWV'},
                                             'geo:erflaatId': {
                                                 'identificator': 'b59f3b37-fe77-4677-9e7c-e5491319e759-b25kZXJkZWVsI0xhYWdzcGFubmluZ3Nib3Jk',
                                                 'toegekendDoor': 'AWV'},
                                             'geo:relatieId': {
                                                 'identificator': 'b80e2ca4-123c-46ac-b747-4b6e8075bf78-b25kZXJkZWVsI0JldmVzdGlnaW5n',
                                                 'toegekendDoor': 'AWV'}}]}],
            'isActief': True,
            'loc:geometrie': 'POINT Z(101489.3 190526.6 0)',
            'loc:omschrijving': '',
            'loc:puntlocatie': {'loc:adres': {'loc:bus': '',
                                              'loc:gemeente': 'Gent',
                                              'loc:nummer': '35',
                                              'loc:postcode': '9051',
                                              'loc:provincie': 'Oost-Vlaanderen',
                                              'loc:straat': 'Luchthavenlaan'},
                                'loc:bron': '',
                                'loc:precisie': '',
                                'loc:puntgeometrie': {'loc:lambert72': {'loc:xcoordinaat': 101489.3,
                                                                        'loc:ycoordinaat': 190526.6,
                                                                        'loc:zcoordinaat': 0}},
                                'loc:weglocatie': {'loc:gemeente': 'Gent',
                                                   'loc:ident2': 'A10',
                                                   'loc:ident8': 'A0100002',
                                                   'loc:referentiepaalAfstand': -9,
                                                   'loc:referentiepaalOpschrift': 47.4,
                                                   'loc:straatnaam': ''}},
            'naam': 'A10N47.4.K_stroomkring',
            'notitie': '',
            'toestand': 'in-gebruik',
            'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring'}
        self.assertEqual(expected, result)

    def test_decode(self):
        responseString = ResponseTestDouble().response
        decoder = EMInfraDecoder()
        lijst = decoder.decodeGraph(responseString)
        self.assertEqual(56, len(lijst))

    def test_trim_keys_from_ld_notation(self):
        decoder = EMInfraDecoder()

        with self.subTest("Testing Dtc"):
            value = {'DtcIdentificator.toegekendDoor': 'AWV',
                     'DtcIdentificator.identificator': '0005bafb-838f-47e0-a4e2-20dd120ede6b-b25kZXJkZWVsI09tdm9ybWVy'}
            result = decoder.trim_json_ld_dict(value)
            expected = {'toegekendDoor': 'AWV', 'identificator': '0005bafb-838f-47e0-a4e2-20dd120ede6b-b25kZXJkZWVsI09tdm9ybWVy'}
            self.assertDictEqual(expected, result)

        with self.subTest("Testing Boolean"):
            value = True
            result = decoder.trim_json_ld_dict(value)
            expected = True
            self.assertEqual(expected, result)

        with self.subTest("Testing Kard *"):
            value = ["geel", "rood"]
            result = decoder.trim_json_ld_dict(value)
            expected = ["geel", "rood"]
            self.assertListEqual(expected, result)

        with self.subTest("Testing Kard * ComplexField"):
            value = [
                {'DtcExterneReferentie.externReferentienummer': 'extern ref 1', 'DtcExterneReferentie.externePartij': 'extern 1'},
                {'DtcExterneReferentie.externReferentienummer': 'extern ref 2', 'DtcExterneReferentie.externePartij': 'extern 2'}]
            result = decoder.trim_json_ld_dict(value)
            expected = [{'externReferentienummer': 'extern ref 1', 'externePartij': 'extern 1'},
                        {'externReferentienummer': 'extern ref 2', 'externePartij': 'extern 2'}]
            self.assertListEqual(expected, result)
