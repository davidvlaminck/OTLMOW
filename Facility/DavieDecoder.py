import json

from Facility.AttributeSetters import AttributeSetterFactory
from OTLModel.ClassLoader import ClassLoader


class DavieDecoder:
    def decode(self, jsonString):
        dict_list = json.loads(jsonString)
        lijst = []
        for obj in dict_list:
            typeURI = next(value for key, value in obj.items() if 'typeURI' in key)

            if 'https://wegenenverkeer.data.vlaanderen.be/ns' not in typeURI:
                raise ValueError('typeURI should start with "https://wegenenverkeer.data.vlaanderen.be/ns" to use this decoder')

            instance = ClassLoader().dynamic_create_instance_from_uri(typeURI)
            lijst.append(instance)

            for key, value in obj.items():
                if 'typeURI' in key or value == '':
                    continue
                if 'geometrie' in key:
                    key = 'loc:Locatie.geometry'
                attr_naam = key.split('.')[-1]
                attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
                if attribute_setter is not None:
                    attribute_setter.set_attribute(value)

        return lijst
