from abc import abstractmethod, ABC


# Generated with OTLClassCreator
class ConstructieElementenGC(ABC):
    """Abstracte om de constructie-elementen te bundelen die gerelateerd zijn aan geluidswerende constructies."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementenGC"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
