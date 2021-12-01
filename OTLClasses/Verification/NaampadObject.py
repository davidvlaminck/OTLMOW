from abc import ABC, abstractmethod

from ModelGenerator.BaseClasses.StringField import StringField
from OTLClasses.Verification.AIMNaamObject import AIMNaamObject


# inherit from ABC to create abstract class
class NaampadObject(AIMNaamObject, ABC):
    """Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad."""
    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject"

    naampad = StringField()
    """Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra)."""

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

