from datetime import datetime
from OTLModel.BaseClasses.OTLField import OTLField


class DateField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'Time'
    objectUri = 'http://www.w3.org/2001/XMLSchema#time'
    definition = 'Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#time.'
    label = 'Tijd'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#time'

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, datetime):
            raise TypeError(f'expecting datetime in {attribuut.naam}')
        # TODO date vars should be 0 0 0
        return True

    @staticmethod
    def value_default(value):
        return value.strftime("%H:%M:%S")

    def __str__(self):
        return OTLField.__str__(self)

