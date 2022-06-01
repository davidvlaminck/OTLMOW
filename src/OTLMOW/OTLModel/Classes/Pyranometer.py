# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Classes.Sensoropstelling import Sensoropstelling
from OTLMOW.OTLModel.Datatypes.KlPyranometerMerk import KlPyranometerMerk
from OTLMOW.OTLModel.Datatypes.KlPyranometerModelnaam import KlPyranometerModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pyranometer(AIMNaamObject, Sensoropstelling):
    """Een meettoestel dat wordt gebruikt om de intensiteit van zonnestraling te meten. Het meetresultaat wordt omgezet in een uitleesbaar signaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pyranometer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Sensoropstelling.__init__(self)

        self._merk = OTLAttribuut(field=KlPyranometerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pyranometer.merk',
                                  definition='Het merk van de pyranometer.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlPyranometerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pyranometer.modelnaam',
                                       definition='De modelnaam van de pyranometer.',
                                       owner=self)

    @property
    def merk(self):
        """Het merk van de pyranometer."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de pyranometer."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
