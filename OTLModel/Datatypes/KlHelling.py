# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHelling(Keuzelijst):
    """Kwarten voor het bepalen van de hellingsgraad."""

    def __init__(self):
        super().__init__(naam="KlHelling",
                         label="Helling",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHelling",
                         definition="Kwarten voor het bepalen van de hellingsgraad.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHelling")

        self.add_option("10-4", "10-4", "10-4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/10-4")
        self.add_option("12-4", "12-4", "12-4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/12-4")
        self.add_option("14-4", "14-4", "14-4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/14-4")
        self.add_option("16-4", "16-4", "16-4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/16-4")
        self.add_option("18-4", "18-4", "18-4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/18-4")
        self.add_option("4-4", "4-4", "4-4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/4-4")
        self.add_option("6-4", "6-4", "6-4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/6-4")
        self.add_option("8-4", "8-4", "8-4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/8-4")
