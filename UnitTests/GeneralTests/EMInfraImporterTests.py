import unittest

from OTLMOW.Facility.FileFormats.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.RequesterFactory import RequesterFactory


class EMInfraImporterTests(unittest.TestCase):
    def test_ImportEmptyFileReturnEmptyList(self):
        otl_facility = OTLFacility(logfile='',
                                   enable_relation_features=True,
                                   settings_path='C:\\resources\\settings_OTLMOW.json')

        requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')

        importer = EMInfraImporter(requester=requester)
        asset_id = '000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n'
        asset = importer.import_asset_from_webservice_by_asset_id(asset_id)

        self.assertEqual(asset_id, asset.assetId.identificator)

    def test_get_asset_id_from_uuid_and_typeURI(self):
        otl_facility = OTLFacility(logfile='',
                                   enable_relation_features=True,
                                   settings_path='C:\\resources\\settings_OTLMOW.json')

        requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')

        asset_id = '000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n'
        uuid = '000d3091-deca-4714-8f82-d95aace9ea90'
        typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring'

        importer = EMInfraImporter(requester=requester)
        result = importer.get_asset_id_from_uuid_and_typeURI(uuid, typeURI)
        self.assertEqual(asset_id, result)
