# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Bebakening import Bebakening
from OTLMOW.OTLModel.Datatypes.KlWildreflectorDrager import KlWildreflectorDrager
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wildreflector(Bebakening, PuntGeometrie):
    """Een wildreflector is een reflecterend afschrikkingssysteem voor groot en klein wild nabij een weg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wildreflector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Bebakening.__init__(self)
        PuntGeometrie.__init__(self)

        self._drager = OTLAttribuut(field=KlWildreflectorDrager,
                                    naam='drager',
                                    label='drager',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wildreflector.drager',
                                    definition='De constructie waar de wildreflector is aan bevestigd.',
                                    owner=self)

    @property
    def drager(self):
        """De constructie waar de wildreflector is aan bevestigd."""
        return self._drager.waarde

    @drager.setter
    def drager(self, value):
        self._drager.set_waarde(value, owner=self)
