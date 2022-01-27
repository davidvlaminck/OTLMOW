# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlFolieType import KlFolieType


# Generated with OTLClassCreator. To modify: extend, do not edit
class RetroreflecterendeFolie(AIMObject):
    """Retroreflecterend bekledingsmateriaal, bijvoorbeeld van een divergentiepuntbebakeningselement, retroreflecterende koker, of het beeldvlak van een retroreflecterend verkeersbord."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._folietype = OTLAttribuut(field=KlFolieType,
                                       naam='folietype',
                                       label='folietype',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie.folietype',
                                       definition='Het type folie dat bevestigd is aan het retroreflecterend verkeersbord.')

    @property
    def folietype(self):
        """Het type folie dat bevestigd is aan het retroreflecterend verkeersbord."""
        return self._folietype.waarde

    @folietype.setter
    def folietype(self, value):
        self._folietype.set_waarde(value, owner=self)
