# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLModel.Datatypes.DtcConstructiestaalspecificaties import DtcConstructiestaalspecificaties
from OTLModel.Datatypes.KwantWrdInKilogram import KwantWrdInKilogram


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenConstructieElement(ABC):
    """Bundeling van gemeenschappelijke eigenschappen van stalen constructie-elementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenConstructieElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._staalspecificaties = OTLAttribuut(field=DtcConstructiestaalspecificaties,
                                                naam='staalspecificaties',
                                                label='staalspecificaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenConstructieElement.staalspecificaties',
                                                definition='Eigenschappen van het gebruikte constructiestaal.')

        self._totaalGewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                           naam='totaalGewicht',
                                           label='totaal gewicht',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenConstructieElement.totaalGewicht',
                                           definition='Een kwantitatieve waarde in kilogram van het totale stalen element.')

    @property
    def staalspecificaties(self):
        """Eigenschappen van het gebruikte constructiestaal."""
        return self._staalspecificaties.waarde

    @staalspecificaties.setter
    def staalspecificaties(self, value):
        self._staalspecificaties.set_waarde(value, owner=self)

    @property
    def totaalGewicht(self):
        """Een kwantitatieve waarde in kilogram van het totale stalen element."""
        return self._totaalGewicht.waarde

    @totaalGewicht.setter
    def totaalGewicht(self, value):
        self._totaalGewicht.set_waarde(value, owner=self)
