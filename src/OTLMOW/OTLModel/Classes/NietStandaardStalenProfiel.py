# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.StalenProfiel import StalenProfiel
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietStandaardStalenProfiel(StalenProfiel):
    """Een stalen constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. Niet-standaard stalen profiel omvat alle speciale, op maat gemaakte en/of niet vaak voorkomende profielen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._profielbreedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='profielbreedte',
                                            label='profielbreedte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel.profielbreedte',
                                            definition='De korte afmeting in millimeter van het profiel.',
                                            owner=self)

        self._profielhoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='profielhoogte',
                                           label='profielhoogte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel.profielhoogte',
                                           definition='De langste afmeting in millimeter van het profiel.',
                                           owner=self)

    @property
    def profielbreedte(self):
        """De korte afmeting in millimeter van het profiel."""
        return self._profielbreedte.waarde

    @profielbreedte.setter
    def profielbreedte(self, value):
        self._profielbreedte.set_waarde(value, owner=self)

    @property
    def profielhoogte(self):
        """De langste afmeting in millimeter van het profiel."""
        return self._profielhoogte.waarde

    @profielhoogte.setter
    def profielhoogte(self, value):
        self._profielhoogte.set_waarde(value, owner=self)
