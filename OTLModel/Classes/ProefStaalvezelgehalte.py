from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefStaalvezelgehalte(Proef):
    """Bepaling van de hoeveelheid staalvezels in de cementbetonverharding."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStaalvezelgehalte"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.staalvezelgehalte = DtcDocument()
        """Het resultaat van de test van het gemeten staalvezelgehalte in de BV laag."""
        self.staalvezelgehalte.naam = "staalvezelgehalte"
        self.staalvezelgehalte.label = "staalvezelgehalte"
        self.staalvezelgehalte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStaalvezelgehalte.staalvezelgehalte"
        self.staalvezelgehalte.definition = "Het resultaat van de test van het gemeten staalvezelgehalte in de BV laag."
        self.staalvezelgehalte.constraints = ""
        self.staalvezelgehalte.usagenote = ""
        self.staalvezelgehalte.deprecated_version = ""
