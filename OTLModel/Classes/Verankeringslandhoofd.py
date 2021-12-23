from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator
class Verankeringslandhoofd(AIMObject):
    """De verankeringsconstructie aan het einde van een cementbetonverharding."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.breedte = KwantWrdInMeter()
        """De breedte van het verankeringslandhoofd in meter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.breedte"
        self.breedte.definition = "De breedte van het verankeringslandhoofd in meter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.lengte = KwantWrdInMeter()
        """De lengte van het verankeringslandhoofd in meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.lengte"
        self.lengte.definition = "De lengte van het verankeringslandhoofd in meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.ribben = IntegerField(naam="ribben",
                                   label="ribben",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.ribben",
                                   definition="Het aantal ribben van het verankeringslandhoofd.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """Het aantal ribben van het verankeringslandhoofd."""
