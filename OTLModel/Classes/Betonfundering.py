from abc import abstractmethod
from OTLModel.Classes.Fundering import Fundering
from OTLModel.Datatypes.DtcAfmetingBxlInM import DtcAfmetingBxlInM
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlFunderingBetonkwaliteit import KlFunderingBetonkwaliteit


# Generated with OTLClassCreator. To modify: extend, do not edit
class Betonfundering(Fundering):
    """Abstracte voor funderingen in beton."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
