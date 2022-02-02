from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.BaseClasses.WKTValidator import WKTValidator


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
            if not WKTValidator.validate_wkt(value):
                raise ValueError(f'{value} is not a valid WKT string for {attribuut.naam}')
            if not value.startswith(attribuut.constraints):
                raise TypeError(f'expecting {attribuut.constraints} in {attribuut.naam}')
        return True

    def __str__(self):
        return OTLField.__str__(self)


