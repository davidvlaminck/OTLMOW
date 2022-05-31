import decimal
import random

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class FloatOrDecimalField(OTLField):
    """Beschrijft een decimaal getal volgens http://www.w3.org/2001/XMLSchema#decimal."""
    naam = 'Decimal'
    objectUri = 'http://www.w3.org/2001/XMLSchema#decimal'
    definition = 'Beschrijft een decimaal getal volgens http://www.w3.org/2001/XMLSchema#decimal.'
    label = 'Decimaal getal'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#decimal'

    @classmethod
    def convert_to_correct_type(cls, value):
        if value is None:
            return None
        if isinstance(value, bool) or isinstance(value, float):
            return value
        if isinstance(value, int) or isinstance(value, decimal.Decimal):
            return float(value)
        try:
            float_value = float(value)
            return float_value
        except ValueError:
            raise CouldNotConvertToCorrectType(f'"{value}" could not be converted to correct type (implied by {cls.__name__})')
        except TypeError:
            raise CouldNotConvertToCorrectType(f'"{value}" could not be converted to correct type (implied by {cls.__name__})')

    @staticmethod
    def validate(value, attribuut):
        if value is not None:
            if isinstance(value, bool) or isinstance(value, float):
                return True
            raise TypeError(f'expecting a number (int, float or Decimal) in {attribuut.naam}')
        return True

    @staticmethod
    def create_dummy_data():
        return round(random.random() * 100, 2)

    def __str__(self):
        return OTLField.__str__(self)
