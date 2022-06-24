# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlContactorType import KlContactorType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Contactor(AIMObject, PuntGeometrie):
    """Toestel dat ter plaatse of op afstand aangestuurd wordt om (grote) vermogensstromen af te schakelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._type = OTLAttribuut(field=KlContactorType,
                                  naam='type',
                                  label='type contactor',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor.type',
                                  definition='Geeft aan of het een K of Q contactor betreft.',
                                  owner=self)

    @property
    def type(self):
        """Geeft aan of het een K of Q contactor betreft."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
