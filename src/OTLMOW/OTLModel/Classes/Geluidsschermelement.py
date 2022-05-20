# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.LijnvormigElement import LijnvormigElement
from OTLMOW.OTLModel.Datatypes.DtcGCMateriaalKarakteristiek import DtcGCMateriaalKarakteristiek
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInKiloNewtonPerVierkanteMeter import KwantWrdInKiloNewtonPerVierkanteMeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geluidsschermelement(LijnvormigElement, LijnGeometrie):
    """Abstracte om de gemeenschappelijke eigenschappen van de verschillende types schermlementen te bundelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        LijnvormigElement.__init__(self)
        LijnGeometrie.__init__(self)

        self._hoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.hoogte',
                                    definition='De hoogte in centimeter van het schermelement, verticaal gemeten.',
                                    owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.lengte',
                                    definition='De lengte van het schermelement in centimeter zonder inbegrip van de profielen, horizontaal gemeten.',
                                    owner=self)

        self._materiaalkarakteristiek = OTLAttribuut(field=DtcGCMateriaalKarakteristiek,
                                                     naam='materiaalkarakteristiek',
                                                     label='materiaalkarakteristiek',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.materiaalkarakteristiek',
                                                     definition='Het materiaal van de geluidswerende constructie en het geluidskarakteristiek van het materiaal.',
                                                     owner=self)

        self._maximaleTotaleDikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                                 naam='maximaleTotaleDikte',
                                                 label='maximale totale dikte',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.maximaleTotaleDikte',
                                                 definition='De maximale totale dikte van het schermelement in centimeter, gemeten ter hoogte van het geluidsabsorberende deel van het schermelement.',
                                                 owner=self)

        self._windbelasting = OTLAttribuut(field=KwantWrdInKiloNewtonPerVierkanteMeter,
                                           naam='windbelasting',
                                           label='windbelasting',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.windbelasting',
                                           definition='Getal in kN/m2 voor de aanduiding van de maximale windbelasting volgens de norm NBN EN 1994-1-4.',
                                           owner=self)

    @property
    def hoogte(self):
        """De hoogte in centimeter van het schermelement, verticaal gemeten."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van het schermelement in centimeter zonder inbegrip van de profielen, horizontaal gemeten."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def materiaalkarakteristiek(self):
        """Het materiaal van de geluidswerende constructie en het geluidskarakteristiek van het materiaal."""
        return self._materiaalkarakteristiek.get_waarde()

    @materiaalkarakteristiek.setter
    def materiaalkarakteristiek(self, value):
        self._materiaalkarakteristiek.set_waarde(value, owner=self)

    @property
    def maximaleTotaleDikte(self):
        """De maximale totale dikte van het schermelement in centimeter, gemeten ter hoogte van het geluidsabsorberende deel van het schermelement."""
        return self._maximaleTotaleDikte.get_waarde()

    @maximaleTotaleDikte.setter
    def maximaleTotaleDikte(self, value):
        self._maximaleTotaleDikte.set_waarde(value, owner=self)

    @property
    def windbelasting(self):
        """Getal in kN/m2 voor de aanduiding van de maximale windbelasting volgens de norm NBN EN 1994-1-4."""
        return self._windbelasting.get_waarde()

    @windbelasting.setter
    def windbelasting(self, value):
        self._windbelasting.set_waarde(value, owner=self)
