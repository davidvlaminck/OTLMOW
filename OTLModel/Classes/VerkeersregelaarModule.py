from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator
class VerkeersregelaarModule(AIMNaamObject):
    """Abstracte voor de verschillende modules waaruit een verkeersregelaar opgebouwd is."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VerkeersregelaarModule"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
