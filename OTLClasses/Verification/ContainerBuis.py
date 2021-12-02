from abc import ABC, abstractmethod


class ContainerBuis(ABC):
    """Abstracte voor het groeperen van eigenschappen en relaties van buisvormige container elementen. Dit zijn buizen die kabels of andere leidingen kunnen bevatten."""

    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis"

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)
