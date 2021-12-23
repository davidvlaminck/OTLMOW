from abc import abstractmethod
from OTLModel.Classes.Laag import Laag
from OTLModel.Classes.LaagProductidentificatiecode import LaagProductidentificatiecode


# Generated with OTLClassCreator
class AndereLaag(Laag, LaagProductidentificatiecode):
    """Abstracte als tussenlaag voor de andere laag-objecten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereLaag"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Laag.__init__(self)
        LaagProductidentificatiecode.__init__(self)
