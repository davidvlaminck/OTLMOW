# coding=utf-8
from abc import abstractmethod, ABC
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class TerreinDeel(ABC):
    """Abstracte voor het gedeelte van het aardoppervlak, met een gelijkaardige functie, dat geen deel uitmaakt van 'waterdeel'."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TerreinDeel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.breedte = KwantWrdInMeter()
        """De breedte van het object in meter. In geval van een ongelijkmatige breedte wordt de gemiddelde breedte opgenomen."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TerreinDeel.breedte"
        self.breedte.definition = "De breedte van het object in meter. In geval van een ongelijkmatige breedte wordt de gemiddelde breedte opgenomen."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.lengte = KwantWrdInMeter()
        """De lengte van het object in meter. In geval van een ongelijkmatige lengte wordt de gemiddelde lengte opgenomen."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TerreinDeel.lengte"
        self.lengte.definition = "De lengte van het object in meter. In geval van een ongelijkmatige lengte wordt de gemiddelde lengte opgenomen."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.niveau = DecimalFloatField(naam="niveau",
                                        label="niveau",
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TerreinDeel.niveau",
                                        definition="Het niveau waarop het object zich bevindt, relatief ten opzichte van andere objecten. Negatieve waarden worden geassocieerd met ondergronds en positieve waarden met bovengronds. Nul wordt beschouwd als een absolute waarde om het maaiveld aan te duiden.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Het niveau waarop het object zich bevindt, relatief ten opzichte van andere objecten. Negatieve waarden worden geassocieerd met ondergronds en positieve waarden met bovengronds. Nul wordt beschouwd als een absolute waarde om het maaiveld aan te duiden."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte in vierkante meter."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TerreinDeel.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte in vierkante meter."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""
