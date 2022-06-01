# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Classes.Sensoropstelling import Sensoropstelling
from OTLMOW.OTLModel.Datatypes.KlOptischeWegdeksensorMerk import KlOptischeWegdeksensorMerk
from OTLMOW.OTLModel.Datatypes.KlOptischeWegdeksensorModelnaam import KlOptischeWegdeksensorModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class OptischeWegdeksensor(AIMNaamObject, Sensoropstelling):
    """Een meettoestel dat gebruik maakt van optische eigenschappen om de wegdekcondities zoals nat, ijs, sneeuw en vorst te meten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OptischeWegdeksensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Sensoropstelling.__init__(self)

        self._merk = OTLAttribuut(field=KlOptischeWegdeksensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OptischeWegdeksensor.merk',
                                  definition='Het merk van de optische wegdeksensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlOptischeWegdeksensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OptischeWegdeksensor.modelnaam',
                                       definition='De modelnaam van de optische wegdeksensor.',
                                       owner=self)

    @property
    def merk(self):
        """Het merk van de optische wegdeksensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de optische wegdeksensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
