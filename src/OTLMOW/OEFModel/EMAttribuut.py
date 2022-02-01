import math
import warnings
from datetime import datetime

from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class EMAttribuut(AttributeInfo):
    def __init__(self, naam='', label='', objectUri='', definitie='', kardinaliteit='1..1', field=OTLField):
        super().__init__()
        self.naam = naam
        self.label = label
        self.objectUri = objectUri
        self.verkorte_uri = objectUri.replace('https://lgc.data.wegenenverkeer.be/ns/attribuut#', '')
        self.definitie = definitie
        self.kardinaliteit = kardinaliteit
        self.waarde = None
        self.field = field

    def default(self):
        return self.waarde

    def set_waarde(self, value, owner=None):
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
