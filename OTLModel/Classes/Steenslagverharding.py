# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AndereVerharding import AndereVerharding
from OTLModel.Datatypes.KlSteenslagType import KlSteenslagType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Steenslagverharding(AndereVerharding, AttributeInfo):
    """Een verharding van gebroken steen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Steenslagverharding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereVerharding.__init__(self)
        AttributeInfo.__init__(self)

        self._type = OTLAttribuut(field=KlSteenslagType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Steenslagverharding.type',
                                  definition='Bepaling van het type steenslagverharding.')

    @property
    def type(self):
        """Bepaling van het type steenslagverharding."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
