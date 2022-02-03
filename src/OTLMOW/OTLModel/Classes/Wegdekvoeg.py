# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlWegdekvoegType import KlWegdekvoegType
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegdekvoeg(AIMObject, LijnGeometrie):
    """Dwarsvoegen en langsvoegen met uitzondering van de krimpvoegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        LijnGeometrie.__init__(self)

        self._heeftDeuvels = OTLAttribuut(field=BooleanField,
                                          naam='heeftDeuvels',
                                          label='heeft deuvels',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.heeftDeuvels',
                                          definition='Aanduiding of de voeg al dan niet verdeuveld is.',
                                          owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.lengte',
                                    definition='De lengte van de wegdekvoeg.',
                                    owner=self)

        self._type = OTLAttribuut(field=KlWegdekvoegType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.type',
                                  definition='Het type van wegdekvoeg.',
                                  owner=self)

    @property
    def heeftDeuvels(self):
        """Aanduiding of de voeg al dan niet verdeuveld is."""
        return self._heeftDeuvels.waarde

    @heeftDeuvels.setter
    def heeftDeuvels(self, value):
        self._heeftDeuvels.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van de wegdekvoeg."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van wegdekvoeg."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
