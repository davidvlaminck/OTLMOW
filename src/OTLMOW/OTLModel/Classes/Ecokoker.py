# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlEcoEcokokerType import KlEcoEcokokerType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecokoker(AIMObject):
    """Een kleine ecotunnel of ecokoker is een doorgang voor dieren onder een weg of spoorweg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecokoker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlEcoEcokokerType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecokoker.type',
                                  definition='Het type van ecokoker zoals bv. amfibieënkoker, ….')

    @property
    def type(self):
        """Het type van ecokoker zoals bv. amfibieënkoker, …."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
