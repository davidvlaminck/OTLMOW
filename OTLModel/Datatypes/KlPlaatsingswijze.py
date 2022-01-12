# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlaatsingswijze(Keuzelijst):
    """Mogelijke manieren van plaatsing van het straatmeubilair."""

    def __init__(self):
        super().__init__(naam="KlPlaatsingswijze",
                         label="Plaatsingswijze",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlaatsingswijze",
                         definition="Mogelijke manieren van plaatsing van het straatmeubilair.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlaatsingswijze")

        self.add_option("vast", "vast", "Vaste plaatsing van het straatmeubilair.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijze/vast")
        self.add_option("wegneembaar", "wegneembaar", "Wegneembare plaatsing van het straatmeubilair.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijze/wegneembaar")
