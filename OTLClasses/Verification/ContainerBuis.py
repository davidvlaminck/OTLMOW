from abc import ABC, abstractmethod

from ModelGenerator.BaseClasses.KardinaliteitField import KardinaliteitField


class ContainerBuis(ABC):
    """Abstracte voor het groeperen van eigenschappen en relaties van buisvormige container elementen. Dit zijn buizen die kabels of andere leidingen kunnen bevatten."""

    kleur = KardinaliteitField(str, 1, "*")
    """De kleur van de coating."""

    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis"

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

    # TODO: add uri for attributes https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur
