import base64

import requests

from src.OTLMOW.Facility.EMInfraDecoder import EMInfraDecoder


class EMInfraImporter:
    def __init__(self, cert_path='', key_path=''):
        self.decoder = EMInfraDecoder()
        self.cert_path = cert_path
        self.key_path = key_path

    def import_asset_from_webservice_by_asset_id(self, asset_id):
        url = f"https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/assets/{asset_id}"
        response = requests.get(url, cert=(self.cert_path, self.key_path))
        data = response.content.decode("utf-8")
        return self.decoder.decodeObject(data)

    def import_asset_from_webservice_by_uuid_and_typeURI(self, uuid, typeURI):
        return self.import_asset_from_webservice_by_asset_id(
            self.get_asset_id_from_uuid_and_typeURI(uuid, typeURI)
        )

    @staticmethod
    def get_asset_id_from_uuid_and_typeURI(uuid, typeURI):
        shortUri = typeURI.split('/ns/')[1]
        shortUri_encoded = base64.b64encode(shortUri.encode('utf-8'))
        return uuid + '-' + shortUri_encoded.decode("utf-8")
