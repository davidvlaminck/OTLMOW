from OTLModel.BaseClasses.OTLField import OTLField


class StringField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'String'
    objectUri = 'http://www.w3.org/2001/XMLSchema#string'
    definition = 'Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string.'
    label = 'String'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#string'

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, str):
            raise TypeError(f'expecting string in {attribuut.naam}')
        return True

    def __str__(self):
        return OTLField.__str__(self)

