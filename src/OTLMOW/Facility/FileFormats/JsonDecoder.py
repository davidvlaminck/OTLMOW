import json

from OTLMOW.Facility.AssetFactory import AssetFactory


class JsonDecoder:
    def __init__(self, settings=None):
        if settings is None:
            settings = {}
        self.settings = settings

        if 'file_formats' not in self.settings:
            raise ValueError("The settings are not loaded or don't contain settings for file formats")
        json_settings = next((s for s in settings['file_formats'] if 'name' in s and s['name'] == 'json'), None)
        if json_settings is None:
            raise ValueError("Unable to find json in file formats settings")

        self.settings = json_settings

    def decode_json_string(self, jsonString):
        dict_list = json.loads(jsonString)
        lijst = []
        for obj in dict_list:
            typeURI = next(value for key, value in obj.items() if 'typeURI' in key)

            if 'https://wegenenverkeer.data.vlaanderen.be/ns' not in typeURI:
                raise ValueError('typeURI should start with "https://wegenenverkeer.data.vlaanderen.be/ns" to use this decoder')

            instance = AssetFactory().dynamic_create_instance_from_uri(typeURI)
            lijst.append(instance)

            for key, value in obj.items():
                if 'typeURI' in key or value == '' or value == [] or key == 'bron' or key == 'doel':
                    continue

                self.set_value_by_dictitem(instance, key, value, self.settings['dotnotatie']['waarde_shortcut_applicable'])
        return lijst

    def set_value_by_dictitem(self, instanceOrAttribute, key, value, waarde_shortcut=False):
        attribute_to_set = getattr(instanceOrAttribute, '_' + key)
        if attribute_to_set.field.waardeObject is not None:  # complex / union / KwantWrd / dte

            if isinstance(value, list):
                for index, listitem in enumerate(value):
                    if attribute_to_set.waarde is None or len(attribute_to_set.waarde) <= index:
                        attribute_to_set.add_empty_value()

                    if attribute_to_set.field.waarde_shortcut_applicable and waarde_shortcut:  # dte / kwantWrd
                        attribute_to_set.waarde[index]._waarde.set_waarde(listitem)
                    else:  # complex / union
                        for k, v in listitem.items():
                            self.set_value_by_dictitem(attribute_to_set.waarde[index], k, v, waarde_shortcut)

            elif isinstance(value, dict):  # only complex / union possible
                if attribute_to_set.waarde is None:
                    attribute_to_set.add_empty_value()

                for k, v in value.items():
                    self.set_value_by_dictitem(attribute_to_set.waarde, k, v, waarde_shortcut)
            else:  # must be a dte / kwantWrd
                if attribute_to_set.waarde is None:
                    attribute_to_set.add_empty_value()

                attribute_to_set.waarde._waarde.set_waarde(value)
        else:
            attribute_to_set.set_waarde(value)
