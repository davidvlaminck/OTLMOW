import copy
import math

from UnitTests.OTLFieldTests.AttributeInfo import AttributeInfo
from UnitTests.OTLFieldTests.ComplexField import ComplexField
from UnitTests.OTLFieldTests.KeuzelijstField import KeuzelijstField
from UnitTests.OTLFieldTests.OTLField import OTLField


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

        if self.field._uses_waarde_object:
            if self.field.waardeObject:
                self.waarde = self.field.waardeObject()
            else:
                pass

    def set_waarde(self, value, owner=None):
        # in combinatie met kard indien nodig
        if self.kardinaliteit_max == '*':
            kardinaliteit_max = math.inf
        else:
            kardinaliteit_max = int(self.kardinaliteit_max)
        if kardinaliteit_max > 1:
            kardinaliteit_min = int(self.kardinaliteit_min)
            if not isinstance(value, list):
                raise TypeError(f'expecting list in {owner.__class__.__name__}.{self.naam}')
            elif len(value) < kardinaliteit_min:
                raise ValueError(f'expecting at least {kardinaliteit_min} element(s) in {owner.__class__.__name__}.{self.naam}')
            elif len(value) > kardinaliteit_max:
                raise ValueError(f'expecting at most {kardinaliteit_max} element(s) in {owner.__class__.__name__}.{self.naam}')
            for el_value in value:
                if not self.field.validate(el_value, self):
                    raise ValueError(f'invalid value in list for {owner.__class__.__name__}.{self.naam}: {el_value} is not valid, must be valid for {self.field.naam}')
            self.waarde = self.field.convert_to_correct_type(value)
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