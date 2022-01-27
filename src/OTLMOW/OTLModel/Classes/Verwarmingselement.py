# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlVerwarmingselementMerk import KlVerwarmingselementMerk
from OTLMOW.OTLModel.Datatypes.KlVerwarmingselementModelnaam import KlVerwarmingselementModelnaam
from OTLMOW.OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verwarmingselement(AIMObject):
    """Toestel dat het verwarmingslint van warmte voorziet afhankelijk van de omgevingstemperatuur."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingselement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlVerwarmingselementMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingselement.merk',
                                  definition='Merk van het element volgens de fabrikant.')

        self._modelnaam = OTLAttribuut(field=KlVerwarmingselementModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingselement.modelnaam',
                                       definition='Modelnaam van het element volgens de fabrikant.')

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingselement.vermogen',
                                      definition='Elektrisch vermogen nodig voor de correcte werking van het element.')

    @property
    def merk(self):
        """Merk van het element volgens de fabrikant."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van het element volgens de fabrikant."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def vermogen(self):
        """Elektrisch vermogen nodig voor de correcte werking van het element."""
        return self._vermogen.waarde

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
