from datetime import time
from src.OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class TimeField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'Time'
    objectUri = 'http://www.w3.org/2001/XMLSchema#time'
    definition = 'Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#time.'
    label = 'Tijd'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#time'

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

