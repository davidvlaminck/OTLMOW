# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACSchokindex(Keuzelijst):
    """De verschillende schokindices."""

    def __init__(self):
        super().__init__(naam="KlLEACSchokindex",
                         label="Schokindex",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACSchokindex",
                         definition="De verschillende schokindices.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACSchokindex")

        self.add_option("a", "a", "ASI <= 1.0 (zeer veilig)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSchokindex/a")
        self.add_option("b", "b", "ASI <= 1.4 (voldoende veilig)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSchokindex/b")
        self.add_option("c", "c", "ASI <= 1.9", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSchokindex/c")
