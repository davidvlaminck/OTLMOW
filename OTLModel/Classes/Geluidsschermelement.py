# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.LijnvormigElement import LijnvormigElement
from OTLModel.Datatypes.DtcGCMateriaalKarakteristiek import DtcGCMateriaalKarakteristiek
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInKiloNewtonPerVierkanteMeter import KwantWrdInKiloNewtonPerVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geluidsschermelement(LijnvormigElement):
    """Abstracte om de gemeenschappelijke eigenschappen van de verschillende types schermlementen te bundelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._hoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.hoogte',
                                    definition='De hoogte in centimeter van het schermelement, verticaal gemeten.')

        self._lengte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.lengte',
                                    definition='De lengte van het schermelement in centimeter zonder inbegrip van de profielen, horizontaal gemeten.')

        self._materiaalkarakteristiek = OTLAttribuut(field=DtcGCMateriaalKarakteristiek,
                                                     naam='materiaalkarakteristiek',
                                                     label='materiaalkarakteristiek',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.materiaalkarakteristiek',
                                                     definition='Het materiaal van de geluidswerende constructie en het geluidskarakteristiek van het materiaal.')

        self._maximaleTotaleDikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                                 naam='maximaleTotaleDikte',
                                                 label='maximale totale dikte',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.maximaleTotaleDikte',
                                                 definition='De maximale totale dikte van het schermelement in centimeter, gemeten ter hoogte van het geluidsabsorberende deel van het schermelement.')

        self._windbelasting = OTLAttribuut(field=KwantWrdInKiloNewtonPerVierkanteMeter,
                                           naam='windbelasting',
                                           label='windbelasting',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.windbelasting',
                                           definition='Getal in kN/m2 voor de aanduiding van de maximale windbelasting volgens de norm NBN EN 1994-1-4.')

    @property
    def hoogte(self):
        """De hoogte in centimeter van het schermelement, verticaal gemeten."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van het schermelement in centimeter zonder inbegrip van de profielen, horizontaal gemeten."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def materiaalkarakteristiek(self):
        """Het materiaal van de geluidswerende constructie en het geluidskarakteristiek van het materiaal."""
        return self._materiaalkarakteristiek.waarde

    @materiaalkarakteristiek.setter
    def materiaalkarakteristiek(self, value):
        self._materiaalkarakteristiek.set_waarde(value, owner=self)

    @property
    def maximaleTotaleDikte(self):
        """De maximale totale dikte van het schermelement in centimeter, gemeten ter hoogte van het geluidsabsorberende deel van het schermelement."""
        return self._maximaleTotaleDikte.waarde

    @maximaleTotaleDikte.setter
    def maximaleTotaleDikte(self, value):
        self._maximaleTotaleDikte.set_waarde(value, owner=self)

    @property
    def windbelasting(self):
        """Getal in kN/m2 voor de aanduiding van de maximale windbelasting volgens de norm NBN EN 1994-1-4."""
        return self._windbelasting.waarde

    @windbelasting.setter
    def windbelasting(self, value):
        self._windbelasting.set_waarde(value, owner=self)
