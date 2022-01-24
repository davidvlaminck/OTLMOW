# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Straatmeubilair import Straatmeubilair
from OTLModel.Datatypes.KlOmegaElementMateriaal import KlOmegaElementMateriaal
from OTLModel.Datatypes.KlPlaatsingswijze import KlPlaatsingswijze


# Generated with OTLClassCreator. To modify: extend, do not edit
class OmegaElement(Straatmeubilair):
    """Een voetgangersafsluiting met als doel om de voetgangers te geleiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._materiaal = OTLAttribuut(field=KlOmegaElementMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement.materiaal',
                                       definition='De materie waaruit het omega-element bestaat.')

        self._plaatsingswijze = OTLAttribuut(field=KlPlaatsingswijze,
                                             naam='plaatsingswijze',
                                             label='plaatsingswijze',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement.plaatsingswijze',
                                             definition='Aanduiding of het omega-element eenvoudig wegneembaar is.')

    @property
    def materiaal(self):
        """De materie waaruit het omega-element bestaat."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def plaatsingswijze(self):
        """Aanduiding of het omega-element eenvoudig wegneembaar is."""
        return self._plaatsingswijze.waarde

    @plaatsingswijze.setter
    def plaatsingswijze(self, value):
        self._plaatsingswijze.set_waarde(value, owner=self)
