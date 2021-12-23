from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class ProefWeerstandAfschilfering(Proef):
    """Controle van de vorst-dooiweerstand volgens CEN/TS 12390-9."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWeerstandAfschilfering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.weerstandAfschilfering = DtcDocument()
        """Proef om de weerstand/afschilfering van de laag te bepalen."""
        self.weerstandAfschilfering.naam = "weerstandAfschilfering"
        self.weerstandAfschilfering.label = "weerstand afschilfering"
        self.weerstandAfschilfering.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWeerstandAfschilfering.weerstandAfschilfering"
        self.weerstandAfschilfering.definition = "Proef om de weerstand/afschilfering van de laag te bepalen."
        self.weerstandAfschilfering.constraints = ""
        self.weerstandAfschilfering.usagenote = ""
        self.weerstandAfschilfering.deprecated_version = ""
