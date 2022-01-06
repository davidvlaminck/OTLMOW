from abc import abstractmethod, ABC
from OTLModel.Datatypes.DtcConstructiestaalspecificaties import DtcConstructiestaalspecificaties
from OTLModel.Datatypes.KwantWrdInKilogram import KwantWrdInKilogram


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenConstructieElement(ABC):
    """Bundeling van gemeenschappelijke eigenschappen van stalen constructie-elementen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenConstructieElement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.staalspecificaties = DtcConstructiestaalspecificaties()
        """Eigenschappen van het gebruikte constructiestaal."""
        self.staalspecificaties.naam = "staalspecificaties"
        self.staalspecificaties.label = "staalspecificaties"
        self.staalspecificaties.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenConstructieElement.staalspecificaties"
        self.staalspecificaties.definition = "Eigenschappen van het gebruikte constructiestaal."
        self.staalspecificaties.constraints = ""
        self.staalspecificaties.usagenote = ""
        self.staalspecificaties.deprecated_version = ""

        self.totaalGewicht = KwantWrdInKilogram()
        """Een kwantitatieve waarde in kilogram van het totale stalen element."""
        self.totaalGewicht.naam = "totaalGewicht"
        self.totaalGewicht.label = "totaal gewicht"
        self.totaalGewicht.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenConstructieElement.totaalGewicht"
        self.totaalGewicht.definition = "Een kwantitatieve waarde in kilogram van het totale stalen element."
        self.totaalGewicht.constraints = ""
        self.totaalGewicht.usagenote = ""
        self.totaalGewicht.deprecated_version = ""
