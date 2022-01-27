# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.ConstructieElement import ConstructieElement
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.KlDamwandMateriaal import KlDamwandMateriaal
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Damwand(ConstructieElement):
    """Een grond- en/of waterkerende constructie, die bestaat uit een verticaal in de grond geplaatste wand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._isWaterdicht = OTLAttribuut(field=BooleanField,
                                          naam='isWaterdicht',
                                          label='is waterdicht',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.isWaterdicht',
                                          definition='Geeft aan of de damwand al dan niet waterdicht is.')

        self._materiaal = OTLAttribuut(field=KlDamwandMateriaal,
                                       naam='materiaal',
                                       label='Damwand materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.materiaal',
                                       definition='Het materiaal waaruit de damwand bestaat.')

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.oppervlakte',
                                         definition='De totale oppervlakte van de damwandconstructie in vierkante meter.')

        self._profiellengte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='profiellengte',
                                           label='profiellengte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.profiellengte',
                                           definition='De lengte van één damwandprofiel.')

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.totaleLengte',
                                          definition='De totale lengte van de damwandconstructie in lopende meter.')

    @property
    def isWaterdicht(self):
        """Geeft aan of de damwand al dan niet waterdicht is."""
        return self._isWaterdicht.waarde

    @isWaterdicht.setter
    def isWaterdicht(self, value):
        self._isWaterdicht.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit de damwand bestaat."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De totale oppervlakte van de damwandconstructie in vierkante meter."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def profiellengte(self):
        """De lengte van één damwandprofiel."""
        return self._profiellengte.waarde

    @profiellengte.setter
    def profiellengte(self, value):
        self._profiellengte.set_waarde(value, owner=self)

    @property
    def totaleLengte(self):
        """De totale lengte van de damwandconstructie in lopende meter."""
        return self._totaleLengte.waarde

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)
