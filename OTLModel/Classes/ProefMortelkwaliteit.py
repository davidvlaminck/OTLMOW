# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefMortelkwaliteit(Proef):
    """Controle van de sterkte van voegmortel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefMortelkwaliteit"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.mortelkwaliteit = DtcDocument()
        """Een rapport van de mortelkwaliteit van de onderbouw laag."""
        self.mortelkwaliteit.naam = "mortelkwaliteit"
        self.mortelkwaliteit.label = "mortelkwaliteit"
        self.mortelkwaliteit.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefMortelkwaliteit.mortelkwaliteit"
        self.mortelkwaliteit.definition = "Een rapport van de mortelkwaliteit van de onderbouw laag."
        self.mortelkwaliteit.constraints = ""
        self.mortelkwaliteit.usagenote = ""
        self.mortelkwaliteit.deprecated_version = ""
