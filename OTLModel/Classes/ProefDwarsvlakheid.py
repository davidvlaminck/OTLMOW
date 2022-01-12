# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDwarsvlakheid(Proef):
    """Controle van de spoorvorming via de latmethode."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDwarsvlakheid"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.dwarsvlakheid = DtcDocument()
        """Proefresultaten van de dwarsvlakheid."""
        self.dwarsvlakheid.naam = "dwarsvlakheid"
        self.dwarsvlakheid.label = "dwarsvlakheid"
        self.dwarsvlakheid.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDwarsvlakheid.dwarsvlakheid"
        self.dwarsvlakheid.definition = "Proefresultaten van de dwarsvlakheid."
        self.dwarsvlakheid.constraints = ""
        self.dwarsvlakheid.usagenote = ""
        self.dwarsvlakheid.deprecated_version = ""
