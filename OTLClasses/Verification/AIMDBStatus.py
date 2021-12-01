from abc import abstractmethod, ABC

from ModelGenerator.BaseClasses.BooleanField import BooleanField
from ModelGenerator.BaseClasses.StringField import StringField


class AIMDBStatus(ABC):
    """Voegt een attribuut toe aan de subklasse dat aangeeft of de asset zichtbaar is in de databank of (zacht) verwijderd is."""
    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus"

    isActief = BooleanField()
    """Geeft aan of het object actief kan gebruikt worden of (zacht) verwijderd is uit het asset beheer systeem."""

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

