from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class ProefRetroreflectie(Proef):
    """Het bepalen van de retroreflectiecoëfficiënt via een manuele retroreflectometer of via labotesten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRetroreflectie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.retroreflectie = DtcDocument()
        """Proef om de retroreflectie van een verkeersbord te bepalen."""
        self.retroreflectie.naam = "retroreflectie"
        self.retroreflectie.label = "retroreflectie"
        self.retroreflectie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRetroreflectie.retroreflectie"
        self.retroreflectie.definition = "Proef om de retroreflectie van een verkeersbord te bepalen."
        self.retroreflectie.constraints = ""
        self.retroreflectie.usagenote = ""
        self.retroreflectie.deprecated_version = ""
