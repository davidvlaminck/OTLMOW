# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Straatmeubilair import Straatmeubilair
from OTLMOW.OTLModel.Datatypes.KlOmegaElementMateriaal import KlOmegaElementMateriaal
from OTLMOW.OTLModel.Datatypes.KlPlaatsingswijze import KlPlaatsingswijze
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class OmegaElement(Straatmeubilair, LijnGeometrie):
    """Een voetgangersafsluiting met als doel om de voetgangers te geleiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Straatmeubilair.__init__(self)
        LijnGeometrie.__init__(self)

        self._materiaal = OTLAttribuut(field=KlOmegaElementMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement.materiaal',
                                       definition='De materie waaruit het omega-element bestaat.',
                                       owner=self)

        self._plaatsingswijze = OTLAttribuut(field=KlPlaatsingswijze,
                                             naam='plaatsingswijze',
                                             label='plaatsingswijze',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement.plaatsingswijze',
                                             definition='Aanduiding of het omega-element eenvoudig wegneembaar is.',
                                             owner=self)

    @property
    def materiaal(self):
        """De materie waaruit het omega-element bestaat."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def plaatsingswijze(self):
        """Aanduiding of het omega-element eenvoudig wegneembaar is."""
        return self._plaatsingswijze.get_waarde()

    @plaatsingswijze.setter
    def plaatsingswijze(self, value):
        self._plaatsingswijze.set_waarde(value, owner=self)
