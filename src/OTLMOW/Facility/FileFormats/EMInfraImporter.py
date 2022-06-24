import base64
import json

from requests import Session

from OTLMOW.Facility.FileFormats.EMInfraDecoder import EMInfraDecoder
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject


class EMInfraImporter:
    def __init__(self, requester: Session):
        self.decoder = EMInfraDecoder()
        self.requester = requester
        self.cursor = ''

    def get_objects_from_oslo_search_endpoint(self, url_part: str, filter_string: str = '{}', size: int = 100,
                                              only_next_page: bool = False) -> [dict]:
        url = f"eminfra/core/api/otl/{url_part}/search"
        body_fixed_part = '{"size": ' + f'{size}' + ''
        if filter_string != '{}':
            body_fixed_part += ', "filters": ' + filter_string

        json_list = []
        while True:
            body = body_fixed_part
            if self.cursor != '':
                body += ', "fromCursor": ' + f'"{self.cursor}"'
            body += '}'
            json_data = json.loads(body)

            response = self.requester.post(url=url, json=json_data)

            decoded_string = response.content.decode("utf-8")
            dict_obj = json.loads(decoded_string)
            keys = response.headers.keys()
            json_list.extend(dict_obj['@graph'])
            if 'em-paging-next-cursor' in keys:
                self.cursor = response.headers['em-paging-next-cursor']
            else:
                self.cursor = ''
            if only_next_page:
                return json_list
            if self.cursor == '':
                return json_list

    def import_assets_from_webservice_by_uuids(self, asset_uuids: [str]) -> [OTLObject]:
        asset_list_string = '", "'.join(asset_uuids)
        filter_string = '{ "uuid": ' + f'["{asset_list_string}"]' + ' }'
        obj_list = self.get_objects_from_oslo_search_endpoint(url_part='assets', filter_string=filter_string)

        asset_list = []
        for obj in obj_list:
            asset_list.append(self.decoder.decode_json_object(obj))
        return asset_list

    def import_assets_from_webservice_by_type_uuid(self, type_uuid: str) -> [OTLObject]:
        filter_string = '{ "type": ' + f'"{type_uuid}"' + ' }'
        obj_list = self.get_objects_from_oslo_search_endpoint(url_part='assets', filter_string=filter_string)

        asset_list = []
        for obj in obj_list:
            asset_list.append(self.decoder.decode_json_object(obj))
        return asset_list

    def import_assetrelaties_from_webservice_by_assetuuids(self, asset_uuids: [str]) -> [OTLObject]:
        asset_list_string = '", "'.join(asset_uuids)
        filter_string = '{ "asset": ' + f'["{asset_list_string}"]' + ' }'
        obj_list = self.get_distinct_set_from_list_of_relations(
            self.get_objects_from_oslo_search_endpoint(url_part='assetrelaties', filter_string=filter_string))

        asset_list = []
        for obj in obj_list:
            asset_list.append(self.decoder.decode_json_object(obj))
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
            asset_list.append(self.decoder.decode_json_object(obj))
        return asset_list

    def import_asset_from_webservice_by_uuid(self, asset_uuid: str) -> OTLObject:
        url = f"https://services.apps.mow.vlaanderen.be/eminfra/core/api/otl/assets/search"
        body = '{"filters": { "uuid": ' + f'["{asset_uuid}"]' + ' }}'
        json_data = json.loads(body)
        response = self.requester.post(url, json=json_data)

        data = response.content.decode("utf-8")
        jsonobj = json.loads(data)
        obj_list = jsonobj["@graph"]

        return self.decoder.decode_json_object(obj_list[0])

    def import_asset_from_webservice_by_asset_id(self, asset_id) -> str:
        url = f"eminfra/core/api/otl/assets/{asset_id}"
        response = self.requester.get(url)
        data = response.content.decode("utf-8")
        return self.decoder.decode_object(data)

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

    @staticmethod
    def get_distinct_set_from_list_of_relations(relation_list: [dict]) -> [dict]:
        return list({x["@id"]: x for x in relation_list}.values())