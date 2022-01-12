# coding=utf-8
from OTLModel.Classes.Bebakening import Bebakening
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWildreflectorDrager import KlWildreflectorDrager


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wildreflector(Bebakening):
    """Een wildreflector is een reflecterend afschrikkingssysteem voor groot en klein wild nabij een weg."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wildreflector"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.drager = KeuzelijstField(naam="drager",
                                      label="drager",
                                      lijst=KlWildreflectorDrager(),
                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wildreflector.drager",
                                      definition="De constructie waar de wildreflector is aan bevestigd.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """De constructie waar de wildreflector is aan bevestigd."""
