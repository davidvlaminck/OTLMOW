from OTLModel.Classes.Geleiding import Geleiding
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlGeleidingMateriaal import KlGeleidingMateriaal
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleidingswand(Geleiding):
    """Een geleidingswand geleidt kleinere dieren zoals amfibieën naar kleinere ecokokers, ecoduikers en dergelijke."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingswand"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.hoogte = KwantWrdInMillimeter()
        """De hoogte van de geleidingswand in millimeter."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingswand.hoogte"
        self.hoogte.definition = "De hoogte van de geleidingswand in millimeter."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.lengte = KwantWrdInMeter()
        """De lengte van de geleidingswand in meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingswand.lengte"
        self.lengte.definition = "De lengte van de geleidingswand in meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlGeleidingMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingswand.materiaal",
                                         definition="Het materiaal van de geleiding.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal van de geleiding."""
