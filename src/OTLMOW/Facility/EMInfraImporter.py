import base64
import json

from requests import Session

from OTLMOW.Facility.EMInfraDecoder import EMInfraDecoder
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject


class EMInfraImporter:
    def __init__(self, requester: Session):
        self.decoder = EMInfraDecoder()
        self.requester = requester

    def import_assets_from_webservice_by_uuids(self, asset_uuids: [str]) -> [OTLObject]:
        url = "eminfra/core/api/otl/assets/search"
        asset_list_string = '", "'.join(asset_uuids)
        body = '{"filters": { "uuid": ' + f'["{asset_list_string}"]' + ' }}'
        json_data = json.loads(body)
        response = self.requester.post(url, json=json_data)

        data = response.content.decode("utf-8")
        jsonobj = json.loads(data)
        obj_list = jsonobj["@graph"]

        asset_list = []
        for obj in obj_list:
            asset_list.append(self.decoder.decodeJsonObject(obj))
        return asset_list

    def import_assetrelaties_from_webservice_by_assetuuid(self, asset_uuid: str) -> [OTLObject]:
        url = "eminfra/core/api/otl/assetrelaties/search"
        body = '{"filters": { "asset": ' + f'["{asset_uuid}"]' + ' }}'
        json_data = json.loads(body)
        response = self.requester.post(url, json=json_data)

        data = response.content.decode("utf-8")
        jsonobj = json.loads(data)
        obj_list = jsonobj["@graph"]

        asset_list = []
        for obj in obj_list:
            asset_list.append(self.decoder.decodeJsonObject(obj))
        return asset_list

    def import_asset_from_webservice_by_uuid(self, asset_uuid: str) -> OTLObject:
        url = f"https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/assets/search"
        body = '{"filters": { "uuid": ' + f'["{asset_uuid}"]' + ' }}'
        json_data = json.loads(body)
        response = self.requester.post(url, json=json_data)

        data = response.content.decode("utf-8")
        jsonobj = json.loads(data)
        obj_list = jsonobj["@graph"]

        return self.decoder.decodeJsonObject(obj_list[0])

    def import_asset_from_webservice_by_asset_id(self, asset_id) -> str:
        url = f"https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/assets/{asset_id}"
        response = self.requester.get(url)
        data = response.content.decode("utf-8")
        return self.decoder.decodeObject(data)

    def import_asset_from_webservice_by_uuid_and_typeURI(self, uuid, typeURI):
        return self.import_asset_from_webservice_by_asset_id(
            self.get_asset_id_from_uuid_and_typeURI(uuid, typeURI)
        )

    @staticmethod
    def get_asset_id_from_uuid_and_typeURI(uuid, typeURI):
        shortUri = typeURI.split('/ns/')[1]
        if 'lgc' in typeURI:
            shortUri = 'lgc:' + shortUri
        shortUri_encoded = base64.b64encode(shortUri.encode('utf-8'))
        shortUri_encoded = shortUri_encoded.decode("utf-8")
        while shortUri_encoded[-1] == '=':
            shortUri_encoded = shortUri_encoded[:-1]
        return uuid + '-' + shortUri_encoded
