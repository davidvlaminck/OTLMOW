from abc import abstractmethod
from OTLModel.Classes.Markering import Markering
from OTLModel.Classes.AOWSType import AOWSType


# Generated with OTLClassCreator
class FiguratieMarkeringToegang(Markering, AOWSType):
    """Abstracte als toegang tot de verschillende soorten figuratiemarkeringen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#FiguratieMarkeringToegang"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Markering.__init__(self)
        AOWSType.__init__(self)
