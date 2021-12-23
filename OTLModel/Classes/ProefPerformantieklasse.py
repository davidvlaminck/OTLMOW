from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACPerformantieklasse import KlLEACPerformantieklasse


# Generated with OTLClassCreator
class ProefPerformantieklasse(Proef):
    """Proef die de performantie (bij impact) bepaalt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieklasse"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
