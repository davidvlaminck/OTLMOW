from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLuchtgehalte(Proef):
    """Proef die de hoeveelheid lucht bepaalt  in vers beton met de drukmethode volgens NBN EN 12350-7."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtgehalte"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.luchtgehalte = DtcDocument()
        """Proefresultaten van het luchtgehalte."""
        self.luchtgehalte.naam = "luchtgehalte"
        self.luchtgehalte.label = "luchtgehalte"
        self.luchtgehalte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtgehalte.luchtgehalte"
        self.luchtgehalte.definition = "Proefresultaten van het luchtgehalte."
        self.luchtgehalte.constraints = ""
        self.luchtgehalte.usagenote = ""
        self.luchtgehalte.deprecated_version = ""
