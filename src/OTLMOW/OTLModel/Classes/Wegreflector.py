# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Bebakening import Bebakening
from OTLMOW.OTLModel.Datatypes.KlWegreflectorType import KlWegreflectorType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegreflector(Bebakening, PuntGeometrie):
    """Heeft als doel de zichtbaarheid van verkeerseilanden te verhogen en geleiding van de weggebruiker langs de weg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegreflector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Bebakening.__init__(self)
        PuntGeometrie.__init__(self)

        self._type = OTLAttribuut(field=KlWegreflectorType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegreflector.type',
                                  definition='De vorm van wegreflector.',
                                  owner=self)

    @property
    def type(self):
        """De vorm van wegreflector."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
