import copy
import math

from UnitTests.OTLFieldTests.AttributeInfo import AttributeInfo
from UnitTests.OTLFieldTests.ComplexField import ComplexField
from UnitTests.OTLFieldTests.OTLField import OTLField


class OTLAttribuut(AttributeInfo):
    def __init__(self, naam='', label='', objectUri='', definition='', constraints='', usagenote='', deprecated_version='',
                 kardinaliteit_min='1', kardinaliteit_max='1', field=type, readonly=False, readonlyValue=None):
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

        t =(field)
        d = t()

        if isinstance(d, ComplexField):
            w = d.waarde()
            self.waarde = w

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
            self.waarde = value
        else:
            if self.field.validate(value, attribuut=self):
                self.waarde = value

    def __str__(self):
        return f"naam: {self.naam}; definitie: {self.definition}"