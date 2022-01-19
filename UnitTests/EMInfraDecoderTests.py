from unittest import TestCase

from EMInfraResponseTestDouble import ResponseTestDouble
from Facility.EMInfraDecoder import EMInfraDecoder
from ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from OTLModel.Classes.Omvormer import Omvormer


class EMInfraDecoderTests(TestCase):
    def test_decodeFirstEntry(self):
        responseString = ResponseTestDouble().response
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

    def test_decodeAndEncode(self):
        responseString = ResponseTestDouble().response
        decoder = EMInfraDecoder()
        lijst = decoder.decodeGraph(responseString)
        encoder = OtlAssetJSONEncoder()
        actualJsonString = encoder.encode(lijst)

