import datetime
import json

from OTLModel.ClassLoader import ClassLoader
from OTLModel.Datatypes.DateField import DateField


def set_attribute_by_dotnotatie(instanceOrAttribute, key, value):
    if isinstance(value, dict):
        for k, v in value.items():
            set_attribute_by_dotnotatie(getattr(instanceOrAttribute, key), k, v)
    elif type(value) is list:
        attr = getattr(instanceOrAttribute, '_' + key)
        if not attr.field._uses_waarde_object:
            setattr(instanceOrAttribute, key, value)
            return
        valueList = []
        for item in value:
            waardeObject = attr.field.waardeObject()
            for k, v in item.items():
                set_attribute_by_dotnotatie(waardeObject, k, v)
            valueList.append(waardeObject)
        setattr(instanceOrAttribute, key, valueList)
    else:
        attr = getattr(instanceOrAttribute, '_' + key)
        if attr.field.waardeObject is not None and not attr.field._uses_waarde_object:
            waardeAttr = getattr(attr, "waarde")
            set_attribute_by_dotnotatie(waardeAttr, "waarde", value)
        else:
            if attr.field is DateField:
                val = datetime.datetime.strptime(value, '%Y-%m-%d')
                setattr(instanceOrAttribute, key, val)
            else:
                setattr(instanceOrAttribute, key, value)


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
                if 'typeURI' in key or value == '' or value == [] or key == 'bron' or key == 'doel':
                    continue
                if 'geometrie' in key:
                    key = 'loc:Locatie.geometry'

                set_attribute_by_dotnotatie(instance, key, value)

                # attr_naam = key.split('.')[-1]
                # getattr(instance, attr_naam)

                # attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
                # if attribute_setter is not None:
                #     attribute_setter.set_attribute(value)

        return lijst
