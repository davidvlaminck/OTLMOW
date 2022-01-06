# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitlaatType(Keuzelijst):
    """De verschillende types van uitlaat."""

    def __init__(self):
        super().__init__(naam="KlUitlaatType",
                         label="Uitlaat type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUitlaatType",
                         definition="De verschillende types van uitlaat.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitlaatType")

        self.add_option("inlaat", "inlaat", "locatie waar water van een open profiel naar een inbuizing overgaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitlaatType/inlaat")
        self.add_option("uitlaat", "uitlaat", "locatie waar water van een inbuizing naar een open profiel overgaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitlaatType/uitlaat")
