# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject
from OTLMOW.OTLModel.Datatypes.KlTypeBalk import KlTypeBalk


# Generated with OTLClassCreator. To modify: extend, do not edit
class Balk(ConstructiefObject):
    """Ruimteoverspannend enkelvoudig constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. De breedte is weer gelijk of kleiner dan de hoogte."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._typeBalk = OTLAttribuut(field=KlTypeBalk,
                                      naam='typeBalk',
                                      label='type balk',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk.typeBalk',
                                      definition='De soort van balk.',
                                      owner=self)

    @property
    def typeBalk(self):
        """De soort van balk."""
        return self._typeBalk.get_waarde()

    @typeBalk.setter
    def typeBalk(self, value):
        self._typeBalk.set_waarde(value, owner=self)
