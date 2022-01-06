from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGemetenDikte(Proef):
    """De effectieve dikte van de laag."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGemetenDikte"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.gemetenDikte = KwantWrdInCentimeter()
        """De gemeten dikte van de laag in centimeter."""
        self.gemetenDikte.naam = "gemetenDikte"
        self.gemetenDikte.label = "gemeten dikte"
        self.gemetenDikte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGemetenDikte.gemetenDikte"
        self.gemetenDikte.definition = "De gemeten dikte van de laag in centimeter."
        self.gemetenDikte.constraints = ""
        self.gemetenDikte.usagenote = ""
        self.gemetenDikte.deprecated_version = ""
