import unittest

from OTLMOW.Facility.CertRequester import CertRequester
from OTLMOW.Facility.EMInfraImporter import EMInfraImporter


class EMInfraImporterTests(unittest.TestCase):
    @unittest.skip('error in EMInfrImporter')
    def test_ImportEmptyFileReturnEmptyList(self):
        asset_id = '000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n'
        cert_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.crt'
        key_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.key'
        certRequester = CertRequester(cert_path, key_path)
        importer = EMInfraImporter(requester=certRequester)
        asset = importer.import_asset_from_webservice_by_asset_id(asset_id)

        self.assertEqual(asset_id, asset.assetId.identificator)

    def test_get_asset_id_from_uuid_and_typeURI(self):
        asset_id = '000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n'
        uuid = '000d3091-deca-4714-8f82-d95aace9ea90'
        typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring'
        cert_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.crt'
        key_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.key'
        certRequester = CertRequester(cert_path, key_path)
        importer = EMInfraImporter(requester=certRequester)
        result = importer.get_asset_id_from_uuid_and_typeURI(uuid, typeURI)
        self.assertEqual(asset_id, result)
