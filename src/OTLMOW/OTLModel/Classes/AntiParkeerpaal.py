# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Straatmeubilair import Straatmeubilair
from src.OTLMOW.OTLModel.Datatypes.AntiParkeerpaalType import AntiParkeerpaalType
from src.OTLMOW.OTLModel.Datatypes.KlAntiparkeerpaalMateriaal import KlAntiparkeerpaalMateriaal
from src.OTLMOW.OTLModel.Datatypes.KlPlaatsingswijze import KlPlaatsingswijze


# Generated with OTLClassCreator. To modify: extend, do not edit
class AntiParkeerpaal(Straatmeubilair):
    """Een paal met als doel het parkeren te verhinderen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._materiaal = OTLAttribuut(field=KlAntiparkeerpaalMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaal.materiaal',
                                       definition='Het materiaal van de Amsterdammer.')

        self._plaatsingswijze = OTLAttribuut(field=KlPlaatsingswijze,
                                             naam='plaatsingswijze',
                                             label='plaatsingswijze',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaal.plaatsingswijze',
                                             definition='Aanduiding of de anti-parkeerpaal eenvoudig wegneembaar is.')

        self._type = OTLAttribuut(field=AntiParkeerpaalType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaal.type',
                                  definition='Vorm van de anti-parkeerpaal.')

    @property
    def materiaal(self):
        """Het materiaal van de Amsterdammer."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def plaatsingswijze(self):
        """Aanduiding of de anti-parkeerpaal eenvoudig wegneembaar is."""
        return self._plaatsingswijze.waarde

    @plaatsingswijze.setter
    def plaatsingswijze(self, value):
        self._plaatsingswijze.set_waarde(value, owner=self)

    @property
    def type(self):
        """Vorm van de anti-parkeerpaal."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
