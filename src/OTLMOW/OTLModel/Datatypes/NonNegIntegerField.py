import random

from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField


class NonNegIntegerField(IntegerField):
    """Beschrijft een natuurlijk getal volgens http://www.w3.org/2001/XMLSchema#nonNegativeInteger."""
    naam = 'NonNegativeInteger'
    objectUri = 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger'
    definition = 'Beschrijft een natuurlijk getal volgens http://www.w3.org/2001/XMLSchema#nonNegativeInteger.'
    label = 'Natuurlijk getal'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#nonNegativeInteger'

    @staticmethod
    def validate(value, attribuut):
        if value is not None:
            if not isinstance(value, int):
                raise TypeError(f'expecting an integer in {attribuut.naam}')
            if value < 0:
                raise ValueError(f'expecting an integer >= 0 in {attribuut.naam}')
        return True

    def __str__(self):
        return OTLField.__str__(self)

    @staticmethod
    def create_dummy_data():
        return random.randint(0, 100)
