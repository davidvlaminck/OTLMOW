# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verankeringslandhoofd(AIMObject, VlakGeometrie):
    """De verankeringsconstructie aan het einde van een cementbetonverharding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.breedte',
                                     definition='De breedte van het verankeringslandhoofd in meter.',
                                     owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.lengte',
                                    definition='De lengte van het verankeringslandhoofd in meter.',
                                    owner=self)

        self._ribben = OTLAttribuut(field=IntegerField,
                                    naam='ribben',
                                    label='ribben',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.ribben',
                                    definition='Het aantal ribben van het verankeringslandhoofd.',
                                    owner=self)

    @property
    def breedte(self):
        """De breedte van het verankeringslandhoofd in meter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van het verankeringslandhoofd in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def ribben(self):
        """Het aantal ribben van het verankeringslandhoofd."""
        return self._ribben.get_waarde()

    @ribben.setter
    def ribben(self, value):
        self._ribben.set_waarde(value, owner=self)
