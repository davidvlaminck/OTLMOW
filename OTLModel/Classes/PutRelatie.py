from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator
class PutRelatie(AIMObject):
    """Abstracte om de relaties van de verschillende soorten putten te groeperen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
