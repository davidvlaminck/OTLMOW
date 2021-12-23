from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class ProefGaafheid(Proef):
    """Controle van het lijnvormig element op de ongeschondenheid, volledigheid en zuiverheid."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGaafheid"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.gaafheid = DtcDocument()
        """De resultaten van de controle."""
        self.gaafheid.naam = "gaafheid"
        self.gaafheid.label = "gaafheid"
        self.gaafheid.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGaafheid.gaafheid"
        self.gaafheid.definition = "De resultaten van de controle."
        self.gaafheid.constraints = ""
        self.gaafheid.usagenote = ""
        self.gaafheid.deprecated_version = ""
