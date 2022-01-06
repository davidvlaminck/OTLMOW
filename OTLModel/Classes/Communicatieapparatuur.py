from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Communicatieapparatuur(AIMNaamObject):
    """Abstracte voor alle benodigde apparatuur voor het ontvangen en verzenden van signalen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Communicatieapparatuur"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
