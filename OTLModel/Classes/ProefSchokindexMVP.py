from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACSchokindexMVP import KlLEACSchokindexMVP


# Generated with OTLClassCreator
class ProefSchokindexMVP(Proef):
    """Proef voor de bepaling van de schokindex parameter van de motorvangplank."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindexMVP"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
