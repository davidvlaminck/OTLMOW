# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlStopcontactAantalPolen import KlStopcontactAantalPolen
from OTLMOW.OTLModel.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere
from OTLMOW.OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stopcontact(AIMObject, PuntGeometrie):
    """Een aansluitpunt op het elektrisch net voor afname van elektrische energie met behulp van een stekker."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._aantalPolen = OTLAttribuut(field=KlStopcontactAantalPolen,
                                         naam='aantalPolen',
                                         label='aantal polen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.aantalPolen',
                                         definition='Typering van het stopcontact volgens het aantal polen op basis van een keuzelijst.',
                                         owner=self)

        self._spanning = OTLAttribuut(field=KwantWrdInVolt,
                                      naam='spanning',
                                      label='spanning',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.spanning',
                                      definition='De voorziene spanning voor het stopcontact.',
                                      owner=self)

        self._stroomsterkte = OTLAttribuut(field=KwantWrdInAmpere,
                                           naam='stroomsterkte',
                                           label='stroomsterkte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.stroomsterkte',
                                           definition='Maximale stroomsterkte van het stopcontact uitgedrukt in ampère.',
                                           owner=self)

    @property
    def aantalPolen(self):
        """Typering van het stopcontact volgens het aantal polen op basis van een keuzelijst."""
        return self._aantalPolen.get_waarde()

    @aantalPolen.setter
    def aantalPolen(self, value):
        self._aantalPolen.set_waarde(value, owner=self)

    @property
    def spanning(self):
        """De voorziene spanning voor het stopcontact."""
        return self._spanning.get_waarde()

    @spanning.setter
    def spanning(self, value):
        self._spanning.set_waarde(value, owner=self)

    @property
    def stroomsterkte(self):
        """Maximale stroomsterkte van het stopcontact uitgedrukt in ampère."""
        return self._stroomsterkte.get_waarde()

    @stroomsterkte.setter
    def stroomsterkte(self, value):
        self._stroomsterkte.set_waarde(value, owner=self)
