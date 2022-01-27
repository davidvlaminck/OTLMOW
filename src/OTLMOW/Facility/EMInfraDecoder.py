import json

from OTLMOW.Facility.ToOTLDecoder import ToOTLDecoder
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

    def decodeJsonObject(self, obj):
        typeURI = next(value for key, value in obj.items() if 'typeURI' in key)

        if 'https://wegenenverkeer.data.vlaanderen.be/ns' not in typeURI:
            return
            #raise ValueError('typeURI should start with "https://wegenenverkeer.data.vlaanderen.be/ns" to use this decoder')

        instance = ClassLoader().dynamic_create_instance_from_uri(typeURI)

        for key, value in obj.items():
            if key.startswith('@') or 'typeURI' in key or value == '' or 'toezichter' in key or 'puntlocatie' in key:
                continue
            if 'geometrie' in key:
                key = 'loc:Locatie.geometry'

            if isinstance(value, str) and 'https://wegenenverkeer.data.vlaanderen.be/id/concept' in value:
                 value = value.split('/')[-1]

            self.set_attribute_by_dotnotatie(instance, key.split('.')[-1], value)

            # attr_naam = key.split('.')[-1]
            # attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            # if attribute_setter is KeuzelijstFieldSetter:
            #     if value != '':
            #         val = value.split('/')[-1]
            #         value = str.lower(val[0]) + val[1:]
            # attribute_setter.set_attribute(value)

        return instance