from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefKorrelverdeling(Proef):
    """Bepaling van de doorval door een reeks zeven van een granulaatmengsel volgens NBN EN 933-1."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKorrelverdeling"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.korrelverdeling = DtcDocument()
        """Het resultaat van de test van de gemeten korrelverdeling in de BV laag."""
        self.korrelverdeling.naam = "korrelverdeling"
        self.korrelverdeling.label = "korrelverdeling"
        self.korrelverdeling.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKorrelverdeling.korrelverdeling"
        self.korrelverdeling.definition = "Het resultaat van de test van de gemeten korrelverdeling in de BV laag."
        self.korrelverdeling.constraints = ""
        self.korrelverdeling.usagenote = ""
        self.korrelverdeling.deprecated_version = ""
