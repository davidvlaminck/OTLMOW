import decimal
import logging
import random

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class IntegerField(OTLField):
    """Beschrijft een geheel getal volgens http://www.w3.org/2001/XMLSchema#integer."""
    naam = 'Integer'
    objectUri = 'http://www.w3.org/2001/XMLSchema#integer'
    definition = 'Beschrijft een DateField getal volgens http://www.w3.org/2001/XMLSchema#integer.'
    label = 'Geheel getal'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#integer'

    @classmethod
    def convert_to_correct_type(cls, value, log_warnings=True):
        if value is None:
            return None
        if isinstance(value, bool):
            if log_warnings:
                logging.warning('Assigned a boolean to an integer datatype. Automatically converted to the correct type. Please change the type')
            return value
        if isinstance(value, int):
            return value
        if isinstance(value, float) or isinstance(value, decimal.Decimal):
            i = int(value)
            if value - i != 0:
                raise CouldNotConvertToCorrectTypeError(f'{value} could not be converted to correct type (implied by {cls.__name__})')
            if log_warnings:
                logging.warning(
                    'Assigned a float/decimal to an integer datatype. Automatically converted to the correct type. Please change the type')
            return i
        try:
            if isinstance(value, str):
                float_value = float(value)
                int_value = int(float_value)
                if int_value != float_value:
                    raise CouldNotConvertToCorrectTypeError(f'{value} could not be converted to correct type (implied by {cls.__name__})')
                if log_warnings:
                    logging.warning('Assigned a string to an integer datatype. Automatically converted to the correct type. Please change the type')
                return int_value
            return int(value)
        except Exception:
            raise CouldNotConvertToCorrectTypeError(f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, int):
            raise TypeError(f'expecting an integer in {attribuut.naam}')
        return True

    def __str__(self):
        return OTLField.__str__(self)

    @classmethod
    def create_dummy_data(cls):
        return random.randint(-100, 100)
