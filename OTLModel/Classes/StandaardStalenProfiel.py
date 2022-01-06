# coding=utf-8
from OTLModel.Classes.StalenProfiel import StalenProfiel
from OTLModel.Datatypes.DtcProfieltype import DtcProfieltype


# Generated with OTLClassCreator. To modify: extend, do not edit
class StandaardStalenProfiel(StalenProfiel):
    """Een stalen constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. Standaard stalen profiel omvat de meest genormeerde soorten profielen, zoals H-, I- en U-profielen met voorgedefinieerde profielhoogtematen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StandaardStalenProfiel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.profieltype = DtcProfieltype()
        """Soort van profiel gecombineerd met de hoogte."""
        self.profieltype.naam = "profieltype"
        self.profieltype.label = "profieltype"
        self.profieltype.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StandaardStalenProfiel.profieltype"
        self.profieltype.definition = "Soort van profiel gecombineerd met de hoogte."
        self.profieltype.constraints = ""
        self.profieltype.usagenote = ""
        self.profieltype.deprecated_version = ""
