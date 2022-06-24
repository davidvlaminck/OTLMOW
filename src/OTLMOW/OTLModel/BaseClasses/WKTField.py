from OTLMOW.Facility.Exceptions.WrongGeometryError import WrongGeometryError
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.BaseClasses.WKTValidator import WKTValidator


class WKTField(OTLField):
    """Een tekstwaarde in WKT string vorm."""
    naam = 'WKT'
    objectUri = ''
    definition = ''
    label = 'WKT'
    usagenote = ''

    @classmethod
    def convert_to_correct_type(cls, value, log_warnings=True) -> object:
        value = value.replace(' Z(', ' Z (').replace('T(', 'T (').replace('G(', 'G (').replace('N(', 'N (')
        return value

    @staticmethod
    def validate(value, attribuut):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError(f'expecting string in {attribuut.naam}')
            if not WKTValidator.validate_wkt(value):
                raise ValueError(f'{value} is not a valid WKT string for {attribuut.naam}')
            geo_type = value.split(' (')[0]
            if geo_type not in attribuut.owner._geometry_types:
                expected_types = ' and '.join(attribuut.owner._geometry_types)
                verkorte_uri = attribuut.owner.typeURI.split('#')[1]
                error_msg = f"Asset type {verkorte_uri} can't be assigned a {geo_type} as geometry, valid types are {expected_types}"
                raise WrongGeometryError(error_msg)
        return True

    def __str__(self):
        return OTLField.__str__(self)


