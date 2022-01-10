from unittest import TestCase

from EMInfraResponseTestDouble import ResponseTestDouble
from Facility.EMInfraDecoder import EMInfraDecoder
from ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from OTLModel.Classes.Omvormer import Omvormer


class EMInfraDecoderTests(TestCase):
    def test_decodeFirstEntry(self):
        responseString = ResponseTestDouble().response
        decoder = EMInfraDecoder()
        list = decoder.decode(responseString)
        first = list[0]
        self.assertTrue(isinstance(first, Omvormer))
        self.assertEqual("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer", first.typeURI)
        self.assertEqual("ENCA0469", first.naam.waarde)
        self.assertEqual(None, first.notitie.waarde)  # TODO check
        self.assertEqual("Encoder", first.type.waarde.invulwaarde)
        self.assertEqual(True, first.isActief.waarde)
        self.assertEqual("in-gebruik", first.toestand.waarde.invulwaarde)
        self.assertEqual("10.216.10.33", first.ipAdres.waarde)
        self.assertEqual("AWV", first.assetId.toegekendDoor.waarde)
        self.assertEqual("0005bafb-838f-47e0-a4e2-20dd120ede6b-b25kZXJkZWVsI09tdm9ybWVy", first.assetId.identificator.waarde)

    def test_decodeAndEncode(self):
        responseString = ResponseTestDouble().response
        decoder = EMInfraDecoder()
        lijst = decoder.decode(responseString)
        encoder = OtlAssetJSONEncoder()
        actualJsonString = encoder.encode(lijst)

