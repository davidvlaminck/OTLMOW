from datetime import datetime
from OTLModel.BaseClasses.OTLField import OTLField


class DateField(OTLField):
    """Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#date."""
    naam = 'Date'
    objectUri = 'http://www.w3.org/2001/XMLSchema#date'
    definition = 'Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#date.'
    label = 'Datum'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#date'

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, datetime):
            raise TypeError(f'expecting datetime in {attribuut.naam}')
        # TODO time vars should be 0 0 0
        return True

    @staticmethod
    def value_default(value):
        return value.strftime("%Y-%m-%d")

    def __str__(self):
        return OTLField.__str__(self)

