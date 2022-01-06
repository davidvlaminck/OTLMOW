from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefConsistentie(Proef):
    """Zetmaat van betonspecie volgens NBN EN 12350-2 bij een cementbetonverharding of een lijnvormig element."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefConsistentie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.consistentie = DtcDocument()
        """Proefresultaten van de consistentie."""
        self.consistentie.naam = "consistentie"
        self.consistentie.label = "consistentie"
        self.consistentie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefConsistentie.consistentie"
        self.consistentie.definition = "Proefresultaten van de consistentie."
        self.consistentie.constraints = ""
        self.consistentie.usagenote = ""
        self.consistentie.deprecated_version = ""
