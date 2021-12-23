from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class ProefDraagvermogen(Proef):
    """Controle van de verdichting van de ondergrond of van een funderingslaag."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraagvermogen"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.draagvermogen = DtcDocument()
        """Proef die het draagvermogen van de laag bepaald."""
        self.draagvermogen.naam = "draagvermogen"
        self.draagvermogen.label = "draagvermogen"
        self.draagvermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraagvermogen.draagvermogen"
        self.draagvermogen.definition = "Proef die het draagvermogen van de laag bepaald."
        self.draagvermogen.constraints = ""
        self.draagvermogen.usagenote = ""
        self.draagvermogen.deprecated_version = ""
