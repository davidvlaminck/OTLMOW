# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Classes.Sensoropstelling import Sensoropstelling
from OTLMOW.OTLModel.Datatypes.KlLichtsensorMerk import KlLichtsensorMerk
from OTLMOW.OTLModel.Datatypes.KlLichtsensorModelnaam import KlLichtsensorModelnaam
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lichtsensor(AIMNaamObject, Sensoropstelling, PuntGeometrie):
    """Sensor die de intensiteit van het invallende licht meet."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtsensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Sensoropstelling.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=KlLichtsensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtsensor.merk',
                                  definition='Het merk van de lichtsensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlLichtsensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtsensor.modelnaam',
                                       definition='De modelnaam van de lichtsensor.',
                                       owner=self)

    @property
    def merk(self):
        """Het merk van de lichtsensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de lichtsensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
