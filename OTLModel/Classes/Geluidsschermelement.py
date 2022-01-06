from abc import abstractmethod
from OTLModel.Classes.LijnvormigElement import LijnvormigElement
from OTLModel.Datatypes.DtcGCMateriaalKarakteristiek import DtcGCMateriaalKarakteristiek
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInKiloNewtonPerVierkanteMeter import KwantWrdInKiloNewtonPerVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geluidsschermelement(LijnvormigElement):
    """Abstracte om de gemeenschappelijke eigenschappen van de verschillende types schermlementen te bundelen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.hoogte = KwantWrdInCentimeter()
        """De hoogte in centimeter van het schermelement, verticaal gemeten."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.hoogte"
        self.hoogte.definition = "De hoogte in centimeter van het schermelement, verticaal gemeten."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.lengte = KwantWrdInCentimeter()
        """De lengte van het schermelement in centimeter zonder inbegrip van de profielen, horizontaal gemeten."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.lengte"
        self.lengte.definition = "De lengte van het schermelement in centimeter zonder inbegrip van de profielen, horizontaal gemeten."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.materiaalkarakteristiek = DtcGCMateriaalKarakteristiek()
        """Het materiaal van de geluidswerende constructie en het geluidskarakteristiek van het materiaal."""
        self.materiaalkarakteristiek.naam = "materiaalkarakteristiek"
        self.materiaalkarakteristiek.label = "materiaalkarakteristiek"
        self.materiaalkarakteristiek.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.materiaalkarakteristiek"
        self.materiaalkarakteristiek.definition = "Het materiaal van de geluidswerende constructie en het geluidskarakteristiek van het materiaal."
        self.materiaalkarakteristiek.constraints = ""
        self.materiaalkarakteristiek.usagenote = ""
        self.materiaalkarakteristiek.deprecated_version = ""

        self.maximaleTotaleDikte = KwantWrdInCentimeter()
        """De maximale totale dikte van het schermelement in centimeter, gemeten ter hoogte van het geluidsabsorberende deel van het schermelement."""
        self.maximaleTotaleDikte.naam = "maximaleTotaleDikte"
        self.maximaleTotaleDikte.label = "maximale totale dikte"
        self.maximaleTotaleDikte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.maximaleTotaleDikte"
        self.maximaleTotaleDikte.definition = "De maximale totale dikte van het schermelement in centimeter, gemeten ter hoogte van het geluidsabsorberende deel van het schermelement."
        self.maximaleTotaleDikte.constraints = ""
        self.maximaleTotaleDikte.usagenote = ""
        self.maximaleTotaleDikte.deprecated_version = ""

        self.windbelasting = KwantWrdInKiloNewtonPerVierkanteMeter()
        """Getal in kN/m2 voor de aanduiding van de maximale windbelasting volgens de norm NBN EN 1994-1-4."""
        self.windbelasting.naam = "windbelasting"
        self.windbelasting.label = "windbelasting"
        self.windbelasting.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement.windbelasting"
        self.windbelasting.definition = "Getal in kN/m2 voor de aanduiding van de maximale windbelasting volgens de norm NBN EN 1994-1-4."
        self.windbelasting.constraints = ""
        self.windbelasting.usagenote = ""
        self.windbelasting.deprecated_version = ""
