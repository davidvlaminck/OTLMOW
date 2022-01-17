import decimal

from UnitTests.OTLFieldTests.OTLField import OTLField


class FloatOrDecimalField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'String'
    objectUri = 'http://www.w3.org/2001/XMLSchema#string'
    definition = 'Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string.'
    label = 'String'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#string'

    @staticmethod
    def convert_to_correct_type(value):
        if isinstance(value, bool):
            return value
        if isinstance(value, int) or isinstance(value, decimal.Decimal):
            return float(value)
        return value

    @staticmethod
    def validate(value, attribuut):
        if value is not None:
            val = attribuut.field.convert_to_correct_type(value)
            if val is not None and not isinstance(val, float):
                raise TypeError(f'expecting a number (int, float or Decimal) in {attribuut.naam}')
            return True
        return False

    def __str__(self):
        return OTLField.__str__(self)

