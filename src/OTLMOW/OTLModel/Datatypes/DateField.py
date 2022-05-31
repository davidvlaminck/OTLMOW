from datetime import date, datetime, timedelta
from random import randrange

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class DateField(OTLField):
    """Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#date."""
    naam = 'Date'
    objectUri = 'http://www.w3.org/2001/XMLSchema#date'
    definition = 'Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#date.'
    label = 'Datum'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#date'

    @classmethod
    def convert_to_correct_type(cls, value):
        if value is None:
            return None
        if isinstance(value, date):
            return value
        if isinstance(value, datetime):
            return date(value.year, value.month, value.day)
        if isinstance(value, str):
            try:
                dt = datetime.strptime(value, "%Y-%m-%d")
                return date(dt.year, dt.month, dt.day)
            except ValueError:
                try:
                    dt = datetime.strptime(value, "%d/%m/%Y")
                    return date(dt.year, dt.month, dt.day)
                except ValueError:
                    raise CouldNotConvertToCorrectType(
                        f'{value} could not be converted to correct type (implied by {cls.__name__})')
        raise CouldNotConvertToCorrectType(f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, date):
            raise TypeError(f'expecting date in {attribuut.naam}')
        return True

    @staticmethod
    def value_default(value):
        return value.strftime("%Y-%m-%d")

    def __str__(self):
        return OTLField.__str__(self)

    @classmethod
    def random_date(cls, start, end):
        delta = end - start
        int_delta = delta.days
        random_days = randrange(int_delta)
        return start + timedelta(days=random_days)

    @staticmethod
    def create_dummy_data():
        return DateField.random_date(start=date(2000, 1, 1), end=date(2020, 1, 1))
