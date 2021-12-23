from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class ProefHechtsterkte(Proef):
    """Het resultaat van de trekproef waarbij een proefstuk wordt blootgesteld aan een stijgende spanning tot er een breuk optreedt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefHechtsterkte"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.hechtsterkte = DtcDocument()
        """Proef om de hechtsterkte van de laag te bepalen."""
        self.hechtsterkte.naam = "hechtsterkte"
        self.hechtsterkte.label = "hechtsterkte"
        self.hechtsterkte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefHechtsterkte.hechtsterkte"
        self.hechtsterkte.definition = "Proef om de hechtsterkte van de laag te bepalen."
        self.hechtsterkte.constraints = ""
        self.hechtsterkte.usagenote = ""
        self.hechtsterkte.deprecated_version = ""
