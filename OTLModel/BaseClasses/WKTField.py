from shapely import wkt
from shapely.errors import WKTReadingError
from OTLModel.BaseClasses.OTLField import OTLField


class WKTField(OTLField):
    """Een tekstwaarde in WKT string vorm."""
    naam = 'WKT'
    objectUri = ''
    definition = ''
    label = 'WKT'
    usagenote = ''

    @staticmethod
    def validate(value, attribuut):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError(f'expecting string in {attribuut.naam}')
            try:
                wkt.loads(value)
            except WKTReadingError as error:
                raise ValueError(f'{value} is not a valid WKT string for {attribuut.naam}: {str(error)}')
        return True

    def __str__(self):
        return OTLField.__str__(self)


