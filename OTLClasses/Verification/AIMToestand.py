from abc import ABC, abstractmethod

from ModelGenerator.BaseClasses.EnumField import EnumField, KlAIMToestand


# inherit from ABC to create abstract class
# class NaampadObject(OTLAsset, ABC):


class AIMToestand(ABC):
    """Voegt een attribuut toe aan de subklasse dat de huidige stand in de levenscyclus van het object aangeeft."""
    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand"
    toestand = EnumField(KlAIMToestand)
    """Geeft de actuele stand in de levenscyclus van het object."""

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

