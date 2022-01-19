import json

from Facility.ToOTLDecoder import ToOTLDecoder
from OTLModel.ClassLoader import ClassLoader


class DavieDecoder(ToOTLDecoder):
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
                if 'typeURI' in key or value == '' or value == [] or key == 'bron' or key == 'doel':
                    continue
                if 'geometrie' in key:
                    key = 'loc:Locatie.geometry'

                self.set_attribute_by_dotnotatie(instance, key, value)
        return lijst
