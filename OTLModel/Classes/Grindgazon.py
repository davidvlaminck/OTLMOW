from OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen
from OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grindgazon(BegroeidVoorkomen):
    """Gazontype specifiek op een gestabiliseerde ondergrond. Het is een substraat ontwikkeld om voertuigen sporadisch toe te laten op gazons zonder dat er spoorvorming optreedt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindgazon"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.isTweelaags = BooleanField(naam="isTweelaags",
                                        label="is tweelaags",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindgazon.isTweelaags",
                                        definition="Geeft aan of het grindgazon tweelaags of éénlaags is.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Geeft aan of het grindgazon tweelaags of éénlaags is."""
