import json

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.DotnotatieHelper import DotnotatieHelper
from OTLMOW.OEFModel.OEFClassLoader import OEFClassLoader
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject


class EMInfraDecoder:
    def decodeGraph(self, responseString):
        dict_obj = json.loads(responseString)
        lijst = []
        for obj in dict_obj["@graph"]:
            lijst.append(self.decode_json_object(obj))

        return lijst

    def decode_object(self, objString):
        obj = json.loads(objString)
        return self.decode_json_object(obj)

    def decode_json_object(self, obj) -> OTLObject:
        typeURI = next(value for key, value in obj.items() if 'typeURI' in key)

        if 'https://wegenenverkeer.data.vlaanderen.be/ns' in typeURI:
            instance = AssetFactory().dynamic_create_instance_from_uri(typeURI)
        else:
            instance = OEFClassLoader().dynamic_create_instance_from_uri(typeURI)

        for key, value in obj.items():
            if key.startswith('@') or 'typeURI' in key or value == '' or 'puntlocatie' in key:
                continue
            if 'geo:' in key:
                if 'geo:Geometrie.log' in obj and len(obj['geo:Geometrie.log']) > 0:
                    geo_item = obj['geo:Geometrie.log'][0]
                    geo_dict = geo_item['geo:DtcLog.geometrie']
                    for key, value in geo_dict.items():
                        if 'geo:DtuGeometrie' in key:
                            DotnotatieHelper.set_attribute_by_dotnotatie(instance, 'geometry', value.replace('(', ' ('))
                continue

            if key == 'AIMObject.assetId':
                pass

            if key == 'loc:Locatie.geometrie':
                if 'geo:Geometrie.log' in obj:
                    continue
                else:
                    DotnotatieHelper.set_attribute_by_dotnotatie(instance, 'geometry', value.replace('(', ' ('))
                    continue

            # TODO fix set attributes

            value = self.trim_keuzelijst_from_ld_notation(value)

            if key != 'loc:Locatie.geometry':
                value = self.trim_keys_from_ld_notation(value)

            DotnotatieHelper.set_attribute_by_dotnotatie(instance, key.split('.')[-1], value, waarde_shortcut_applicable=True)

        return instance

    @classmethod
    def trim_keys_from_ld_notation(cls, value):
        if isinstance(value, dict):
            for k, v in set(value.items()):
                value[k.split('.')[-1]] = v
                value.pop(k)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    cls.trim_keys_from_ld_notation(item)
        return value

    @classmethod
    def trim_keuzelijst_from_ld_notation(cls, value):
        if isinstance(value, str) and 'https://wegenenverkeer.data.vlaanderen.be/id/concept' in value:
            return value.split('/')[-1]
        elif isinstance(value, dict):
            for k, v in set(value.items()):
                value[k] = cls.trim_keuzelijst_from_ld_notation(v)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                value[index] = cls.trim_keys_from_ld_notation(item)
        return value

