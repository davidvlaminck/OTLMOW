import logging
import random

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class BooleanField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'Boolean'
    objectUri = 'http://www.w3.org/2001/XMLSchema#boolean'
    definition = 'Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.'
    label = 'Boolean'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#boolean'

    @classmethod
    def convert_to_correct_type(cls, value, log_warnings=True):
        if value is None:
            return None
        if value == True or value == False:
            return value
        if isinstance(value, str):
            if value.lower() == 'false':
                if log_warnings:
                    logging.warning('Assigned a string to a boolean datatype. Automatically converted to the correct type. Please change the type')
                return False
            elif value.lower() == 'true':
                if log_warnings:
                    logging.warning('Assigned a string to a boolean datatype. Automatically converted to the correct type. Please change the type')
                return True
            else:
                raise CouldNotConvertToCorrectType(f'{value} could not be converted to correct type (implied by {cls.__name__})')
        raise CouldNotConvertToCorrectType(f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, bool):
            raise TypeError(f'expecting bool in {attribuut.naam}')
        return True

    def __str__(self):
        return OTLField.__str__(self)

    @staticmethod
    def create_dummy_data():
        return random.choice([True, False])
