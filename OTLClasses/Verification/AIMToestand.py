from abc import ABC, abstractmethod


from OTLClasses.Verification.KlAIMToestand import KlAIMToestand


class AIMToestand(ABC):
    """Voegt een attribuut toe aan de subklasse dat de huidige stand in de levenscyclus van het object aangeeft."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    toestand = KlAIMToestand()
    """Geeft de actuele stand in de levenscyclus van het object."""

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

