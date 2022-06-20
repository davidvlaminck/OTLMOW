# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlEcoBoombrugType import KlEcoBoombrugType
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Boombrug(AIMObject, LijnGeometrie):
    """Een eenvoudige constructie die een oversteek biedt voor soorten die in bomen leven, voornamelijk eekhoorns."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        LijnGeometrie.__init__(self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug.hoogte',
                                    definition='De hoogte van de boombrug in meter.',
                                    owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug.lengte',
                                    definition='De lengte van de boombrug in meter.',
                                    owner=self)

        self._type = OTLAttribuut(field=KlEcoBoombrugType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug.type',
                                  definition='Het type van boombrug.',
                                  owner=self)

    @property
    def hoogte(self):
        """De hoogte van de boombrug in meter."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van de boombrug in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van boombrug."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
