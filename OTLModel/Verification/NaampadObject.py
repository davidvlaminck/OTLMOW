from abc import ABC, abstractmethod

from OTLModel.Datatypes.StringField import StringField
from OTLModel.Verification.AIMNaamObject import AIMNaamObject


# inherit from ABC to create abstract class
class NaampadObject(AIMNaamObject, ABC):
    """Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad."""
    typeUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.naampad = StringField()
        """Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra)."""

    # TODO naampad aanvullen