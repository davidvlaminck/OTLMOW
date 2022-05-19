import json
from datetime import datetime

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.OTLModel.Datatypes.DateField import DateField


class JsonDecoder:
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

                self.set_value_by_dictitem(instance, key, value, True)  # get True from settings
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

        return

        if isinstance(value, dict):
            for k, v in value.items():
                self.set_value_by_dictitem(getattr(instanceOrAttribute, key), k, v)
        elif type(value) is list:
            attr = getattr(instanceOrAttribute, '_' + key)
            if not attr.field.waarde_shortcut_applicable:
                setattr(instanceOrAttribute, key, value)
                return
            valueList = []
            for item in value:
                waardeObject = attr.field.waardeObject()
                for k, v in item.items():
                    self.set_value_by_dictitem(waardeObject, k, v)
                valueList.append(waardeObject)
            setattr(instanceOrAttribute, key, valueList)
        else:
            attr = getattr(instanceOrAttribute, '_' + key)
            if attr.field.waardeObject is not None and attr.field.waarde_shortcut_applicable:
                waardeAttr = attr.get_waarde()
                self.set_value_by_dictitem(waardeAttr, "waarde", value)
            else:
                if attr.field is DateField:
                    val = datetime.datetime.strptime(value, '%Y-%m-%d')
                    setattr(instanceOrAttribute, key, val)
                else:
                    setattr(instanceOrAttribute, key, value)



