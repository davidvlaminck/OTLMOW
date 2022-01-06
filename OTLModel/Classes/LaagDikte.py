# coding=utf-8
from abc import abstractmethod, ABC
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class LaagDikte(ABC):
    """Abstracte waarmee aan een laag het attribuut dikte wordt toegekend."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.dikte = KwantWrdInCentimeter()
        """De gemiddelde dikte van een laag in centimeter."""
        self.dikte.naam = "dikte"
        self.dikte.label = "dikte"
        self.dikte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte.dikte"
        self.dikte.definition = "De gemiddelde dikte van een laag in centimeter."
        self.dikte.constraints = ""
        self.dikte.usagenote = ""
        self.dikte.deprecated_version = ""
