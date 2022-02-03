# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AndereVerharding import AndereVerharding
from OTLMOW.OTLModel.Datatypes.KlSteenslagType import KlSteenslagType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Steenslagverharding(AndereVerharding):
    """Een verharding van gebroken steen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Steenslagverharding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlSteenslagType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Steenslagverharding.type',
                                  definition='Bepaling van het type steenslagverharding.',
                                  owner=self)

    @property
    def type(self):
        """Bepaling van het type steenslagverharding."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
