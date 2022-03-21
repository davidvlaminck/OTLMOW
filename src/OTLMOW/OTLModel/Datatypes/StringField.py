from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class StringField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'String'
    objectUri = 'http://www.w3.org/2001/XMLSchema#string'
    definition = 'Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string.'
    label = 'String'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#string'

    @classmethod
    def convert_to_correct_type(cls, value):
        if value is None:
            return None
        try:
            str_val = str(value)
            return str_val
        except TypeError:
            raise CouldNotConvertToCorrectType(f'The given value of object of type {type(value)} could not be converted to string (implied by {cls.__name__})')

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, str):
            raise TypeError(f'expecting string in {attribuut.naam}')
        return True

    def __str__(self):
        return OTLField.__str__(self)

