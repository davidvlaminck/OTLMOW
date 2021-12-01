from abc import ABC, abstractmethod


from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField
from OTLClasses.Verification.KlAIMToestand import KlAIMToestand


class AIMToestand(ABC):
    """Voegt een attribuut toe aan de subklasse dat de huidige stand in de levenscyclus van het object aangeeft."""

    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand"

    toestand = KeuzelijstField(KlAIMToestand())
    """Geeft de actuele stand in de levenscyclus van het object."""

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

