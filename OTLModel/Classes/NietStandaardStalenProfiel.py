# coding=utf-8
from OTLModel.Classes.StalenProfiel import StalenProfiel
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietStandaardStalenProfiel(StalenProfiel):
    """Een stalen constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. Niet-standaard stalen profiel omvat alle speciale, op maat gemaakte en/of niet vaak voorkomende profielen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.profielbreedte = KwantWrdInMillimeter()
        """De korte afmeting in millimeter van het profiel."""
        self.profielbreedte.naam = "profielbreedte"
        self.profielbreedte.label = "profielbreedte"
        self.profielbreedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel.profielbreedte"
        self.profielbreedte.definition = "De korte afmeting in millimeter van het profiel."
        self.profielbreedte.constraints = ""
        self.profielbreedte.usagenote = ""
        self.profielbreedte.deprecated_version = ""

        self.profielhoogte = KwantWrdInMillimeter()
        """De langste afmeting in millimeter van het profiel."""
        self.profielhoogte.naam = "profielhoogte"
        self.profielhoogte.label = "profielhoogte"
        self.profielhoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel.profielhoogte"
        self.profielhoogte.definition = "De langste afmeting in millimeter van het profiel."
        self.profielhoogte.constraints = ""
        self.profielhoogte.usagenote = ""
        self.profielhoogte.deprecated_version = ""
