# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWatergehalte(Proef):
    """Bepaling van de hoeveelheid water die opgenomen kan worden in een betonverharding."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWatergehalte"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.watergehalte = DtcDocument()
        """Het resultaat van de test van het gemeten watergehalte in de BV laag."""
        self.watergehalte.naam = "watergehalte"
        self.watergehalte.label = "watergehalte"
        self.watergehalte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWatergehalte.watergehalte"
        self.watergehalte.definition = "Het resultaat van de test van het gemeten watergehalte in de BV laag."
        self.watergehalte.constraints = ""
        self.watergehalte.usagenote = ""
        self.watergehalte.deprecated_version = ""
