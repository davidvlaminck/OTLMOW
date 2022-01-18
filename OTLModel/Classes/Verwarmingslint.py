# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verwarmingslint(AIMObject, AttributeInfo):
    """Verwarmbare omwikkeling voor onderdelen die moeten beschermd worden tegen bevriezing."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingslint'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingslint.vermogen',
                                      definition='Het vereiste vermogen in watt voor de correcte werking van het verwarmingslint.')

    @property
    def vermogen(self):
        """Het vereiste vermogen in watt voor de correcte werking van het verwarmingslint."""
        return self._vermogen.waarde

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
