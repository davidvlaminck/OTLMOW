import math
import warnings
from datetime import datetime

from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class EMAttribuut(AttributeInfo):
    def __init__(self, naam='', label='', objectUri='', definitie='', kardinaliteit='1..1', field=OTLField, owner=None):
        super().__init__()
        self.naam = naam
        self.label = label
        self.objectUri = objectUri
        self.verkorte_uri = objectUri.replace('https://lgc.data.wegenenverkeer.be/ns/attribuut#', '')
        self.definitie = definitie
        self.kardinaliteit = kardinaliteit
        self.waarde = None
        self.field = field
        self.owner = owner
        self.kardinaliteit_max = '1'

        if self.field.waardeObject:
            self.waarde = self.field.waardeObject()
            self.waarde._parent = self

    def default(self):
        return self.waarde

    def set_waarde(self, value, owner=None):
        if owner is not None:
            if hasattr(owner, 'deprecated_version'):
                if owner.deprecated_version != '':
                    if hasattr(owner, 'typeURI'):
                        warnings.warn(message=f'{owner.typeURI} is deprecated since version {owner.deprecated_version}',
                                      category=DeprecationWarning)
                    else:
                        warnings.warn(message=f'used a class that is deprecated since version {owner.deprecated_version}',
                                      category=DeprecationWarning)

        if self.kardinaliteit != '1..1':
            kardinaliteit_max = math.inf
        else:
            kardinaliteit_max = 1

        if kardinaliteit_max > 1 and value is not None:
            kardinaliteit_min = 1
            if not isinstance(value, list):
                raise TypeError(f'expecting a list in {owner.__class__.__name__}.{self.naam}')
            elif isinstance(value, list) and isinstance(value, set):
                raise TypeError(f'expecting a non set type of list in {owner.__class__.__name__}.{self.naam}')
            elif 0 < len(value) < kardinaliteit_min:
                raise ValueError(f'expecting at least {kardinaliteit_min} element(s) in {owner.__class__.__name__}.{self.naam}')
            elif len(value) > kardinaliteit_max:
                raise ValueError(f'expecting at most {kardinaliteit_max} element(s) in {owner.__class__.__name__}.{self.naam}')
            for el_value in value:
                try:
                    field_validated = self.field.validate(self.field.convert_to_correct_type(el_value), self)
                    if not field_validated:
                        raise ValueError(
                            f'invalid value in list for {owner.__class__.__name__}.{self.naam}: {el_value} is not valid, must be valid for {self.field.naam}')
                except TypeError as error:
                    raise ValueError(
                        f'invalid value in list for {owner.__class__.__name__}.{self.naam}: {el_value} is not valid, must be valid for {self.field.naam}\n' + str(
                            error))
            new_list = []
            for el_value in value:
                new_list.append(self.field.convert_to_correct_type(el_value))
            self.waarde = new_list
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
                if self.field.validate(value=self.field.convert_to_correct_type(value), attribuut=self):
                    self.waarde = self.field.convert_to_correct_type(value)

    def __str__(self):
        s = (f'information about {self.naam}:\n'
             f'naam: {self.naam}\n'
             f'uri: {self.objectUri}\n'
             f'definitie: {self.definitie}\n'
             f'label: {self.label}\n'             
             f'kardinaliteit: {self.kardinaliteit}\n')
        return s
