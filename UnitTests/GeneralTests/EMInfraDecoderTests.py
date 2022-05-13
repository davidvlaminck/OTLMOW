import unittest
from unittest import TestCase

from GeneralTests.EMInfraResponseTestDouble import ResponseTestDouble
from OTLMOW.Facility.EMInfraDecoder import EMInfraDecoder
from OTLMOW.OTLModel.Classes.Omvormer import Omvormer


class EMInfraDecoderTests(TestCase):
    def test_decodeFirstEntry(self):
        responseString = ResponseTestDouble().response
        decoder = EMInfraDecoder()
        first = decoder.decodeGraph(responseString)[0]
        # TODO parse EM Infra graph so that keys don't contain dots

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

    def test_decode(self):
        responseString = ResponseTestDouble().response
        decoder = EMInfraDecoder()
        lijst = decoder.decodeGraph(responseString)
        self.assertEqual(56, len(lijst))

    def test_trim_keys_from_ld_notation(self):
        decoder = EMInfraDecoder()

        with self.subTest("Testing Dtc"):
            value = {'DtcIdentificator.toegekendDoor': 'AWV', 'DtcIdentificator.identificator': '0005bafb-838f-47e0-a4e2-20dd120ede6b-b25kZXJkZWVsI09tdm9ybWVy'}
            result = decoder.trim_keys_from_ld_notation(value)
            expected = {'toegekendDoor': 'AWV', 'identificator': '0005bafb-838f-47e0-a4e2-20dd120ede6b-b25kZXJkZWVsI09tdm9ybWVy'}
            self.assertDictEqual(expected, result)

        with self.subTest("Testing Boolean"):
            value = True
            result = decoder.trim_keys_from_ld_notation(value)
            expected = True
            self.assertEqual(expected, result)

        with self.subTest("Testing Kard *"):
            value = ["geel", "rood"]
            result = decoder.trim_keys_from_ld_notation(value)
            expected = ["geel", "rood"]
            self.assertListEqual(expected, result)

        with self.subTest("Testing Kard * ComplexField"):
            value = [{'DtcExterneReferentie.externReferentienummer': 'extern ref 1', 'DtcExterneReferentie.externePartij': 'extern 1'},
                     {'DtcExterneReferentie.externReferentienummer': 'extern ref 2', 'DtcExterneReferentie.externePartij': 'extern 2'}]
            result = decoder.trim_keys_from_ld_notation(value)
            expected = [{'externReferentienummer': 'extern ref 1', 'externePartij': 'extern 1'},
                        {'externReferentienummer': 'extern ref 2', 'externePartij': 'extern 2'}]
            self.assertListEqual(expected, result)
