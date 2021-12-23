from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class ProefDraineervermogen(Proef):
    """Controle van de waterdoorlatendheid van een open verharding."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraineervermogen"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.draineervermogen = DtcDocument()
        """Proefresultaten van het drainvermogen."""
        self.draineervermogen.naam = "draineervermogen"
        self.draineervermogen.label = "draineervermogen"
        self.draineervermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraineervermogen.draineervermogen"
        self.draineervermogen.definition = "Proefresultaten van het drainvermogen."
        self.draineervermogen.constraints = ""
        self.draineervermogen.usagenote = ""
        self.draineervermogen.deprecated_version = ""
