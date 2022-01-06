# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLangsvlakheid(Proef):
    """De controle van de langsvlakheid nieuwe verhardingen bij verschillende golflengten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLangsvlakheid"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.langsvlakheid = DtcDocument()
        """Het resultaat van de meting."""
        self.langsvlakheid.naam = "langsvlakheid"
        self.langsvlakheid.label = "langsvlakheid"
        self.langsvlakheid.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLangsvlakheid.langsvlakheid"
        self.langsvlakheid.definition = "Het resultaat van de meting."
        self.langsvlakheid.constraints = ""
        self.langsvlakheid.usagenote = ""
        self.langsvlakheid.deprecated_version = ""
