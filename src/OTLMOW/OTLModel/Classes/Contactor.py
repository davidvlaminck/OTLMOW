# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlContactorType import KlContactorType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Contactor(AIMObject):
    """Toestel dat ter plaatse of op afstand aangestuurd wordt om (grote) vermogensstromen af te schakelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlContactorType,
                                  naam='type',
                                  label='type contactor',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor.type',
                                  definition='Geeft aan of het een K of Q contactor betreft.')

    @property
    def type(self):
        """Geeft aan of het een K of Q contactor betreft."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
