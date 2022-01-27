# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Datatypes.KlEcoBoombrugType import KlEcoBoombrugType
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Boombrug(AIMObject):
    """Een eenvoudige constructie die een oversteek biedt voor soorten die in bomen leven, voornamelijk eekhoorns."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._hoogte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug.hoogte',
                                    definition='De hoogte van de boombrug in meter.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug.lengte',
                                    definition='De lengte van de boombrug in meter.')

        self._type = OTLAttribuut(field=KlEcoBoombrugType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug.type',
                                  definition='Het type van boombrug.')

    @property
    def hoogte(self):
        """De hoogte van de boombrug in meter."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van de boombrug in meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van boombrug."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
