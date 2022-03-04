# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class Flitspaalbehuizing(AIMObject, PuntGeometrie):
    """Een weersbestendige en vandalismebestendige behuizing waarin een snelheids- en/of roodlichtcamera kan worden bevestigd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitspaalbehuizing'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=StringField,  # TODO KlFlitspaalbehuizingMerk
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitspaalbehuizing.merk',
                                  definition='Het merk van de flitspaalbehuizing.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=StringField,  # TODO KlFlitspaalbehuizingModelnaam
                                  naam='modelnaam',
                                  label='modelnaam',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitspaalbehuizing.modelnaam',
                                  definition='Het model of productrange van de flitspaalbehuizing.',
                                  owner=self)

    @property
    def merk(self):
        """Het merk van de flitspaalbehuizing."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Het model of productrange van de flitspaalbehuizing."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
