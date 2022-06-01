# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Classes.Sensoropstelling import Sensoropstelling
from OTLMOW.OTLModel.Datatypes.KlThermoHygrometerMerk import KlThermoHygrometerMerk
from OTLMOW.OTLModel.Datatypes.KlThermoHygrometerModelnaam import KlThermoHygrometerModelnaam
from OTLMOW.OTLModel.Datatypes.KlTypeStralingsscherm import KlTypeStralingsscherm


# Generated with OTLClassCreator. To modify: extend, do not edit
class ThermoHygrometer(AIMNaamObject, Sensoropstelling):
    """Een meettoestel dat de temperatuur en vochtigheid van een omgeving of medium meet. Het meetresultaat wordt omgezet in een uitleesbaar signaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ThermoHygrometer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Sensoropstelling.__init__(self)

        self._merk = OTLAttribuut(field=KlThermoHygrometerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ThermoHygrometer.merk',
                                  definition='Het merk van de thermo- hygrometer.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlThermoHygrometerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ThermoHygrometer.modelnaam',
                                       definition='De modelnaam van de thermo- hygrometer.',
                                       owner=self)

        self._stralingsschermType = OTLAttribuut(field=KlTypeStralingsscherm,
                                                 naam='stralingsschermType',
                                                 label='stralingsscherm type',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ThermoHygrometer.stralingsschermType',
                                                 definition='Het type van stralingsscherm.',
                                                 owner=self)

    @property
    def merk(self):
        """Het merk van de thermo- hygrometer."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de thermo- hygrometer."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def stralingsschermType(self):
        """Het type van stralingsscherm."""
        return self._stralingsschermType.get_waarde()

    @stralingsschermType.setter
    def stralingsschermType(self, value):
        self._stralingsschermType.set_waarde(value, owner=self)
