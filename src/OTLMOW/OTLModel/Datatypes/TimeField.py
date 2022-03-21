from datetime import time, datetime

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class TimeField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'Time'
    objectUri = 'http://www.w3.org/2001/XMLSchema#time'
    definition = 'Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#time.'
    label = 'Tijd'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#time'

    @classmethod
    def convert_to_correct_type(cls, value):
        if value is None:
            return None
        if isinstance(value, time):
            return value
        if isinstance(value, datetime):
            return time(value.hour, value.minute, value.second)
        if isinstance(value, str):
            try:
                dt = datetime.strptime(value, "%H:%M:%S")
                return time(dt.hour, dt.minute, dt.second)
            except Exception:
                raise CouldNotConvertToCorrectType(f'{value} could not be converted to correct type (implied by {cls.__name__})')
        raise CouldNotConvertToCorrectType(f'{value} could not be converted to correct type (implied by {cls.__name__})')


    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, time):
            raise TypeError(f'expecting datetime in {attribuut.naam}')
        return True

    @staticmethod
    def value_default(value):
        if value is None:
            return None
        return value.strftime("%H:%M:%S")

    def __str__(self):
        return OTLField.__str__(self)

