import json

from OTLMOW.Facility.ToOTLDecoder import ToOTLDecoder
from OTLMOW.OEFModel.OEFClassLoader import OEFClassLoader
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject
from OTLMOW.OTLModel.ClassLoader import ClassLoader


class EMInfraDecoder(ToOTLDecoder):
    def decodeGraph(self, responseString):
        dict_obj = json.loads(responseString)
        lijst = []
        for obj in dict_obj["@graph"]:
            lijst.append(self.decodeJsonObject(obj))

        return lijst

    def decodeObject(self, objString):
        obj = json.loads(objString)
        return self.decodeJsonObject(obj)

    def decodeJsonObject(self, obj) -> OTLObject:
        typeURI = next(value for key, value in obj.items() if 'typeURI' in key)

        if 'https://wegenenverkeer.data.vlaanderen.be/ns' in typeURI:
            instance = ClassLoader().dynamic_create_instance_from_uri(typeURI)
        else:
            instance = OEFClassLoader().dynamic_create_instance_from_uri(typeURI)

        for key, value in obj.items():
            if key.startswith('@') or 'typeURI' in key or value == '' or 'puntlocatie' in key or 'geo:' in key:
                continue
            if 'geometrie' in key:
                key = 'loc:Locatie.geometry'

            value = self.trim_keuzelijst_from_ld_notation(value)

            if key != 'loc:Locatie.geometry':
                value = self.trim_keys_from_ld_notation(value)

            self.set_attribute_by_dotnotatie(instance, key.split('.')[-1], value)

        return instance

    def trim_keys_from_ld_notation(self, value):
        if isinstance(value, dict):
            for k, v in set(value.items()):
                value[k.split('.')[-1]] = v
                value.pop(k)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    self.trim_keys_from_ld_notation(item)
        return value

    def trim_keuzelijst_from_ld_notation(self, value):
        if isinstance(value, str) and 'https://wegenenverkeer.data.vlaanderen.be/id/concept' in value:
            return value.split('/')[-1]
        elif isinstance(value, dict):
            for k, v in set(value.items()):
                value[k] = self.trim_keuzelijst_from_ld_notation(v)
        elif isinstance(value, list):
            for item in value:
                i = list.index(value, item)
                value[i] = self.trim_keys_from_ld_notation(item)
        return value

