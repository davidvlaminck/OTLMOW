# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Persleiding import Persleiding
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KwantWrdInBar import KwantWrdInBar


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brandleiding(Persleiding):
    """Segment uit de leiding die water aanvoert voor het blussen van een brand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._isGeisoleerd = OTLAttribuut(field=BooleanField,
                                          naam='isGeisoleerd',
                                          label='is geïsoleerd',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding.isGeisoleerd',
                                          definition='Geeft aan of de brandleiding voorzien is van eigen isolatie.')

        self._leidingdruk = OTLAttribuut(field=KwantWrdInBar,
                                         naam='leidingdruk',
                                         label='leidingdruk',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding.leidingdruk',
                                         definition='De vastgelegde druk die moet voorzien worden op de leiding in functie van de aanvoer van bluswater.')

    @property
    def isGeisoleerd(self):
        """Geeft aan of de brandleiding voorzien is van eigen isolatie."""
        return self._isGeisoleerd.waarde

    @isGeisoleerd.setter
    def isGeisoleerd(self, value):
        self._isGeisoleerd.set_waarde(value, owner=self)

    @property
    def leidingdruk(self):
        """De vastgelegde druk die moet voorzien worden op de leiding in functie van de aanvoer van bluswater."""
        return self._leidingdruk.waarde

    @leidingdruk.setter
    def leidingdruk(self, value):
        self._leidingdruk.set_waarde(value, owner=self)
