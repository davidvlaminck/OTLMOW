# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSierbeplPlantmaat(Keuzelijst):
    """De plantmaten van de sierplant."""

    def __init__(self):
        super().__init__(naam="KlSierbeplPlantmaat",
                         label="Sierbepl plantmaat",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSierbeplPlantmaat",
                         definition="De plantmaten van de sierplant.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSierbeplPlantmaat")

        self.add_option("20-30", "20-30", "20/30", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplPlantmaat/20-30")
        self.add_option("30-40", "30-40", "30/40", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplPlantmaat/30-40")
        self.add_option("40-60", "40-60", "40/60", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplPlantmaat/40-60")
