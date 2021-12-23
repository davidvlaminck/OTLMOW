from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class ProefVlakheid(Proef):
    """Controle van de effenheid van het oppervlak met behulp van een 3 meter lange rei volgens NBN EN 13036-7."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.vlakheid = DtcDocument()
        """Proefresultaten van de vlakheid."""
        self.vlakheid.naam = "vlakheid"
        self.vlakheid.label = "vlakheid"
        self.vlakheid.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid.vlakheid"
        self.vlakheid.definition = "Proefresultaten van de vlakheid."
        self.vlakheid.constraints = ""
        self.vlakheid.usagenote = ""
        self.vlakheid.deprecated_version = ""
