# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Datatypes.KlStopcontactAantalPolen import KlStopcontactAantalPolen
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stopcontact(AIMObject):
    """Een aansluitpunt op het elektrisch net voor afname van elektrische energie met behulp van een stekker."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalPolen = OTLAttribuut(field=KlStopcontactAantalPolen,
                                         naam='aantalPolen',
                                         label='aantal polen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.aantalPolen',
                                         definition='Typering van het stopcontact volgens het aantal polen op basis van een keuzelijst.')

        self._spanning = OTLAttribuut(field=KwantWrdInVolt,
                                      naam='spanning',
                                      label='spanning',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.spanning',
                                      definition='De voorziene spanning voor het stopcontact.')

        self._stroomsterkte = OTLAttribuut(field=KwantWrdInAmpere,
                                           naam='stroomsterkte',
                                           label='stroomsterkte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.stroomsterkte',
                                           definition='Maximale stroomsterkte van het stopcontact uitgedrukt in ampère.')

    @property
    def aantalPolen(self):
        """Typering van het stopcontact volgens het aantal polen op basis van een keuzelijst."""
        return self._aantalPolen.waarde

    @aantalPolen.setter
    def aantalPolen(self, value):
        self._aantalPolen.set_waarde(value, owner=self)

    @property
    def spanning(self):
        """De voorziene spanning voor het stopcontact."""
        return self._spanning.waarde

    @spanning.setter
    def spanning(self, value):
        self._spanning.set_waarde(value, owner=self)

    @property
    def stroomsterkte(self):
        """Maximale stroomsterkte van het stopcontact uitgedrukt in ampère."""
        return self._stroomsterkte.waarde

    @stroomsterkte.setter
    def stroomsterkte(self, value):
        self._stroomsterkte.set_waarde(value, owner=self)
