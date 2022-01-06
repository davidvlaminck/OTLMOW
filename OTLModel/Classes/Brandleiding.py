from OTLModel.Classes.Persleiding import Persleiding
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KwantWrdInBar import KwantWrdInBar


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brandleiding(Persleiding):
    """Segment uit de leiding die water aanvoert voor het blussen van een brand."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.isGeisoleerd = BooleanField(naam="isGeisoleerd",
                                         label="is geïsoleerd",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding.isGeisoleerd",
                                         definition="Geeft aan of de brandleiding voorzien is van eigen isolatie.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Geeft aan of de brandleiding voorzien is van eigen isolatie."""

        self.leidingdruk = KwantWrdInBar()
        """De vastgelegde druk die moet voorzien worden op de leiding in functie van de aanvoer van bluswater."""
        self.leidingdruk.naam = "leidingdruk"
        self.leidingdruk.label = "leidingdruk"
        self.leidingdruk.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding.leidingdruk"
        self.leidingdruk.definition = "De vastgelegde druk die moet voorzien worden op de leiding in functie van de aanvoer van bluswater."
        self.leidingdruk.constraints = ""
        self.leidingdruk.usagenote = ""
        self.leidingdruk.deprecated_version = ""
