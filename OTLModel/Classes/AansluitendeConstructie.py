# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AfschermendeConstructie import AfschermendeConstructie
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class AansluitendeConstructie(AfschermendeConstructie):
    """Abstracte die alle aansluitende constructies bundelt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.totaleLengte = KwantWrdInMeter()
        """De totale lengte van de elementen van de aansluitende constructie."""
        self.totaleLengte.naam = "totaleLengte"
        self.totaleLengte.label = "totale lengte"
        self.totaleLengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie.totaleLengte"
        self.totaleLengte.definition = "De totale lengte van de elementen van de aansluitende constructie."
        self.totaleLengte.constraints = ""
        self.totaleLengte.usagenote = ""
        self.totaleLengte.deprecated_version = ""
