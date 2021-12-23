from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class ProefTextuurdiepte(Proef):
    """Bepaling van de uitwasdiepte van de verharding na een oppervlaktebehandeling volgens NBN EN ISO 13473-1."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTextuurdiepte"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.textuurdiepte = DtcDocument()
        """Proefresultaten van de textuurdiepte van de toplaag."""
        self.textuurdiepte.naam = "textuurdiepte"
        self.textuurdiepte.label = "textuurdiepte"
        self.textuurdiepte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTextuurdiepte.textuurdiepte"
        self.textuurdiepte.definition = "Proefresultaten van de textuurdiepte van de toplaag."
        self.textuurdiepte.constraints = ""
        self.textuurdiepte.usagenote = ""
        self.textuurdiepte.deprecated_version = ""
