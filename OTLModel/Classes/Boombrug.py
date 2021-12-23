from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEcoBoombrugType import KlEcoBoombrugType
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator
class Boombrug(AIMObject):
    """Een eenvoudige constructie die een oversteek biedt voor soorten die in bomen leven, voornamelijk eekhoorns."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.hoogte = KwantWrdInMeter()
        """De hoogte van de boombrug in meter."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug.hoogte"
        self.hoogte.definition = "De hoogte van de boombrug in meter."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.lengte = KwantWrdInMeter()
        """De lengte van de boombrug in meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug.lengte"
        self.lengte.definition = "De lengte van de boombrug in meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlEcoBoombrugType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boombrug.type",
                                    definition="Het type van boombrug.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van boombrug."""
