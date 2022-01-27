from src.OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class URIField(OTLField):
    """Een tekstwaarde die een verwijzing naar meer informatie van het element bevat volgens http://www.w3.org/2001/XMLSchema#anyURI ."""
    naam = 'AnyURI'
    objectUri = 'http://www.w3.org/2001/XMLSchema#anyURI'
    definition = 'Een tekstwaarde die een verwijzing naar meer informatie van het element bevat volgens http://www.w3.org/2001/XMLSchema#anyURI.'
    label = 'URI'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#anyURI'

    @staticmethod
    def validate(value, attribuut):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError(f'expecting string in {attribuut.naam}')
            # TODO add URI validation
        return True

    def __str__(self):
        return OTLField.__str__(self)

