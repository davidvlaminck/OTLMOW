from abc import ABC, abstractmethod

from ModelGenerator.BaseClasses.KardinaliteitField import KardinaliteitField


class ContainerBuis(ABC):
    """Abstracte voor het groeperen van eigenschappen en relaties van buisvormige container elementen. Dit zijn buizen die kabels of andere leidingen kunnen bevatten."""

    kleur = KardinaliteitField(str, 1, "*")
    """De kleur van de coating."""

    typeUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

    # TODO: add typeURI for attributes https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur
