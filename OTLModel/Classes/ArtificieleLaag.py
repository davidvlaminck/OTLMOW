from abc import abstractmethod
from OTLModel.Classes.Laag import Laag
from OTLModel.Classes.LaagDikte import LaagDikte
from OTLModel.Classes.LaagProductidentificatiecode import LaagProductidentificatiecode


# Generated with OTLClassCreator
class ArtificieleLaag(Laag, LaagDikte, LaagProductidentificatiecode):
    """Abstracte als noemer om de abstracten Laag, LaagProductidentificatiecode en LaagDikte te groeperen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ArtificieleLaag"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Laag.__init__(self)
        LaagDikte.__init__(self)
        LaagProductidentificatiecode.__init__(self)
