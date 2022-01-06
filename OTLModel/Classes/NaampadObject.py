# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class NaampadObject(AIMNaamObject):
    """Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.naampad = StringField(naam="naampad",
                                   label="naampad",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad",
                                   definition="Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra).",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra)."""
