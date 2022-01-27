# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.KlWegdekvoegType import KlWegdekvoegType
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegdekvoeg(AIMObject):
    """Dwarsvoegen en langsvoegen met uitzondering van de krimpvoegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._heeftDeuvels = OTLAttribuut(field=BooleanField,
                                          naam='heeftDeuvels',
                                          label='heeft deuvels',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.heeftDeuvels',
                                          definition='Aanduiding of de voeg al dan niet verdeuveld is.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.lengte',
                                    definition='De lengte van de wegdekvoeg.')

        self._type = OTLAttribuut(field=KlWegdekvoegType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.type',
                                  definition='Het type van wegdekvoeg.')

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
