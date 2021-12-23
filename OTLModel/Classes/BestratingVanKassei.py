from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.DtcAfmetingBxlInCm import DtcAfmetingBxlInCm


# Generated with OTLClassCreator
class BestratingVanKassei(Bestrating):
    """Bestrating van kasseien, in rij gelegd. Kasseien zijn bestratingselementen van porfier, kwartsiet, graniet, of van harde zandsteen die geen schilferige structuur heeft. Ze hebben een dicht aaneengesloten en homogene korrel, zonder steenkorst, kwade aders of kwakaders en vertonen geen diamantkop."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanKassei"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.afmetingVanBestratingselementBxl = DtcAfmetingBxlInCm()
        """Afmeting van de breedte in cm (langste)
 en van de lengte in cm (kortste)
 van de kassei."""
        self.afmetingVanBestratingselementBxl.naam = "afmetingVanBestratingselementBxl"
        self.afmetingVanBestratingselementBxl.label = "afmeting van bestratingselement bxl"
        self.afmetingVanBestratingselementBxl.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanKassei.afmetingVanBestratingselementBxl"
        self.afmetingVanBestratingselementBxl.definition = "Afmeting van de breedte in cm (langste)
 en van de lengte in cm (kortste)
 van de kassei."
        self.afmetingVanBestratingselementBxl.constraints = ""
        self.afmetingVanBestratingselementBxl.usagenote = ""
        self.afmetingVanBestratingselementBxl.deprecated_version = ""
