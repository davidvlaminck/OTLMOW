# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteIPv4AdresWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteIPv4Adres.waarde',
                                    usagenote='Het formaat is een decimale notatie bv. 91.198.174.232',
                                    definition='De string die het IPv4 adres representeert.')

    @property
    def waarde(self):
        """De string die het IPv4 adres representeert."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteIPv4Adres(OTLField, AttributeInfo):
    """Beschrijft een ip-adres volgens de ipv4 specificatie."""
    naam = 'DteIPv4Adres'
    label = 'IPv4-adres'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteIPv4Adres'
    definition = 'Beschrijft een ip-adres volgens de ipv4 specificatie.'
    waardeObject = DteIPv4AdresWaarden

    def __str__(self):
        return OTLField.__str__(self)

