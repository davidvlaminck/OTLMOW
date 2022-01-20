import math
import warnings
from datetime import datetime
from msilib import sequence

from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLField import OTLField


class OTLAttribuut(AttributeInfo):
    def __init__(self, naam='', label='', objectUri='', definition='', constraints='', usagenote='', deprecated_version='',
                 kardinaliteit_min='1', kardinaliteit_max='1', field=OTLField, readonly=False, readonlyValue=None):
        self.naam = naam
        self.label = label
        self.objectUri = objectUri
        self.definition = definition
        self.constraints = constraints
        self.usagenote = usagenote
        self.deprecated_version = deprecated_version
        self.readonly = readonly
        self.kardinaliteit_min = kardinaliteit_min
        self.kardinaliteit_max = kardinaliteit_max
        self.readonlyValue = None
        self.waarde = None
        self.field = field

        if readonly:
            self.__dict__["waarde"] = readonlyValue

        if self.field.waardeObject:
            self.waarde = self.field.waardeObject()
        else:
            pass

    def default(self):
        if self.waarde is not dict and isinstance(self.waarde, list):
            valueList = []
            for item in self.waarde:
                if self.field.waardeObject is not None:
                    waardeDict = vars(item)
                    valueDict = {}
                    for k, v in waardeDict.items():
                        if v.default() is not None:
                            valueDict[k[1:]] = v.default()
                    if len(valueDict) != 0:
                        valueList.append(valueDict)
                else:
                    valueList.append(item)
            return valueList
        if self.field.waardeObject is not None:
            waardeDict = vars(self.waarde)
            valueDict = {}
            for k, v in waardeDict.items():
                if v.default() is not None:
                    valueDict[k[1:]] = v.default()
            if len(valueDict) == 0:
                return None
            return valueDict
        else:
            if isinstance(self.waarde, datetime):
                if self.waarde.hour == 0 and self.waarde.minute == 0 and self.waarde.second == 0:
                    return self.waarde.strftime("%Y-%m-%d")
                else:
                    return self.waarde.strftime("%Y-%m-%d %H:%M:%S")
            else:
                return self.waarde

    def set_waarde(self, value, owner=None, union_type=False):
        if self.kardinaliteit_max == '*':
            kardinaliteit_max = math.inf
        else:
            kardinaliteit_max = int(self.kardinaliteit_max)
        if kardinaliteit_max > 1 and value is not None:
            kardinaliteit_min = int(self.kardinaliteit_min)
            if not isinstance(value, list):
                raise TypeError(f'expecting a list in {owner.__class__.__name__}.{self.naam}')
            elif isinstance(value, list) and isinstance(value, set):
                raise TypeError(f'expecting a non set type of list in {owner.__class__.__name__}.{self.naam}')
            elif len(value) < kardinaliteit_min:
                raise ValueError(f'expecting at least {kardinaliteit_min} element(s) in {owner.__class__.__name__}.{self.naam}')
            elif len(value) > kardinaliteit_max:
                raise ValueError(f'expecting at most {kardinaliteit_max} element(s) in {owner.__class__.__name__}.{self.naam}')
            for el_value in value:
                try:
                    field_validated = self.field.validate(el_value, self)
                    if not field_validated:
                        raise ValueError(f'invalid value in list for {owner.__class__.__name__}.{self.naam}: {el_value} is not valid, must be valid for {self.field.naam}')
                except TypeError as error:
                    raise ValueError(
                        f'invalid value in list for {owner.__class__.__name__}.{self.naam}: {el_value} is not valid, must be valid for {self.field.naam}\n' + str(error))

            self.waarde = self.field.convert_to_correct_type(value)
        else:
            if self.field.waardeObject is not None and isinstance(value, self.field.waardeObject):
                props = vars(self.field.waardeObject)
                for prop_key, prop_value in props.items():
                    if prop_key.startswith('_'):
                        continue
                    if prop_key != 'standaardEenheid':
                        a = getattr(value, prop_key)
                        setattr(self.waarde, prop_key, a)
            else:
                if self.field.validate(value=value, attribuut=self):
                    self.waarde = self.field.convert_to_correct_type(value)



    def __str__(self):
        return f"""information about {self.naam}:
naam: {self.naam}
uri: {self.objectUri}
definition: {self.definition}
label: {self.label}
usagenote: {self.usagenote}
constraints: {self.constraints}
readonly: {self.readonly}
kardinaliteit_min: {self.kardinaliteit_min}
kardinaliteit_max: {self.kardinaliteit_max}
deprecated_version: {self.deprecated_version}"""