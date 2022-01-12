# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWateropslorping(Proef):
    """Proef waarbij de compactheid of poreusheid van het proefstuk door onderdompeling wordt bepaald."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.wateropslorping = DtcDocument()
        """Proef om de wateropslorping van de laag te bepalen."""
        self.wateropslorping.naam = "wateropslorping"
        self.wateropslorping.label = "wateropslorping"
        self.wateropslorping.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping.wateropslorping"
        self.wateropslorping.definition = "Proef om de wateropslorping van de laag te bepalen."
        self.wateropslorping.constraints = ""
        self.wateropslorping.usagenote = ""
        self.wateropslorping.deprecated_version = ""
