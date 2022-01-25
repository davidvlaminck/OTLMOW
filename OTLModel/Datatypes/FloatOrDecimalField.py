import decimal

from OTLModel.BaseClasses.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLModel.BaseClasses.OTLField import OTLField


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
        if isinstance(value, bool):
            return value
        if isinstance(value, int) or isinstance(value, decimal.Decimal):
            return float(value)
        try:
            return float(value)
        except Exception:
            raise CouldNotConvertToCorrectType(f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @staticmethod
    def validate(value, attribuut):
        if value is not None:
            val = attribuut.field.convert_to_correct_type(value)
            if val is not None and not isinstance(val, float):
                raise TypeError(f'expecting a number (int, float or Decimal) in {attribuut.naam}')
        return True

    def __str__(self):
        return OTLField.__str__(self)
