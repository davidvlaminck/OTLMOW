# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Classes.KabelAardingSamenstelling import KabelAardingSamenstelling
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aardingspen(AIMNaamObject, KabelAardingSamenstelling):
    """De aardingspen is het deel van de aardingsinstallatie dat in direct contact staat met de grond / de aarde."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingspen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        KabelAardingSamenstelling.__init__(self)

        self._lengte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingspen.lengte',
                                    definition='De totale lengte van de aardingspen.',
                                    owner=self)

    @property
    def lengte(self):
        """De totale lengte van de aardingspen."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)
