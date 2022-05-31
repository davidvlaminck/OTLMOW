from datetime import datetime, timedelta
from random import randrange

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class DateTimeField(OTLField):
    """Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#dateTime."""
    naam = 'DateTime'
    objectUri = 'http://www.w3.org/2001/XMLSchema#dateTime'
    definition = 'Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#dateTime.'
    label = 'Datumtijd'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#dateTime'

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, datetime):
            raise TypeError(f'expecting datetime in {attribuut.naam}')
        return True

    @classmethod
    def convert_to_correct_type(cls, value):
        if value is None:
            return None
        if isinstance(value, datetime):
            return value
        if isinstance(value, str):
            try:
                if 'T' in value:
                    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
                else:
                    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            except Exception:
                raise CouldNotConvertToCorrectType(f'{value} could not be converted to correct type (implied by {cls.__name__})')
        try:
            return datetime(value)
        except Exception:
            raise CouldNotConvertToCorrectType(f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @staticmethod
    def value_default(value):
        return value.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return OTLField.__str__(self)

    @staticmethod
    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    @staticmethod
    def create_dummy_data():
        return DateTimeField.random_date(start=datetime(2000, 1, 1, 0, 0, 0), end=datetime(2020, 1, 1, 0, 0, 0))
