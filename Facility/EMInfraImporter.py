import base64

import requests

from Facility.EMInfraDecoder import EMInfraDecoder


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

    def get_asset_id_from_uuid_and_typeURI(self, uuid, typeURI):
        type = typeURI.split('/ns/')[1]
        type_encoded = base64.b64encode(type.encode('utf-8'))
        return uuid + '-' + type_encoded.decode("utf-8")


# cert_path = 'datamanager_eminfra_prd.awv.vlaanderen.be.crt'
# key_path = 'datamanager_eminfra_prd.awv.vlaanderen.be.key'
# url = "https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/assets"
# response = requests.get(url, cert=(cert_path, key_path))  # headers={"accept": "application/vnd.awv.eminfra.v2+json"}
#
# decoded_string = response.content.decode("utf-8")

# 000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n
# 000d0d69-e1fc-40e3-9f45-99ac8e6aa341-b25kZXJkZWVsI05ldHdlcmtwb29ydA