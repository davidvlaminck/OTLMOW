import unittest
from unittest import TestCase

from OTLMOW.OTLModel.Classes.Camera import Camera
from OTLMOW.OTLModel.Classes.Voedt import Voedt

expected_result = """{
  "@graph" : [
    {
      "@id" : "https://data.awvvlaanderen.be/id/asset/a11ed3b6-6480-49ca-9a23-406bb12e5d51",
      "@type" : "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera",
      "AIMDBStatus.isActief" : true,
      "loc:Locatie.geometrie" : "POINT Z(153605.7 213882.55 0)"
    },
    {
      "@id" : "https://data.awvvlaanderen.be/id/assetrelatie/ba228f57-2cab-4806-bee7-2d335860bb72",
      "@type" : "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt",
      "RelatieObject.bron" : {
        "@id" : "https://data.awvvlaanderen.be/id/asset/507d4c37-c200-4441-b972-0d4c7bd4684a-b25kZXJkZWVsI1N0cm9vbWtyaW5n",
        "@type" : "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring"
      },
      "RelatieObject.doel" : {
        "@id" : "https://data.awvvlaanderen.be/id/asset/a11ed3b6-6480-49ca-9a23-406bb12e5d51",
        "@type" : "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera"
      },
      "AIMDBStatus.isActief" : true,
      "Voedt.aansluitspanning" : 1
    }
  ]
}"""

@unittest.skip("feature request")
class JsonLDEncoder(TestCase):
    def test_encode_json_ld(self):
        camera = Camera()
        camera.isActief = True
        camera.assetId.identificator = 'a11ed3b6-6480-49ca-9a23-406bb12e5d51'
        camera.geometry = 'POINT Z(153605.7 213882.55 0)'

        voedt = Voedt()
        voedt.assetId.identificator = 'ba228f57-2cab-4806-bee7-2d335860bb72'
        voedt.bronAssetId.identificator = '507d4c37-c200-4441-b972-0d4c7bd4684a'
        voedt.doelAssetId.identificator = 'a11ed3b6-6480-49ca-9a23-406bb12e5d51'
        voedt.isActief = True
        voedt.aansluitspanning.waarde = 1

        list_of_objects = [camera, voedt]

        encoder = OtlAssetJSONLDEncoder(indent=4)
        self.assertEqual(expected_result, self.encoder.encode(list_of_objects))

