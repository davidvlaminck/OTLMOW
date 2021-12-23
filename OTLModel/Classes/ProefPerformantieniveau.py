from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACPerformantieniveau import KlLEACPerformantieniveau


# Generated with OTLClassCreator
class ProefPerformantieniveau(Proef):
    """Bepaling van het performantieniveau."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieniveau"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
