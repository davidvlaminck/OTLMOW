# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.KlAfmetingsensorMerk import KlAfmetingsensorMerk
from src.OTLMOW.OTLModel.Datatypes.KlAfmetingsensorModelnaam import KlAfmetingsensorModelnaam
from src.OTLMOW.OTLModel.Datatypes.KlAfmetingsensorType import KlAfmetingsensorType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afmetingsensor(AIMNaamObject):
    """Registratie van voertuigafmetingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlAfmetingsensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor.merk',
                                  definition='Het merk van de afmetingsensor.')

        self._modelnaam = OTLAttribuut(field=KlAfmetingsensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor.modelnaam',
                                       definition='De modelnaam van de afmetingsensor.')

        self._type = OTLAttribuut(field=KlAfmetingsensorType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor.type',
                                  definition='Het type van de afmetingsensor.')

    @property
    def merk(self):
        """Het merk van de afmetingsensor."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de afmetingsensor."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de afmetingsensor."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
