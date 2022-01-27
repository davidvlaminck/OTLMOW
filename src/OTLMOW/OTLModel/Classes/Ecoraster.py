# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.ComplexeGeleiding import ComplexeGeleiding
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.KlEcoPaalmateriaal import KlEcoPaalmateriaal
from src.OTLMOW.OTLModel.Datatypes.KlRasterMazen import KlRasterMazen
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecoraster(ComplexeGeleiding):
    """Een geleiding om dieren te leiden naar een plaats (ecoduct, ecotunnel, ...) waar ze veilig een drukke weg kunnen oversteken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._heeftPrikkeldraad = OTLAttribuut(field=BooleanField,
                                               naam='heeftPrikkeldraad',
                                               label='heeft prikkeldraad',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.heeftPrikkeldraad',
                                               definition='Aanduiding of het ecoraster is voorzien van prikkeldraad.')

        self._heeftSpandraden = OTLAttribuut(field=BooleanField,
                                             naam='heeftSpandraden',
                                             label='heeft spandraden',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.heeftSpandraden',
                                             definition='Aanduiding of het ecoraster is voorzien van spandraden.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.lengte',
                                    definition='De lengte van het ecoraster in meter.')

        self._paalMateriaal = OTLAttribuut(field=KlEcoPaalmateriaal,
                                           naam='paalMateriaal',
                                           label='paal materiaal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.paalMateriaal',
                                           definition='Het materiaal van de paal in het ecoraster.')

        self._paalhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='paalhoogte',
                                        label='paalhoogte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.paalhoogte',
                                        definition='De hoogte van de paal in het ecoraster in meter.')

        self._typeMazen = OTLAttribuut(field=KlRasterMazen,
                                       naam='typeMazen',
                                       label='type mazen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.typeMazen',
                                       definition='Het type van de mazen in het ecoraster.')

    @property
    def heeftPrikkeldraad(self):
        """Aanduiding of het ecoraster is voorzien van prikkeldraad."""
        return self._heeftPrikkeldraad.waarde

    @heeftPrikkeldraad.setter
    def heeftPrikkeldraad(self, value):
        self._heeftPrikkeldraad.set_waarde(value, owner=self)

    @property
    def heeftSpandraden(self):
        """Aanduiding of het ecoraster is voorzien van spandraden."""
        return self._heeftSpandraden.waarde

    @heeftSpandraden.setter
    def heeftSpandraden(self, value):
        self._heeftSpandraden.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van het ecoraster in meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def paalMateriaal(self):
        """Het materiaal van de paal in het ecoraster."""
        return self._paalMateriaal.waarde

    @paalMateriaal.setter
    def paalMateriaal(self, value):
        self._paalMateriaal.set_waarde(value, owner=self)

    @property
    def paalhoogte(self):
        """De hoogte van de paal in het ecoraster in meter."""
        return self._paalhoogte.waarde

    @paalhoogte.setter
    def paalhoogte(self, value):
        self._paalhoogte.set_waarde(value, owner=self)

    @property
    def typeMazen(self):
        """Het type van de mazen in het ecoraster."""
        return self._typeMazen.waarde

    @typeMazen.setter
    def typeMazen(self, value):
        self._typeMazen.set_waarde(value, owner=self)
