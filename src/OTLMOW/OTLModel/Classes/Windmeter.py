# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Classes.Sensoropstelling import Sensoropstelling
from OTLMOW.OTLModel.Datatypes.KlWindmeterMerk import KlWindmeterMerk
from OTLMOW.OTLModel.Datatypes.KlWindmeterModelnaam import KlWindmeterModelnaam
from OTLMOW.OTLModel.Datatypes.KlWindmeterType import KlWindmeterType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Windmeter(AIMNaamObject, Sensoropstelling):
    """Een meettoestel dat windsnelheid en/of windrichting meet. Het meetresultaat wordt omgezet in een uitleesbaar signaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Windmeter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Sensoropstelling.__init__(self)

        self._merk = OTLAttribuut(field=KlWindmeterMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Windmeter.merk',
                                  definition='Het merk van de windmeter.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlWindmeterModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Windmeter.modelnaam',
                                       definition='De mùodelnaam van de windmeter.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlWindmeterType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Windmeter.type',
                                  definition='Het type van windmeter.',
                                  owner=self)

    @property
    def merk(self):
        """Het merk van de windmeter."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De mùodelnaam van de windmeter."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van windmeter."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
