from datetime import datetime
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

    @staticmethod
    def value_default(value):
        return value.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return OTLField.__str__(self)
