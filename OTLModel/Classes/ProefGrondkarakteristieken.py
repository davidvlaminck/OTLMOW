from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class ProefGrondkarakteristieken(Proef):
    """Bepaling van de grondeigenschappen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGrondkarakteristieken"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.bepalingGrondkarakteristieken = DtcDocument()
        """Proef met de resultaten van de grondkarakteristieken."""
        self.bepalingGrondkarakteristieken.naam = "bepalingGrondkarakteristieken"
        self.bepalingGrondkarakteristieken.label = "bepaling grondkarakteristieken"
        self.bepalingGrondkarakteristieken.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGrondkarakteristieken.bepalingGrondkarakteristieken"
        self.bepalingGrondkarakteristieken.definition = "Proef met de resultaten van de grondkarakteristieken."
        self.bepalingGrondkarakteristieken.constraints = ""
        self.bepalingGrondkarakteristieken.usagenote = ""
        self.bepalingGrondkarakteristieken.deprecated_version = ""
