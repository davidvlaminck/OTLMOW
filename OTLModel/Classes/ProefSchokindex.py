from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACSchokindex import KlLEACSchokindex


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefSchokindex(Proef):
    """Proef voor de bepaling van de schokindex parameter."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindex"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
