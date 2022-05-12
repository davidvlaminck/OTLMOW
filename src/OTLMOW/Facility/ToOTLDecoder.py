import datetime

from OTLMOW.Facility.Exceptions.DotNotationError import DotNotationError
from OTLMOW.OTLModel.Datatypes import DateField


class ToOTLDecoder:
    def __init__(self):
        pass

    def set_value_by_dotnotatie(self, assetOrAttribuut, dotnotatie, value):
        try:
            eval(f'assetOrAttribuut.{dotnotatie}')
            exec(f'assetOrAttribuut.{dotnotatie} = value')
        except:
            raise DotNotationError(f'{dotnotatie} of {assetOrAttribuut.__repr__()} can not be set to {value}')

    def set_attribute_by_dotnotatie(self, instanceOrAttribute, key, value):
        if isinstance(value, dict):
            for k, v in value.items():
                self.set_attribute_by_dotnotatie(getattr(instanceOrAttribute, key), k, v)
        elif type(value) is list:
            attr = getattr(instanceOrAttribute, '_' + key)
            if not attr.field.waarde_shortcut_applicable:
                setattr(instanceOrAttribute, key, value)
                return
            valueList = []
            for item in value:
                waardeObject = attr.field.waardeObject()
                for k, v in item.items():
                    self.set_attribute_by_dotnotatie(waardeObject, k, v)
                valueList.append(waardeObject)
            setattr(instanceOrAttribute, key, valueList)
        else:
            attr = getattr(instanceOrAttribute, '_' + key)
            if attr.field.waardeObject is not None and not attr.field.waarde_shortcut_applicable:
                waardeAttr = getattr(attr, "waarde")
                self.set_attribute_by_dotnotatie(waardeAttr, "waarde", value)
            else:
                if attr.field is DateField:
                    val = datetime.datetime.strptime(value, '%Y-%m-%d')
                    setattr(instanceOrAttribute, key, val)
                else:
                    setattr(instanceOrAttribute, key, value)


