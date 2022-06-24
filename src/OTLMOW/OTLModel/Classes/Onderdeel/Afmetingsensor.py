# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlAfmetingsensorMerk import KlAfmetingsensorMerk
from OTLMOW.OTLModel.Datatypes.KlAfmetingsensorModelnaam import KlAfmetingsensorModelnaam
from OTLMOW.OTLModel.Datatypes.KlAfmetingsensorType import KlAfmetingsensorType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afmetingsensor(AIMNaamObject, PuntGeometrie):
    """Registratie van voertuigafmetingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=KlAfmetingsensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor.merk',
                                  definition='Het merk van de afmetingsensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlAfmetingsensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor.modelnaam',
                                       definition='De modelnaam van de afmetingsensor.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlAfmetingsensorType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor.type',
                                  definition='Het type van de afmetingsensor.',
                                  owner=self)

    @property
    def merk(self):
        """Het merk van de afmetingsensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de afmetingsensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de afmetingsensor."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
