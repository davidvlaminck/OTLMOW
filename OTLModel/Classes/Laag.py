from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLaagRol import KlLaagRol
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator
class Laag(AIMObject):
    """Abstracte voor de gemeenschappelijke eigenschappen van de onderliggende verhardings- en funderings-onderdelen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.breedte = KwantWrdInMeter()
        """De (gemiddelde) breedte van een laag in meter. Dit kan ook de nominale breedte zijn afhankelijk van de laag en situatie."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.breedte"
        self.breedte.definition = "De (gemiddelde) breedte van een laag in meter. Dit kan ook de nominale breedte zijn afhankelijk van de laag en situatie."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.laagRol = KeuzelijstField(naam="laagRol",
                                       label="laagrol",
                                       lijst=KlLaagRol(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.laagRol",
                                       definition="De functie die de laag vervult in de verticale opbouw.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """De functie die de laag vervult in de verticale opbouw."""

        self.lengte = KwantWrdInMeter()
        """De (gemiddelde) lengte van een laag in meter. Dit kan ook de nominale lengte zijn afhankelijk van de laag en situatie."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.lengte"
        self.lengte.definition = "De (gemiddelde) lengte van een laag in meter. Dit kan ook de nominale lengte zijn afhankelijk van de laag en situatie."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van een laag in vierkante meter."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van een laag in vierkante meter."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""
