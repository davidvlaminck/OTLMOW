# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Detectielus import Detectielus
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class SelNietSelLus(Detectielus):
    """Abstracte klasse die de eigenschappen van selectieve en niet-selectieve lussen combineert."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._heeftMofInTrekput = OTLAttribuut(field=BooleanField,
                                               naam='heeftMofInTrekput',
                                               label='heeft mof in trekput',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus.heeftMofInTrekput',
                                               definition='Aanduiding of de mof bereikbaar is via een trekput.')

        self._isPrioritair = OTLAttribuut(field=BooleanField,
                                          naam='isPrioritair',
                                          label='is prioritair',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus.isPrioritair',
                                          definition='Geeft aan of de lus prioritair hersteld moet worden bij defect.')

    @property
    def heeftMofInTrekput(self):
        """Aanduiding of de mof bereikbaar is via een trekput."""
        return self._heeftMofInTrekput.waarde

    @heeftMofInTrekput.setter
    def heeftMofInTrekput(self, value):
        self._heeftMofInTrekput.set_waarde(value, owner=self)

    @property
    def isPrioritair(self):
        """Geeft aan of de lus prioritair hersteld moet worden bij defect."""
        return self._isPrioritair.waarde

    @isPrioritair.setter
    def isPrioritair(self, value):
        self._isPrioritair.set_waarde(value, owner=self)
