# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verankeringslandhoofd(AIMObject):
    """De verankeringsconstructie aan het einde van een cementbetonverharding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.breedte',
                                     definition='De breedte van het verankeringslandhoofd in meter.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.lengte',
                                    definition='De lengte van het verankeringslandhoofd in meter.')

        self._ribben = OTLAttribuut(field=IntegerField,
                                    naam='ribben',
                                    label='ribben',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.ribben',
                                    definition='Het aantal ribben van het verankeringslandhoofd.')

    @property
    def breedte(self):
        """De breedte van het verankeringslandhoofd in meter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van het verankeringslandhoofd in meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def ribben(self):
        """Het aantal ribben van het verankeringslandhoofd."""
        return self._ribben.waarde

    @ribben.setter
    def ribben(self, value):
        self._ribben.set_waarde(value, owner=self)
