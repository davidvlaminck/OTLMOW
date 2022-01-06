from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefBindmiddeldosering(Proef):
    """Proef om de hoeveelheid bindmiddel te bepalen die nodig is om de grond als funderingslaag te garanderen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBindmiddeldosering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.technischVerslagBindmiddeldosering = DtcDocument()
        """Het technisch verslag van een aangewezen bindmiddeldosering."""
        self.technischVerslagBindmiddeldosering.naam = "technischVerslagBindmiddeldosering"
        self.technischVerslagBindmiddeldosering.label = "technisch verslag bindmiddeldosering"
        self.technischVerslagBindmiddeldosering.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBindmiddeldosering.technischVerslagBindmiddeldosering"
        self.technischVerslagBindmiddeldosering.definition = "Het technisch verslag van een aangewezen bindmiddeldosering."
        self.technischVerslagBindmiddeldosering.constraints = ""
        self.technischVerslagBindmiddeldosering.usagenote = ""
        self.technischVerslagBindmiddeldosering.deprecated_version = ""
