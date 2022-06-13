# coding=utf-8
from abc import abstractmethod, ABC


# Generated with OTLClassCreator. To modify: extend, do not edit
class OmhullendeInrichting(ABC):
    """Abstracte voor het groeperen van de relaties voor onderdelen die kabels kunnen omhullen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        pass
