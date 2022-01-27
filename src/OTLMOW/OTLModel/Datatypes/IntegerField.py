from src.OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from src.OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class IntegerField(OTLField):
    """Beschrijft een geheel getal volgens http://www.w3.org/2001/XMLSchema#integer."""
    naam = 'Integer'
    objectUri = 'http://www.w3.org/2001/XMLSchema#integer'
    definition = 'Beschrijft een geheel getal volgens http://www.w3.org/2001/XMLSchema#integer.'
    label = 'Geheel getal'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#integer'

    @classmethod
    def convert_to_correct_type(cls, value):
        if value is None:
            return None
        if isinstance(value, bool) or isinstance(value, int):
            return value
        try:
            return int(value)
        except Exception:
            raise CouldNotConvertToCorrectType(f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, int):
            raise TypeError(f'expecting an integer in {attribuut.naam}')
        return True

    def __str__(self):
        return OTLField.__str__(self)

