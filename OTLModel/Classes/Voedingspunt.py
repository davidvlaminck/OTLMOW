from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voedingspunt(AIMNaamObject):
    """Abstracte voor het aansluitpunt van de voeding."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Voedingspunt"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
